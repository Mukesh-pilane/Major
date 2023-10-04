# import pickle
# import nltk
# from nltk.stem import WordNetLemmatizer
# import numpy as np
# import random
# data={"intents":[
#     {"tag":"greeting",
#      "patterns":["Hello","How are you?","Hi There","Hi","What's up"],
#      "responses":["Howdy Partner!","Hello","How are you doing?","Greetings!","How do you do"]
#         },
#     {"tag":"age",
#      "patterns":["how old are you","when is your birthday","when was you born"],
#      "responses":["I am 24 years old","I was born in 1966","My birthday is July 3rd and I was born in 1996","03/07/1996"]
#         },
#     {"tag":"date",
#      "patterns":["what are you doing this weekend",
#                 "do you want to hangout sometime?","what are your plans for this week"],
#      "responses":["I am available this week","I don't have any plans","I am not busy"]
#         },
#     {"tag":"name",
#      "patterns":["what's your name","what are you called","who are you"],
#      "responses":["My name is Kippi","I'm Kippi","Kippi"]
#         },
#     {"tag":"goodbye",
#      "patterns":["bye","g2g","see ya","adios","cya"],
#      "responses":["It was nice speaking to you","See you later","Speak Soon"]
#         },
# ]}
# # Load the trained model from the pickle file
# with open('chatbot_model.pkl', 'rb') as file:
#     loaded_model = pickle.load(file)

# # Load the words and classes lists
# with open('chatbot_words.pkl', 'rb') as file:
#     loaded_words = pickle.load(file)

# with open('chatbot_classes.pkl', 'rb') as file:
#     loaded_classes = pickle.load(file)

# nltk.download("punkt")
# nltk.download("wordnet")
# lemmatizer = WordNetLemmatizer()

# def clean_text(text):
#     tokens = nltk.word_tokenize(text)
#     tokens = [lemmatizer.lemmatize(word) for word in tokens]
#     return tokens

# def bag_of_words(text, vocab):
#     tokens = clean_text(text)
#     bow = [0] * len(vocab)
#     for w in tokens:
#         for idx, word in enumerate(vocab):
#             if word == w:
#                 bow[idx] = 1
#     return np.array(bow)

# def pred_class(text, vocab, labels):
#     bow = bag_of_words(text, vocab)
#     result = loaded_model.predict(np.array([bow]))[0]
#     thresh = 0.2
#     y_pred = [[idx, res] for idx, res in enumerate(result) if res > thresh]

#     y_pred.sort(key=lambda x: x[1], reverse=True)
#     return_list = []
#     for r in y_pred:
#         return_list.append(labels[r[0]])
#     return return_list

# def get_response(intents_list, intents_json):
#     tag = intents_list[0]
#     list_of_intents = intents_json["intents"]
#     for i in list_of_intents:
#         if i["tag"] == tag:
#             result = random.choice(i["responses"])
#             break
#     return result

# def bot(user_input):
#     # Predict the intent
#     intents = pred_class(user_input, loaded_words, loaded_classes)

#     # Get a response
#     response = get_response(intents, data)

#     return response

############################################################################

# rule based 


