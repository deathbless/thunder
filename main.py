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
tasks = []  # �Ѿ����ٵ����񣬿������ظ������list��¼��
allTasks = []  # �ܹ���������ʾ������
flyNum = 0

#TODO ������֧��,һ���������������TaskId
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
                         % (tableName, taskId, AccTaskId, LocalSub))  # ��ȡ�������������ֵ

    # data��ȡ������һ�����ϣ���Ȼ�����������ֻ��һ������where������֤��
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
    # ����Ƿ�ɹ��ı�

    data = conn.queryAll("SELECT UserData FROM %s WHERE LocalTaskId=%s AND AccelerateTaskId=%s AND LocalSubFileIndex=%s"\
                         % (tableName, taskId, AccTaskId, LocalSub))  # ��ȡ�������������ֵ
    UserData = data[0][0]
    string = str(UserData).decode("utf-8")
    string = eval(string)
    if "Result" in string.keys():
        if string['Result'] == 0 and taskId not in tasks:
            flyNum += 1
            data = conn.queryAll("SELECT Name FROM TaskBase WHERE TaskId=%s" % taskId)
            print "�Ѿ�������%s����" % str(data[0][0]).decode("utf-8")
            tasks.append(taskId)


def find():
    # �����ú�����������
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
    print "�������ڶ�ȡ���ݿ�..."
    getTask()
    print "ִ����ϣ������ܹ���%s��������������,�¼�����%s������" % (num, flyNum)