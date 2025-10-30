from flask_restful import Api, Resource
from flask import request

from model import db, pizza

api = Api()

class hello(Resource):
    def get(self):
        return {"message": "hello world"}
    
api.add_resource(hello,"/message")


class testing(Resource):
    def get(self,pizza_id = None):
            if pizza_id:
                Pizza = pizza.query.get(pizza_id)
                if Pizza is None:
                    return{'pizza not found'}
                return {'id':Pizza.id,'name':Pizza.name,'toppings':Pizza.toppings}
            Pizza = pizza.query.all()
            return [{'id':p.id,'name':p.name,'Toppings':p.toppings} for p in Pizza]
           
    
    

    def post(self):
        data = request.get_json()
        if not data or 'name' not in data or not data['name']:
            return {'message':'not created'}
        
        Pizza = pizza (
            name = data['name'],
            toppings = data.get('toppings',False))
        
        db.session.add(Pizza)
        db.session.commit()



    
    def put(self,pizza_id = None):
        data = request.get_json()
        if data is None:
            return{'message':'Pizza id is required'}
        Pizza = pizza.query.get(pizza_id)
        if not Pizza:
            return{'message':'pizza not found'}
        
        Pizza.name = data.get('name',Pizza.name)
        Pizza.toppings = data.get('toppings',Pizza.toppings)
        db.session.commit()
        
        return {'message': 'pizza updated'}
    

    def delete(self,pizza_id = None):
        data = request.get_json()
        if data is None:
            return {'message': 'pizza id is required'}
        Pizza = pizza.query.get(pizza_id)
        if Pizza is None:
            return{'message':'pizza not found'}
        db.session.delete(Pizza)
        db.session.commit()
        return{'message':'pizza deleted successfully'}
    


    
    
api.add_resource(testing, '/test', '/test/<pizza_id>')

