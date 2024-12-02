import os
import tkinter
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfilename

from click import command


def file_select():
    file_name = filedialog.askopenfilename(initialdir = '/',title='Выберите файл',
                                           filetypes=(("Текстовый файл",'.txt'),('Все файлы', '*')))
    if file_name:
        text['text'] = text['text'] + file_name
        os.startfile(file_name)

def file_open():
    file_path = filedialog.askopenfilename(title='Выберите файл',
                                           filetypes=(("Текстовый файл",'.txt'),('Все файлы', '*')))
    if file_path:
        print(f'Открыт файл  {file_path}')

def about():
    name = 'about.txt'
    file_text = ''
    with open(name, encoding='utf-8') as file:
        for line in file:
            file_text = file_text + ''.join(line)+'\n'
    text_about = tkinter.Label(window, text= file_text)
    text_about.grid(column=1, row = 3)

def help():
    name = 'help.txt'
    file_text = ''
    with open(name, encoding='utf-8') as file:
        for line in file:
            file_text = file_text + ''.join(line) + '\n'
    text_help = tkinter.Label(window, text=file_text)
    text_help.grid(column=1, row=4)

def create():
    file_new = filedialog.asksaveasfilename(title='Создать новый текстовый документ',
                                            defaultextension='.txt',
                                            filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")))
    if file_new:
        print(file_new)

def exit_app():
    window.quit()

window = tkinter.Tk()
window.title("Файловый менеджер")
window.geometry("450x250")
window.resizable(width=False, height=False)

text = tkinter.Label(window ,text ="Файл " ,height=5, width=65, background='silver')
text.grid(column = 1, row=1)
button_select = tkinter.Button(window, text='Выбрать файл', width=20, height=3, foreground='blue',command = file_select)
button_select.grid(column=1, row=2)

menu_bar = tkinter.Menu(window)

menu_file = tkinter.Menu(menu_bar, tearoff=0)
menu_file.add_command(label='Открыть', command=file_open)
menu_file.add_command(label='Создать', command= create)
menu_file.add_separator()
menu_file.add_command(label='Выход',command=exit_app)


menu_about = tkinter.Menu(menu_bar, tearoff=0)
menu_about.add_command(label='О нас', command=about)
menu_help = tkinter.Menu(menu_bar, tearoff=0)
menu_help.add_command(label='Справка', command = help)


menu_bar.add_cascade(label="Файл", menu=menu_file)
menu_bar.add_cascade(label="Инфо", menu=menu_about)
menu_bar.add_cascade(label='Руководство', menu=menu_help)


window.config(menu=menu_bar)
window.configure(background='black')


window.mainloop()

