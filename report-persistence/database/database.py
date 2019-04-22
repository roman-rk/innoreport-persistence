from py2neo import Graph, NodeMatcher
from database.report import *
import configparser

GRAPH = None

def __init__():
    pass

def connect_to_db():
    global GRAPH
    dburl = r"http://10.90.138.222:7474"
    GRAPH = Graph(dburl)

def db_get_report_info(id):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    matcher = NodeMatcher(GRAPH)
    return list(matcher.match("Report").where("_.id =~ " + str(id)))

def db_get_all_reports(id, user_email):
    if GRAPH == None:
        raise Exception("Not connected to the database")
    matcher = NodeMatcher(GRAPH)
    return matcher.match("Report")

def db_post_user(data):
    report = make_report(data)
    return GRAPH.create(user)

def db_update_report(data):
    if data["id"] == None:
        raise Exception("Cannot find report without id")
    report = make_report(data)
    return GRAPH.push(user)
