import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt", 'w') as file:
        pass

sg.theme("Reds")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do: ")
input_box = sg.Input(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", tooltip="Add the todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])


edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

close_button = sg.CloseButton("Exit", tooltip="Close the window",
                              size=44)


window = sg.Window("Marco's TO-DO App",
                   layout=[[clock], [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [close_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.",
                         font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("Please select an item first.",
                         font=('Helvetica', 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
