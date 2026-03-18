#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install textblob


# In[ ]:


python -m textblob.download_corpora


# In[3]:


from textblob import TextBlob
# defining
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
 #condition
    if sentiment_score > 0:
        sentiment = "Positive 😊"
    elif sentiment_score < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
    
    return sentiment, sentiment_score

# Example usage
print("=== Sentiment Analyzer ===")
user_input = input("Enter your text: ")
result, score = analyze_sentiment(user_input)

print(f"\nSentiment: {result}")
print(f"Polarity Score: {score}")
