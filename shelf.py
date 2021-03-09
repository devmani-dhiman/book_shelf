import streamlit as st
import db

current_reading = ['Rework']
completed = ['The Kite Runner', 'The Psychology of Money', 'Atomic Habbits', 'Harry Potter Serires']

want_to_read = ['Sapiens', 'Angels and Demons', 'Sapiens', 'No Rules Rules']


st.header("Welcome to my book shelf.")

selected = st.selectbox("Select", ["Reading", "Competed", "Future Reads"])

if selected == "Reading":
    books = db.get_reading()
    st.write(books) 

elif selected == "Future Reads":
    st.write(want_to_read)

else:
    st.write(completed)