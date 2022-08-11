from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api
from flask_jwt_extended import JWTManager
from restapi_sqlalch.resources.resources import Auth,Item,ItemList
from restapi_sqlalch.resources.user import UserRegister
from  restapi_sqlalch.db import db
from restapi_sqlalch.resources.storeResource import Store,StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data1.db' #present in root folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #turns off flask sqlalchemay tracker not sqlachemy inbuilt tracker

api = Api(app)
app.config['JWT_SECRET_KEY'] = 'Ashwin'
jwt = JWTManager(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Auth,'/auth')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000,debug = True)


#https://stackoverflow.com/questions/61713217/flask-jwt-extended-bad-authorization-header



