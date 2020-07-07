# Artie Bias Corpus

This repo includes text and code relating to the Artie Bias Corpus, and is intended for detecting demographic bias in ASR systems.

### Requirements

You need three things to use this code:

1. Your ASR model's predictions on the audio of the Artie Bias Corpus.
2. The `artie-bias-corpus.tsv` file of ground-truth transcriptions.
3. The `detect_bias.py` script.


### What is Possible with this Code

1. Detect bias in a single model between two demographic groups.
2. Compare two models in their performance on a single demographic group.


## How to Run the Code

We recommend using a virtual environment to make life easier.

```
$ python3 -m venv artie
$ source artie/bin/activate
(artie) $ pip install -r requirements.txt
```
Once you have the proper environment, you can perform the following two analyses on any models and demographics in the corpus:

1. Finding bias in a single model (male vs female):

```
(artie) $ python detect_bias.py "data/artie-bias-corpus.tsv" "model_A_predictions.tsv" "male,female"
```

2. Finding difference between two models (for female voices):

```
(artie) $ python detect_bias.py "data/artie-bias-corpus.tsv" "model_A_predictions.tsv,model_B_predictions.tsv" "female"
```


## Your Model Predictions Format

When you provide the predictions of your model(s) on the Artie Bias Corpus, those files should be two-columns and contain Tab Separated Values (TSV). The header for the first column should be `"path"` and the header for the second column should be `"prediction"`. Take a look at the included predictions in the `predictions` directory for an example.

```
$ head model_A_predictions.tsv
path	prediction
common_voice_en_18421078.wav	it amazing she said drinking me in and more
common_voice_en_12197.wav	a very company we for man and woman posing rounded the bay several of her women
common_voice_en_673730.wav	basketball player in blue is attempting to block a player in white during the game
common_voice_en_606947.wav	a buried man in green coat tails into the camera is
common_voice_en_648457.wav	a bird is birth or line of some sort attached to pull
common_voice_en_675200.wav	the gratification and atone
common_voice_en_221209.wav	a blond girl posed for a picture at carry park in that
common_voice_en_479225.wav	a boy or two as parlors
common_voice_en_191986.wav	a boy is hanging on monkey bears
```

### Verifying your setup

To test your setup, run the `test.sh` script from within the `misc` directory.

```
misc$ ./test.sh
```

If you see only `PASS` you're OK. If you see some `FAIL`s, you will need to dig into the `test.sh` script identify the problem.


# How we made the Artie Bias Corpus 

We took two main steps to create the ABC. First we filtered data of interest from Common Voice. Second, we re-validated the data.

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

### Total number of Clips
```
1712 utterances
970 speakers
```

### Ages
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

### Genders
```
$ cut -d"   " -f 7 artie-bias-corpus.tsv | sort | uniq -c
    257 female
      1 gender
   1431 male
     20 NA
      4 other
```

### Accents
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

### Artie Bias Corpus Format

You should use the provided `artie-bias-corpus.tsv` file provided in this repo. It has the following column structure:

```
client_id	path	sentence	up_votes	down_votes	age	gender	accent
01a44ed5d1339a03c5f65cb467a609e63b71ed24c761cabf3bba66be59c92418e0313dce376ec5e11d6b209f9314ffd3bd8ff629e559dddb9911bc4cb13f9b9f	common_voice_en_17779714.mp3	Two-wave sources are perfectly coherent if they have a constant phase difference and the same frequency.20	thirties	male	canada
032083e1375f0a0fc284ab394bd184aa293b8fdb6af5a6f73a0fac36acad718dd7a42c682e3b8b323d901afbd749cfc261877ca94ab3a7df1e68ef8f92124e75	common_voice_en_18275190.mp3	This fiscal year.	2	0	twenties	male	NA
051427aae19a8edb1ecc7e438a117f63fc3358f1fd9d5ba9e35636bf8dfff88332469860d6c192fb09d67eaf614ca6916b0405adb4becfce54c8f274da1e999c	common_voice_en_125399.mp3	Thai dancers happily going through their steps in unison.	2	1	seventies	female	england
059a80ab35ec3e57e6746df0ffcb4cdcea4871d4819cb3796e1d12908c30265c208797a64e62c60509eeece846b775248462b6d0b57c8d7ae74f056fdacdfd6d	common_voice_en_18274221.mp3	It is entirely your prerogative.	2	1	twenties	male	us
06546553aed17027b4e638d4afb56f39b216026088cf4048ce8dc0b81e4dc211f5b5edbd1d78c5c63394d844db1f0a361ca8a9ed79f2fb2d8dd4a50fedea7fa4	common_voice_en_17147389.mp3	Women form less than half of the group.	2	0	twenties	male	us
07df65e4465dbe1499668503f5f4446042b86e0403ede1defe56196a7cd4ba6893af79881a15b481384338c24e5e9dc5f3ab0f1ab8e9c5416cc1ecd6f910c58b	common_voice_en_534327.mp3	Plastic surgery has become more popular.	2	0	fourties	female	us
08d5df578ef5c27af11465120a91b016ad09e4d6f9bfb01860f65c16b125349755b03a995e9cbe07e1cf5bfdd69da45249368a2b4653350591b2f24153b12d41	common_voice_en_459460.mp3	What game do you want to play?	2	0	twenties	male	NA
093580a6c59fa73c86513a8a98ce889f6418871e62b673ee1b42f771bb00bfa4a3113b7132c114db2e9508e82470ff1c2b24596287d2b03b70d010163300006f	common_voice_en_18506358.mp3	Are the main galleries any good?	2	0	twenties	male	indian
0cc15679f23808650907f621dcc48e480516aebf6bfc0aee186de287f2ce87581ca9380529569f95fb46f885ee817d3902bb70a8f1a96b86415a59e76c356b48	common_voice_en_18171738.mp3	What do you know about him?	2	0	teens	female	us
```
