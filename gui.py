import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.Input(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", tooltip="Add the todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])


edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

close_button = sg.CloseButton("Exit", tooltip="Close the window")


window = sg.Window("Marco's TO-DO App",
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [close_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
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
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window["todo"].update(value='')
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
