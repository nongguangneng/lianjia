from lianjia.items import HouseItem
import pymysql

class MyPipeline(object):
    db = pymysql.connect("localhost", "root", "123456", "test", charset="utf8")
    cursor = db.cursor()
    def process_item(self, item, spider):
        if (isinstance(item, HouseItem)):
            # print(item)
            table_name = 'home'
            col_str = ''
            row_str = ''
            for key in item.keys():
                col_str = col_str + " " + key + ","
                row_str = "{}'{}',".format(row_str, item[key])
                sql = "insert INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE ".format(table_name, col_str[1:-1],
                                                                                        row_str[:-1])
            for (key, value) in item.items():
                sql += "{} = '{}', ".format(key, value)
            sql = sql[:-2]
            try:
                print(sql)
                self.cursor.execute(sql)  # 执行SQL
                self.db.commit()  # 写入操作
                # print('insert/update succeed:%s' % item.url)
            except BaseException as e:
                self.db.rollback()
                print('db err : %s' % e)
            # finally:
            #     self.db.close()