import streamlit as st
from utils import generate_prefill_data

st.title("⚡ Generate Prompt for Organization Data Extraction")


company_info = st.text_area("Company Information", height=600, value="")

prompt = f"""
You are an advanced AI language model
tasked with extracting structured information from text about companies,
foundations, or groups that are focused on climate change. For the given information about a company, please extract the following fields:

- **Company Name:**
- **About the Organization:**
- **Year Founded:**
- **Head Office Location (City/Province):**
- **Country:**
- **Geographic Reach (Local / Regional / International):**
- **Organization Size - Number of members / employees:**
- **Area of Expertise:**
- **Founder:**
- **Board Members:**
- **Conferences and Event Participation:**
- **Link to the Website:**

Please format your response with each field on a new line. If a field has multiple values, separate them with a semicolon (;).

**Company Information:**
{company_info}

**Requested Extracted Information:**
- **Company Name:** 
- **About the Organization:** 
- **Year Founded:** 
- **Head Office Location (City/Province):** 
- **Country:** 
- **Geographic Reach (Local / Regional / International):** 
- **Organization Size - Number of members / employees:** 
- **Area of Expertise:** 
- **Founder:** 
- **Board Members:** 
- **Conferences and Event Participation:** 
- **Link to the Website:** 

If a field is not present in the text, leave it blank. If you are unable to extract a field, leave it blank. If you are unsure about a field, fill it with your best guess and mark it with a question mark (?).
"""

with st.expander("🤖 Generated Prompt", expanded=False):
    st.code(prompt, language="markdown")


model_name = st.sidebar.selectbox("🤖 LLM Model", ['gpt-4o', 'gpt-4-1106-preview', 'gpt-4', 'gpt-3.5-turbo', 'gpt-3.5-turbo-0125'], index=0)
if st.button("🤖 Generate LLM Response", use_container_width=True):
    llm_response = generate_prefill_data(model_name, prompt)
    st.markdown(llm_response)