nutrition_facts = {
    "apple": {
        "calories": 95,
        "carbohydrates": 25,
        "fiber": 4,
        "protein": 1,
    },
    "banana": {
        "calories": 105,
        "carbohydrates": 27,
        "fiber": 3.1,
        "protein": 1.3,
    },
    "chocolate": {
        "calories": 152,
        "carbohydrates": 15,
        "fiber": 2.1,
        "protein": 1.6,
    },
    "apple": {
        "calories": 95,
        "carbohydrates": 25,
        "fiber": 4,
        "protein": 1,
    },
    "banana": {
        "calories": 105,
        "carbohydrates": 27,
        "fiber": 3.1,
        "protein": 1.3,
    },
     "orange": {
        "calories": 62,
        "carbohydrates": 15,
        "fiber": 3.1,
        "protein": 1.2
    },
    "strawberries": {
        "calories": 32,
        "carbohydrates": 7.7,
        "fiber": 2,
        "protein": 0.7
    },
    "grapes": {
        "calories": 69,
        "carbohydrates": 18,
        "fiber": 0.9,
        "protein": 0.7
    },
    "kiwi": {
        "calories": 61,
        "carbohydrates": 14.9,
        "fiber": 3.0,
        "protein": 1.3
    },
    "pineapple": {
        "calories": 50,
        "carbohydrates": 13.1,
        "fiber": 1.4,
        "protein": 0.5
    },
    "mango": {
        "calories": 60,
        "carbohydrates": 15,
        "fiber": 1.6,
        "protein": 0.8
    },
    "watermelon": {
        "calories": 30,
        "carbohydrates": 7.6,
        "fiber": 0.4,
        "protein": 0.6
    },
    "blueberries": {
        "calories": 32,
        "carbohydrates": 8.0,
        "fiber": 1.7,
        "protein": 0.7
    },
    "peaches": {
        "calories": 39,
        "carbohydrates": 9.5,
        "fiber": 1.5,
        "protein": 0.9
    },
    "avocado": {
        "calories": 160,
        "carbohydrates": 9,
        "fiber": 7,
        "protein": 2
    },
    "pear": {
        "calories": 57,
        "carbohydrates": 15,
        "fiber": 3.1,
        "protein": 0.4
    },
    "pomegranate": {
        "calories": 83,
        "carbohydrates": 19,
        "fiber": 4,
        "protein": 1.7
    },
    "apricot": {
        "calories": 48,
        "carbohydrates": 12,
        "fiber": 2,
        "protein": 1.4
    },
    "blackberries": {
        "calories": 43,
        "carbohydrates": 9,
        "fiber": 5.3,
        "protein": 2
    },
    "cranberries": {
        "calories": 46,
        "carbohydrates": 12,
        "fiber": 4.6,
        "protein": 0.4
    },
    "grapefruit": {
        "calories": 52,
        "carbohydrates": 13,
        "fiber": 2,
        "protein": 1
    },
    "guava": {
        "calories": 68,
        "carbohydrates": 14,
        "fiber": 9,
        "protein": 2.6
    },
    "lemon": {
        "calories": 29,
        "carbohydrates": 9,
        "fiber": 2.8,
        "protein": 1.1
    },
    "lime": {
        "calories": 30,
        "carbohydrates": 9,
        "fiber": 2.8,
        "protein": 1.1
    },
    "cantaloupe": {
        "calories": 34,
        "carbohydrates": 8.2,
        "fiber": 0.9,
        "protein": 0.8
    },
    "kiwifruit": {
        "calories": 61,
        "carbohydrates": 14.9,
        "fiber": 3.0,
        "protein": 1.3
    },
    "mangosteen": {
        "calories": 73,
        "carbohydrates": 17.9,
        "fiber": 1.8,
        "protein": 0.9
    },
    "dragon fruit": {
        "calories": 60,
        "carbohydrates": 9,
        "fiber": 1.9,
        "protein": 1.5
    },
    "papaya": {
        "calories": 43,
        "carbohydrates": 11,
        "fiber": 1.7,
        "protein": 0.5
    },
    "figs": {
        "calories": 74,
        "carbohydrates": 19,
        "fiber": 2.9,
        "protein": 0.8
    },
    "passion fruit": {
        "calories": 97,
        "carbohydrates": 23.4,
        "fiber": 10.4,
        "protein": 2.2
    },
    "raspberries": {
        "calories": 52,
        "carbohydrates": 11.9,
        "fiber": 6.5,
        "protein": 1.5
    },
    "cherries": {
        "calories": 50,
        "carbohydrates": 12.2,
        "fiber": 2.1,
        "protein": 1.0
    },
    "guava": {
        "calories": 68,
        "carbohydrates": 14,
        "fiber": 9,
        "protein": 2.6
    },
    "carrot": {
        "calories": 41,
        "carbohydrates": 10.0,
        "fiber": 2.8,
        "protein": 0.9
    },
    "broccoli": {
        "calories": 34,
        "carbohydrates": 7.2,
        "fiber": 2.6,
        "protein": 2.8
    },
    "spinach": {
        "calories": 23,
        "carbohydrates": 3.6,
        "fiber": 2.2,
        "protein": 2.9
    },
    "tomato": {
        "calories": 18,
        "carbohydrates": 3.9,
        "fiber": 1.2,
        "protein": 0.9
    },
    "bell pepper": {
        "calories": 31,
        "carbohydrates": 6.0,
        "fiber": 2.1,
        "protein": 0.9
    },
    "cucumber": {
        "calories": 16,
        "carbohydrates": 3.6,
        "fiber": 0.5,
        "protein": 0.7
    },
    "kale": {
        "calories": 50,
        "carbohydrates": 8.8,
        "fiber": 3.6,
        "protein": 3.3
    },
    "zucchini": {
        "calories": 17,
        "carbohydrates": 3.1,
        "fiber": 1.0,
        "protein": 1.2
    },
    "potato": {
        "calories": 77,
        "carbohydrates": 17.5,
        "fiber": 2.2,
        "protein": 2.0
    },
    "onion": {
        "calories": 40,
        "carbohydrates": 9.3,
        "fiber": 1.7,
        "protein": 1.1
    },
    "asparagus": {
        "calories": 20,
        "carbohydrates": 3.7,
        "fiber": 2.0,
        "protein": 2.0
    },
    "cauliflower": {
        "calories": 25,
        "carbohydrates": 5.0,
        "fiber": 2.0,
        "protein": 1.9
    },
    "green beans": {
        "calories": 31,
        "carbohydrates": 7.1,
        "fiber": 2.7,
        "protein": 1.8
    },
    "sweet potato": {
        "calories": 86,
        "carbohydrates": 20.1,
        "fiber": 3.0,
        "protein": 1.6
    },
    "eggplant": {
        "calories": 25,
        "carbohydrates": 6.0,
        "fiber": 3.0,
        "protein": 1.0
    },
    "brussels sprouts": {
        "calories": 43,
        "carbohydrates": 8.0,
        "fiber": 3.8,
        "protein": 3.4
    },
    "butternut squash": {
        "calories": 45,
        "carbohydrates": 11.7,
        "fiber": 2.0,
        "protein": 1.0
    },
    "celery": {
        "calories": 16,
        "carbohydrates": 3.4,
        "fiber": 1.6,
        "protein": 0.7
    },
    "cabbage": {
        "calories": 25,
        "carbohydrates": 6.0,
        "fiber": 2.5,
        "protein": 1.3
    },
    "lettuce": {
        "calories": 5,
        "carbohydrates": 1.0,
        "fiber": 0.5,
        "protein": 0.5
    },
    "radish": {
        "calories": 16,
        "carbohydrates": 3.4,
        "fiber": 1.6,
        "protein": 0.7
    },
    "corn": {
        "calories": 86,
        "carbohydrates": 19.0,
        "fiber": 2.0,
        "protein": 3.3
    },
    "pumpkin": {
        "calories": 26,
        "carbohydrates": 6.5,
        "fiber": 0.5,
        "protein": 1.0
    },
    "cucumber": {
        "calories": 16,
        "carbohydrates": 3.6,
        "fiber": 0.5,
        "protein": 0.7
    },
    "mushroom": {
        "calories": 22,
        "carbohydrates": 3.3,
        "fiber": 1.0,
        "protein": 3.1
    },
    "cilantro": {
        "calories": 23,
        "carbohydrates": 3.7,
        "fiber": 2.8,
        "protein": 2.1
    },
    "garlic": {
        "calories": 149,
        "carbohydrates": 33.1,
        "fiber": 2.1,
        "protein": 6.4
    },
    "ginger": {
        "calories": 80,
        "carbohydrates": 17.8,
        "fiber": 2.0,
        "protein": 1.8
    },
    "parsley": {
        "calories": 36,
        "carbohydrates": 6.3,
        "fiber": 3.3,
        "protein": 3.0
    },
    "milk whole": {
        "calories": 61,
        "carbohydrates": 4.8,
        "fiber": 0,
        "protein": 3.2
    },
    "milk skim": {
        "calories": 34,
        "carbohydrates": 5.1,
        "fiber": 0,
        "protein": 3.4
    },
    "cheese": {
        "calories": 403,
        "carbohydrates": 1.3,
        "fiber": 0,
        "protein": 25
    },
    "mozzarella cheese": {
        "calories": 280,
        "carbohydrates": 2.2,
        "fiber": 0,
        "protein": 28
    },
    "yogurt": {
        "calories": 63,
        "carbohydrates": 9.2,
        "fiber": 0.4,
        "protein": 5.8
    },
    "Greek yogurt": {
        "calories": 73,
        "carbohydrates": 3.9,
        "fiber": 0,
        "protein": 5.7
    },
    "butter": {
        "calories": 717,
        "carbohydrates": 0.1,
        "fiber": 0,
        "protein": 0.9
    },
    "cream heavy": {
        "calories": 345,
        "carbohydrates": 2.8,
        "fiber": 0,
        "protein": 2.0
    },
    "cream": {
        "calories": 195,
        "carbohydrates": 5.3,
        "fiber": 0,
        "protein": 1.3
    },
    "butter margarine": {
        "calories": 717,
        "carbohydrates": 0.1,
        "fiber": 0,
        "protein": 0.9
    },
    "cottage cheese": {
        "calories": 72,
        "carbohydrates": 3.2,
        "fiber": 0.3,
        "protein": 12
    },
    "butter": {
        "calories": 717,
        "carbohydrates": 0.1,
        "fiber": 0,
        "protein": 0.9
    },
    "vanilla icecream": {
        "calories": 207,
        "carbohydrates": 27,
        "fiber": 0.4,
        "protein": 3.5
    },
    "chocolate icecream": {
        "calories": 208,
        "carbohydrates": 25,
        "fiber": 2.3,
        "protein": 3.4
    },
    "strawberry icecream": {
        "calories": 139,
        "carbohydrates": 24,
        "fiber": 2.0,
        "protein": 2.1
    },
   "rice": {
        "calories": 130,
        "carbohydrates": 28,
        "fiber": 0.6,
        "protein": 2.7
    },
    "pasta": {
        "calories": 200,
        "carbohydrates": 40,
        "fiber": 2.5,
        "protein": 7.0
    },
    "white bread": {
        "calories": 79,
        "carbohydrates": 15,
        "fiber": 0.9,
        "protein": 2.7
    },
    "whole wheat bread": {
        "calories": 69,
        "carbohydrates": 12,
        "fiber": 2.2,
        "protein": 2.8
    },
     "chickpeas": {
        "calories": 164,
        "carbohydrates": 27.4,
        "fiber": 7.6,
        "protein": 8.9
    },
    "black beans": {
        "calories": 114,
        "carbohydrates": 20.4,
        "fiber": 7.5,
        "protein": 7.6
    },
    "red kidney beans": {
        "calories": 127,
        "carbohydrates": 23.8,
        "fiber": 7.4,
        "protein": 7.5
    },
    "lentils": {
        "calories": 165,
        "carbohydrates": 29.9,
        "fiber": 7.9,
        "protein": 9.0
    },
    "green peas": {
        "calories": 62,
        "carbohydrates": 11.6,
        "fiber": 4.6,
        "protein": 4.2
    },
    "pinto beans ": {
        "calories": 245,
        "carbohydrates": 45.0,
        "fiber": 15.4,
        "protein": 15.4
    },
    "navy beans": {
        "calories": 127,
        "carbohydrates": 23.9,
        "fiber": 9.7,
        "protein": 7.5
    },
    "split peas ": {
        "calories": 116,
        "carbohydrates": 20.6,
        "fiber": 8.3,
        "protein": 8.2
    },
    "lima beans": {
        "calories": 115,
        "carbohydrates": 20.2,
        "fiber": 6.2,
        "protein": 7.8
    },
    "black-eyed peas": {
        "calories": 160,
        "carbohydrates": 35.0,
        "fiber": 8.2,
        "protein": 8.7
    },
    "adzuki beans": {
        "calories": 128,
        "carbohydrates": 26.0,
        "fiber": 8.5,
        "protein": 7.5
    },
    "mung beans": {
        "calories": 212,
        "carbohydrates": 38.7,
        "fiber": 15.4,
        "protein": 14.2
    },
    "garbanzo beans": {
        "calories": 164,
        "carbohydrates": 27.4,
        "fiber": 7.6,
        "protein": 8.9
    },
      "dark chocolate": {
        "calories": 604,
        "carbohydrates": 46,
        "fiber": 11,
        "protein": 7
    },
    "milk chocolate": {
        "calories": 535,
        "carbohydrates": 59,
        "fiber": 3.4,
        "protein": 7.9
    },
    "white chocolate": {
        "calories": 539,
        "carbohydrates": 60,
        "fiber": 0,
        "protein": 7.1
    },
    "chocolate truffle": {
        "calories": 70,
        "carbohydrates": 6,
        "fiber": 0.5,
        "protein": 0.7
    },
     "chocolate cake": {
        "calories": 235,
        "carbohydrates": 38,
        "fiber": 1.7,
        "protein": 2.3
    },
    "vanilla cake": {
        "calories": 249,
        "carbohydrates": 33,
        "fiber": 0.5,
        "protein": 2.6
    },
    "carrot cake": {
        "calories": 305,
        "carbohydrates": 50,
        "fiber": 1.8,
        "protein": 3.1
    },
    "cheesecake": {
        "calories": 257,
        "carbohydrates": 19,
        "fiber": 0.2,
        "protein": 5.4
    },
    "red velvet cake": {
        "calories": 225,
        "carbohydrates": 32,
        "fiber": 0.6,
        "protein": 2.3
    },
    "lemon cake": {
        "calories": 270,
        "carbohydrates": 42,
        "fiber": 0.8,
        "protein": 2.8
    },
    "coconut cake": {
        "calories": 365,
        "carbohydrates": 45,
        "fiber": 2.2,
        "protein": 3.5
    },
    "hamburger": {
        "calories": 250,
        "carbohydrates": 31,
        "fiber": 2,
        "protein": 12
    },
    "french fries": {
        "calories": 365,
        "carbohydrates": 63,
        "fiber": 5,
        "protein": 3.4
    },
    "pizza": {
        "calories": 285,
        "carbohydrates": 36,
        "fiber": 2.1,
        "protein": 12
    },
    "hot dog": {
        "calories": 150,
        "carbohydrates": 1,
        "fiber": 0,
        "protein": 5
    },
    "fried chicken": {
        "calories": 320,
        "carbohydrates": 10,
        "fiber": 0,
        "protein": 20
    },
    "chicken nuggets":{
        "calories": 280,
        "carbohydrates": 14,
        "fiber": 0.7,
        "protein": 10
    },
    "onion rings": {
        "calories": 276,
        "carbohydrates": 35,
        "fiber": 2.3,
        "protein": 2.5
    },
    "cheeseburger": {
        "calories": 303,
        "carbohydrates": 32,
        "fiber": 1.9,
        "protein": 14
    },
    "taco": {
        "calories": 170,
        "carbohydrates": 13,
        "fiber": 1,
        "protein": 9
    },
    "burrito": {
        "calories": 362,
        "carbohydrates": 52,
        "fiber": 4.7,
        "protein": 10
    },
    "potato chips": {
        "calories": 152,
        "carbohydrates": 15,
        "fiber": 1.3,
        "protein": 2
    },
    "soda": {
        "calories": 140,
        "carbohydrates": 39,
        "fiber": 0,
        "protein": 0
    },
    "ice cream": {
        "calories": 137,
        "carbohydrates": 16,
        "fiber": 0,
        "protein": 2.2
    },
    "donut": {
        "calories": 260,
        "carbohydrates": 31,
        "fiber": 0.6,
        "protein": 2.3
    },
    "chocolate chip cookie": {
        "calories": 49,
        "carbohydrates": 6,
        "fiber": 0.3,
        "protein": 0.6
    },
    "nachos": {
        "calories": 351,
        "carbohydrates": 41,
        "fiber": 4.6,
        "protein": 8.2
    },
    "soft pretzel": {
        "calories": 483,
        "carbohydrates": 100,
        "fiber": 4.8,
        "protein": 10
    },
    "corn dog": {
        "calories": 225,
        "carbohydrates": 19,
        "fiber": 1.3,
        "protein": 5
    },
    "mozzarella sticks": {
        "calories": 302,
        "carbohydrates": 16,
        "fiber": 1.4,
        "protein": 12
    },
    "cheese fries": {
        "calories": 365,
        "carbohydrates": 37,
        "fiber": 2.9,
        "protein": 8
    },
     "brownie": {
        "calories": 112,
        "carbohydrates": 20,
        "fiber": 0.9,
        "protein": 1.3
    },
    "cupcake": {
        "calories": 158,
        "carbohydrates": 26,
        "fiber": 0.3,
        "protein": 1.3
    },
     "cotton candy": {
        "calories": 171,
        "carbohydrates": 44,
        "fiber": 0,
        "protein": 0
    },
    "caramel popcorn ": {
        "calories": 106,
        "carbohydrates": 21,
        "fiber": 1.5,
        "protein": 1.3
    },
    "jelly beans": {
        "calories": 105,
        "carbohydrates": 27,
        "fiber": 0,
        "protein": 0.9
    },
    "gummy bears": {
        "calories": 97,
        "carbohydrates": 23,
        "fiber": 0,
        "protein": 0.8
    },
    "licorice": {
        "calories": 104,
        "carbohydrates": 26,
        "fiber": 0.3,
        "protein": 0.7
    },
    "marshmallows": {
        "calories": 90,
        "carbohydrates": 22,
        "fiber": 0,
        "protein": 0.9
    },
    "apple pie": {
        "calories": 320,
        "carbohydrates": 48,
        "fiber": 2,
        "protein": 2
    },
    "cherry pie": {
        "calories": 375,
        "carbohydrates": 58,
        "fiber": 2,
        "protein": 2
    },
    "fudge": {
        "calories": 98,
        "carbohydrates": 18,
        "fiber": 0.5,
        "protein": 1
    },
    "black tea": {
        "calories": 2,
        "carbohydrates": 0.5,
        "fiber": 0,
        "protein": 0
    },
    "green tea": {
        "calories": 2,
        "carbohydrates": 0.5,
        "fiber": 0,
        "protein": 0
    },
    "herbal tea": {
        "calories": 2,
        "carbohydrates": 0.4,
        "fiber": 0,
        "protein": 0
    },
    "oolong tea": {
        "calories": 2,
        "carbohydrates": 0.5,
        "fiber": 0,
        "protein": 0
    },
    "white tea": {
        "calories": 2,
        "carbohydrates": 0.5,
        "fiber": 0,
        "protein": 0
    },
    "tea ": {
        "calories": 90,
        "carbohydrates": 14,
        "fiber": 0,
        "protein": 3
    },
    "peppermint tea": {
        "calories": 2,
        "carbohydrates": 0.4,
        "fiber": 0.1,
        "protein": 0.1
    },
    "ginger tea": {
        "calories": 2,
        "carbohydrates": 0.5,
        "fiber": 0.1,
        "protein": 0.1
    },
    "rooibos tea": {
        "calories": 0,
        "carbohydrates": 0,
        "fiber": 0,
        "protein": 0
    },
    "mate tea": {
        "calories": 2,
        "carbohydrates": 0.4,
        "fiber": 0.2,
        "protein": 0.3
    },
     "raisins": {
        "calories": 85,
        "carbohydrates": 22,
        "fiber": 1.3,
        "protein": 1
    },
    "dates": {
        "calories": 85,
        "carbohydrates": 22,
        "fiber": 2,
        "protein": 0.7
    },
    "apricots": {
        "calories": 18,
        "carbohydrates": 4,
        "fiber": 1,
        "protein": 0.4
    },
    "fig": {
        "calories": 42,
        "carbohydrates": 11,
        "fiber": 1.6,
        "protein": 0.5
    },
     "pistachios": {
        "calories": 158,
        "carbohydrates": 8,
        "fiber": 3,
        "protein": 6
    },
    "cashew": {
        "calories": 157,
        "carbohydrates": 9,
        "fiber": 1,
        "protein": 5
    },
    "almond": {
        "calories": 160,
        "carbohydrates": 6,
        "fiber": 3.5,
        "protein": 6
    },
}

# Define rules for the chatbot
def bot(user_input):
    user_input = user_input.lower()
    if user_input in nutrition_facts:
        facts = nutrition_facts[user_input]
        response = f"Nutrition facts for {user_input}:\nCalories: {facts['calories']} kcal\nCarbohydrates: {facts['carbohydrates']} grams\nFiber: {facts['fiber']} grams\nProtein: {facts['protein']} grams"
    else:
        response = "I don't have nutrition facts for that food. Please ask about a different food."
    return response

# Main loop for the chatbot for cli
# while True:
#     user_input = input("Ask me about the nutrition facts of a food (e.g., 'apple', 'rice'): ")
#     if user_input.lower() == 'exit':
#         break
#     response = bot(user_input)
#     print(response)


