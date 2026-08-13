#web app for the book collection program

from flask import Flask, render_template, request, redirect, url_for, flash

from bookdetails import BookCollection

app = Flask(__name__)
app.secret_key = "book-collection-secret-key"

collection = BookCollection()


@app.route("/")
def index():
    query = request.args.get("q", "").strip()
    results = collection.search_book(query) if query else None
    return render_template(
        "index.html",
        books=collection.books,
        query=query,
        results=results,
    )


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    if not title or not author:
        flash("Please provide both a title and an author.")
    else:
        flash(collection.add_book(title, author))
    return redirect(url_for("index"))


@app.route("/remove", methods=["POST"])
def remove():
    title = request.form.get("title", "").strip()
    if not title:
        flash("Please provide a title to remove.")
    else:
        flash(collection.remove_book(title))
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
