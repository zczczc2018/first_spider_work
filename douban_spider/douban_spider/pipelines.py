# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from .model.mysqlOperator import MysqlOperator
from .model.doubanSpiderModel import DoubanMovie

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


class SqlAlchemyPipeline:
    def process_item(self, item, spider):
        data = dict(item)
        DoubanMovie().add_movie_info(**data)


