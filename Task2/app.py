import os
from dotenv import find_dotenv, load_dotenv
import streamlit as st
import google.generativeai as genai  

path = find_dotenv() # find the path of the .env file 
load_dotenv(path) #  load the .env file
API_KEY = os.getenv("API_KEY") # storing the api key to a variable from .env file
genai.configure(api_key=API_KEY) # configure model using api key

model = genai.GenerativeModel('gemini-1.5-flash') # create an instance of GenerativeModel to use gemini-1.5-flash

st.title('Flash chat') # app title

if "messages" not in st.session_state: 
    st.session_state.messages = [ # creates a dictionary with two keys: role (assistant or user) and content
        {
            "role":"assistant",
            "content":"How can I help you?"
        }
    ]

for message in st.session_state.messages: # display each message in the chat history [list]
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def google_it(query): # calling model api to generate from gemini-1.5-flas
    response = model.generate_content(query,
                                    generation_config= genai.types.GenerationConfig(
                                        max_output_tokens=200, # restrict response size to 200 tokens
                                        candidate_count=1, # one reply
                                        temperature=0.7) # creative response
                                    
                                    )
    
    sentence = response.text.split('.') # split response into sentences ending with '.'
    if len(sentence)>4: 
        reply = '.'.join(sentence[:4]) + '.' # reply with only few sentences (adjust according to preference)
    else:
        reply = response.text # if less number of sentences in response, reply without limiting
    
    # displaying assistant response
    with st.chat_message("assistant"):
        st.markdown(reply)

    # appending user prompts to chat history
    st.session_state.messages.append(
        {
            "role":"user",
            "content": query # storing user prompts to "content"
        } 
    )
    # appending assistant reply to the dictionary 
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content": reply # extract text in response 
        }
    )

prompt = st.chat_input('Enter a prompt here:') # access streamlit chat input data

if prompt:
    # display prompt on the interface
    with st.chat_message("user"):
        st.markdown(prompt) 

    google_it(prompt) # call the google_it function to get genai response 