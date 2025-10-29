from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
from model import db
db.init_app(app)





class hello(Resource):
    def get(self):
        return {'message' : 'hello world'}
    
api.add_resource(hello, '/message')




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
