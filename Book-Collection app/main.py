#main program
#command-line interface for the book collection: reads user commands in a loop
#and delegates the actual work to BookCollection (bookdetails.py).

from bookdetails import BookCollection


def main():
    invalid_message = "Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author."
    # one collection lives for the whole session; it resets when the program exits
    collection = BookCollection()

    # main loop: keep asking for commands until the user types EXIT
    while True:
        command_input = input("Enter command (ADD, REMOVE, SEARCH, LIST) followed by title and author, or type 'EXIT' to stop: ")

        if command_input.upper() == "EXIT":
            break

        # LIST takes no extra arguments, so it's handled before the split() below
        if command_input.upper() == "LIST":
            for line in collection.display_books():
                print(line)
            continue

        try:
            # split into the command word (ADD/REMOVE/SEARCH) and everything after it
            action, details = command_input.split(' ', 1)
            action = action.upper()

            if action == "ADD":
                # ADD expects "title, author" - split on the comma
                title, author = details.split(',', 1)
                print(collection.add_book(title.strip(), author.strip()))
            elif action == "REMOVE":
                # REMOVE just needs the title
                print(collection.remove_book(details.strip()))
            elif action == "SEARCH":
                # SEARCH can return multiple matches, so print each line
                for line in collection.search_book(details.strip()):
                    print(line)
            else:
                # command word wasn't recognized
                print(invalid_message)
        except ValueError:
            # raised if command_input or details.split() didn't produce enough parts
            # (e.g. no space after the command, or ADD without a comma)
            print(invalid_message)


if __name__ == "__main__":
    main()
