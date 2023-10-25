import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.Input(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", tooltip="Add the todo")
close_button = sg.CloseButton("x", tooltip="Close the window")

window = sg.Window("Marco's TO-DO App",
                   layout=[[label], [input_box, add_button],[close_button]],
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
        case sg.WINDOW_CLOSED:
            break

window.close()
