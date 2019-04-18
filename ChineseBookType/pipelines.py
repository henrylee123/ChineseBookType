# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  cx_Oracle
from cx_Oracle import IntegrityError

class ChinesebooktypePipeline(object):
    conn_dct = {
        "dsn": "200.100.100.69/dgr",
        "user": "hiibase",
        "password": "hiibase"
        }
    conn = cx_Oracle.connect(**conn_dct)
    cur = conn.cursor()
    sql = "insert into chinesebooktype_new (fcode, ftitle, flevel, flastcode, flasttitle, furl, fisuse) values (:1, :2, :3, :4, :5, :6, '1')"

    def process_item(self, item, spider):

        l  = [item["fcode"], item["ftitle"], item["flevel"], item["flastcode"], item["flasttitle"], item["furl"]]

        try:
            self.cur.execute(self.sql, l)
        except IntegrityError:
            print("重复: " + str(l))
        else:
            self.conn.commit()
        return item