import getData
import getBeWell
import getMindbodygreenData
import getEverydayHealthData
from nltk.corpus import stopwords
from nltk import *
from nltk.tag import pos_tag
import pickle

LOAD_MAMA_WELLNESS = False
SCRAP_MAMA_WELLNESS = False

LOAD_BE_WELL = False
SCRAP_BE_WELL = False

LOAD_MGB = False
SCRAP_MGB = False

LOAD_EVERYDAYHEALTH = True
SCRAP_EVERYDAYHEALTH = False
    

DONT_COMPUTE = False

titles = []

def getProperNoun(tag):
    if(tag[1] == 'NNP'):
        return x[0]
    return None

def getStopWords():

    stop_words_nltk = set(stopwords.words('english'))
    stop_words = stop_words_nltk

    extra_stop_words = open("extra_stop_words.txt", "r")
    for word in extra_stop_words:
        stop_words.add(word.strip())

    return stop_words

def getPosTag(data):
    return pos_tag(data)

stop_words = getStopWords()

if SCRAP_MAMA_WELLNESS == True:
    getData.getBlogLinks()
    titles = getData.all_headings
    data_file = open("mama_wellness.pickle", "wb")
    pickle.dump(titles, data_file)
    data_file.close()
elif( LOAD_MAMA_WELLNESS == True):
    data_file = open("mama_wellness.pickle", "rb")
    titles.extend(pickle.load(data_file))

if SCRAP_BE_WELL == True:
    getBeWell.getBlogLinks()
    titles = getBeWell.all_headings
    data_file = open("be_well.pickle", "wb")
    pickle.dump(titles, data_file)
    data_file.close()
elif( LOAD_BE_WELL == True):
    data_file = open("be_well.pickle", "rb")
    titles.extend(pickle.load(data_file))

if SCRAP_MGB == True:
    getMindbodygreenData.getBlogLinks()
    titles = getMindbodygreenData.all_headings
    data_file = open("mgb.pickle", "wb")
    pickle.dump(titles, data_file)
    data_file.close()
elif( LOAD_MGB == True):
    data_file = open("mgb.pickle", "rb")
    titles.extend(pickle.load(data_file))

if SCRAP_EVERYDAYHEALTH == True:
    getEverydayHealthData.getBlogLinks()
    titles = getEverydayHealthData.all_headings
    data_file = open("everydayhealth.pickle", "wb")
    pickle.dump(titles, data_file)
    data_file.close()
elif( LOAD_EVERYDAYHEALTH == True):
    data_file = open("everydayhealth.pickle", "rb")
    titles.extend(pickle.load(data_file))


########## EXIT #######
if DONT_COMPUTE:
    exit(0)

corpus = ""

corpus = " ".join(titles).lower().split(" ")
filtered_corpus = [w for w in corpus if ((not w in stop_words) and w.isalnum() and not w.isdigit()) ]
fdist = FreqDist(filtered_corpus)

#print titles
print( fdist.most_common(100) )


