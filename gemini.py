import google.generativeai as genai
import streamlit as st

st.title("📝 AI Data Science Tutor 💎 ")

#user's input
f = open("keys/.gemini.txt")
key = f.read()

genai.configure(api_key = key)


model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest',
                              system_instruction=""" 
                              you are an AI Data Science Tutor and your task is to resolve only the data science doubts of the user.
""")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Init the chat object
chat = model.start_chat(history=st.session_state['chat_history'])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message('user').write(user_prompt)
    response = chat.send_message(user_prompt, stream=True)
    response.resolve()
    st.chat_message('ai').write(response.text)
    st.session_state['chat_history'] = chat.history






