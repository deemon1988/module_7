import os
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Пример Treeview")

# Создаем Treeview
tree = ttk.Treeview(root)
tree.pack(fill='both', expand=True)

# Добавляем корневую директорию
root_node = tree.insert('', 'end', text=os.path.abspath(os.sep), open=True)

root_path = os.path.abspath(os.sep)
excluded_dirs = {'$RECYCLE.BIN'}
for item in os.listdir(root_path):
    if item in excluded_dirs:
        continue
    item_path = os.path.join(root_path, item)
    print(item_path)
# Запуск
#root.mainloop()
