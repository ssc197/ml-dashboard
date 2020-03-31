import urllib.request
from bs4 import BeautifulSoup
from unidecode import unidecode
import warnings
import nltk
import gensim
from gensim import corpora
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
from models.utils import cleanData, tokenizeData, stuff_to_be_removed
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import matplotlib.colors as mcolors
nltk.download('words')

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64 
from nltk.corpus import stopwords
from string import punctuation
stuff_to_be_removed = list(stopwords.words("english"))+list(punctuation)
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 


def fetchData(query):
    _abc = []  
    for j in search(query, tld="com", num=20, stop=5, pause=2): 
        req = urllib.request.Request(j,headers={'User-Agent': 'Mozilla/5.0'} )
        response = urllib.request.urlopen(req)
        the_page = response.read() 
        soup = BeautifulSoup(the_page, 'lxml')
        for p in soup.find_all("p"):
            text = p.text.lower()
            _abc.append(text)
    #final_text = cleanData(_abc)
    final_text = [cleanData(s) for s in _abc]
    
    final_text = [y for y in final_text if y not in stuff_to_be_removed]
    #final_text = tokenizeData(_abc)
    final_text = [tokenizeData(s) for s in final_text]
    _image = initializeModelwithTopicModel(final_text)
    return _image

#fetchData(query)
    
cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]  # more colors: 'mcolors.XKCD_COLORS'
def initializeModel(final_data):
    final_data = " ".join(final_data)
    wordcloud = WordCloud(stopwords=stuff_to_be_removed,width=200, height=200, background_color="white" ,random_state=21, max_font_size=300).generate(final_data)
    # plot wordcloud
    fig = plt.figure(figsize=(12,8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    plt.tight_layout()
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String+= base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String

def initializeModelwithTopicModel(final_data):
    id2word = corpora.Dictionary(final_data)
    mycorpus = [id2word.doc2bow(s) for s in final_data]
    lda_model = gensim.models.ldamodel.LdaModel(corpus=mycorpus,
                                               id2word=id2word,
                                               num_topics=4, 
                                               random_state=42,
                                               update_every=1,
                                               chunksize=100,
                                               passes=10,
                                               alpha='auto',
                                               per_word_topics=True)
    
    cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]  # more colors: 'mcolors.XKCD_COLORS'

    cloud = WordCloud(stopwords=stuff_to_be_removed,
                      background_color='white',
                      max_words=10,
                      colormap='tab10',
                      color_func=lambda *args, **kwargs: cols[i],
                      prefer_horizontal=1.0)
    
    topics = lda_model.show_topics(formatted=False)
    
    fig, axes = plt.subplots(2 ,2 , figsize=(10,10), sharex=True, sharey=True)
    
    for i, ax in enumerate(axes.flatten()):
        fig.add_subplot(ax)
        topic_words = dict(topics[i][1])
        cloud.generate_from_frequencies(topic_words, max_font_size=300)
        plt.gca().imshow(cloud,interpolation='bilinear')
        plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
        plt.gca().axis('off')
    
    
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.axis('off')
    plt.margins(x=0, y=0)
    plt.tight_layout()

    
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String+= base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String
#fetchData("apple")