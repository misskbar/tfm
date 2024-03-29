from __future__ import division

__author__ = 'shekhargulati'

import inspect, os

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

POS_WORDS_FILE = os.path.join(path + '/Palabras-Espanol', 'palabras-positivas.txt')
NEG_WORDS_FILE = os.path.join(path + '/Palabras-Espanol', 'palabras-negativas.txt')

pos_words = []
neg_words = []

for pos_word in open(POS_WORDS_FILE, 'r', encoding='utf-8',
                 errors='ignore').readlines()[35:]:
    pos_words.append(({pos_word.rstrip(): True}, 'positive'))

for neg_word in open(NEG_WORDS_FILE, 'r', encoding='utf-8',
                 errors='ignore').readlines()[35:]:
    neg_words.append(({neg_word.rstrip(): True}, 'negative'))

print ("First 5 positive words %s " % pos_words[:5])
print ("First 5 negative words %s" % neg_words[:5])

print ("Number of positive words %d" % len(pos_words))

print ("Number of negative words %d" % len(neg_words))

all_words_with_sentiment = pos_words + neg_words

print ("Total number of words %d" % len(all_words_with_sentiment))

from nltk.classify import NaiveBayesClassifier

classifier = NaiveBayesClassifier.train(all_words_with_sentiment)


def to_dictionary(words):
    return dict([(word, True) for word in words])


test_data = []


def predict_sentiment(text, expected_sentiment=None):
    text_to_classify = to_dictionary(text.split())
    result = classifier.classify(text_to_classify)
    test_data.append([text_to_classify, expected_sentiment])
    return result


TEST_FILE = os.path.join(path, 'test.txt')

import collections

import nltk.classify
import nltk.metrics


def run_sentiment_analysis_on_rt():
    rt_positive_reviewers = open(TEST_FILE, 'r')

    expected_pos_set = collections.defaultdict(set)
    actual_pos_set = collections.defaultdict(set)

    for index, review in enumerate(rt_positive_reviewers.readlines()):
        expected_pos_set['positive'].add(index)
        actual_sentiment = predict_sentiment(review, 'positive')
        actual_pos_set[actual_sentiment].add(index)

    print ("Total Negative found in positive reviews %s" % len(actual_pos_set['negative']))

    rt_negative_reviews = open(TEST_FILE, 'r')

    expected_neg_set = collections.defaultdict(set)
    actual_neg_set = collections.defaultdict(set)

    for index, review in enumerate(rt_negative_reviews.readlines()):
        expected_neg_set['negative'].add(index)
        actual_sentiment = predict_sentiment(review, 'negative')
        actual_neg_set[actual_sentiment].add(index)

    print ("Total Positive found in negative reviews %s" % len(actual_neg_set['positive']))

    print ('accuracy: %.2f' % nltk.classify.util.accuracy(classifier, test_data))
    print ('pos precision: %.2f' % nltk.metrics.precision(expected_pos_set['positive'], actual_pos_set['positive']))
    print ('pos recall: %.2f' % nltk.metrics.recall(expected_pos_set['positive'], actual_pos_set['positive']))
    print ('neg precision: %.2f' % nltk.metrics.precision(expected_neg_set['negative'], actual_neg_set['negative']))
    print ('neg recall: %.2f' % nltk.metrics.recall(expected_neg_set['negative'], actual_neg_set['negative']))

run_sentiment_analysis_on_rt()