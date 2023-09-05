import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()

directory = 'C:/Users/victo/OneDrive/Desktop/pythonCode/PythonChatbot/'

intents = json.loads(open(directory + 'intents.json').read())

words = pickle.load(open(directory + 'words.pkl', 'rb'))
classes = pickle.load(open(directory + 'classes.pkl', 'rb'))
model = load_model(directory + 'chatbotmodel.h5')


#functions to clean sentences, get bag of word, to predict class based on sentence, to get a response

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1 #if the word matches, change its value in the array from 0 to 1

    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence) #create a bag of words from the sentence
    res = model.predict(np.array([bow]))[0] #predict result based on bag of words
    ERROR_THRESHOLD = 0.25 #error threshold of 25%
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD] #don't want too much uncertainty

    results.sort(key=lambda x: x[1], reverse=True) #sort by probability, reverse so that the highest probability is first
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print('PROGRAM IS LAUNCHED')
print(f"Please type something: \n")


#chatting/printing the messages

while True:
    message = input("")
    ints = predict_class(message)
    resp = get_response(ints, intents)
    print(resp)



#TODO
# Before everything, save a copy of this project and name the new one Discord Bot or something
# 1. Figure out how to read, and write on Discord
# 2. Using what you read from a pattern-response format (1 from a user, 1 response from a user), eliminate
# and get rid of useless words (as well as NSFW words) to find important key words
# 3. If the pattern matches close enough (using our created functions) to an existing intents.json pattern, append the 
# response to the "responses": section.
# 4. Elif the response matches close enough (using our created functions) to an existing intents.json response, append the
# pattern to the "pattern": section.
# 5. If neither, create a new intent section with the "pattern": and "response": and continue
# 6. Make the json file rewrite itself as its scanning a Discord server chat
# 7. Afterwards, I can go through the intents briefly and remove/add necessary elements. Then, I can train the bot again.
# 8. Make sure it reads content that is considered "good"