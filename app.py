from flask import Flask,render_template,request,redirect,url_for
from models import db, posts
from api import api

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blogDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

#Initialize the app with the db instance
db.init_app(app)
api.init_app(app)

# @app.route('/api')
# def api():
#     return

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/read')
def read():
    all_post = posts.query.all()
    return render_template('read.html', posts=all_post)

@app.route('/post')
def add():
    return render_template('add_post.html')

@app.route('/post/add', methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        post = posts(title=title, content=content, author=author)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('read.html')

@app.route('/post/edit/<int:id>',methods=['GET','POST']) 
def edit_post(id) :
    post=posts.query.get(id)
    if request.method == 'POST':
         post.title= request.form['title']
         post.author=request.form['author']
         post.content=request.form['content']
         db.session.commit()
         return redirect(url_for('post_details',id=post.id))
    return render_template('edit_post.html',post=post)

@app.route('/post/<int:id>')
def post_details(id):
    post = posts.query.get(id)
    return render_template('post_details.html', post=post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/delete/<int:id>',methods=['GET','POST'])
def delete_post(id):
    post=posts.query.get(id)
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('delete_post.html',post=post)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)

# @app.route('/')
# def base():
#     return render_template('base.html')
