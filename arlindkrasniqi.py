import string
class Book:
    def __init__(self, filepath, title, author, genre):
        self.filepath = filepath
        self.title = title
        self.author = author
        self.genre = genre
        self.words = {}
        self.most_common_words = []

    def __str__(self):
        return f'Title:{self.title}\nAuthor:{self.author}\nGenre:{self.genre}'

    def process_file(self):
        f = open(self.filepath, encoding="utf8")
        for l in f:
            self.process_line(l)
        return self.words

    def process_line(self, l):
        l = l.replace('-', ' ')
        for word in l.split():
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            self.words[word] = self.words.get(word, 0) + 1

    def total_words(self):
        return sum(self.words.values())

    def different_words(self):
        return len(self.words)

    def populate_most_common_words(self):
        for key, value in self.words.items():
            self.most_common_words.append((value, key))
        self.most_common_words.sort(reverse=True)

    def print_most_common_words(self):
        print('The most common words are:')
        for freq, word in self.most_common_words[:10]:
            print(word, freq, sep='\t')

b=Book('./emma.txt','EMA','JANE AUSTEN',"NOVEL")
print(b)
b.process_file()
b.populate_most_common_words()
b.total_words()
b.different_words()
b.print_most_common_words()







