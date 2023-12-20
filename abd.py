import streamlit as st
import requests
import google.generativeai as genai

genai.configure(api_key="AIzaSyCpU47km6BczdQl0g-0IqrF8PtWSlv2HLA")

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.4,
  'candidate_count': 4,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
}

# Tampilan Streamlit
st.title('Grammar Checker')
st.write('Enter text below to check grammar:')

input_text = st.text_area('Input your text here', height=200)

if st.button('Check Grammar'):
  prompt = f"""Rewrite the following sentence and fix any grammar issues.

  {input_text}."""

  response = genai.generate_text(
    **defaults,
    prompt=prompt
  )

  st.write(response.result)