from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + self.title


all_posts = [
    {
        'title': 'Jenkins',
        'content': 'How to use automation with Jenkins',
        'author': 'Tom'
    },
    {
        'title': 'AWS',
        'content': 'Getting started with AWS'
    }
]


@app.route('/')
def index():
    return render_template('index.html')

# Name here and name in the arguement need to be the same
@app.route('/home/<int:id>')
def hello(id):
    # This is how you get data from the URL 
    return "Hello, " + str(id)   

@app.route('/posts', methods=['POST', 'GET'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new_post BlogPost(title = post_title, content=post_content, author='Tom')
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.all()
    return render_template('posts.html', posts=all_posts)

# Allows your request methods so you can't get the page is post is required
@app.route('/onlyget', methods=['POST', 'GET'])
def get_req():
    return 'you can only get this webpage.'

if __name__ == "__main__":
    app.run(debug=True)