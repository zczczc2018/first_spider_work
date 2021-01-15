import pymysql
from config import MYSQL_DB, MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT


class MysqlOperator(object):
    db = None
    cursor = None

    def __init__(self):
        self.db = pymysql.connect(db=MYSQL_DB, host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT)
        self.cursor = self.db.cursor()

    def insert(self, table, data):
        """
        插入一条sql记录
        :param table: 目标表
        :param data: 插入数据，以字典形式插入
        :return: None
        """
        keys = ",".join(data.keys())
        values = ",".join(['%s'] * len(data))
        sql = f"INSERT INTO {table}({keys}) VALUES ({values})"
        try:
            # 检查当前连接是否断开，如果断开就重连
            self.db.ping(reconnect=True)
            if self.cursor.execute(sql, tuple(data.values())):
                print("Success to insert")
            self.db.commit()
        except:
            print("Failed to insert")
            self.db.rollback()
        self.db.close()

    def update(self, table, data):
        """
        数据存在就更新，数据不存在就插入
        :param table:
        :param data:
        :return:
        """
        keys = ",".join(data.keys())
        values = ",".join(['%s'] * len(data))
        sql = f"INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE "
        update = ",".join(["{key}=%s".format(key=key) for key in data])
        sql += update
        try:
            # 检查当前连接是否断开，如果断开就重连
            self.db.ping(reconnect=True)
            if self.cursor.execute(sql, tuple(data.values())*2):
                print("Success to update")
                self.db.commit()
        except Exception as e:
            print(e.args)
            print("Failed to update")
            self.db.rollback()
        self.db.close()