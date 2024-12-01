import os
import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Пример Treeview - Иерархия")
window.geometry("1280x250")
window.resizable(width=False, height=False)

tree = ttk.Treeview(window)
tree.pack(fill='both', expand=True)

# Добавляем корневой узел
root_node = tree.insert('', tkinter.END, text='Корневой узел')
# Добавляем дочерние узлы
child1 = tree.insert(root_node, tkinter.END, text='Дочерний элемент 1')
child2 = tree.insert(root_node, tkinter.END, text='Дочерний элемент 2')
# Добавляем под-узлы
tree.insert(child1, tkinter.END, text="Подэлемент 1.1")
tree.insert(child1, tkinter.END, text="Подэлемент 1.2")
tree.insert(child2, tkinter.END, text="Подэлемент 2.1")
# Раскрываем корневой узел
tree.item(root_node, open=True)
tree.heading("#0", text="Directory Structure", anchor='w')
tree.grid(row=0, column=0, sticky='nsew')
# Создаем вертикальный скроллбар
vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
vsb.grid(row=0, column=1, sticky='ns')
tree.configure(yscrollcommand=vsb.set)
# Создаем корневой узел
root_node = tree.insert('', 'end', text=os.path.abspath(os.sep), open=True)


window = tkinter.mainloop()
