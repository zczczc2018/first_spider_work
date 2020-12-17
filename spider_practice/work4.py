import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import time
import os


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    "referer": "https://www.programcreek.com/"
}


def get_module_url():
    """
    获取包含request的所有库
    :return: 库地址的URL列表
    """
    start_url = 'https://www.programcreek.com/python/?ClassName=request&submit=Search'
    res = requests.get(url=start_url, headers=headers)
    bs_result = BeautifulSoup(res.text, 'html.parser')
    a_tags = bs_result.find('ul', id='api-list').find_all('a')
    modules = []
    for a_tag in a_tags:
        modules.append({"module_name": a_tag.get_text(), "module_url":a_tag.attrs['href']})
    print("所有库的URL爬取完成")
    return modules


def parse_code_page(url, module_name, func_name):
    """
    解析方法页面，获取代码并写入txt文件
    :param url: 某个方法页面的URL
    :return:    不返回，直接写入文件
    """
    res = requests.get(url, headers=headers)
    bs_result = BeautifulSoup(res.text, 'html.parser')
    code_tags = bs_result.find_all('pre', class_='prettyprint')
    code_text = []
    for code_tag in code_tags:
        code_text.append(code_tag.get_text())

    if not os.path.exists('code/{0}'.format(module_name)):  # 文件夹不存在就创建
        os.mkdir('code/{0}'.format(module_name))

    if not os.path.exists("code/{0}/{1}.txt".format(module_name, func_name)):  # 为了减少运行时间，爬过先不爬
        with open("code/{0}/{1}.txt".format(module_name, func_name), "w", encoding='utf8') as file:
            for code_str in code_text:
                file.write(code_str)
                file.write("\n******************************\n")
        print("{0}.{1}代码已写入完成".format(module_name, func_name))
    else:
        print("{0}.{1}代码已存在".format(module_name, func_name))


def get_code(module):
    """
    从某个库中获取所有方法的URL并解析页面获取代码
    :param url: 某个库的URL
    :return: 不返回
    """
    res = requests.get(module["module_url"], headers=headers)
    bs_result = BeautifulSoup(res.text, 'html.parser')
    a_tags = bs_result.find('ul', id='api-list').find_all('a')
    funcs = []
    for a_tag in a_tags:
        funcs.append({"func_name": a_tag.get_text(), "func_url": a_tag.attrs['href']})

    for func in funcs:
        parse_code_page(func["func_url"], module['module_name'], func["func_name"])
        time.sleep(2)
    print('进程{0}爬取{1}完成'.format(os.getpid(), module['module_name']))


if __name__ == "__main__":
    modules = get_module_url()
    pool = Pool(4)
    try:
        pool.map(get_code, (modules))
    except Exception as e:
        print(e.args)
    finally:
        pool.close()
        pool.join()
    print("所有代码爬取完毕，爬虫已退出")