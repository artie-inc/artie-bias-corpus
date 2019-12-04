#!/bin/bash

python3 -m venv /tmp/venv
source /tmp/venv/bin/activate
pip install -r ../requirements.txt

echo "BEGIN *SINGLE* MODEL TESTS"
#single model success
python ../detect_bias.py ../artie-bias-corpus.tsv "word" ../predictions/official-v0.5.1-predictions.tsv "male,female" >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "char" ../predictions/official-v0.5.1-predictions.tsv "male,female" >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "word" ../predictions/official-v0.5.1-predictions.tsv "us,indian" >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "char" ../predictions/official-v0.5.1-predictions.tsv "us,indian" >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
# single model fail
python ../detect_bias.py ../artie-bias-corpus.tsv "char" "foo" "male,female" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "foo" ../predictions/official-v0.5.1-predictions.tsv "male,female" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py "foo" "char" ../predictions/official-v0.5.1-predictions.tsv "male,female" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "char" ../predictions/official-v0.5.1-predictions.tsv "male,foo" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "char" ../predictions/official-v0.5.1-predictions.tsv "foo,female" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "char" "foo" "male,female" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;

echo "BEGIN *DOUBLE* MODEL TESTS"
#double model pass
python ../detect_bias.py ../artie-bias-corpus.tsv "char" "../predictions/official-v0.5.1-predictions.tsv,../predictions/official-v0.6.0-predictions.tsv" female >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "word" "../predictions/official-v0.5.1-predictions.tsv,../predictions/official-v0.6.0-predictions.tsv" male >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "char" "../predictions/official-v0.5.1-predictions.tsv,../predictions/official-v0.6.0-predictions.tsv" us >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "word" "../predictions/official-v0.5.1-predictions.tsv,../predictions/official-v0.6.0-predictions.tsv" indian >/tmp/log; if [ $? -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi;
#double model fail
python ../detect_bias.py ../artie-bias-corpus.tsv "foo" "../predictions/official-v0.5.1-predictions.tsv,../predictions/official-v0.6.0-predictions.tsv" female >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "char" "../predictions/official-v0.5.1-predictions.tsv,../predictions/official-v0.6.0-predictions.tsv" "female,male" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "word" "../predictions/official-v0.5.1-predictions.tsv,foo" "female,male" >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
python ../detect_bias.py ../artie-bias-corpus.tsv "word" "../predictions/official-v0.5.1-predictions.tsv,../predictions/official-v0.6.0-predictions.tsv" foo >/tmp/log; if [ $? -eq 1 ]; then echo "PASS"; else echo "FAIL"; fi;
