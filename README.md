# 📧 Spam Message Classifier
---
Welcome to the Spam Message Detection App! 

About the Project
This project is a text classification system that can distinguish between spam and ham (legitimate) SMS messages. Using Natural Language Processing (NLP) and machine learning, it learns patterns from past messages and predicts whether new messages are spam.
The application is wrapped in an easy-to-use Streamlit interface, so you can try it out directly from your browser!


## 📌 Project Overview

- **Model**: Multinomial Naive Bayes
- **Vectorizer**: TF-IDF
- **Training Tool**: GridSearchCV for hyperparameter tuning
- **Interface**: Streamlit app for prediction
- **Goal**: To detect unwanted messages with high accuracy

---

## 🧠 How It Works


Text Cleaning: The messages are converted to lowercase, and all numbers, punctuation, and extra whitespace are removed.

Vectorization: Words are converted into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency).

Model: A Multinomial Naive Bayes model is trained to recognize spam patterns.

Tuning: We used GridSearchCV to fine-tune parameters for the best accuracy---

## 📬 Example
![image](https://github.com/user-attachments/assets/7891781c-1b26-4961-8d26-e6839b25f39b)

## 🛠 How to Run

Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/spam-classifier.git
   cd spam-classifier

   Install dependencies:
   pip install -r requirements.txt

   Run the Streamlit app:
   streamlit run app.py
