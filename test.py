from textblob import TextBlob # Importing Textblob
from newspaper import Article # Importing newspaper
import nltk # Importing NTLK
import speech_recognition
import pyttsx3





def URL():
    url = 'https://www.nbcnews.com/news/world/live-blog/morocco-earthquake-live-updates-death-toll-aid-rcna104569' # Article URL
    article = Article(url) # Define article with the Artcle URL as parameter of the Article() function.

    article.download() # Download the article
    article.parse() # Parse the article 
    article.nlp()
    text = article.summary # Summarize the article content. Making it easier to be analyzed
    print("", text)
 
    return article


URL()
