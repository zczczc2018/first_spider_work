import requests
from bs4 import BeautifulSoup
import re
import multiprocessing
from multiprocessing import Queue


pattern = re.compile('企业介绍|关于我们|企业发展|发展历史|企业概况|企业简介|公司简介|公司介绍')
urls_set = Queue(100)       # 使用multiprocessing.manager.Manager.list也能实现进程间共享？
url_queue = Queue(100)


def get_url():
    with open('url.txt', 'r', encoding='utf8') as file:
        for i in range(100):
            url_queue.put(file.readline().strip("\n"))
        print('url read over')


def spider(queue, i, urls_set):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    while not queue.empty():
        url = queue.get()
        try:
            res = requests.get(url, headers=headers, timeout=5)
            if res.status_code == 200:
                if res.apparent_encoding == "utf-8":
                    res.encoding = 'utf-8'
                elif res.apparent_encoding == 'GB2312':
                    res.encoding = 'gbk'
                bs_result = BeautifulSoup(res.text, 'html.parser')
                tag = bs_result.find('a', text=pattern)
                if tag and tag.attrs['href']:
                    if 'http' in tag.attrs['href']:
                        urls_set.put(tag.attrs['href'])
                    else:
                        urls_set.put(res.url+tag.attrs['href'])
        except Exception as e:
            print("spider {0} failed to crawl {1}, error info:{2}".format(i, url, str(e.args)))
        else:
            print("spider {0} success crawl {1}".format(i, url))


if __name__ == "__main__":
    get_url()
    process_list = []
    for i in range(8):
        process = multiprocessing.Process(target=spider, args=(url_queue, i, urls_set))
        process_list.append(process)
        process.start()
    # map(multiprocessing.Process.join, process_list)
    for process in process_list:
        process.join()
    print(urls_set.qsize())
    for i in range(urls_set.qsize()):
        print(urls_set.get())
