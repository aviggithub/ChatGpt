# -*- coding: utf-8 -*-
"""
Create Chatbot web application using openAI API
@author: Avinash G
"""
import streamlit as st
import openai
secret = ''
st.set_page_config(
    page_title="ChatGPT OpenAI API",
    page_icon=":robot:"
)

openai.api_key = "chatgpt key"

def Bot_generate_msg(human_msg):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=human_msg,
    temperature=0,
    max_tokens=50,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=[" Human:", " AI:"]
    )
    print(response.choices[0].text)
    return response.choices[0].text

st.header("Create AI Chatbot using CHATGPT Python")

if 'Bot_msg' not in st.session_state:
    st.session_state['Bot_msg'] = []

if 'History_msg' not in st.session_state:
    st.session_state['History_msg'] = []


def get_text():
    input_text = st.text_input("Enter Your Text", key="input")
    return input_text 


user_input = get_text()

if user_input:
    st.session_state.History_msg.append(user_input)
    st.session_state.Bot_msg.append(Bot_generate_msg(user_input))

if st.session_state['Bot_msg']:
    for i in range(len(st.session_state['Bot_msg'])-1, -1, -1):
        st.markdown("BOT :- "+" "+st.session_state["Bot_msg"][i])
        st.markdown("HUMAN :- "+"\n"+st.session_state['History_msg'][i])
 
        