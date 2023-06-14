import nltk.downloader

# Download the 'punkt' resource
nltk.downloader.download('punkt')

# Download the 'wordnet' resource
nltk.downloader.download('wordnet')

import random
import pickle
import numpy as np
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Load the preprocessed data
data = pickle.load(open('chatbot_data.pkl', 'rb'))
words = data['words']
labels = data['labels']
training = data['training']
output = data['output']
# Create a lemmatizer object
lemmatizer = WordNetLemmatizer()

# Load the pretrained model
model = load_model('chatbot_model.h5')

# Function to predict and generate a response

def predict_and_reply(sentence):
    # Tokenize and lemmatize the user input
    sentence_words = word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]

    # Create a bag of words for the user input
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1

    # Check if the bag contains any non-zero values
    if sum(bag) == 0:
        important_word = random.choice(sentence_words)
    else:
        max_index = np.argmax(bag)
        important_word = words[max_index]

    # Search for similar tags based on the most important word
    similar_tags = []
    for intent in data['intents']:
        if important_word in intent['patterns']:
            similar_tags.append(intent['tag'])

    # Predict the intent based on the user input
    results = model.predict(np.array([bag]))[0]
    index = np.argmax(results)
    tag = labels[index]

    # Generate a response based on the predicted intent
    for intent in data['intents']:
        if intent['tag'] == tag or intent['tag'] in similar_tags:
            responses = intent['responses']
            reply = random.choice(responses)
            return reply
