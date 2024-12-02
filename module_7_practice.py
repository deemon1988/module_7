import os
import tkinter
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfilename

from PIL.ImageOps import expand
from click import command


def file_select():
    file_name = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                           filetypes=(("Текстовый файл", '.txt'), ('Все файлы', '*')))
    if file_name:
        text['text'] = text['text'] + file_name
        os.startfile(file_name)


def file_open():
    file_path = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                           filetypes=(("Текстовый файл", '.txt'), ('Все файлы', '*')))
    if file_path:
        print(f'Открыт файл  {file_path}')
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        # Создание нового окна для отображения содержимого
        new_window = tkinter.Toplevel(window)
        new_window.title(f'Просмотр файла - {file_path}')
        # Добавление текстового поля для отображения содержимого
        text_widget = tkinter.Text(new_window, wrap='word')
        text_widget.insert('1.0', content)
        text_widget.config(state="disabled")  # Запрет редактирования
        text_widget.pack(expand=True, fill='both')


def file_save():
    file_save = filedialog.asksaveasfilename(title='Сохранить текстовый документ',
                                             defaultextension='.txt',
                                             filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")))
    if file_save:
        with open(file_save, 'w', encoding='utf-8') as file:
            pass
        print(file_save)


def file_create():
    window_file = tkinter.Toplevel(window)
    menu_bar_file = tkinter.Menu(window_file)
    menu_new_file = tkinter.Menu(menu_bar, tearoff=0)
    menu_new_file.add_command(label='Сохранить', command=file_save)
    menu_bar_file.add_cascade(label='Файл', menu=menu_new_file)
    window_file.configure(menu=menu_bar_file)

    # file_path = filedialog.asksaveasfilename(title='Сохранить текстовый документ',
    #                              defaultextension='.txt',
    #                              filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")))
    # if file_path:
    #     with open(file_path, 'w', encoding='utf-8') as file:
    #        pass

    # with open(file_path, 'r', encoding='utf-8') as r_file:
    #    content =  r_file.read()
    content = ''
    text_widget = tkinter.Text(window_file, wrap='word')
    text_widget.insert('1.0', content)
    text_widget.pack(expand=True, fill='both')


def about():
    name = 'about.txt'
    content = ''
    with open(name, encoding='utf-8') as file:
        for line in file:
            content = content + ''.join(line) + '\n'
    window_about = tkinter.Toplevel(window)
    window_about.geometry("350x250")
    window_about.resizable(width=False, height=False)
    text_about = tkinter.Label(window_about, text=content, font=("Arial"))
    text_about.grid(row=0, column=0, padx=65, pady=50, sticky='nsew')


def help():
    name = 'help.txt'
    file_text = ''
    with open(name, encoding='utf-8') as file:
        for line in file:
            file_text = file_text + ''.join(line) + '\n'
    text_help = tkinter.Label(window, text=file_text)
    text_help.grid(column=1, row=4)


def exit_app():
    window.quit()


window = tkinter.Tk()
window.title("Файловый менеджер")
window.geometry("450x250")
window.resizable(width=False, height=False)

text = tkinter.Label(window, text="Файл ", height=5, width=65, background='silver')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, text='Выбрать файл', width=20, height=3, foreground='blue', command=file_select)
button_select.grid(column=1, row=2)

menu_bar = tkinter.Menu(window)

menu_file = tkinter.Menu(menu_bar, tearoff=0)
menu_file.add_command(label='Открыть', command=file_open)
menu_file.add_command(label='Создать', command=file_create)
menu_file.add_command(label='Сохранить', command=file_save)
menu_file.add_separator()
menu_file.add_command(label='Выход', command=exit_app)

menu_about = tkinter.Menu(menu_bar, tearoff=0)
menu_about.add_command(label='О нас', command=about)
menu_help = tkinter.Menu(menu_bar, tearoff=0)
menu_help.add_command(label='Справка', command=help)

menu_bar.add_cascade(label="Файл", menu=menu_file)
menu_bar.add_cascade(label="Инфо", menu=menu_about)
menu_bar.add_cascade(label='Руководство', menu=menu_help)

window.config(menu=menu_bar)
window.configure(background='black')

window.mainloop()
