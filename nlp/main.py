from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

porter = PorterStemmer()
lancaster = LancasterStemmer()

def stemmers():

    words = ['friend', 'friendship', 'stabil', 'destabilize',
             'misunderstanding', 'railroad', 'moonlight', 'football']


    print("{0:20}{1:20}{2:20}".format(
        'WORD', 'PORTER STEMMER', 'LANCASTER STEMMER'))
    print('---------------------------------------------------------')

    for word in words:
        print("{0:20}{1:20}{2:20}".format(
            word, porter.stem(word), lancaster.stem(word)))


def stemSentence(sen):
    token_words = word_tokenize(sen)
    stem_sen = []

    for word in token_words:
        stem_sen.append(porter.stem(word))
        stem_sen.append(" ")

    return "".join(stem_sen)

sen = ''

import nltk 

print(nltk.corpus.gutenberg.fileids(), end=' ')