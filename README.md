# 📧 Spam Message Classifier

This project is a machine learning model that classifies text messages as **Spam** or **Ham** (not spam). It's built using Python, trained with a Naive Bayes algorithm, and deployed using Streamlit for a user-friendly interface.

---

## 📌 Project Overview

- **Model**: Multinomial Naive Bayes
- **Vectorizer**: TF-IDF
- **Training Tool**: GridSearchCV for hyperparameter tuning
- **Interface**: Streamlit app for prediction
- **Goal**: To detect unwanted messages with high accuracy

---

## 🧠 How It Works

1. **Text Preprocessing** (removes numbers, punctuation, lowercases, etc.)
2. **TF-IDF Vectorization** of the cleaned text
3. **Model Prediction** using a trained Naive Bayes classifier
4. **Web Interface** shows prediction: Spam or Ham

---

## 🛠 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/spam-classifier.git
   cd spam-classifier

Install dependencies:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

  Local URL: [http://localhost:8501](http://localhost:8501)
  Network URL: http://192.168.1.170:8501

![image](https://github.com/user-attachments/assets/7891781c-1b26-4961-8d26-e6839b25f39b)

