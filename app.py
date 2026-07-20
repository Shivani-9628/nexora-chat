 import streamlit as st

st.title("🤖 Nexora AI v2")
st.write("Welcome to Nexora AI!")

user_input = st.text_input("Ask me anything:")

if st.button("Submit"):
    if user_input.strip().lower() == "hello":
        st.success("Hello! How can I help you?")
    elif user_input.strip().lower() == "bye":
        st.success("Goodbye! Have a nice day!")
    elif user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        st.success("Thanks for your question! Nexora AI is under development.")