# coding=gbk
__author__ = 'deathbless'

from sqlobject.sqlite import builder
# name = raw_input()
# name = "TaskDb.dat"
# name="D:/Program Files (x86)/Thunder Network/Thunder9/Profiles/TaskDb.dat"
def connect(name="TaskDb.dat"):
    return builder()(name)