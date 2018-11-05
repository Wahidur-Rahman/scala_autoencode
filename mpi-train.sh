#!/bin/bash
if [ $# -ne 1 ]
then
  echo "Usage: $0 coreNum"
  exit -1
fi

N=$1
DEMODIR=`pwd -P`
export PYTHONPATH=$DEMODIR/bin/str2vec/src
mpirun -n $1 -mca btl ^openib  python $PYTHONPATH/nn/lbfgstrainer.py\
  -instances $DEMODIR/input/sample-training-file.txt\
  -model $DEMODIR/output/sample-training-file.mpi-$N.model.gz\
  -word_vector $DEMODIR/input/sample-word-vectors-trained-by-word2vec.txt\
  -lambda_reg 0.15\
  -m 2
