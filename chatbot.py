from flask import Flask, request, render_template
import pickle
import json 
import numpy as np
from tensorflow import keras


app = Flask(__name__)

# Load the pickled function



with open("intent.json") as file:
    data = json.load(file)


def chat(input):
    # load trained model
    model = keras.models.load_model('chat_model')
    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([input]),
                                            truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            return np.random.choice(i['responses'])





# Route for the home page
@app.route('/')
def hello_world():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    message = request.json['message']
    output = chat(message)
    return output

if __name__ == '__main__':
    app.run()