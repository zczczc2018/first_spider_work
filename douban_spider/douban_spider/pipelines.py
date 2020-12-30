# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from mysqlOperator import MysqlOperator

class DoubanSpiderPipeline:
    def process_item(self, item, spider):
        return item


class MysqlPipeline:
    mysqloperator = None

    def open_spider(self, spider):
        self.mysqloperator = MysqlOperator()

    def process_item(self, item, spider):
        data = dict(item)
        self.mysqloperator.update("movies", data)


