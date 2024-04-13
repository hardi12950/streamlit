# Cell 1: Setup
import streamlit as st
from openai import OpenAI
import os

# Get your OpenAI API key from environment variables

# api_key = os.getenv("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")  # Used in production - Uncomment this line when you deploy
# api_key = "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" # Used in development - Delete this line when you deploy - This api_key is only made for demonstration purposes

# Cell 2: Title & Description
st.title('🤖 AI Data Interview Assistant')
st.markdown('I was made to you answer Data interview questions. This app demonstrates how to use OpenAI GPT-3.5 to answer data-related interview questions in a deployed envionment. Remember, always verify AI-generated responses.')

# Cell 3: Function to analyze text using OpenAI
def analyze_text(text):
  """
  This function sends a text prompt to the OpenAI API using the GPT-3.5 model.

  Args:
      text (str): The tech interview question to be answered.

  Returns:
      str: The response generated by the GPT-3.5 model.
  """

  # Ensure your OPENAI_API_KEY is set as an environment variable
  if not api_key:
      st.error("OpenAI API key is not set. Please set it in your environment variables.")
      return

  client = OpenAI(api_key=api_key)
  model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

  # Instructions for the AI (adjust if needed)
  messages = [
      {"role": "system", "content": "You are an assistant who answers interview and technical questions for a data science related jobs."},
      {"role": "user", "content": f"Answer the following job interview question:\n{text}"}
  ]

  response = client.chat.completions.create(
      model=model,
      messages=messages,
      temperature=0  # Lower temperature for less random responses
  )
  return response.choices[0].message.content

# Cell 4: Streamlit UI
user_input = st.text_area("Enter question to answer:", "How should you maintain a deployed model?")

if st.button('Answer Interview Question'):
  with st.spinner('Answering...'):
      result = analyze_text(user_input)
      st.write(result)
