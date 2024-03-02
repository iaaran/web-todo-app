import os


FILEPATH = "todos.txt"
if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file1:
        pass


def get_todos(filepath=FILEPATH):
    """ Read the text file and return
       the list of to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def set_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
    print("Executed 'functions' to test")
