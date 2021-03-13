import streamlit as st
import db


st.header("Welcome to my book shelf.")

selected = st.selectbox("Select", ["All","Reading", "Completed", "Future Reads"])

tag = ""

def select_subCategory():
    sCategory = db.get_subCategory()
    sub_cat = []
    for sc in sCategory:
        sub_cat.append(sc[0])
    subCategory = st.selectbox("Category", sub_cat)
    return subCategory


if selected == "Completed":
    tag = "C" 
    subCat = select_subCategory()
    completed = db.get_completed()
    to_show = db.book_with_subCategory(subCat, tag)
    st.write(to_show)


elif selected == "Future Reads":
    tag = "F"
    want_to_read = db.get_want_to_read()
    st.write(want_to_read)


elif selected == "Reading":
    completed = db.get_reading()
    tag = "R"
    st.write(completed)

else:
    all = db.get_all_items(r'D:\sqlite\db\books.db')
    st.write(all)
