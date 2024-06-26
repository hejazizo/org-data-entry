import streamlit as st
import json
import os
import yaml
import re
from utils import generate_prefill_data

def save_data(org_name, data):
    filename = f"saved_files/{org_name}.json"
    if not os.path.exists("saved_files"):
        os.makedirs("saved_files")
    with open(filename, "w") as f:
        json.dump(data, f)

def load_data(org_name):
    filename = f"saved_files/{org_name}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def extract_yaml(text):
    pattern = r"```yaml\n(.*?)```"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        yaml_data = match.group(1)
        return yaml_data.strip()
    else:
        return None


def main():
    st.title("⚡ Organization Data Entry")


    org_names = open('org_names.txt', 'r').read()
    names = st.sidebar.text_area(
        "📋 Organization Names",
        value=org_names,
        height=400
    )
    with open('org_names.txt', 'w') as f:
        f.write(names)
        st.sidebar.success("Organization names saved successfully!", icon="✅")

    org_list = names.split("\n")

    if not org_list:
        st.warning("Please enter organization names in the sidebar to get started.")
        return

    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    def next_org():
        st.session_state.current_index = (st.session_state.current_index + 1) % len(org_list)

    def prev_org():
        st.session_state.current_index = (st.session_state.current_index - 1) % len(org_list)

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.button("⬅️ Previous", use_container_width=True):
            prev_org()

    with col2:
        org_name = org_list[st.session_state.current_index]
        st.progress((st.session_state.current_index + 1) / len(org_list))
        st.write(f"Current Organization: **{org_name}**")

    with col3:
        if st.button("➡️ Next", use_container_width=True):
            next_org()

    model_name = st.sidebar.selectbox("🤖 LLM Model", ['gpt-4o', 'gpt-4-1106-preview', 'gpt-4', 'gpt-3.5-turbo', 'gpt-3.5-turbo-0125'], index=0)
    PROMPT_TEXT = open('prompt.txt', 'r').read()
    prompt_text = st.sidebar.text_area("📝 Prompt Text", value=PROMPT_TEXT.replace('<Organization Name>', org_name).strip(), height=600)

    if st.button("🤖 Prefill with LLM", use_container_width=True):
        llm_response = generate_prefill_data(model_name, prompt_text)
        with st.expander("🤖 LLM Response"):
            st.write(llm_response)
        # remove ```yaml, ``` and extra text from the generated data
        data = extract_yaml(llm_response)
        data = yaml.safe_load(data)
        data = json.loads(json.dumps(data))
        with st.expander("📊 Parsed LLM Response"):
            st.write(data)
    else:
        data = load_data(org_name)

    st.header("📊 Organization Data")
    data["Organization Name"] = org_name
    st.write(f'Organization Name: **{org_name}**')
    data["About the Organization"] = st.text_area("📄 About the Organization", value=data.get("About the Organization", ""))
    data["Year Founded"] = st.text_input("📅 Year Founded", value=data.get("Year Founded", ""))

    col1, col2 = st.columns(2)
    with col1:
        data["Head Office Location"] = st.text_input("📍 Head Office Location (City/Province)", value=data.get("Head Office Location", ""))
    with col2:
        data["Country"] = st.text_input("🌍 Country", value=data.get("Country", ""))

    data["Geographic Reach"] = st.text_input("🗺️ Geographic Reach", value=data.get("Geographic Reach", ""))

    col1, col2 = st.columns(2)
    with col1:
        data["Organization Size - Number of members / employees"] = st.text_input("👥 Organization Size - Number of members / employees", value=data.get("Organization Size - Number of members / employees", ""))
    with col2:
        data["Organization Size - Country Chapters"] = st.text_input("🌐 Organization Size - Country Chapters", value=data.get("Organization Size - Country Chapters", ""))

    data["Area of Expertise"] = st.text_input("🎓 Area of Expertise", value=data.get("Area of Expertise", ""))
    data["Area of Expertise Theme"] = st.text_input("🧩 Area of Expertise Theme", value=data.get("Area of Expertise Theme", ""))
    data["Issue Focus Areas"] = st.text_area("🎯 Issue Focus Areas", value=data.get("Issue Focus Areas", ""))
    data["IPCC Theme / Topic Context"] = st.text_input("🌍 IPCC Theme / Topic Context", value=data.get("IPCC Theme / Topic Context", ""))
    data["Partner Organizations"] = st.text_area("🤝 Partner Organizations", value=data.get("Partner Organizations", ""))

    col1, col2 = st.columns(2)
    with col1:
        data["Total Funding"] = st.text_input("💰 Total Funding", value=data.get("Total Funding", ""))
    with col2:
        data["Funding Sources"] = st.text_input("💸 Funding Sources", value=data.get("Funding Sources", ""))

    col1, col2 = st.columns(2)
    with col1:
        data["Government Funding"] = st.text_input("🏛️ Government Funding", value=data.get("Government Funding", ""))
    with col2:
        data["Private Funding"] = st.text_input("💼 Private Funding", value=data.get("Private Funding", ""))

    data["Founder"] = st.text_input("👤 Founder", value=data.get("Founder", ""))
    data["Board Members"] = st.text_area("👥 Board Members", value=data.get("Board Members", ""))
    data["Connection to First-response Organizations / Climate Emergency Relief Support"] = st.text_area("🚨 Connection to First-response Organizations / Climate Emergency Relief Support", value=data.get("Connection to First-response Organizations / Climate Emergency Relief Support", ""))
    data["Academic Institute Collaborations"] = st.text_area("🎓 Academic Institute Collaborations", value=data.get("Academic Institute Collaborations", ""))
    data["Current AI Related Project"] = st.text_area("🤖 Current AI Related Project", value=data.get("Current AI Related Project", ""))
    data["Potential for AI research integration"] = st.text_area("🔬 Potential for AI research integration", value=data.get("Potential for AI research integration", ""))
    data["Campaigns"] = st.text_area("📣 Campaigns", value=data.get("Campaigns", ""))
    data["Conferences and Event Participation"] = st.text_area("🎤 Conferences and Event Participation", value=data.get("Conferences and Event Participation", ""))
    data["Papers and books published"] = st.text_area("📚 Papers and books published", value=data.get("Papers and books published", ""))
    data["Link to the Website"] = st.text_input("🌐 Link to the Website", value=data.get("Link to the Website", ""))
    data["Data Sources"] = st.text_area("📊 Data Sources", value=data.get("Data Sources", ""))

    save_data(org_name, data)
    st.success("Data saved successfully!", icon="✅")

if __name__ == "__main__":
    main()
