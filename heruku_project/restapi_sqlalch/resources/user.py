import sqlite3
from flask_restful import Resource, reqparse
from restapi_sqlalch.models.user import User

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required = True)
    parser.add_argument('password',
                        type = str,
                        required = True)
    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {"Message":"User already exist"},400

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "INSERT INTO users VALUES(NULL, ?, ?)"
        # cursor.execute(query,(data['username'],data['password'],))
        # connection.commit()
        # connection.close()
        #user = User(**data) #User(data['username'],data['password'])
        print(data)
        user = User(_id=None,user=data['username'],_pass=data['password'])
        user.save_to_db()
        return {"message":"User is created"},201


