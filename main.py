# coding=gbk
__author__ = 'deathbless'

import os
import sqlobject
from sqlobject.sqlbuilder import *
from connection import conn

class data(sqlobject.SQLObject):
    _connection = conn

num = 0
flyNum = 0

#TODO 多任务支持,一个任务可能有两个TaskId
def getTask():
    tables = conn.listTables()
    for table in tables:
        if "superspeed" in table or "offline" in table:
            read = conn.queryAll("SELECT LocalTaskId FROM %s" % table)
            print read
            read = conn.queryAll("SELECT UserData FROM %s" % table)
            for one in read:
                print str(one[0])
            exit(0)

def find():
    global num
    tables = conn.listTables()
    for table in tables:
        if "superspeed" in table or "offline" in table:
            print table
            read = conn.queryAll("SELECT UserData FROM %s" % table)
            string = str(read[0][0]).decode("utf-8")
            print string
            string = str(read[1][0]).decode("utf-8")
            print string
            string = eval(string)
            string['Message'] = "fuck u thunder"
            string['Result'] = 0
            update = Update(table, values={"UserData":str(string).replace("'", '"').encode("utf-8")})
            query = conn.sqlrepr(update)
            # conn.query(query)
            read = conn.queryAll("SELECT UserData FROM %s" % table)
            string = str(read[0][0]).decode("utf-8")
            string = eval(string)
            if string.get('Result',-1) == 0:
                num += 1

if __name__ == '__main__':
    getTask()