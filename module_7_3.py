# Домашнее задание по теме "Оператор "with"


class WordsFinder:
    def __init__(self, *files_txt):
        self.file_names = files_txt
        self._all_words = None

    def get_all_words(self):
        if self._all_words is not None:
            return self._all_words
        all_words = {}
        del_simbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for elem in self.file_names:
            words = []
            with open(elem, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for k in del_simbols:
                        if k in line:
                            line = line.replace(k, '')
                    line = line.split()
                    if line:
                        words.extend(line)
                all_words[elem] = words
        self._all_words = all_words
        print(all_words)
        return all_words

    def find(self, word):
        find_words = {}
        for key, value in self.get_all_words().items():
            for w in value:
                if word.lower() == w:
                    find_words[key] = value.index(w) + 1
                    print(find_words)
                    return find_words

    def count(self, word):
        count = 0
        count_dict = {}
        for key, value in self.get_all_words().items():
            for w in value:
                if word.lower() == w:
                    count += 1
            count_dict[key] = count
            count = 0
        print(count_dict)
        return count_dict


finder1 = WordsFinder('test_file.txt', 'products.txt')
dict_ = finder1.get_all_words()
# print(dict_.keys())

finder1.find("TEXT")
finder1.count('TExt')

# list_ = 'Potato, 50.0, Vagetables'.split()
# for i in list_:
#     if ',' in i:
#         i = i.replace(',', '')
#     try:
#         if float(i):
#             print(i)
#     except:
#         continue
