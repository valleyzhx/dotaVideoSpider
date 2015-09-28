# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from os import path
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import sqlite3

class DotavideoPipeline(object):

    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)

    def process_item(self,item,spider):
        self.conn.execute('insert into dotaVideo values(?,?,?,?,?,?,?)',(None,item['itemType'],item['title'],item['contentUrl'],item['author'],None,item['time']))
        return item

    def initialize(self):
        if path.exists('/Users/xiang/dotaVideoSpider/dotaVideo/dotaVideo.sqlite'):
            self.conn=sqlite3.connect('/Users/xiang/dotaVideoSpider/dotaVideo/dotaVideo.sqlite')
        else:
            self.conn=self.create_table('/Users/xiang/dotaVideoSpider/dotaVideo/dotaVideo.sqlite')

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None

    def create_table(self,filename):
        conn=sqlite3.connect(filename)
        conn.execute("""create table dotaVideo(id integer primary key autoincrement, type text, title text, contentUrl text, author text, img text, time text)""")
        conn.commit()
        return conn
