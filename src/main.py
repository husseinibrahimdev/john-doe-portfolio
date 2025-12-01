from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    
    return render_template("about.html")

@app.route('/projects')
def projects():
    posts = [
    {
        'author': "Hussein Ibrahim",
        'date_published': '01/01/2024',
        'content': 'This is a test post content.',
        'title': "Title 1"
    },
    {
        'author': "Sarah Ahmed",
        'date_published': '02/01/2024',
        'content': 'Today I learned how to use Python dictionaries effectively.',
        'title': "Learning Python"
    },
    {
        'author': "Omar Khaled",
        'date_published': '05/01/2024',
        'content': 'Exploring web development with Django has been fun!',
        'title': "Django Journey"
    },
    {
        'author': "Lina Hassan",
        'date_published': '10/01/2024',
        'content': 'Working on a new UI design prototype this week.',
        'title': "Design Update"
    },
    {
        'author': "Ali Mohammed",
        'date_published': '15/01/2024',
        'content': 'Just finished reading a great book on clean code principles.',
        'title': "Clean Code Thoughts"
    }
]
    
    return render_template('projects.html',posts=posts)



if __name__ == "__main__":
    app.run(debug=True)
