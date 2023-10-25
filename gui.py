import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add", tooltip="Add the todo")
close_button = sg.CloseButton("x", tooltip="Close the window")

window = sg.Window("Marco's TO-DO App", layout=[[label], [input_box, add_button],[close_button]])

window.read()
window.close()
