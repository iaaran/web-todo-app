import streamlit as st
import functions as fn


def add_todo():
    new_todo = st.session_state['new_todo'] + "\n"
    todos.append(new_todo)
    fn.set_todos(todos)

todos = fn.get_todos()

st.title("My To-DO App")
st.subheader(" This is my To-Do app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo ...",
              on_change=add_todo, key='new_todo')

st.session_state