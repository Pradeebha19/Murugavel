import pickle
import streamlit as st

# Load the trained model
with open("spam_classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("📩 Spam Detection App")

st.write("Enter a message below to check if it's Spam or Ham:")

message = st.text_area("Message", "")

if st.button("Predict"):
    if not message.strip():
        st.warning("⚠️ Please enter a message!")
    else:
        prediction = model.predict([message])[0]
        result = "🚨 Spam" if prediction == 1 else "✅ Ham"
        st.subheader(f"This message is: {result}")

