import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Файловый менеджер")
window.geometry("1280x250")
window.resizable(width=False, height=False)

text = tkinter.Label(window ,text ="Файл" ,height=5, width=20, background='silver')
text.grid(column = 1, row=1)
button_select = tkinter.Button(window, text='Выбрать файл', width=20, height=3, foreground='blue')
button_select.grid(column=1, row=2)
window.configure(background='black')
window.mainloop()

