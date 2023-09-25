import customtkinter
import tkinter
from textblob import TextBlob # Importing Textblob
from newspaper import Article # Importing newspaper
import nltk # Importing NTLK
import speech_recognition
import pyttsx3
from tkinter import *



customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")


root = customtkinter.CTk()
root.geometry("600x800")


frame = customtkinter.CTkFrame(master=root)
frame.pack(fill="both", expand=True)









# From a txt file
def txt(): 
    with open('test.txt', 'r') as f:
        text = f.read()
        return

# Input hte comment
def comment():
    text = input('How do you feel about the product: ')
    return

# Speech recognition module






# # different Tabs (URL, Audio and Text)
tab = customtkinter.CTkTabview(frame, width=600, height=800)
tab.pack()
tab.add("URL")
tab.add("Audio")
tab.add("Text")
tab.tab("URL").grid_columnconfigure(0, weight=1)
tab.tab("Audio").grid_columnconfigure(0, weight=1)
tab.tab("Text").grid_columnconfigure(0, weight=1)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Url tab elements

# URL Sentiment Analysis
label = customtkinter.CTkLabel(tab.tab("URL"), text="URL Sentiment Analysis", font=("Roboto", 20))
label.pack(pady=20)

# Input the URL
input1 = customtkinter.CTkEntry(tab.tab("URL"), placeholder_text="Input the URL", width=200, height=30)
input1.pack(padx=10, pady=10)


def URL():
    # url = input("Write article:"  ) # Article URL
    url= input1.get() #Get input from entry
    article = Article(url) # Define article with the Artcle URL as parameter of the Article() function.

    article.download() # Download the article
    article.parse() # Parse the article 
    article.nlp()
    text = article.summary # Summarize the article content. Making it easier to be analyzed
    text1= str(text) #Transform result to string
    summary1.configure(text=text, font= ("ariel", 16), width=20, height=300, achor="e") #Display the summary label
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # -1 to 1
    # print(sentiment)

    if sentiment > 0:
        sentiments.configure(text="Positive", text_color="Green") #Update Sentiment label to positive

    elif sentiment < 0:
        sentiments.configure(text="Negative", text_color="Red") #Update Sentiment label to negative

    else:
        sentiments.configure(text="Neutral", text_color="white") #Update Sentiment label to neutral

    return

def clear(): #Function to clear all
    input1.delete(0, END) 
    summary1.configure(text="URL Summary", width=20)
    sentiments.configure(text="Sentiment")
    pass

# Generate Button
btnurl= customtkinter.CTkButton(tab.tab("URL"), text="Generate", font=("Roboto", 18), height=30, command=URL)
btnurl.pack(pady=30)

#Clear Button
btnclr= customtkinter.CTkButton(tab.tab("URL"), text="Clear", font=("Roboto", 18), height=30, command=clear)
btnclr.pack(pady=10)

# Summary text Lqbel
summary1 = customtkinter.CTkLabel(tab.tab("URL"), text="URL Summary", font=("Roboto", 18), width=20, height=400)
summary1.pack()

# Sentiment result Label
sentiments = customtkinter.CTkLabel(tab.tab("URL"), text="Sentiment", font=("Roboto", 18))
sentiments.pack(pady=10)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Audio tab
audiotab = customtkinter.CTkLabel(tab.tab("Audio"), text="Audio TAB", font=("Roboto", 20))
audiotab.pack(pady=20)

def recognize():
    recognizer = speech_recognition.Recognizer()

    while True:

        try:
            with speech_recognition.Microphone() as mic:
        
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                recognized.configure(text="Listening", font=("ariel bold", 18))
                print("listening:")
                audio =  recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()

                print(f"Recognized: {text}")
                recognized.configure(text=text, font=("ariel bold", 18))
                break
            
        except speech_recognition.UnknownValueError:

            # recognizer = speech_recognition.Recognizer()
            print("Sorry i did'nt understand what yousaid")
            continue

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # -1 to 1
    print(sentiment)

    
    if (sentiment > 0) and (sentiment <1):
        sentimentaud.configure(text="Positive", text_color="Green") #Update Sentiment label to positive

    elif sentiment < 0 > -1:
        sentimentaud.configure(text="Negative", text_color="Red") #Update Sentiment label to negative

    elif sentiment == 0:
        sentimentaud.configure(text="Neutral", text_color="white") #Update Sentiment label to neutral

    else:
        sentimentaud.configure(text="Sorry, i don't understand. Try again", text_color="orange") #In case of error




btnaud = customtkinter.CTkButton(tab.tab("Audio"), text="Record", font=("ariel bold", 20), command=recognize)
btnaud.pack(pady=30)

recognized = customtkinter.CTkLabel(tab.tab("Audio"), text="What you say will apear here", font=("ariel bold", 20))
recognized.pack(pady=20)

sentimentaud= customtkinter.CTkLabel(tab.tab("Audio"), text="Sentiment", font=("ariel", 20))
sentimentaud.pack()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Text Tab
texttab = customtkinter.CTkLabel(tab.tab("Text"), text="Text TAB", font=("Roboto", 20))
texttab.pack(pady=20)


entry3 = customtkinter.CTkEntry(tab.tab("Text"), placeholder_text="Enter you comment")
entry3.pack(pady=10)


def comment():
    input3 = entry3.get()
    sentiment3.configure(text=input3)

    
    blob = TextBlob(input3)
    sentiment = blob.sentiment.polarity  # -1 to 1
        # print(sentiment)

    if sentiment > 0:
        sentiment3.configure(text="Positive", text_color="Green") #Update Sentiment label to positive

    elif sentiment < 0:
        sentiment3.configure(text="Negative", text_color="Red") #Update Sentiment label to negative

    else:
        sentiment3.configure(text="Neutral", text_color="white") #Update Sentiment label to neutral
    return

def delete3():
    entry3.delete(0, END)
    sentiment3.configure(text="Sentiment", text_color="black")
    pass

btn3 = customtkinter.CTkButton(tab.tab("Text"), text="Generate", font=("ariel", 20), command=comment)
btn3.pack(pady=10)

btndel = customtkinter.CTkButton(tab.tab("Text"), text="Clear", font=("ariel", 20), command=delete3)
btndel.pack(pady=10)

sentiment3 = customtkinter.CTkLabel(tab.tab("Text"), text="Sentiment", font=("ariel", 20))
sentiment3.pack(pady=10)



root.mainloop()

