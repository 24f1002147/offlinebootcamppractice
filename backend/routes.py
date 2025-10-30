from flask_restful import Api, Resource
from flask import request
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
from model import db, pizza,User

api = Api()

class hello(Resource):
    def get(self):
        return {"message": "hello world"}
    
api.add_resource(hello,"/message")


#authentication endpoint 


class registeration(Resource):
    def post(self):
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data or 'password' not in data:
            return{'message':'email or name or password is required'}
        existinguser = User.query.filter_by(email = data['email']).first()
        if existinguser:
            return{'message':'user already exists'}
        newuser = User(
            name = data['name'],
            email = data['email'],
            password = data['password']
        )
        db.session.add(newuser)
        db.session.commit()

        return{'message':'user created successfully'}
    
api.add_resource(registeration,'/register')



class login(Resource):
    def post(self):
        data = request.get_json()
        if 'email' not in data or 'password' not in data or 'name' not in data:
            return{"message":"name or email or password is required"}
        user = User.query.filter_by(email = data['email'], password = data['password']).first()
        if not user:
            return{'message':'user not found'}
        token = create_access_token(identity=user.role)
        return{'message':'user logged in successfully','token':token}
    
api.add_resource(login,'/login')
#Admin endpoints

class testing(Resource):
    @jwt_required()
    def get(self,pizza_id = None):
            if pizza_id:
                Pizza = pizza.query.get(pizza_id)
                if Pizza is None:
                    return{'pizza not found'}
                return {'id':Pizza.id,'name':Pizza.name,'toppings':Pizza.toppings}
            Pizza = pizza.query.all()
            return [{'id':p.id,'name':p.name,'Toppings':p.toppings} for p in Pizza]
           
    
    
    @jwt_required()


    def post(self):
        data = request.get_json()
        if not data or 'name' not in data or not data['name']:
            return {'message':'not created'}
        

        Pizza = pizza (
            name = data['name'],
            toppings = data.get('toppings',False))
        
        db.session.add(Pizza)
        db.session.commit()



    @jwt_required()
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
    
    @jwt_required()
    def delete(self,pizza_id = None):
        
        user = User.query.filter_by(email=get_jwt_identity()).first()
        if user.role != 'Admin':
            return {'message': 'Admin privilege required!'}, 403
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




#user endpoints

