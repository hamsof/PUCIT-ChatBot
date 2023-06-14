from flask import Flask, request, render_template
from chatbotModule import predict_and_reply

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    message = request.json['message']
    output = predict_and_reply(message)
    return output

if __name__ == '__main__':
    app.run()