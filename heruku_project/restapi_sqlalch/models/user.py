import sqlite3
from restapi_sqlalch.db import db
class User(db.Model):
    __tablename__ =  'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80))
    _pass = db.Column(db.String(80))

    def __init__(self, _id, user, _pass):
        self.id = _id
        self.username = user
        self._pass = _pass


    @classmethod
    def find_by_username(cls,username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "select * from users where username=?"
        # result = cursor.execute(query,(username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user
        return cls.query.filter_by(username=username).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls,_id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "select * from users where id=?"
        # result = cursor.execute(query,(_id,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user
        return cls.query.filter_by(id=_id).first()