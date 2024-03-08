import os
import base64
import streamlit as st
from streamlit_option_menu import option_menu
from gemini_utility import (load_gemini_pro_model, gemini_pro_vision_response , simple_QA)
from PIL import Image
# to get the file path directly
working_directory = os.path.dirname(os.path.abspath(__file__))

# using the st.set_page_config we are setting names
st.set_page_config(
    page_title="Vamsi's Gemini AI",
    page_icon="⚡",
    layout="centered"
)

with st.sidebar:
    selected = option_menu('Gemini AI',
                           ['ChatBot',
                            'Image Captioning',

                            'Ask me anything'],
                           menu_icon='robot',
                           icons=['chat-heart-fill', 'image-fill',  'patch-question-fill'],
                           default_index=0
                           )




def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


if selected == "ChatBot":

    model = load_gemini_pro_model()
    # streamlit dont have the chat session(history of prev conversation)
    # so we need to have chat session in order to strore the prev messages

    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    st.title("🤖 EEE boys chat bot  ")
    # to display the chat history
    for message in st.session_state.chat_session.history:
        # st.chat_message is an in built function which will display the conversation in a chat format inside brackets we specify the role of the person
        # and based on the role we will get the convo ex: user , assistant

        with st.chat_message(translate_role_for_streamlit(message.role)):
            # st.markdown( message.parts[0].text)
            st.markdown(message.parts[0].text)

            #  in message which was returned by st.session_state.chat_session.history it has many details in that we just want info related to chat .this is present in the

    # input feild where we are taking the conversation
    user_prompt = st.chat_input("Ask Something Bro... 😜")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        # we are sending the user prompt to gemini and model is sending us the gemini_response

        with st.chat_message("assistant"):
            # st.markdown(gemini_response.text)
            st.markdown(gemini_response.text)

if selected == "Image Captioning":
    st.title("Hello boys 😎 Here is your solution generator 📷 ")
    uploaded_image = st.file_uploader(" upload an image ")
    if st.button("Generate Caption"):
        image = Image.open(uploaded_image)
        col1 , col2 = st.columns(2)
        with col1:
            resized = image.resize((800 , 500 ))
            st.image(resized)

        default_prompt = "explain me about this in detail with examples "
        # getting response
        with col2:
            caption = gemini_pro_vision_response(default_prompt , image )
            st.info(caption)

if selected == 'Ask me anything':
    st.title("ASK Me a question ❓")
    user_prompt = st.text_area(label='', placeholder="Ask me anything...")

    if st.button("Get Response"):
        response = simple_QA(user_prompt)
        st.markdown(response)




