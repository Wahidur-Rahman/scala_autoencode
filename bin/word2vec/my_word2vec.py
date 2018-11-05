#!/usr/bin/python

import warnings

import argparse

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import word2vec
import logging


def readfile(file_name):
    """
    read the data in the file and load it into an array
    :param file_name:
    :return: an array of string
    """
    fp = open(file_name)
    content = fp.read()
    fp.close()
    content = content.replace("\n", "")
    data = []
    data.append(content.split())
    return data


if __name__ == '__main__':
    """
    word embedding
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('src', help='input file, each line is a phrase')
    parser.add_argument('out', help='word vector file')
    parser.add_argument('size', help='word embedding size')
    options = parser.parse_args()
    logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
    data = readfile(options.src)
    size = int(options.size)
    model = word2vec.Word2Vec(data, size, window=10, sample=1e-4, hs=1,negative=0, min_count=1, sg=0,iter=20)
    model.wv.save_word2vec_format(options.out, binary=False)
