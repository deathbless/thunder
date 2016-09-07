# coding=gbk
__author__ = 'deathbless'

import os
import sqlobject
from sqlobject.sqlbuilder import *
from connection import conn

class data(sqlobject.SQLObject):
    _connection = conn


def find():
    tables = conn.listTables()
    for table in tables:
        if "superspeed" in table or "offline" in table:
            print table
            read = conn.queryAll("SELECT UserData FROM %s" % table)
            string = str(read[0][0]).decode("utf-8")
            string = eval(string)
            string['Message'] = "fuck u thunder"
            string['Result'] = 0
            update = Update(table, values={"UserData":str(string).replace("'", '"').encode("utf-8")})
            query = conn.sqlrepr(update)
            conn.query(query)

if __name__ == '__main__':
    find()