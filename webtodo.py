import streamlit as st
import functions as fn

todos = fn.get_todos()

st.title("My To-DO App")
st.subheader(" This is my To-Do app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo ...")