# -*- coding: utf-8 -*-
import re
import os
from math import log

class TextAnalyzer:
  def __init__(self, training_path):
    self.pos_words = self.rateWords(training_path + 'pos/')
    self.neg_words = self.rateWords(training_path + 'neg/')
    self.vocabulary = set(self.neg_words.keys()).union(set(self.pos_words.keys()))

  def __getStopWords(self, filepath):
    f = open(filepath, 'r')
    stop_words = set(f.read().split())
    return stop_words

  def __countAllFiles(self, start_path):
    # Start_path is the path data/subset/train/pos/ for example
    count = 0
    for folder in os.listdir(start_path):
      count += len(os.listdir(start_path+folder))
    return count

  def __pruneWordCount(self, wordCount, upperLimit):
    # Dictionary builder notation, elements is only included if the if-statement evaluates to True
    return {k: v for k, v in wordCount.iteritems() if v > upperLimit}

  def __n_grams(self, words, n):
    n_grams = []
    for i in xrange(len(words)-n):
      cur_gram = ''
      for m in xrange(n):
        cur_gram += words[i+m]
        if m != n-1:
          cur_gram += '_'
      n_grams.append(cur_gram)
    return n_grams

  def readFromFile(self, filepath):
    f = open(filepath, 'r')
    # Read the file, split it, keep only the alphanumerical characters of the lowered string with regex and make it a set to remove dupes.
    words = map(lambda w: re.sub(r'\W+', '', w.lower()), f.read().split())
    words.extend(self.__n_grams(words, 2))
    words.extend(self.__n_grams(words, 3))
    # Remove dem stop_words and return it
    return set(words) - self.__getStopWords('./data/stop_words.txt')

  def mostPopularWords(self, start_path):
    files = os.listdir(start_path)
    totalCount = self.__countAllFiles(start_path+'../')
    wordCount = {}
    for f in files:
      for w in self.readFromFile(start_path+f):
          try:
            wordCount[w] += 1
          except KeyError:
            wordCount[w] = 1
    wordCount = {k: v/float(totalCount) for k, v in wordCount.iteritems()}
    # Prune it, sort it (descending in popularity) and return the 25 most popular ones
    return sorted(self.__pruneWordCount(wordCount, 0.02), key=wordCount.get, reverse=True)[:25]

  def rateWords(self, start_path):
    # This method does basically the same as the one above, except it doesnt return a sorted list. It returns a dictionary used for looking up when classifying a file
    files = os.listdir(start_path)
    totalCount = self.__countAllFiles(start_path+'../')
    wordCount = {}
    for f in files:
      for w in self.readFromFile(start_path+f):
          try:
            wordCount[w] += 1
          except KeyError:
            wordCount[w] = 1
    wordCount = {k: v/float(totalCount) for k, v in wordCount.iteritems()}
    # Prune it and return it
    return self.__pruneWordCount(wordCount, 0.02)

  def __getWordsFromFile(self, filepath):
    f = open(filepath, 'r')
    words = map(lambda w: re.sub(r'\W+', '', w.lower()), f.read().split())
    return (set(words).difference(self.__getStopWords('./data/stop_words.txt'))).intersection(self.vocabulary)

  def classifyFile(self, filepath):
    posScore = 0
    negScore = 0
    for word in self.readFromFile(filepath):
      if word in self.pos_words.keys():
        posScore += log(self.pos_words[word])
      if word in self.neg_words.keys():
        negScore += log(self.neg_words[word])
    return 'pos' if posScore < negScore else 'neg'

  def testIt(self, path_to_test):
    correct = 0
    posCorrect = 0
    negCorrect = 0
    totalCount = self.__countAllFiles(path_to_test)
    for folder in os.listdir(path_to_test):
      for f in os.listdir(path_to_test+folder):
        if self.classifyFile(path_to_test+folder+'/'+f) == folder:
          correct += 1
          if folder == 'pos':
            posCorrect += 1
          else:
            negCorrect += 1
    print('Positive, Negative - success ratio')
    print(posCorrect/(float(totalCount/2)), negCorrect/(float(totalCount/2)))

    print(correct, totalCount)
    return correct/float(totalCount)




t = TextAnalyzer('data/subset/train/')
print(t.testIt('data/subset/test/'))
