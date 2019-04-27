from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom
from py2neo import Graph

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

# Have to repeat the models in order to build relationships,
# because services cannot share them
class User(GraphObject):
    __primarykey__ = "email"
    name = Property()
    email = Property()
    password = Property()
    token = Property()
    SUBMITS = RelatedTo("Report")

class Entity(GraphObject):
    __primarykey__ = "eId"
    Name = Property()
    eId = Property()
    Email = Property()
    Address = Property()
    Tags = Property()

def make_report(data):
    report = Report()
    if 'rId' in data.keys(): report.rId = data['rId']
    if 'title' in data.keys(): report.title = data['title']
    if 'description' in data.keys(): report.description = data['description']
    if 'location' in data.keys(): report.location = data['location']
    if 'date' in data.keys(): report.date = data['date']
    if 'imagePath' in data.keys(): report.imagePath = data['imagePath']
    if 'status' in data.keys(): report.status = data['status']
    if 'tags' in data.keys(): report.tags = data['tags']
    return report

def clear_report(rep):
    return dict((name, getattr(rep, name))
                for name in dir(rep)
                if not callable(getattr(rep, name)) and not name.startswith('__') and not name.startswith('_') and not str(getattr(rep, name)).startswith("<py2neo.ogm"))
