from flask import Flask
from flask_cors import CORS
from model import User
from flask_jwt_extended import JWTManager


app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'My-Secret-Key'
jwt = JWTManager(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
from model import db
db.init_app(app)



from routes import api

api.init_app(app)





if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(email = "admin@gmail.com").first()
        if not admin:
            Admin = User(
                email = 'admin@gmail.com',
                password = 'AdminPassword',
                name = "Admin",
                role = "Admin"
                
            )
            db.session.add(Admin)
            db.session.commit()
            print("admin created")
        else:
            print("admin already exists")
    app.run(debug=False)
