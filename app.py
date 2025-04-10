import openai
import streamlit as st
import os

# Set OpenAI API Key from environment variable or Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")  # or st.secrets["openai_api_key"]

# Function to generate response from GPT
def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # or "gpt-4" if you have access
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit Interface
st.title("Polylingo - Learn Polish with AI")

# User input
user_input = st.text_input("Ask me anything in English or Polish:")

if user_input:
    prompt = f"Translate this sentence to Polish: {user_input}"
    result = get_gpt_response(prompt)
    st.write(f"Translation: {result}")
else:
    st.write("Please enter a sentence to translate.")
