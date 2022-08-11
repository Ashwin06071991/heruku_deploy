import sqlite3
from restapi_sqlalch.db import db
#@classmethod to be used when returning object else not required
class ItemModel(db.Model):
    __tablename__ = 'items'
    #id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80),primary_key = True)
    price = db.Column(db.Float(precision=2))

    store_id  = db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship('storeModel')
    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls,name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items where name = ?"
        # result = cursor.execute(query,(name,))
        # row = result.fetchone()
        # print(row)
        # connection.close()
        # if row:
        #     return cls(*row)
        return cls.query.filter_by(name = name).first() #item model object

    def save_to_db(self):      #insert(self):  #
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "INSERT INTO items VALUES (?, ?)"
        # cursor.execute(query,(self.name,self.price,))
        # connection.commit()
        # connection.close()
        db.session.add(self)  # can perform both insert and update
        db.session.commit()

    def delete_from_db(self):#update(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "update items set price = ? where name = ?"
        # cursor.execute(query,(self.price,self.name))
        # connection.commit()
        # connection.close()
        # return {"message":"Item got deleted"}
        db.session.delete(self)  # can perform both insert and update
        db.session.commit()