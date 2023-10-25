import time

from functions import get_todos, write_todos

now = time.strftime("%b %d, - %Y %H:%M")
print("It is ", now)
while True:
    user_action = input("Type add, show, edit, complete or exit:" )
    user_action = user_action.strip()

    if user_action.startswith('add'):
        try:
            todo = user_action[4:]
            todo = todo.capitalize()
            todo = todo.rstrip()

            todos = get_todos()

            todos.append(todo + '\n')

            write_todos(todos)

        except ValueError:
            continue

    elif user_action.startswith('show'):

        todos = get_todos()

        new_todos = []

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}.- {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number-1

            todos = get_todos()

            new_todo = input('Enter a new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Insert the number of the todo to edit")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"The todo: {todo_to_remove.upper()} has been removed"
            print(message)
        except IndexError:
            print("You are out of range")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("That is not a valid option...")
print("C'ya")
