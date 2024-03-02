import streamlit as st
import functions as fn


todos = fn.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + "\n"
    todos.append(new_todo)
    fn.set_todos(todos)
    st.session_state['new_todo'] = ""


st.title("My To-DO App")
st.subheader(" This is my To-Do app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo{index}")
    if checkbox:
        st.write(f"Completed: {todos.pop(index)}")
        fn.set_todos(todos)
        del st.session_state[f"todo{index}"]
        st.experimental_rerun()


st.text_input(label="Enter new todo", label_visibility='hidden', placeholder="Add new todo ...",
              on_change=add_todo, key='new_todo')

st.write(st.session_state)