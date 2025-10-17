# main.py
import streamlit as st

# --- Placeholder for backend logic (will be developed later) ---
def handle_user_query(query):
    # For now, it just gives a simple, fixed response.
    if "IPC 302" in query:
        return "IPC Section 302 pertains to the punishment for murder..."
    else:
        return "I am ready to help with your legal question."

# --- Streamlit User Interface (UI) Code ---

# This creates the main title of your application.
st.title("⚖️ LegalBot")

# This is a best practice to initialize the chat history.
if "messages" not in st.session_state:
    st.session_state.messages = []

# This loop displays any past messages in the chat.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# This creates the text input box at the bottom of the page.
# When the user types and hits Enter, the code inside this 'if' block runs.
if prompt := st.chat_input("Explain your legal problem here..."):
    # Display the user's new message.
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get the bot's response and display it.
    response = f"LegalBot: {handle_user_query(prompt)}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})