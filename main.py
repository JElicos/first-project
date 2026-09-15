from flask import Flask, render_template
from Library import Library

app = Flask(__name__)
library = Library()


@app.route("/")
def index():
    return render_template("index.html", books=library.books)


if __name__ == "__main__":
    app.run(debug=True)