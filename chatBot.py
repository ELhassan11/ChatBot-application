import os
import streamlit as st
import google.generativeai as genai
api = os.getenv("GEMINI_API_KEY")
st.title('Google AI Text Generation')

#configure google generative ai
if api:
    genai.configure(api_key= api)
else:
    st.error('Your API is Not Valid')
#define a function for text generation
def Generate_Text(text):
    #call generative model('gemini-2.5-flash')
    model = genai.GenerativeModel('gemini-2.5-flash')
    response=model.generate_content(text)
    return response.text
if 'messages'not in st.session_state:
    st.session_state.messages=[]
#display all messages
for message in st.session_state.messages:
    with st.chat_message(message['role']):#role----> user/assistant
        st.markdown(message['content'])#content---->user_input / response

#input area for user input
if user_input :=st.chat_input('Enter Your Text...'):
    #display user message
    with st.chat_message('user'):
        st.markdown(user_input)

    #append user message in session state
    st.session_state.messages.append({'role':'user','content':user_input})

    #generate response from google generative ai model 
    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        with st.spinner('Generating response...'):
            response_text = Generate_Text(user_input)
            message_placeholder.markdown(f'{response_text}')
    #append model response in session state
    st.session_state.messages.append({'role':'assistant','content': response_text})





