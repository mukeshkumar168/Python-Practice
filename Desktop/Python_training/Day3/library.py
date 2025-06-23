class Book:

    """
    Book class => book title, author and availability status 
    """
    def __init__(self, title, author ):
        self.title = title
        self.author = author
        self.available = True  # all books are available (default)

    def __str__(self):

        """Returns readable string with book details and status 
           returns:
                str: book details
            """
        
        if self.available:
            status = "Available"
        else:
            status = "Not Available"
        return f'{self.title} by {self.author} [{status}]'
    

class Library:

    """Library class => Hold and manages  book
        Methods: 
            add_book - add book to libray
            display_book - display books in library """
            
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)  # add book to self.books list
    
    def display_books(self):

        print("Library Books:")
        for book in self.books: 
            print(f'-{book}')
        print()

class Member:

    """Member class =>Library members with borrow and return books status
    Methods:
        borrow: allow member to borrow if it available in library
        return_b: member to return the borrowed book """


    def __init__(self, name):
        self.name = name
        self.borrowed = []  # borrowed_list
    
    def borrow(self, book): 
        if book.available:
            self.borrowed.append(book)  # add book to borrowed_list
            book.available = False
            print(f'{self.name} Borrowed {book.title}') 
        else:
            print(f'Book not available  ')

    def return_b(self, book):
        if book in self.borrowed:
            self.borrowed.remove(book)  # remove book from borrowed_list
            book.available = True
            print(f'{self.name} returned {book.title}')
        else:
            print(f'{self.name} not borrowed {book.title}')



# main funtion
if __name__ == '__main__':
    
    # object for library class
    my_library = Library()

    # create book
    book1 = Book('Python Programming', 'abc')
    book2 = Book('Data Science', 'def')
    book3 = Book('Machine Learning', 'ghi')

    # add book to library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # create a library
    member1 = Member('Ram')

    # display book in library
    my_library.display_books()

    # member borrows a book
    member1.borrow(book2)
    my_library.display_books()

    # member return a book
    member1.return_b(book2)
    
    my_library.display_books()


