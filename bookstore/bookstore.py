class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def get_books(self):
        return self.books

    def search_books(self, title=None, author=None):
        found_books = []
        if self.books != None:
            for book in self.books:
                if title != None and title.lower() in book.title.lower():
                    found_books.append(book)
                elif author != None and author.name.lower() in book.author.name.lower():
                    found_books.append(book)
                else: continue
        return found_books

    def add_book(self, title):
        self.books.append(title)
        
class Author(Bookstore):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
    
    def get_books(self):
        return self.books


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
        
#Pray4Travis