import requests
import time
import multiprocessing
import random


url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20"



"""
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: no-cache
Connection: keep-alive
Cookie: bid=hAoi6-l8I04; douban-fav-remind=1; __utmc=30149280; ll="108288"; __utmc=223695111; __yadk_uid=WHFuqvWTypIoDz9ZmDxvQZcWj8cLp8lO; _vwo_uuid_v2=D947B61D50629F4B949612CE00329AA6C|95f95961588fbff8d028f9385513d4c2; __gads=ID=c971254ae558e718-224c37b6eec400f3:T=1606491258:RT=1606491258:S=ALNI_Maqok3B-GjobYciHC_ijkkoexycgA; ct=y; viewed="34938311"; gr_user_id=057adc8d-7202-4639-a393-db41087a6d94; push_doumail_num=0; push_noty_num=0; __utmz=30149280.1609665971.35.9.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1609665971.34.8.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1609739690%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.565803361.1605104867.1609665971.1609739690.36; __utmb=30149280.0.10.1609739690; __utma=223695111.1117890868.1606491204.1609665971.1609739690.35; __utmb=223695111.0.10.1609739690; ap_v=0,6.0; _pk_id.100001.4cf6=74817fb476940c64.1606491204.35.1609740666.1609665971.
DNT: 1
Host: movie.douban.com
Pragma: no-cache
Referer: https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
X-Requested-With: XMLHttpRequest
"""

headers = {
                'Accept': '*/*',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'DNT': '1',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Pragma': 'no-cache',
                'Cookie': 'bid=hAoi6-l8I04; douban-fav-remind=1; __utmc=30149280; ll="108288"; __utmc=223695111; __yadk_uid=WHFuqvWTypIoDz9ZmDxvQZcWj8cLp8lO; _vwo_uuid_v2=D947B61D50629F4B949612CE00329AA6C|95f95961588fbff8d028f9385513d4c2; __gads=ID=c971254ae558e718-224c37b6eec400f3:T=1606491258:RT=1606491258:S=ALNI_Maqok3B-GjobYciHC_ijkkoexycgA; ct=y; __utmz=223695111.1609151206.23.7.utmcsr=search.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/movie/subject_search; viewed="34938311"; gr_user_id=057adc8d-7202-4639-a393-db41087a6d94; __utmz=30149280.1609301795.27.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_doumail_num=0; push_noty_num=0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1609563331%2C%22https%3A%2F%2Fsearch.douban.com%2Fmovie%2Fsubject_search%3Fsearch_text%3D%25E8%259D%25B4%25E8%259D%25B6%25E6%2595%2588%25E5%25BA%2594%26cat%3D1002%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.565803361.1605104867.1609497379.1609563331.34; __utmb=30149280.0.10.1609563331; __utma=223695111.1117890868.1606491204.1609497379.1609563331.33; __utmb=223695111.0.10.1609563331; _pk_id.100001.4cf6=74817fb476940c64.1606491204.33.1609563342.1609499918.',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
                'Host': 'movie.douban.com',
                'Referer': 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=',
                'X-Requested-With': 'XMLHttpRequest',
            }
'''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: no-cache
Connection: keep-alive
Cookie: bid=hAoi6-l8I04; douban-fav-remind=1; __utmc=30149280; ll="108288"; __utmc=223695111; __yadk_uid=WHFuqvWTypIoDz9ZmDxvQZcWj8cLp8lO; _vwo_uuid_v2=D947B61D50629F4B949612CE00329AA6C|95f95961588fbff8d028f9385513d4c2; __gads=ID=c971254ae558e718-224c37b6eec400f3:T=1606491258:RT=1606491258:S=ALNI_Maqok3B-GjobYciHC_ijkkoexycgA; ct=y; viewed="34938311"; gr_user_id=057adc8d-7202-4639-a393-db41087a6d94; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1609843363%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.565803361.1605104867.1609739690.1609843363.37; __utmb=30149280.0.10.1609843363; __utmz=30149280.1609843363.37.10.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1117890868.1606491204.1609739690.1609843363.36; __utmb=223695111.0.10.1609843363; __utmz=223695111.1609843363.36.9.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=74817fb476940c64.1606491204.36.1609843822.1609740666.
DNT: 1
Host: movie.douban.com
Pragma: no-cache
Referer: https://accounts.douban.com/
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-site
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36
'''

detail_headers = {
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
 'Cache-Control': 'no-cache',
 'Connection': 'keep-alive',
 #'Cookie': 'bid=hAoi6-l8I04; douban-fav-remind=1; __utmc=30149280; ll="108288"; __utmc=223695111; __yadk_uid=WHFuqvWTypIoDz9ZmDxvQZcWj8cLp8lO; _vwo_uuid_v2=D947B61D50629F4B949612CE00329AA6C|95f95961588fbff8d028f9385513d4c2; __gads=ID=c971254ae558e718-224c37b6eec400f3:T=1606491258:RT=1606491258:S=ALNI_Maqok3B-GjobYciHC_ijkkoexycgA; ct=y; viewed="34938311"; gr_user_id=057adc8d-7202-4639-a393-db41087a6d94; push_noty_num=0; push_doumail_num=0; dbcl2="203345136:KzjNWNj7ZYo"; ck=vwHi; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1610450328%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.565803361.1605104867.1610380699.1610450328.43; __utmb=30149280.0.10.1610450328; __utmz=30149280.1610450328.43.12.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1117890868.1606491204.1610380699.1610450328.42; __utmb=223695111.0.10.1610450328; __utmz=223695111.1610450328.42.11.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=74817fb476940c64.1606491204.42.1610450332.1610380844.', 'DNT': '1',
 'Host': 'movie.douban.com',
 'Pragma': 'no-cache',
 'Referer': 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=',
 'Sec-Fetch-Dest': 'document',
 'Sec-Fetch-Mode': 'navigate',
 'Sec-Fetch-Site': 'same-site',
 'Sec-Fetch-User': '?1',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
}


start = 20
detail_url = 'https://movie.douban.com/subject/3541415/'


proxy = "127.0.0.1:7890"

proxies = {
    "http": "http://" + proxy,
    "https": "https://" + proxy,
}


def proxy_test():
    for i in range(20):
        res = requests.get(url=detail_url, headers=detail_headers)
        print(res.status_code)
        time.sleep(3)


if __name__ == "__main__":
   for i in range(3):
       process = multiprocessing.Process(target=proxy_test)
       process.start()


