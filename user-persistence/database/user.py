from py2neo.ogm import GraphObject, Property, RelatedTo

class User(GraphObject):
    __primarykey__ = "email"

    name = Property()
    email = Property()
    password = Property()
    token = Property()

    submits = RelatedTo("Report")

def make_user(data):
    user = User()
    if 'name' in data.keys: user.name = data['name']
    if 'email' in data.keys: user.email = data['email']
    if 'password' in data.keys: user.password = data['password']
    if 'token' in data.keys: user.token = data['token']
    return user