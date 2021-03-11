from re import sub
import streamlit as st
import db


st.header("Welcome to my book shelf.")

selected = st.selectbox("Select", ["Reading", "Completed", "Future Reads"])


def select_subCategory():
    sCategory = db.get_subCategory()
    sub_cat = []
    for sc in sCategory:
        sub_cat.append(sc[0])
    subCategory = st.selectbox("Category", sub_cat)
    return subCategory


if selected == "Completed":
    subCat = select_subCategory()
    completed = db.get_completed()
    to_show = db.book_with_subCategory(subCat)
    st.write(to_show)


elif selected == "Future Reads":
    subCat = select_subCategory()
    want_to_read = db.get_want_to_read()
    st.write(want_to_read)

else:
    completed = db.get_reading()
    print(type(completed))
    print(completed)
    st.write(completed)

db.book_with_subCategory("Fiction")

db.get_completed()