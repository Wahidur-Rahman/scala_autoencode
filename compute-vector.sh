#!/bin/bash
DEMODIR=`pwd -P`
export PYTHONPATH=$DEMODIR/bin/str2vec/src
python $PYTHONPATH/nn/rae.py\
  $DEMODIR/input/sample-training-file.txt\
  $DEMODIR/input/sample-word-vectors-trained-by-word2vec.txt\
  $DEMODIR/output/sample-training-file.mpi-2.model.gz\
  $DEMODIR/output/sample-training-file.vec.txt
