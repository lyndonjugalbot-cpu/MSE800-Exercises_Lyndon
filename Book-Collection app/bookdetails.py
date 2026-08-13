#book collection class
#holds the in-memory list of books and the operations the app/CLI can perform on it.
#unlike the CLI version, these methods RETURN strings/lists instead of printing,
#so the web app (app.py) can flash() or render them in HTML.

class BookCollection:
    def __init__(self):
        # each book is stored as a dict: {"title": ..., "author": ...}
        self.books = []

    def add_book(self, title, author):
        # prevent duplicate titles (case-insensitive check)
        if any(book["title"].lower() == title.lower() for book in self.books):
            return f"'{title}' is already in the collection."
        # store the new book and confirm it was added
        self.books.append({"title": title, "author": author})
        return f"Added: {title} by {author}"

    def remove_book(self, title):
        # scan for a case-insensitive title match and remove the first one found
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                return f"Removed: {title}"
        # no matching book was found
        return "Book not found"

    def search_book(self, keyword):
        # find every book whose title contains the keyword (case-insensitive, partial match)
        matches = [book for book in self.books if keyword.lower() in book["title"].lower()]
        if not matches:
            return ["Book not found"]
        # return one formatted line per match
        return [f"Book found: {book['title']} by {book['author']}" for book in matches]

    def display_books(self):
        # return a line per book, or a placeholder message if the collection is empty
        if not self.books:
            return ["No books in the collection."]
        return [f"{book['title']} by {book['author']}" for book in self.books]
