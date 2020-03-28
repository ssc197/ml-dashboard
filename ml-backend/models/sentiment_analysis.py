from textblob import TextBlob
from models.utils import cleanData, tokenizeData, stuff_to_be_removed

def checkTheSentiment(text):
    testimonial = text
    sentiment = {'sentiment' : 0}
    testimonial = cleanData(testimonial)
        
    testimonial = str(tokenizeData(testimonial))
    testimonial= TextBlob(testimonial)
    if testimonial.sentiment.polarity < 0:
       sentiment['sentiment'] = -1   #Negavtive
    elif testimonial.sentiment.polarity > 0:
        sentiment['sentiment'] =  1     #Postive
    else:
        sentiment['sentiment'] =  0      #Neutral
        

    return sentiment