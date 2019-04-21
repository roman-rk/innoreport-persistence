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

def match_user(email):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    matcher = NodeMatcher(GRAPH)
    return matcher.match("User").where("_.email =~ " + str(email))

def db_post_user(data):
    user = make_user(data)
    return GRAPH.create(user)

def db_put_token(data):
    user = make_user(data)
    return GRAPH.push(user)
