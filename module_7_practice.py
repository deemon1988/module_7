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
        new_window.title(os.path.basename(file_path))
        # Добавление текстового поля для отображения содержимого
        text_widget = tkinter.Text(new_window, wrap='word')
        text_widget.insert('1.0', content)
        # text_widget.config(state="disabled")  # Запрет редактирования
        text_widget.pack(expand=True, fill='both')
        menu_bar = tkinter.Menu(new_window)
        file_menu = tkinter.Menu(menu_bar, tearoff=0)
        def curent_content_save():
            content = text_widget.get('1.0', tkinter.END)
            file_save(content)

        file_menu.add_command(label="Сохранить", command=curent_content_save)
        menu_bar.add_cascade(label='Файл', menu=file_menu)

        new_window.configure(menu=menu_bar)


def file_save(content):

    file_path = filedialog.asksaveasfilename(title='Сохранить текстовый документ',
                                             defaultextension='.txt',
                                             filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")))
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Контент успешно сохранен в файл.{file_path}")

    return os.path.basename(file_path)


def file_create():

    window_file = tkinter.Toplevel(window)
    window_file.title('Новый текстовый документ')

    text_widget = tkinter.Text(window_file, wrap='word')
    text_widget.pack(expand=True, fill='both')

    menu_bar_file = tkinter.Menu(window_file)
    menu_new_file = tkinter.Menu(menu_bar, tearoff=0)

    def save_current_content():
        content = text_widget.get('1.0', tkinter.END)
        win_title = file_save(content)
        window_file.title(win_title)
    menu_new_file.add_command(label='Сохранить', command=save_current_content)
    menu_bar_file.add_cascade(label='Файл', menu=menu_new_file)

    window_file.configure(menu=menu_bar_file)





def about():
    name = 'about.txt'
    content = ''
    with open(name, encoding='utf-8') as file:
        for line in file:
            content = content + ''.join(line) + '\n'
    window_about = tkinter.Toplevel(window)
    window_about.title("About")
    window_about.geometry("350x250")
    window_about.resizable(width=False, height=False)
    text_about = tkinter.Label(window_about, text=content)
    text_about.grid(row=0, column=0, padx=65, pady=50, sticky='nsew')


def info():
    name = 'help.txt'
    content = ''
    with open(name, encoding='utf-8') as file:
        for line in file:
            content = content + ''.join(line) + '\n'
    window_info = tkinter.Tk()
    window_info.title('Info')
    text_info = tkinter.Label(window_info, text=content)
    text_info.grid(column=0, row=0)


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
# menu_file.add_command(label='Сохранить', command=file_save)
menu_file.add_separator()
menu_file.add_command(label='Выход', command=exit_app)

menu_about = tkinter.Menu(menu_bar, tearoff=0)
menu_about.add_command(label='О нас', command=about)
menu_help = tkinter.Menu(menu_bar, tearoff=0)
menu_help.add_command(label='О программе', command=info)

menu_bar.add_cascade(label="Файл", menu=menu_file)
menu_bar.add_cascade(label="Инфо", menu=menu_about)
menu_bar.add_cascade(label='Справка', menu=menu_help)


window.config(menu=menu_bar)
window.configure(background='black')

window.mainloop()
