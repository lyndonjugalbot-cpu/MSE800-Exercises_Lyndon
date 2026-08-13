#web app for the book collection program

#import necessary modules
#Flask: creates the web app and handles routing
#render_template: fills in the HTML template with data
#request: reads incoming form fields and URL query params
#redirect/url_for: sends the browser to another route after an action
#flash: stores a one-time message to show the user on the next page load
from flask import Flask, render_template, request, redirect, url_for, flash

from bookdetails import BookCollection

# create the Flask application instance
app = Flask(__name__)
# secret_key is required by Flask to sign session cookies used for flash messages
app.secret_key = "book-collection-secret-key"

# single shared collection used by every visitor/request (in-memory, resets on restart)
collection = BookCollection()


# home page: shows the add/remove/search forms and the full book list
@app.route("/")
def index():
    # read the "q" query param from the URL, e.g. /?q=dune
    query = request.args.get("q", "").strip()
    # only run a search if the user actually typed something
    results = collection.search_book(query) if query else None
    # render index.html, passing in the data it needs to display
    return render_template(
        "index.html",
        books=collection.books,
        query=query,
        results=results,
    )


# handles the "Add a book" form submission
@app.route("/add", methods=["POST"])
def add():
    # pull title/author out of the submitted form data
    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    if not title or not author:
        # missing input: show a validation message
        flash("Please provide both a title and an author.")
    else:
        # valid input: add the book and show the result message it returns
        flash(collection.add_book(title, author))
    # redirect back to "/" so refreshing the page doesn't resubmit the form
    return redirect(url_for("index"))


# handles the "Remove a book" form submission
@app.route("/remove", methods=["POST"])
def remove():
    title = request.form.get("title", "").strip()
    if not title:
        flash("Please provide a title to remove.")
    else:
        flash(collection.remove_book(title))
    return redirect(url_for("index"))


# only start the dev server when this file is run directly (not on import)
if __name__ == "__main__":
    app.run(debug=True)
