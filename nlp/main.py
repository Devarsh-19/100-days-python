from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()


words = ['friend', 'friendship', 'stabil', 'destabilize', 'misunderstanding', 'railroad', 'moonlight', 'football']


print("{0:20}{1:20}{2:20}".format('WORD', 'PORTER STEMMER', 'LANCASTER STEMMER'))
print('---------------------------------------------------------')

for word in words:
    print("{0:20}{1:20}{2:20}".format(word, porter.stem(word), lancaster.stem(word)))