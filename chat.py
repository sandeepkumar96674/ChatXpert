from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Loading the Gemini Model  to get response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_response(question):
    response=chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="ChatBuddy")
st.header("ChatBuddy: Your Personal Chat Assistant 😎")

 # Add "Connect with Sandeep" button with LinkedIn profile link
if st.button("Connect with Sandeep"):
    # Use JavaScript to trigger the link opening upon button click
    st.markdown(
        '<a href="https://www.linkedin.com/in/the-sandeep-kumar" target="_blank">Click here to connect with me on LinkedIn</a>',
        unsafe_allow_html=True
    )


#Initialization of Sessio State to Track the History (if Session Doesn't exist, It'll create a new session)
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Write your Query:",key="Ques")
submit=st.button("Ask your Question")

if submit and input:
    response=get_response(input)

    #Adding Users Question and Response to session chat History
    st.session_state['chat_history'].append(("You",input))
    st.subheader("Here is Your Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("ChatBuddy",chunk.text))

st.subheader("Your Chat History is:")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")