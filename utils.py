
import streamlit as st
from openai import OpenAI


OPEN_AI_API_KEY = st.sidebar.text_input("🔑 OpenAI API Key", type="password")
if not OPEN_AI_API_KEY:
    st.error("Please set your OPEN_AI_API_KEY environment variable.")


@st.cache_resource
def generate_prefill_data(model_name, prompt_text):
    temperature = 0.7
    max_tokens = 1000

    client = OpenAI(api_key=OPEN_AI_API_KEY)

    with st.spinner("🤖 Generating prefill data..."):
        response = client.chat.completions.create(
            model=model_name,
            messages=[{'role': 'user', 'content': prompt_text}],
            temperature=temperature,
            max_tokens=max_tokens
        )

    return response.choices[0].message.content.strip()
