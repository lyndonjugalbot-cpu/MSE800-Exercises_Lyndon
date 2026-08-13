#book collection class

class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        if any(book["title"].lower() == title.lower() for book in self.books):
            print(f"'{title}' is already in the collection.")
            return
        self.books.append({"title": title, "author": author})
        print(f"Added: {title} by {author}")

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"Removed: {title}")
                return
        print("Book not found")

    def search_book(self, keyword):
        matches = [book for book in self.books if keyword.lower() in book["title"].lower()]
        if not matches:
            print("Book not found")
            return
        for book in matches:
            print(f"Book found: {book['title']} by {book['author']}")

    def display_books(self):
        if not self.books:
            print("No books in the collection.")
            return
        for book in self.books:
            print(f"{book['title']} by {book['author']}")
