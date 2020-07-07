#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# some code here is based on DeepSpeech/util/evaluate_tools.py
# https://github.com/mozilla/DeepSpeech/blob/daa6167829e7eee45f22ef21f81b24d36b664f7a/util/evaluate_tools.py

from __future__ import absolute_import, division, print_function

import string
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.special as special
from scipy import stats
import os


def levenshtein(a,b):
    '''
    The following code is from: http://hetland.org/coding/python/levenshtein.py
    This is a straightforward implementation of a well-known algorithm, and thus
    probably shouldn't be covered by copyright to begin with. But in case it is,
    the author (Magnus Lie Hetland) has, to the extent possible under law,
    dedicated all copyright and related and neighboring rights to this software
    to the public domain worldwide, by distributing it under the CC0 license,
    version 1.0. This software is distributed without any warranty. For more
    information, see <http://creativecommons.org/publicdomain/zero/1.0>
    
    Calculates the Levenshtein distance between a and b.
    '''
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current = list(range(n+1))
    for i in range(1, m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1, n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]


def get_error_rate(item, unit):
    '''
    The WER is defined as the edit/Levenshtein distance on word level divided by
    the amount of words in the original text.
    In case of the original having more words (N) than the result and both
    being totally different (all N words resulting in 1 edit operation each),
    the WER will always be 1 (N / N = 1).
    '''
    error_rate = (item[unit+'_dist'] / item[unit+'_len'])
    return error_rate


def get_levenshtein_distance(item, unit):
    '''
    unit is either char or word
    '''
    # lowercase both ground-truth and prediction and remove punctuation
    # for calculation of edit distance
    ground_truth = item['sentence'].lower().translate(str.maketrans('', '', string.punctuation))
    prediction = item['prediction'].lower().translate(str.maketrans('', '', string.punctuation))

    if unit == 'word':
        distance = levenshtein(ground_truth.split(), prediction.split())
    elif unit == 'char':
        distance = levenshtein(ground_truth, prediction)
    else:
        print('ERROR: must be word or char')

    return distance



def get_merged_df(artie_bias_file, prediction_file):
    # Import the ground-truth transcripts and demographic tags
    ground_truth_df = pd.read_csv(artie_bias_file, delimiter='\t')
    if not ground_truth_df.columns.tolist() == ['client_id', 'path', 'sentence',
                                                'up_votes', 'down_votes', 'age',
                                                'gender', 'accent']:
        print("\n### ERROR: Your ARTIE_CORPUS TSV file does not have the correct column structure.\n")
        exit(1)
    else:
        ground_truth_df['path'] = ground_truth_df['path'].apply(lambda path: os.path.splitext(path)[0])

    prediction_df = pd.read_csv(prediction_file, delimiter='\t')
    if not prediction_df.columns.tolist() == ['path','prediction']:
        print("\n### ERROR: Your PREDICTIONS TSV file does not have the correct column structure.\n")
        exit(1)
    else:
        prediction_df['path'] = prediction_df['path'].apply(lambda path: os.path.splitext(path)[0])
        prediction_df['prediction'].fillna("", inplace=True)
    
    # Merge ground-truth (which has demographic data) and predictions
    pred_df = pd.merge(left=ground_truth_df,
                  right=prediction_df,
                  left_on='path',
                  right_on='path')
    # calculate utterance-level statistics
    if unit == 'word':
        pred_df[unit+'_len'] = pred_df['sentence'].str.split().str.len()
    elif unit == 'char':
        pred_df[unit+'_len'] = pred_df['sentence'].str.len()
    pred_df[unit+'_dist'] = pred_df.apply(get_levenshtein_distance, axis=1, unit=unit)
    pred_df[unit+'_error_rate'] = pred_df.apply(get_error_rate, axis=1, unit=unit)

    return pred_df


def get_demographic_class(demographic):
    if demographic in ['male','female']:
        return "gender"
        
    elif demographic in ['african','australia','bermuda','canada','england',
                         'hongkong','indian','ireland','malaysia','newzealand',
                         'philippines','scotland','singapore','southatlandtic',
                         'us','wales']:
        return "accent"
        
    elif demographic in ['teens','twenties','thirties', 'fourties', 'fifties',
                         'sixties', 'seventies', 'eighties', 'nineties']:
        return "age"
        
    else:
        print("ERROR: your requested demographic:", demographic, " is not a default, please check spelling or add it to this script.")
        print("Here is the list of demographics in the Artie Bias Corpus:",
              ['male','female','african','australia','bermuda','canada',
               'england','hongkong','indian','ireland','malaysia','newzealand',
               'philippines','scotland','singapore','southatlandtic',
               'us','wales','teens','twenties','thirties', 'fourties', 'fifties',
               'sixties', 'seventies', 'eighties', 'nineties'])
        exit(1)

        
