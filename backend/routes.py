from flask_restful import Api, Resource
from flask import request

from model import db, pizza

api = Api()

class hello(Resource):
    def get(self):
        return {"message": "hello world"}
    
api.add_resource(hello,"/message")


class testing(Resource):
    def get(self):
        return {'message': 'pizza found'}
    

    def post(self):
        data = request.get_json()
        if not data or 'name' not in data or not data['name']:
            return {'message':'not created'}
        
        Pizza = pizza (
            name = data['name'],
            toppings = data.get('toppings',False))
        
        db.session.add(Pizza)
        db.session.commit()



    
    def put(self):
        return {'message': 'pizza updated'}
    
    def delete(self):
        return {'message':'pizza deleted'}
    
api.add_resource(testing, '/test')

