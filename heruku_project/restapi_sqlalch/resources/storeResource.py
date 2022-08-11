from flask_restful import Resource
from restapi_sqlalch.models import storeModel
from flask import request
from restapi_sqlalch.models.user import User
from hmac import compare_digest
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
import sqlite3
from restapi_sqlalch.models.resources import ItemModel

class Store(Resource):
    def get(self,name):
        store = storeModel.storeModel.find_by_name(name)
        if store:
            return store.json(),200
        return {'message': 'Store not found'},404

    def post(self,name):
        print('******************************')
        if storeModel.storeModel.find_by_name(name):
            return {'message':'Already present'}
        store = storeModel.storeModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'Exception'},500
        return store.json,201

    def delete(self,name):
        if storeModel.storeModel.find_by_name(name):
            storeModel.storeModel.delete_from_db()
            return {'message':'Store deleted'}
        return {'message':'Store not present'}

class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in storeModel.storeModel.query.all()]}

