
import streamlit as st
import backend as bk

st.set_page_config(page_title="Cohere Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Cohere Chatbot")
st.write("Talk to an AI powered by Cohere!")

if "conversations" not in st.session_state:
    st.session_state.conversations = {} 
if "active_chat" not in st.session_state:
    st.session_state.active_chat = "Chat 1"
    st.session_state.conversations["Chat 1"] = []



st.sidebar.header("💬 Chat History")

chat_names = list(st.session_state.conversations.keys())
selected_chat = st.sidebar.selectbox(
    "Select a chat",
    chat_names,
    index=chat_names.index(st.session_state.active_chat)
)


st.session_state.active_chat = selected_chat

if st.sidebar.button("➕ New Chat"):
    new_name = f"Chat {len(chat_names) + 1}"
    st.session_state.conversations[new_name] = []
    st.session_state.active_chat = new_name
    st.rerun()


history = st.session_state.conversations[st.session_state.active_chat]

for msg in history:
    with st.chat_message("user" if msg["role"] == "USER" else "assistant"):
        st.write(msg["message"])


if prompt := st.chat_input("Type your message..."):
  
    history.append({"role": "USER", "message": prompt})
    with st.chat_message("user"):
        st.write(prompt)

   
    try:
        bot_response = bk.get_text_output(history, prompt)
    except Exception as e:
        bot_response = f"⚠️ Error: {e}"

   
    history.append({"role": "CHATBOT", "message": bot_response})
    with st.chat_message("assistant"):
        st.write(bot_response)



    
    

