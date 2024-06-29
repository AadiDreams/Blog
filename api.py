from flask_restful import Resource, Api
from models import db, posts
from flask import jsonify, request, make_response

class PostResource(Resource):
    def get(self, id=None):
        if id is None:
            posts = posts.query.all()
            list = []
            for post in posts:
                list.append({
                    'id':post.id,
                    'title':post.title,
                    'content':post.content,
                    'author':post.author
                })
            return list,200
        else:
            post = posts.query.get(id)
            return {'id':post.id, 'title':post.content, 'content':post.content,'author':post.author}
        
    def post(self):
        data = request.get_json()
        post = posts(title=data['title'], content=data['content'], author=data['author'])
        db.session.add(post)
        db.session.commit()
        return make_response(jsonify({'message':'Post added successfully','id':post.id}),201)
    
    def put(self,id):
        post = posts.query.get(id)
        data = request.get_json()
        post.title = data['title']
        post.content = data['content']
        post.author = data['author']
        db.session.commit()
        return jsonify({'message':'post updated successfully'})
    
    def delete(self,id):
        post=posts.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return make_response(jsonify({'message':'post deleted successfully'}),200)
    
api=Api()
api.add_resource(PostResource,'/api/posts','/api/posts/<int:id>')
