import pickle
from flask import Flask, request, render_template

# Load the trained model
with open("spam_classifier.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        message = request.form['message']
        if not message.strip():
            return render_template('index.html', prediction_text="⚠️ Please enter a message!")

        prediction = model.predict([message])[0]
        result = "Spam" if prediction == 1 else "Ham"
        return render_template('index.html', prediction_text=f'This message is: {result}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
