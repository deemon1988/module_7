# Домашнее задание по теме "Оператор "with"
from operator import index
from os.path import split


class WordsFinder:
    def __init__(self, *files_txt):
        self.file_names = files_txt
        self._all_words = None

    def get_all_words(self):
        if self._all_words is not None:
            return self._all_words
        all_words = {}
        del_simbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        words = []
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for k in del_simbols:
                        if k in line:
                            line = line.replace(k, '')
                    line = line.split()
                    if line:
                        words.extend(line)
                all_words[i] = words
                print(all_words)
        self._all_words = all_words
        return all_words

    def find(self, word):
        find_words = {}
        for key, value in self.get_all_words().items():
            for w in value:
                if word.lower() == w:
                    find_words[key] = value.index(w)+1
                    print(find_words)
                    return find_words


finder1 = WordsFinder('test_file.txt')
finder1.get_all_words()
finder1 = WordsFinder('products.txt')
finder1.get_all_words()

finder1.find("TEXT")
