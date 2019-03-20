#-*- coding: utf-8 -*-
'''
Training example class
@author: lpeng
'''
import re
class Instance(object):
  '''A reordering training example'''
  
  def __init__(self, words, freq=1):
    '''
    Args:
      words: numpy.array (an int array of word indices)
      freq: frequency of this training example
    '''
    self.words = words
    self.freq = freq

  def __str__(self):
    parts = []
    parts.append(' '.join([str(i) for i in self.words]))
    parts.append(str(self.freq))
    return ' ||| '.join(parts)
    
  @classmethod
  def parse_from_str(cls, line, word_vector):
    '''The format of the line should be like the following:
       src_word1, src_word2,..., src_wordn ||| freq
       freq is optional
    '''
    indices = [m.start() for m in re.finditer(' ||| ', line)]
    pos = line.find(' ||| ')
    if (len(indices) > 1):
      pos = indices[-1]
    
    words = [word_vector.get_word_index(word) for word in line[0:pos].split()]
    if pos >= 0:
      try:
        freq = int(line[pos+5:])
      except:
        freq = 1
    #  freq = int(line[pos+5:])
    else:
      freq = 1

    return Instance(words, freq)
