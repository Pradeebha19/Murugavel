from flask import Flask, request, render_template
import pickle
app = Flask(__name__)

# Load the trained model
with open("spam_classifier.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form.get("email_text")
    prediction = model.predict([email_text])[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)