from flask_restful import Resource
from flask import request
from restapi_sqlalch.models.user import User
from hmac import compare_digest
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import sqlite3
from restapi_sqlalch.models.resources import ItemModel
# between function 1 line gap and between class two ines gap
# set environment variable in postman with test cases

class Auth(Resource):
    def post(self):
        request_data = request.get_json()
        username = request_data['username']
        password = request_data['password']
        print(username)
        user = User.find_by_username(username)   #username_mapping.get(username,None)
        print(user)
        _pass = user._pass
        if user and compare_digest(_pass, password):
            token = create_access_token(username)
            return {'access_token':token}
        return {'message':'Bad user'}

    def get(self):
        current_user = get_jwt_identity()
        return current_user

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'Item not found'},404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name {} already present'.format(name)}
        request_data = request.get_json()
        item = ItemModel(name,request_data['price'],request_data['store_id'])#{'name': name, 'price': request_data['price']}
        try:
            #ItemModel.insert(item)
            #item.insert()
            item.save_to_db()
        except:
            return {'message':'Error has occured'}, 500  #internal server error
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "delete from items where name = ?"
        # cursor.execute(query,(name,))
        # connection.commit()
        # connection.close()
        # return {"message":"Item got deleted"}
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

    @jwt_required()
    def put(self, name):
        request_data = request.get_json()
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name,request_data['price'])#{'name': name, 'price': request_data['price']}
        if item is None:
            item = ItemModel(name,request_data['price'],request_data['store_id'])
            # try:
            #     #ItemModel.insert(updated_item)
            #     updated_item.insert()
            # except:
            #     return {'message':'Error has occured'}, 500
        else:
            # try:
            #     #ItemModel.update(updated_item)
            #     updated_item.update()
            # except:
            #     return {'message':'Error has occured'}, 500
            item.price = request_data['price']
        item.save_to_db()
        return item.json() #updated_item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "select * from items"
        # result = cursor.execute(query)
        # item = []
        # for row in result:
        #     item.append({'item':row[0],'price': row[1]})
        # connection.commit()
        # connection.close()
        # return {'items':item}
        return {'items': [item.json() for item in ItemModel.query.all()]}
        #return {'items': list(map(lambda x: x.json,ItemModel.query.all()))}