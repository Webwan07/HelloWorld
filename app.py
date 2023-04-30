import streamlit as st
import clipboard
st.set_page_config("Test Web",layout='centered',initial_sidebar_state='auto')

text = "Hello world"
st.subheader(text)
if st.button("Copy"):
    clipboard.copy(text)
    st.success("text copied to clipboard")

