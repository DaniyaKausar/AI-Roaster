import random
from textblob import TextBlob
from compliment_bank import positive_compliments, neutral_compliments, negative_comforts
def detect_sentiment(text):
    blob=TextBlob(text)
    polarity=blob.sentiment.polarity
    if polarity >0.3:
        return "positive"
    elif polarity<-0.1:
        return "negative"
    else:
        return "neutral"
def sweet_sentiment_compliment(user_input, override_sentiment=None):
    user_input=user_input.strip()
    if not user_input:
        return "No compliment for silence, say something sweet"
    if isinstance(override_sentiment, float):
        if  override_sentiment>0.3:  
            sentiment="positve" 
        elif  override_sentiment<-0.1:
            sentiment="negative"
        else:
            sentiment="neutral"
    else:
        sentiment=detect_sentiment(user_input)               
    if sentiment=="positive":
        compliment_list=positive_compliments
    elif sentiment=="negative":
        compliments_list=negative_comforts
    else:
        compliments_list=neutral_compliments
    compliments=random.choice(compliments_list)
    return compliments
   