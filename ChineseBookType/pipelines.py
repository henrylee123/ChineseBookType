# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  cx_Oracle

class ChinesebooktypePipeline(object):
    conn_dct = {
        "dsn": "200.100.100.69/dgr",
        "user": "hiibase",
        "password": "hiibase"
        }
    conn = cx_Oracle.connect(**conn_dct)
    cur = conn.cursor()
    sql = "insert into chinesebooktype (code, title) values (:1, :2)"

    def process_item(self, item, spider):

        l  = [item["code"], item["title"]]
        
        self.cur.execute(self.sql, l)
        self.conn.commit()

        return item