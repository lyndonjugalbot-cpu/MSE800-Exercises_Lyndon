#book collection class

class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        if any(book["title"].lower() == title.lower() for book in self.books):
            return f"'{title}' is already in the collection."
        self.books.append({"title": title, "author": author})
        return f"Added: {title} by {author}"

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                return f"Removed: {title}"
        return "Book not found"

    def search_book(self, keyword):
        matches = [book for book in self.books if keyword.lower() in book["title"].lower()]
        if not matches:
            return ["Book not found"]
        return [f"Book found: {book['title']} by {book['author']}" for book in matches]

    def display_books(self):
        if not self.books:
            return ["No books in the collection."]
        return [f"{book['title']} by {book['author']}" for book in self.books]
