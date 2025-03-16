class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}"

    def check_out(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True

class Member:

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"ID: {self.member_id}, Name: {self.name}, Borrowed Books: {len(self.borrowed_books)}"

    def borrow_book(self, book):
        if book.check_out():
            self.borrowed_books.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        else:
            return False

class Library:

    def __init__(self):
        self.books = {}  # book_id: Book object
        self.members = {} # member_id : Member object

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def find_book(self, book_id):
        return self.books.get(book_id)

    def find_member(self, member_id):
        return self.members.get(member_id)

    def display_books(self):
        for book in self.books.values():
            print(book)

    def display_members(self):
        for member in self.members.values():
            print(member)

library = Library()

book1 = Book(1, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
book2 = Book(2, "Pride and Prejudice", "Jane Austen")
book3 = Book(3, "1984", "George Orwell")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

member1 = Member(101, "Alice")
member2 = Member(102, "Bob")

library.add_member(member1)
library.add_member(member2)

library.display_books()
library.display_members()

print("\nAlice borrows a book:")
if member1.borrow_book(library.find_book(1)):
    print("Book borrowed successfully!")
else:
    print("Book not available.")

print("\nAlice's borrowed books:")
print(member1)

print("\nBob tries to borrow the same book:")
if member2.borrow_book(library.find_book(1)):
    print("Book borrowed successfully!")
else:
    print("Book not available.")

print("\nAlice returns the book:")
if member1.return_book(library.find_book(1)):
    print("Book returned successfully!")
else:
    print("Book return failed.")

print("\nBob now borrows the same book:")
if member2.borrow_book(library.find_book(1)):
    print("Book borrowed successfully!")
else:
    print("Book not available.")

print("\nBob's borrowed books:")
print(member2)