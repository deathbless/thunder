# coding=gbk
__author__ = 'deathbless'

import os
import sqlobject
from sqlobject.sqlbuilder import *
from connection import conn
import array


class data(sqlobject.SQLObject):
    _connection = conn

num = 0
tasks = []  # 已经加速的任务，可能有重复因此用list记录下
allTasks = []  # 总共的任务，显示数量用
flyNum = 0

#TODO 多任务支持,一个任务可能有两个TaskId
def getTask():
    global num, allTasks
    tables = conn.listTables()
    for table in tables:
        if "superspeed" in table or "offline" in table:
            read = conn.queryAll("SELECT LocalTaskId,AccelerateTaskId,LocalSubFileIndex FROM %s" % table)
            for task in read:
                crack(task[0], table, task[1], task[2])
                if task[0] not in allTasks:
                    num += 1
                    allTasks.append(task[0])

def crack(taskId, tableName, AccTaskId, LocalSub):
    global flyNum, tasks
    data = conn.queryAll("SELECT UserData FROM %s WHERE LocalTaskId=%s AND AccelerateTaskId=%s AND LocalSubFileIndex=%s"\
                         % (tableName, taskId, AccTaskId, LocalSub))  # 获取到单个任务的数值

    # data获取到的是一个集合，虽然这个集合里面只有一个任务（where条件保证）
    UserData = data[0][0]
    string = str(UserData).decode("utf-8")
    string = eval(string)
    if "Message" in string.keys():
        string['Message'] = "fuck u thunder"
    if "Result" in string.keys():
        if string['Result'] == 0:
            return
        string['Result'] = 0
    update = Update(tableName, values={"UserData": buffer(array.array('c',str(string).replace("'", '"').encode("utf-8")))},\
                    where="LocalTaskId=%s AND AccelerateTaskId=%s AND LocalSubFileIndex=%s"\
                          % (taskId, AccTaskId, LocalSub))
    query = conn.sqlrepr(update)
    # print query
    conn.query(query)
    # 检测是否成功改变

    data = conn.queryAll("SELECT UserData FROM %s WHERE LocalTaskId=%s AND AccelerateTaskId=%s AND LocalSubFileIndex=%s"\
                         % (tableName, taskId, AccTaskId, LocalSub))  # 获取到单个任务的数值
    UserData = data[0][0]
    string = str(UserData).decode("utf-8")
    string = eval(string)
    if "Result" in string.keys():
        if string['Result'] == 0 and taskId not in tasks:
            flyNum += 1
            data = conn.queryAll("SELECT Name FROM TaskBase WHERE TaskId=%s" % taskId)
            print "已经加速了%s任务" % str(data[0][0]).decode("utf-8")
            tasks.append(taskId)


def find():
    # 测试用函数，已舍弃
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
            if string.get('Result', -1) == 0:
                num += 1

if __name__ == '__main__':
    print "现在正在读取数据库..."
    getTask()
    print "执行完毕，现在总共有%s个任务在下载中,新加速了%s个任务" % (num, flyNum)