import streamlit as st
#import db
import pandas as pd

st.header("Welcome to my book shelf.")

selected = st.selectbox(
    "Select", ["All", "Reading", "Completed", "Future Reads"])


books = pd.read_excel('Booklist.xlsx', header=0)

if selected == "Completed":
    books_completed = books.loc[books["Status"] == "C"]
    st.table(books_completed)


elif selected == "Future Reads":
    books_future = books.loc[books["Status"] == "F"]
    st.table(books_future)


elif selected == "Reading":
    books_reading = books.loc[books["Status"] == "R"]
    st.table(books_reading)

else:
    st.table(books)


st.markdown("<address>If you want to send your recommendation you can send it to <a href=\"mailto:devmani96@gmail.com\">devmani96@gmail.com</a>  &#128512</address>",
            unsafe_allow_html=True)


st.markdown("If you want to brush your Vocabulary <a href=\"https://twitter.com/learningtoget19\">Click Here</a> &#9889", unsafe_allow_html=True)