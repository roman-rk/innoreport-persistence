from py2neo import Graph, NodeMatcher
from database.user import *
import configparser

GRAPH = None

def __init__():
    pass

def connect_to_db():
    global GRAPH
    dburl = r"http://10.90.138.222:7474"
    GRAPH = Graph(dburl)

def db_match_user(email):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    user = User()
    user.email = email
    print(user)
    GRAPH.pull(user)
    return str(clear_user(user))

def db_post_user(data):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    user = make_user(data)
    print(user)
    GRAPH.create(user)
    GRAPH.pull(user)
    return str(user.token)

def db_put_token(data):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    user = User()
    user.email = data['email']
    print(str(user))
    GRAPH.pull(user)
    user.token = data['token']
    GRAPH.push(user)
    GRAPH.pull(user)
    return str(user.token)
