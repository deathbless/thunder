# coding=gbk
__author__ = 'deathbless'

from sqlobject.sqlite import builder
# name = raw_input()
name = "D:/Program Files (x86)/Thunder Network/Thunder9/Profiles/TaskDb.dat"
# name = "TaskDb.dat"
conn = builder()(name)
