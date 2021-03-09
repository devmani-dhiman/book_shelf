import streamlit as st
from streamlit.elements.altair import generate_chart
import db


st.header("Welcome to my book shelf.")

selected = st.selectbox("Select", ["Reading", "Completed", "Future Reads"])

def select_genre():
    genre = st.selectbox("Genre", ["Fiction", "Non Fiction"])
    return genre

def select_subCategory():
    subCategory = st.multiselect("Sub Category", ["Auto Biography", "Crime", "Thriller", "Drama", "Self-Help", "Fantasy"])
    return subCategory


if selected == "Completed":
    genre = select_genre()
    subCat = select_subCategory()
    completed = db.get_completed()
    st.write(completed)

elif selected == "Future Reads":
    genre = select_genre()
    subCat = select_subCategory()
    want_to_read = db.get_want_to_read()
    st.write(want_to_read)

else:
    completed = db.get_reading()
    print(type(completed))
    print(completed)
    st.write(completed)