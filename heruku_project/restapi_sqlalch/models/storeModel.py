import sqlite3
from restapi_sqlalch.db import db
#@classmethod to be used when returning object else not required
class storeModel(db.Model):
    __tablename__ = 'stores'
    #store_id = db.Column(db.Integer,primary_key = True)
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel',lazy='dynamic') #when lazy is dynamic self.item is no longer a list but a query builder

    def __init__(self,name):
        self.name = name
        #self.items = items

    def json(self):
        print([item.json() for item in self.items.all()])
        return {'name': self.name, 'price': [item.json() for item in self.items.all()]}

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