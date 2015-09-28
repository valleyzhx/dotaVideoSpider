# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import sae

class DotavideoPipeline(object):
    def __init__(self):
        self.conn=None
        dispatcher.connect(self.initialize,signals.engine_started)
        dispatcher.connect(self.finalize,signals.engine_stopped)
    def process_item(self,item,spider):
        #self.conn.execute('insert into dotaVideo values(?,?,?,?,?,?,?)',(None,item['type'],item['title'],item['contentUrl'],item['author'],item['img'],item['time']))
        return item

    def initialize(self):
        if path.exists('dotaVideo.sqlite'):
            self.conn=sqlite3.connect('dotaVideo.sqlite')
        else:
            self.conn=self.create_table('dotaVideo.sqlite')
    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None
    def create_table(self,filename):
        conn=sqlite3.connect(filename)
        conn.execute("""CREATE TABLE IF NOT EXISTS dotaVideo(id integer primary key autoincrement,type text,title text,contentUrl text,author text,img text,time text)""")
        conn.commit()
        return conn
