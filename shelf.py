current_reading = ['Rework']
completed = ['The Kite Runner', 'The Psychology of Money', 'Atomic Habbits', 'Harry Potter Serires']

want_to_read = ['Sapiens', 'Angels and Demons', 'Sapiens', 'No Rules Rules']

import streamlit as st

st.header("Welcome to my book shelf.")

selected = st.selectbox("Select", ["Reading", "Competed", "Future Reads"])

if selected == "Reading":
    st.write(current_reading)

elif selected == "Future Reads":
    st.write(want_to_read)

else:
    st.write(completed)