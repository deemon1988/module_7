import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Пример Treeview - Таблица")
window.geometry("1280x250")
window.resizable(width=False, height=False)

# Создаем Treeview
tree = ttk.Treeview(window, columns=('Name', 'Age', 'City'),show='headings')
tree.pack(fill='both', expand=True)
# Настройка заголовков колонок
tree.heading('Name', text='Имя')
tree.heading('Age', text='Возраст')
tree.heading('City', text='Город')
# Настройка ширины колонок
tree.column('Name', width=150)
tree.column('Age', width=100, anchor='center')
tree.column('City', width=150)
# Добавляем данные
tree.insert('',tkinter.END, values=("Иван", 25, "Москва"))
tree.insert("", tkinter.END, values=("Анна", 30, "Санкт-Петербург"))
tree.insert("", tkinter.END, values=("Петр", 22, "Екатеринбург"))

window = tkinter.mainloop()