from bs4 import BeautifulSoup
from unidecode import unidecode
import re
import warnings
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem.porter import *
from string import punctuation
from nltk.stem import WordNetLemmatizer 
from matplotlib import pyplot as plt
nltk.download('words')

stuff_to_be_removed = stop_words = list(punctuation)+['``', "'s", "..."]+['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'don', 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y',  'ma', 'mightn', 'needn', 'shouldn', "shouldn't"]
lemmatizer = WordNetLemmatizer()
words = set(nltk.corpus.words.words())


_url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
# function to remove user handles
SMILEY = {
':-)' :  'grin',
    ':lol:' :  'LOL',
    ':(':'sad',
        ':((':'sad',
        ':(((':'sad',
    ':cheese:' :  'cheese',
    ':)' :  'smile',
    ':]' :  'smile',
    ':))' : 'really launghing',
    ':)))' : 'really launghing',
    ':))))' : 'really launghing',
    ';-)' :  'wink',
    ':3'  : 'curly lips',
    ';)' :  'wink',
    ':/': 'unsure',
    ':*' : 'kiss',
    ':-*' : 'kiss',
     ':-/': 'perplexed',
    '8-)'  : 'glasses',
    '8)'  : 'glasses',
    'B|' : 'sunglasses',
    'B-|' : 'sunglasses',
    '8|' : 'sunglasses',
    '8-|' : 'sunglasses',
    '>:O'  : 'upset',
    '>:-O'  : 'upset',
    '>:-O'  : 'upset',
     '>:-O'  : 'upset',
    'o.O' : 'confused',
    'O.o' : 'confused',
    '(^^^)' : 'shark',
    ':v'  : 'pacman',
    '-_-'  : 'squint',
    'O:)' : 'angel',
    'O:-)' : 'angel',
    '3:)': 'devil',
    '3:-)': 'devil',
    ":'(" : 'cry',
    ':|]' : 'robot',
    '<3'  : 'heart',
    '(Y)':'Thumbs Up',
    '^_^' : 'happy',
    ':smirk:' :  'smirk',
    ':roll:' :  'rolleyes',
    ':-S' :  'confused',
    ':-??' : 'confused',
    ':wow:' :  'surprised',
    ':P' :  'playful',
    ':-P' : 'playful',
    ':ohh:' :  'ohh',
    ':grrr:' :  'grrr',
    ':gulp:' :  'gulp',
    ':down:' :  'downer',
    ':sick:' :  'sick',
    ':-/' :  'hmmm',
    '>:(' :  'mad',
    ':mad:' :  'mad',
    '>:-(' :  'angry',
    ':angry:' :  'angry',
    ':zip:' :  'zipper',
    ':kiss:' :  'kiss',
    ':ahhh:' :  'shock',
    ':vampire:' :  'vampire',
    ':snake:' :  'snake',
    ':exclaim:' :  'excaim',
    ':question:' :  'question',
        ':coolsmile:' :  'cool smile',
    ':coolsmirk:' :  'cool smirk',
    ':coolgrin:' :  'cool grin',
    ':coolhmm:' :  'cool hmm',
    ':coolmad:' :  'cool mad',
    ':coolcheese:' :  'cool cheese',
        '8-/' :  'oh oh',
            ':shut:' :  'shut eye',
                ':red:' :  'red face',
                    ':blank:' :  'blank stare',
    ':long:' :  'long face',
        ':bug:' :  'big surprise',
    ':-P' :  'tongue laugh',
    '%-P' :  'tongue rolleye',
    ';-P' :  'tongue wink'
}

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase
    
def remove_pattern (input_txt , pattern):
    r = re.findall(pattern, str(input_txt))
    print(r)
    # remove user handles
    for match in r:
        input_txt= re.sub(match, '', str(input_txt))
    return input_txt

def remove_non_ascii1(text):
    input_txt = ''.join([i if ord(i) < 128 else ' ' for i in text])
    input_txt = re.sub(r'[^\x00-\x7F]+','', input_txt)
    return input_txt


def handleSmiley(tweet):
    words = tweet.split()
    reformed = [SMILEY[word] if word in SMILEY else word for word in words]
    tweet = " ".join(reformed)
    return tweet

_regex =["_", "\\" "#","http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))"]

def cleanData(data):
    for reg in _regex:
        data= remove_pattern(data, reg)
        
    data = remove_non_ascii1(str(data))
    data = BeautifulSoup(data, "lxml").text  #remove html enuty
    data = handleSmiley(data) #Handled SMileys

    return data

def tokenizeData(_data):
    _data = str(_data)
    _data = _data.lower() 
    _data= nltk.word_tokenize(_data)
    _data = [word for word in _data if len(word) > 2]
    _data = [word for word in _data if word not in stuff_to_be_removed]
    _data = [decontracted(p) for p in _data]
    
    # lemmatizing words
    lamme = WordNetLemmatizer()
    # stemming words
    _data= [lamme.lemmatize(i) for i in _data]

    #_data = unidecode(_data)
    #_data = [t for t in _data if not any(c.isdigit() for c in t)]

    return _data