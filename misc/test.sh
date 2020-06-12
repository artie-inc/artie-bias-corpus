#!/bin/bash

python3 -m venv /tmp/venv
source /tmp/venv/bin/activate
pip install -r ../requirements.txt

echo "BEGIN *SINGLE* MODEL TESTS"
#single model success
python ../detect_bias.py ../data/artie-bias-corpus.tsv ../predictions/deepspeech/v0-5-1.tsv "male,female" >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../data/artie-bias-corpus.tsv ../predictions/deepspeech/v0-5-1.tsv "us,indian" >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
# single model fail
python ../detect_bias.py ../data/artie-bias-corpus.tsv "foo" "male,female" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py "foo" ../predictions/deepspeech/v0-5-1.tsv "male,female" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../data/artie-bias-corpus.tsv ../predictions/deepspeech/v0-5-1.tsv "male,foo" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../data/artie-bias-corpus.tsv ../predictions/deepspeech/v0-5-1.tsv "foo,female" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../data/artie-bias-corpus.tsv "foo" "male,female" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;

echo "BEGIN *DOUBLE* MODEL TESTS"
#double model pass
python ../detect_bias.py ../data/artie-bias-corpus.tsv "../predictions/deepspeech/v0-5-1.tsv,../predictions/deepspeech/v0-6-0.tsv" female >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../data/artie-bias-corpus.tsv "../predictions/deepspeech/v0-5-1.tsv,../predictions/deepspeech/v0-6-0.tsv" male >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../data/artie-bias-corpus.tsv "../predictions/deepspeech/v0-5-1.tsv,../predictions/deepspeech/v0-6-0.tsv" us >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../data/artie-bias-corpus.tsv "../predictions/deepspeech/v0-5-1.tsv,../predictions/deepspeech/v0-6-0.tsv" indian >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
#double model fail
python ../detect_bias.py ../data/artie-bias-corpus.tsv "../predictions/deepspeech/v0-5-1.tsv,../predictions/deepspeech/v0-6-0.tsv" "female,male" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../data/artie-bias-corpus.tsv "../predictions/deepspeech/v0-5-1.tsv,foo" "female,male" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../data/artie-bias-corpus.tsv "../predictions/deepspeech/v0-5-1.tsv,../predictions/deepspeech/v0-6-0.tsv" foo >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
