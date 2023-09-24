import pickle
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
data={"intents":[
    {"tag":"greeting",
     "patterns":["Hello","How are you?","Hi There","Hi","What's up"],
     "responses":["Howdy Partner!","Hello","How are you doing?","Greetings!","How do you do"]
        },
    {"tag":"age",
     "patterns":["how old are you","when is your birthday","when was you born"],
     "responses":["I am 24 years old","I was born in 1966","My birthday is July 3rd and I was born in 1996","03/07/1996"]
        },
    {"tag":"date",
     "patterns":["what are you doing this weekend",
                "do you want to hangout sometime?","what are your plans for this week"],
     "responses":["I am available this week","I don't have any plans","I am not busy"]
        },
    {"tag":"name",
     "patterns":["what's your name","what are you called","who are you"],
     "responses":["My name is Kippi","I'm Kippi","Kippi"]
        },
    {"tag":"goodbye",
     "patterns":["bye","g2g","see ya","adios","cya"],
     "responses":["It was nice speaking to you","See you later","Speak Soon"]
        },
]}
# Load the trained model from the pickle file
with open('chatbot_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Load the words and classes lists
with open('chatbot_words.pkl', 'rb') as file:
    loaded_words = pickle.load(file)

with open('chatbot_classes.pkl', 'rb') as file:
    loaded_classes = pickle.load(file)

nltk.download("punkt")
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

def bag_of_words(text, vocab):
    tokens = clean_text(text)
    bow = [0] * len(vocab)
    for w in tokens:
        for idx, word in enumerate(vocab):
            if word == w:
                bow[idx] = 1
    return np.array(bow)

def pred_class(text, vocab, labels):
    bow = bag_of_words(text, vocab)
    result = loaded_model.predict(np.array([bow]))[0]
    thresh = 0.2
    y_pred = [[idx, res] for idx, res in enumerate(result) if res > thresh]

    y_pred.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in y_pred:
        return_list.append(labels[r[0]])
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result

def bot(user_input):
    # Predict the intent
    intents = pred_class(user_input, loaded_words, loaded_classes)

    # Get a response
    response = get_response(intents, data)

    return response



