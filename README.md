# Artie Bias Corpus + Tools

This repo includes processed transcrtipts and tools for the Artie Bias Corpus. You can download the audio and original transcripts of the corpus here [[0](http://ml-corpora.artie.com/artie-bias-corpus.tar.gz)]. The intended use of both the code and the data is to detect demographic bias in speech technology systems. You can find more information in the blog post [[1](https://www.artie.com/blog/the-artie-bias-corpus)] or the academic publication [[2](http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.796.pdf)].

## Datasheet

You may find the Artie Bias Corpus [Datasheet](/data/DATASHEET.md) in the `data/` directory. Please review before use.


# Using the Tools

You can use the corpus and these tools to perform one of two tasks:

1. Detect bias in a single model between two demographic groups.
2. Compare two models in their performance on a single demographic group.

## Requirements

You need three things to use this code:

1. Your ASR model's predictions on the audio of the Artie Bias Corpus.
2. The `artie-bias-corpus.tsv` file of ground-truth transcriptions.
3. The `detect_bias.py` script.


### Your Model Predictions Format

When you provide the predictions of your model(s) on the Artie Bias Corpus, those files should be two-columns and contain Tab Separated Values (TSV). The header for the first column should be `"path"` and the header for the second column should be `"prediction"`. Take a look at the included predictions in the `predictions/` directory for an example.

```
$ head your-model-predictions.tsv
path	prediction
common_voice_en_18421078.wav	it amazing she said drinking me in and more
common_voice_en_12197.wav	a very company we for man and woman posing rounded the bay several of her women
common_voice_en_673730.wav	basketball player in blue is attempting to block a player in white during the game
```

## Setup

We recommend using a virtual environment to make life easier.

```
$ python3 -m venv artie
$ source artie/bin/activate
(artie) $ pip install -r requirements.txt
```

### Verifying your setup

To test your setup, run the `test.sh` script from within the `misc` directory.

```
misc$ ./test.sh
```

If you see only `PASS` you're OK. If you see some `FAIL`s, you will need to dig into the `test.sh` script identify the problem.


## Usage

Once you have the proper environment, you can perform the following two analyses on any models and demographics in the corpus:

1. Finding bias in a single model (male vs female):

```
(artie) $ python detect_bias.py "data/artie-bias-corpus.tsv" "model_A_predictions.tsv" "male,female"
```

2. Finding difference between two models (for female voices):

```
(artie) $ python detect_bias.py "data/artie-bias-corpus.tsv" "model_A_predictions.tsv,model_B_predictions.tsv" "female"
```


# Creating the Artie Bias Corpus 

We took two main steps to create the Artie Bias Corpus. First we filtered data of interest from Common Voice. Second, we re-validated the data. You can find more details in the blog post [[1](https://www.artie.com/blog/the-artie-bias-corpus)] or the academic publication [[2](http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.796.pdf)].

## Filtering Common Voice 

- Download and extract the Common Voice release / language of interest.
- Identify the `test.tsv`.
- Filter only utterances with `age` OR `gender` OR `accent`.
- Replace blank entries with `NA` (because `pandas`).

## Artie Validation

- Annotators were trained using the validation criteria found in `misc/VALIDATION_CRITERIA.md`.
- The subset of clips resulting from the previous step was validated via a fork of the Common Voice web-app.
- Clips receiving less than two out of three upvotes were discarded from the corpus.

Additionally, we removed 24 clips given other concerns. 22 clips were removed based on concerns that the speakers were not over 18 years old. 1 clip was removed because the user sang the sentence, and 1 clip was removed for problematic content of the text.


# Distributions in the Artie Bias Corpus

## Unique clips and speakers
```
1712 utterances
970 speakers
```

## Distribution over age
```
$ cut -d"   " -f 6 artie-bias-corpus.tsv | sort | uniq -c
    101 fifties
    152 fourties
     14 NA
      1 nineties
     18 seventies
     46 sixties
    187 teens
    366 thirties
    827 twenties
```

## Distribution over gender
```
$ cut -d"   " -f 7 artie-bias-corpus.tsv | sort | uniq -c
    257 female
   1431 male
     20 NA
      4 other
```

## Distribution over accent
```
$ cut -d"   " -f 8 artie-bias-corpus.tsv | sort | uniq -c
     24 african
     19 australia
     10 bermuda
     42 canada
    131 england
     10 hongkong
    264 indian
     21 ireland
      9 malaysia
    562 NA
     11 newzealand
     24 other
      7 philippines
     12 scotland
      2 singapore
      3 southatlandtic
    558 us
      3 wales
```

## Artie Bias Corpus Format

You should use the provided `artie-bias-corpus.tsv` file provided in this repo. It has the following column structure:

```
client_id	path	sentence	up_votes	down_votes	age	gender	accent
01a44ed5d1339a03c5f65cb467a609e63b71ed24c761cabf3bba66be59c92418e0313dce376ec5e11d6b209f9314ffd3bd8ff629e559dddb9911bc4cb13f9b9f	common_voice_en_17779714.mp3	Two-wave sources are perfectly coherent if they have a constant phase difference and the same frequency.20	thirties	male	canada
032083e1375f0a0fc284ab394bd184aa293b8fdb6af5a6f73a0fac36acad718dd7a42c682e3b8b323d901afbd749cfc261877ca94ab3a7df1e68ef8f92124e75	common_voice_en_18275190.mp3	This fiscal year.	2	0	twenties	male	NA
051427aae19a8edb1ecc7e438a117f63fc3358f1fd9d5ba9e35636bf8dfff88332469860d6c192fb09d67eaf614ca6916b0405adb4becfce54c8f274da1e999c	common_voice_en_125399.mp3	Thai dancers happily going through their steps in unison.	2	1	seventies	female	england
```
