import streamlit as st
import functions as fn


todos = fn.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'].strip().capitalize() + "\n"
    if new_todo == "\n" or new_todo == " ":
        return
    todos.append(new_todo)
    fn.set_todos(todos)
    st.session_state['new_todo'] = ""


def done_todo(key):
    index_local = int(key)
    st.write(f"Completed: {todos.pop(index_local)}")
    fn.set_todos(todos)


st.title("My ToDo App")
st.subheader(" This is my ToDo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    st.checkbox(todo, key=index, on_change=done_todo, args=(str(index)))

st.text_input(label="Enter new todo", label_visibility='hidden', placeholder="Add new todo ...",
              on_change=add_todo, key='new_todo',
              help='Type a new todo and press enter to add it to')

# st.write(st.session_state)