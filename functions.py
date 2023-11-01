
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH): #Default parameter
    """
        Read a text file and return the list
        of todos items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local



def write_todos(todos_arg, filepath=FILEPATH ): # los default parameter deben
    # ir despues de los no default parameter.
    """Write the todo items list in a file text."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


