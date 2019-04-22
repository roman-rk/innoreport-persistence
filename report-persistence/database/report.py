from py2neo.ogm import GraphObject, Property, RelatedTo

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

    submits = RelatedTo("Entity")

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
