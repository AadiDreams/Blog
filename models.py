from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db= SQLAlchemy()

class posts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    content=db.Column(db.String,nullable=False)
    author=db.Column(db.String,nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    
    def serialize(self):
        return{
            'id':self.id,
            'title':self.title,
            'content':self.content,
            'author':self.author,
            'date_post':self.date_post.strftime('%Y-%m-%d %H:%M:%S')
        }
