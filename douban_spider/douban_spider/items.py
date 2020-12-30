# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 片名
    movie_name = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 编剧
    scriptwriter = scrapy.Field()
    # 演员，存储为字符串，每个演员用/分割
    actors = scrapy.Field()
    # 星级
    rating = scrapy.Field()
    # 类型
    movie_type = scrapy.Field()
    # 制片国家/地区
    movie_country = scrapy.Field()
    # 语言
    language = scrapy.Field()
    # 上映日期
    play_date = scrapy.Field()
    # 片长
    movie_length = scrapy.Field()
    # 又名
    other_name = scrapy.Field()
