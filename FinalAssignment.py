"""
This is a project designed to make text sentiment analysis. This is project which aims only the text data.
"""

from textblob import TextBlob # Importing Textblob
from newspaper import Article # Importing newspaper
import nltk # Importing NTLK

nltk.download('punkt')

url = 'https://www.nbcnews.com/news/world/live-blog/morocco-earthquake-live-updates-death-toll-aid-rcna104569' # Article URL
article = Article(url) # Define article with the Artcle URL as parameter of the Article() function.

# with open('test.txt', 'r') as f:
#     text = f.read()

# text = input('How do you feel about the product: ')

article.download() # Download the article
article.parse() # Parse the article 
article.nlp()

text = article.summary # Summarize the article content. Making it easier to be analyzed
print("", text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)

if sentiment > 0:
    print("positive")

elif sentiment < 0:
    print("negative")

else:
    print("neutral")
