#main program

from bookdetails import BookCollection


def main():
    invalid_message = "Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author."
    collection = BookCollection()
    while True:
        command_input = input("Enter command (ADD, REMOVE, SEARCH, LIST) followed by title and author, or type 'EXIT' to stop: ")
        if command_input.upper() == "EXIT":
            break
        if command_input.upper() == "LIST":
            collection.display_books()
            continue
        try:
            action, details = command_input.split(' ', 1)
            action = action.upper()
            if action == "ADD":
                title, author = details.split(',', 1)
                collection.add_book(title.strip(), author.strip())
            elif action == "REMOVE":
                collection.remove_book(details.strip())
            elif action == "SEARCH":
                collection.search_book(details.strip())
            else:
                print(invalid_message)
        except ValueError:
            print(invalid_message)


if __name__ == "__main__":
    main()
