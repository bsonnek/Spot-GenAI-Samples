import streamlit as st
from streamlit_chat import message
import dotenv
import os
import openai
import datetime
import json


# Set up the Open AI Client

openai.api_type = "azure"
openai.api_base = os.environ.get("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.environ.get("AZURE_OPENAI_API_VERSION")
openai.api_key = os.environ.get("AZURE_OPENAI_API_KEY")

# endregion

# region PROMPT SETUP
st.set_page_config(page_title="Spot ChatGPT Demo", layout="wide", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: left;'>Spot ChatGPT Demo </h1>", unsafe_allow_html=True)
st.sidebar.markdown(
    f"""
    <div style="display:table;margin-top:-40%;margin-left:5%;">
        <img src="https://github.com/bsonnek/Spot-GenAI-Samples/assets/10324197/1aab906e-ab44-420a-9823-1d9f3432e50a" width="500" height="200">
    </div>
    """,
    unsafe_allow_html=True,
)

default_prompt = """
You are an AI assistant  that helps users write concise\
 reports on sources provided according to a user query.\
 You will provide reasoning for your summaries and deductions by\
 describing your thought process. You will highlight any conflicting\
 information between or within sources. Greet the user by asking\
 what they'd like to investigate.
"""
st.sidebar.title("Playground Settings")
system_prompt = st.sidebar.text_area("System Prompt", value=default_prompt, key='system_prompt', height=300)
seed_message = {"role": "system", "content": system_prompt}
update_prompt_button = st.sidebar.button("Update System Prompt", key="update")
Temp_var = st.sidebar.slider("Set Temp - 2 is most creative", 0.0, 2.0, 0.7, 0.20)

if update_prompt_button:
    seed_message = {"role": "system", "content": system_prompt}
    st.session_state["messages"] = [seed_message]
# endregion

# region SESSION MANAGEMENT
# Initialise session state variables
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
if "messages" not in st.session_state:
    st.session_state["messages"] = [seed_message]
if "model_name" not in st.session_state:
    st.session_state["model_name"] = []
if "cost" not in st.session_state:
    st.session_state["cost"] = []
if "total_tokens" not in st.session_state:
    st.session_state["total_tokens"] = []
if "total_cost" not in st.session_state:
    st.session_state["total_cost"] = 0.0
# endregion

# region SIDEBAR SETUP
model_name = st.sidebar.radio("Choose a model:", ("gpt-35-turbo", "gpt-35-turbo-16k", "GPT-4"))
counter_placeholder = st.sidebar.empty()
counter_placeholder.write(
    f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}"
)
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# Map model names to OpenAI model IDs
if model_name == "gpt-35-turbo":
    model = "gpt-35-turbo"
if model_name == "gpt-35-turbo-16k":
    model = "gpt-35-turbo-16k"
if model_name == "GPT-4":
    model = "GPT-4"

if clear_button:
    st.session_state["generated"] = []
    st.session_state["past"] = []
    st.session_state["messages"] = [seed_message]
    st.session_state["number_tokens"] = []
    st.session_state["model_name"] = []
    st.session_state["cost"] = []
    st.session_state["total_cost"] = 0.0
    st.session_state["total_tokens"] = []
    counter_placeholder.write(
        f"Total cost of this conversation: £{st.session_state['total_cost']:.5f}"
    )


download_conversation_button = st.sidebar.download_button(
    "Download Conversation",
    data=json.dumps(st.session_state["messages"]),
    file_name=f"conversation.json",
    mime="text/json",
)

# endregion


def generate_response(prompt):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    message_placeholder = st.empty()
    full_response = ""
    total_tokens = ""
    prompt_tokens = ""
    completion_tokens = ""
    for response in openai.ChatCompletion.create(
        engine=model,
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        stream=True,
        ):
        full_response += response.choices[0].delta.get("content", "")
        total_tokens += response.usage.total_tokens
        prompt_tokens += response.usage.prompt_tokens
        completion_tokens += response.usage.completion_tokens
        message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state["messages"].append({"role": "assistant", "content": full_response})

    # print(st.session_state['messages'])

    return full_response, total_tokens, prompt_tokens, completion_tokens



# container for chat history
response_container = st.container()
# container for text box
container = st.container()

with container:
    with st.form(key="my_form", clear_on_submit=True):
        user_input = st.text_area("You:", key="input", height=100)
        submit_button = st.form_submit_button(label="Send")

    if submit_button and user_input:
        output, total_tokens, prompt_tokens, completion_tokens = generate_response(
            user_input
        )
        st.session_state["past"].append(user_input)
        st.session_state["generated"].append(output)
        st.session_state["model_name"].append(model)
        st.session_state["total_tokens"].append(total_tokens)

        # from https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/#pricing
        if model_name == "gpt-35-turbo":
            cost = total_tokens * 0.002 / 1000
        if model_name == "gpt-35-turbo-16k":
            cost = total_tokens * 0.002 / 1000
        if model_name == "GPT-4":
            cost = (prompt_tokens * 0.03 + completion_tokens * 0.06) / 1000

        cost = total_tokens * 0.001625 / 1000

        st.session_state["cost"].append(cost)
        st.session_state["total_cost"] += cost


if st.session_state["generated"]:
    with response_container:
        for i in range(len(st.session_state["generated"])):
            message(
                st.session_state["past"][i],
                is_user=True,
                key=str(i) + "_user",
            )
            message(st.session_state["generated"][i], key=str(i))
            st.write(
                f"Model used: {st.session_state['model_name'][i]} -- Number of tokens: {st.session_state['total_tokens'][i]} -- Cost: ${st.session_state['cost'][i]:.5f}"
            )
        counter_placeholder.write(
            f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}"
        )