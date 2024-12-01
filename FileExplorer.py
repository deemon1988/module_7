import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class FileExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple File Explorer")
        self.root.geometry("600x400")

        # Создаем дерево для отображения структуры каталогов
        self.tree = ttk.Treeview(self.root)
        self.tree.heading("#0", text="Directory Structure", anchor='w')
        self.tree.grid(row=0, column=0, sticky='nsew')

        # Создаем вертикальный скроллбар
        self.vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.tree.configure(yscrollcommand=self.vsb.set)

        # Создаем корневой узел
        self.root_node = self.tree.insert('', 'end', text=os.path.abspath(os.sep), open=True)
        self.process_directory(self.root_node, os.path.abspath(os.sep))

        # Настройка раскладки
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Добавляем кнопку для выбора файла
        self.select_button = ttk.Button(self.root, text="Select File", command=self.open_file)
        self.select_button.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

    def process_directory(self, parent, path):
        excluded_dirs = {'$RECYCLE.BIN'}
        for item in os.listdir(path):
            if item in excluded_dirs:
                continue
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                node = self.tree.insert(parent, 'end', text=item, open=False)
                self.process_directory(node, item_path)
            else:
                self.tree.insert(parent, 'end', text=item, open=False)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Select a File")
        if file_path:
            print(f"Selected file: {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorer(root)
    root.mainloop()