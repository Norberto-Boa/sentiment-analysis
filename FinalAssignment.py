"""
This is a project designed to make text sentiment analysis. This is project which aims only the text data.
"""

from textblob import TextBlob # Importing Textblob
from newspaper import Article # Importing newspaper
import nltk # Importing NTLK
import speech_recognition
import pyttsx3

# def URL():
#     url = 'https://www.nbcnews.com/news/world/live-blog/morocco-earthquake-live-updates-death-toll-aid-rcna104569' # Article URL
#     article = Article(url) # Define article with the Artcle URL as parameter of the Article() function.

#     article.download() # Download the article
#     article.parse() # Parse the article 
#     article.nlp()
#     return


# From a txt file
# def txt(): 
#     with open('test.txt', 'r') as f:
#         text = f.read()
#         return

# Input hte comment
# def comment():
#     text = input('How do you feel about the product: ')
#     return

# Speech recognition module

recognizer = speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:
        
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            print("listening:")
            audio =  recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized: {text}")
            break
            
    except speech_recognition.UnknownValueError:

        recognizer = speech_recognition.Recognizer()
        continue






# text = article.summary # Summarize the article content. Making it easier to be analyzed
# print("", text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)

if sentiment > 0:
    print("positive")

elif sentiment < 0:
    print("negative")

else:
    print("neutral")
