from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom
import ast

class User(GraphObject):
    __primarykey__ = "email"
    name = Property()
    email = Property()
    password = Property()
    token = Property()
    SUBMITS = RelatedTo("Report")

def make_user(data):
    user = User()
    if type(data) is str:
        print("check")
        data = ast.literal_eval(data)
    print(type(data))
    if 'name' in data.keys(): user.name = data['name']
    if 'email' in data.keys(): user.email = data['email']
    if 'password' in data.keys(): user.password = data['password']
    if 'token' in data.keys(): user.token = data['token']
    return user

def clear_user(user):
    return dict((name, getattr(user, name))
    for name in dir(user) if not callable(getattr(user, name)) and not name.startswith('__') and not name.startswith('_') and not str(getattr(user, name)).startswith("<py2neo.ogm"))


class Report(GraphObject):
    __primarykey__ = "rId"
    rId = Property()
    title = Property()
    description = Property()
    location = Property()
    date = Property()
    imagePath = Property()
    status = Property()
    tags = Property()
    SUBMITS = RelatedFrom("User")
    BELONGS = RelatedTo("Entity")

class Entity(GraphObject):
    __primarykey__ = "eId"
    Name = Property()
    eId = Property()
    Email = Property()
    Address = Property()
    Tags = Property()