def compare_two_models(unit, demographic, pred_dfs):
    '''
    run the main program
    '''

    demographic_class = get_demographic_class(demographic)
        
    groups=[]
    for i,df in enumerate(pred_dfs):
        errors=df[df[demographic_class] == demographic][unit+'_error_rate']
        groups.append(errors)
        print("\n###", demographic, unit, "error rate on" ,"for model", i, "=", np.mean(errors),
              "( for", len(errors), "audio clips )")
        
    print("\n###", "one-way ANOVA result:", stats.f_oneway(groups[0], groups[1]))


def detect_bias_in_one_model(unit, demographics, pred_df):
    '''
    run the main program
    '''

    groups=[]
    for demographic in demographics:
        demographic_class = get_demographic_class(demographic)
        errors=pred_df[pred_df[demographic_class] == demographic][unit+'_error_rate']
        groups.append(errors)
        print("\n###", demographic, unit, "error rate =", np.mean(errors),
              "( for", len(errors), "audio clips )")

    print("\n###", "one-way ANOVA result:", stats.f_oneway(groups[0], groups[1]))


def plot_demographic_error(df, unit, demographic, user_file):  
    '''
    create a bar plot along a certain demographic, according to
    either CER or WER
    run the main program
    '''

    demographic_class = get_demographic_class(demographic)
    
    demo_df = df.groupby([demographic_class])[[unit+'_dist', unit+'_len']].sum()
    demo_df[unit+'_error_rate'] = demo_df.apply(get_error_rate, axis=1, unit=unit)
    ax = demo_df.sort_values(unit+'_error_rate').plot.bar(y=unit+'_error_rate', rot=0)
    plt.title('Effect of *' + demographic_class.upper() + '* on '
              + unit.upper() + ' Error Rate in ' + user_file.upper())
    plt.ylabel('Average Percentage (%) ' + unit +'_error_rate' + ' for Population')
    plt.xlabel(demographic_class + ' of Talker')
    plt.show()

        
def print_args_error(error):
    print("\n","ERROR: `detect_bias.py` requires **three** positional arguments, at least one of them is", error) 

    print(
        '''
        Usage: detect_bias.py ARTIE_CORPUS PREDICTIONS DEMOGRAPHIC
        
        ARTIE_CORPUS: string: the path to the artie-bias-corpus.tsv file provided in this repo under data/.
        PREDICTIONS:  string: prediction TSV(s) for the models you wish to compare. If more than one, then comma-separated
        DEMOGRAPHIC:  string: the demographic(s) used for comparison.  If more than one, then comma-separated
                              ['male', 'female', 'indian', 'england', 'twenties', 
                               'thirties', etc. - consult the README for a full list]

        e.g.:  $ ./detect_bias.py "artie-bias-corpus.tsv" "your-model-predictions.tsv" "male,female"
        '''
        #UNIT:         string: 'word' for Word Error Rate comparison, and 'char' for Character Error Rate comparison.
    )


def check_args(user_files,artie_data,unit,demographics):
    '''
    a function to check all the input arguments and throw errors if needed
    '''
    if len(user_files)>2:
        print('''
        ERROR: You are trying to compare more than two models. 
               This is not currently supported. You should make changes
               to the main() function call to suit your needs.
              ''')
        exit(1)
    bool_exist=[os.path.isfile(i) for i in user_files]
    bool_exist.append(os.path.isfile(artie_data))
    if sum(bool_exist)<(len(user_files)+1):
        print("Provided Args: ", artie_data, unit, user_files, demographics)
        print_args_error("invalid")
        exit(1)
    if not (unit in ["char","word"]):
        print('ERROR: unit must be either "char" or "word", not', unit)
        exit(1)
    return True



if __name__ == '__main__':
    import sys
    import os

    try:
        artie_data = sys.argv[1]
        user_files = [ i.strip() for i in str(sys.argv[2]).split(",") ]
        demographics = [ i.strip() for i in str(sys.argv[3]).split(",") ]
        unit = "word" # TODO make this an optional CL arg
    except IndexError:
        print_args_error("missing")
        exit(1)

    check_args(user_files,artie_data,unit,demographics)
        
    ## COMPARE TWO DEMOGRAPHICS
    if len(demographics)>1 and len(user_files)==1:
        print("BEGIN BIAS DETECTION in", user_files[0])
        
        pred_df = get_merged_df(artie_data, user_files[0])
        detect_bias_in_one_model(unit, demographics, pred_df)
        pred_dfs=[pred_df]
        
    ### COMPARE TWO MODELS
    elif len(demographics)==1 and len(user_files)>1:
        print("BEGIN MODEL COMPARISON of", user_files)
        
        pred_dfs = [ get_merged_df(artie_data, user_file)
                     for user_file in user_files]
        compare_two_models(unit, demographics[0], pred_dfs)

    else:
        print('''
        ERROR: Currently you can only compare two models 
               along one demographic line, or one model along two demographics.
               If you want to do something else you can make changes to the code.
        ''')
        exit(1)

    vizualize=True
    if vizualize:
        for i,pred_df in enumerate(pred_dfs):
            
            plot_demographic_error(pred_df,unit,demographics[0],user_files[i])

