#!/bin/bash

DEMODIR=`pwd -P`
export PYTHONPATH=$DEMODIR/bin/word2vec/
python $PYTHONPATH/my_word2vec.py\
  $DEMODIR/input/sample-training-file.txt\
  $DEMODIR/input/sample-word-vectors-trained-by-word2vec.txt\
  100