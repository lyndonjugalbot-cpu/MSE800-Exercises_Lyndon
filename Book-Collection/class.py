book_collection = []

#add book to the collection
def add_book(title, author):
    for book in book_collection:
        if book['title'] == title and book['author'] == author:
            print(f"Book '{title}' by {author} already exists in the collection.")
            return
    book_collection.append({'title': title, 'author': author})
    print(f"Book '{title}' by {author} added to the collection.")

#remove book from the collection
def remove_book(title, author):
    for book in book_collection:
        if book['title'] == title and book['author'] == author:
            book_collection.remove(book)
            print(f"Book '{title}' by {author} removed from the collection.")
            return
    print(f"Book '{title}' by {author} not found in the collection.")  

#search for a book in the collection
def search_book(title, author):
    for book in book_collection:
        if book['title'] == title and book['author'] == author:
            print(f"Book '{title}' by {author} found in the collection.")
            return
    print(f"Book '{title}' by {author} not found in the collection.")

