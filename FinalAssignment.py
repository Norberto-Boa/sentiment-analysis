from textblob import TextBlob
from newspaper import Article
import nltk

# url = 'https://www.nbcnews.com/news/world/live-blog/morocco-earthquake-live-updates-death-toll-aid-rcna104569'
# article = Article(url)

# with open('test.txt', 'r') as f:
#     text = f.read()

text = input('How do you feel about the product: ')

# article.download()
# article.parse()
# article.nlp()

# text = article.summary
# print(""text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)

if sentiment > 0:
    print("positive")

elif sentiment < 0:
    print("negative")

else:
    print("neutral")
