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

def db_match_user(token):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    matcher = NodeMatcher(GRAPH)
    user = User()
    user.token = token
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
    user = make_user(data)
    print(str(user))
    GRAPH.push(user)
    GRAPH.pull(user)
    return str(user.token)
