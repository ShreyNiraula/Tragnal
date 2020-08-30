from tragnal2 import db, login_manager
from flask_login import UserMixin

# this funciton is IMPORTANT
# this is for reloading the user from user id stored in session
# see doc for more
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(70), unique=False, nullable=False)
    password = db.Column(db.String(25), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable = False)

    # relation with Hobby class
    #hobbies = db.relationship('Hobby', backref='person', lazy=True)

    # this represents how model will be represented
    def __repr__(self):
        return f"User('{self.username}, {self.age}')"

class Junction(db.Model, UserMixin):
    current_phase = db.Column(db.Integer, primary_key=True)
    density = db.Column(db.Integer)

    def __repr__(self):
        return f"Junction('{self.current_phase}, {self.red},  {self.yellow},  {self.green}')"
# class Junction(db.Model, UserMixin):
#     current_phase = db.Column(db.Integer, primart_key=True)
#     red = db.Column(db.Boolean, nullable =False)
#     yellow = db.Column(db.Boolean, nullable =False)
#     green = db.Column(db.Boolean, nullable =False)
#
#     def __repr__(self):
#         return f"Junction('{self.current_phase}, {self.red},  {self.yellow},  {self.green}')"

#
# class Vehicles(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     type = db.Column(db.String(1), nullable=False)