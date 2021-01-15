import scrapy
import requests
from ..items import DoubanSpiderItem
from config import PROXY_TOOL_PORT
import json
import re
import random


class SingleProcessSpider(scrapy.Spider):
    def __init__(self, start):
        self.start = start

    name = "single_process_spider"
    allowed_domains = ['movie.douban.com']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'bid=hAoi6-l8I04; douban-fav-remind=1; __utmc=30149280; ll="108288"; __utmc=223695111; __yadk_uid=WHFuqvWTypIoDz9ZmDxvQZcWj8cLp8lO; _vwo_uuid_v2=D947B61D50629F4B949612CE00329AA6C|95f95961588fbff8d028f9385513d4c2; __gads=ID=c971254ae558e718-224c37b6eec400f3:T=1606491258:RT=1606491258:S=ALNI_Maqok3B-GjobYciHC_ijkkoexycgA; ct=y; viewed="34938311"; gr_user_id=057adc8d-7202-4639-a393-db41087a6d94; push_noty_num=0; push_doumail_num=0; dbcl2="203345136:KzjNWNj7ZYo"; ck=vwHi; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1610450328%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.565803361.1605104867.1610380699.1610450328.43; __utmb=30149280.0.10.1610450328; __utmz=30149280.1610450328.43.12.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1117890868.1606491204.1610380699.1610450328.42; __utmb=223695111.0.10.1610450328; __utmz=223695111.1610450328.42.11.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=74817fb476940c64.1606491204.42.1610450787.1610380844.',            'Host': 'movie.douban.com',
            'Pragma': 'no-cache',
            'Referer': 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
                   }
               }

    def start_requests(self):
        movie_list_page_url = f'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start={self.start}&limit=20'
        headers = {
            'Accept': '*/*',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Pragma': 'no-cache',
            'Cookie': 'bid=hAoi6-l8I04; douban-fav-remind=1; __utmc=30149280; ll="108288"; __utmc=223695111; __yadk_uid=WHFuqvWTypIoDz9ZmDxvQZcWj8cLp8lO; _vwo_uuid_v2=D947B61D50629F4B949612CE00329AA6C|95f95961588fbff8d028f9385513d4c2; __gads=ID=c971254ae558e718-224c37b6eec400f3:T=1606491258:RT=1606491258:S=ALNI_Maqok3B-GjobYciHC_ijkkoexycgA; ct=y; viewed="34938311"; gr_user_id=057adc8d-7202-4639-a393-db41087a6d94; push_noty_num=0; push_doumail_num=0; dbcl2="203345136:KzjNWNj7ZYo"; ck=vwHi; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1610450328%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.565803361.1605104867.1610380699.1610450328.43; __utmb=30149280.0.10.1610450328; __utmz=30149280.1610450328.43.12.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1117890868.1606491204.1610380699.1610450328.42; __utmb=223695111.0.10.1610450328; __utmz=223695111.1610450328.42.11.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=74817fb476940c64.1606491204.42.1610450332.1610380844.', 'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=',
            'X-Requested-With': 'XMLHttpRequest',
        }
        '''proxy = PROXY_TOOL_PORT
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy,
        }'''
        result = requests.get(movie_list_page_url, headers=headers)
        if result.status_code == 200:
            try:
                result_json = result.json()
            except:
                print("json文件请求失败")
                return
        else:
            return
        if result_json == []:
            return
        for movie_info in result_json:
            movie_info_dict = {}
            # 部分字段在列表页的json文件中可以找到
            if 'actors' in movie_info.keys():
                movie_info_dict['actors'] = "/".join(movie_info['actors'])
            if 'score' in movie_info.keys():
                movie_info_dict['rating'] = movie_info['score']
            if 'regions' in movie_info.keys():
                movie_info_dict['movie_country'] = "/".join(movie_info['regions'])
            if 'title' in movie_info.keys():
                movie_info_dict['movie_name'] = movie_info['title']
            if 'types' in movie_info.keys():
                movie_info_dict['movie_type'] = "/".join(movie_info['types'])
            if 'release_date' in movie_info.keys():
                movie_info_dict['play_time'] = movie_info['release_date']
            if 'url' in movie_info.keys():
                yield scrapy.Request(url=movie_info['url'], meta={'movie_info_dict': movie_info_dict})

    def parse(self, response, **kwargs):
        item = DoubanSpiderItem()
        # 获取数据json
        info_dict = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first(""), strict=False)
        # 片名字段解析
        if "name" in info_dict.keys():
            item['movie_name'] = info_dict['name']
        else:
            item['movie_name'] = response.meta['movie_info_dict']['movie_name']
        # 导演字段解析
        if "director" in info_dict.keys() and info_dict['director']:
            director_list = []
            for director in info_dict['director']:
                director_list.append(director['name'])
            item['director'] = "/".join(director_list)
        else:
            item['director'] = response.xpath('//*[@id="info"]/span[1]/span[2]/a//text()').get("")
        # 编剧字段解析
        if "author" in info_dict.keys() and info_dict['author']:
            scrpitwriter_list = []
            for scriptwriter in info_dict['author']:
                scrpitwriter_list.append(scriptwriter['name'])
            item['scriptwriter'] = "/".join(scrpitwriter_list)
        else:
            item['scriptwriter'] = response.xpath('//*[@id="info"]/span[2]/span[2]/a//text()').get("")
        # 演员字段解析
        if "actor" in info_dict.keys():
            actor_list = []
            for actor in info_dict['actor']:
                actor_list.append(actor['name'])
            item['actors'] = "/".join(actor_list)
        else:
            item['actors'] = response.meta['movie_info_dict']['actors']
        # 评分字段解析
        if "aggregateRating" in info_dict.keys() and "ratingValue" in info_dict['aggregateRating'].keys():
            item['rating'] = info_dict['aggregateRating']['ratingValue']
        else:
            item['rating'] = response.meta['movie_info_dict']['rating']
        item['movie_type'] = response.meta["movie_info_dict"]['movie_type']
        item['movie_country'] = response.meta["movie_info_dict"]['movie_country']
        play_dates = response.xpath('//div[@id="info"]//span[@property="v:initialReleaseDate"]')
        play_date_list = []
        for play_date in play_dates:
            play_date_list.append("".join(play_date.xpath('text()').getall()).replace('\n', ''))
        item['play_date'] = "/".join(play_date_list)
        item['movie_length'] = response.xpath('//*[@id="info"]/span[@property="v:runtime"]//text()').extract_first("")
        info_text = "".join(response.xpath('//div[@id="info"]//text()').extract())
        if re.search("语言: .*\n", info_text):
            item['language'] = re.search("语言: (.*)\n", info_text).group(1)
        else:
            item['language'] = ""
        if re.search("又名: (.*)(IMDb链接)?", info_text):
            item['other_name'] = re.search("又名: (.*)(IMDb链接)?", info_text).group(1)
        else:
            item['other_name'] = ""
        yield item
