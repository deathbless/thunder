# coding=gbk
__author__ = 'deathbless'

from sqlobject.sqlite import builder
# name = raw_input()
# name = "TaskDb.dat"
path="D:/Program Files (x86)/Thunder Network/Thunder9/Profiles/TaskDb.dat"
def connect(name=path):
    return builder()(name)