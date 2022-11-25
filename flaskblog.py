"""
flask web app
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Nikita',
        'title': 'Blog post 1',
        'content': 'Content of the first blog post',
        'date_posted': 'November 24, 2022'
    },
    {
        'author': 'Nikita',
        'title': 'Blog post 2',
        'content': 'Content of the second blog post',
        'date_posted': 'November 25, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)