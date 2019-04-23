from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

class Report(GraphObject):
    __primarykey__ = "id"
    id = Property()
    title = Property()
    description = Property()
    location = Property()
    date = Property()
    imagePath = Property()
    status = Property()
    tags = Property()
    SUBMITS = RelatedFrom("User")
    BELONGS = RelatedTo("Entity")

class User(GraphObject):
    __primarykey__ = "token"
    name = Property()
    email = Property()
    password = Property()
    token = Property()
    SUBMITS = RelatedTo("Report")

def make_report(data):
    report = Report()
    if 'id' in data.keys: user.id = data['id']
    if 'title' in data.keys: user.title = data['title']
    if 'description' in data.keys: user.description = data['password']
    if 'location' in data.keys: user.location = data['location']
    if 'date' in data.keys: user.date = data['date']
    if 'imagePath' in data.keys: user.imagePath = data['imagePath']
    if 'status' in data.keys: user.status = data['status']
    if 'tags' in data.keys: user.tags = data['tags']
    return report

def clear_report(rep):
    return dict((name, getattr(rep, name)) for name in dir(rep) if not callable(getattr(rep, name)) and not name.startswith('__') and not name.startswith('_') and not str(getattr(rep, name)).startswith("<py2neo.ogm"))
