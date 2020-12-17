import re
import threading
import os


url_set = set()


def match_url():
    with open("webspiderUrl.txt", 'r', encoding='utf8') as file:
        for line in file.readlines():
            urls = re.findall("http://[a-z]*[\x00-\xff]+(?=;|')", line)
            for url in urls:
                url = url.replace(" ", "").replace(')', '').replace('\'', '')
                atom_urls = url.split(";")
                if "<br>" in url:
                    atom_urls = url.split("<br>")
                if "," in url:
                    atom_urls = url.split(',')
                for atom_url in atom_urls:
                    url_set.add(atom_url)


def write_to_txt():
    with open("url.txt", 'a+', encoding='utf8') as file:
        while url_set:
            url = url_set.pop()
            file.write(url+'\n')


if __name__ == "__main__":
    match_url()
    if os.path.exists('url.txt'):       #如果已经存在url文件，删除它
        os.remove('url.txt')
    for i in range(5):
        try:
            thread = threading.Thread(target=write_to_txt)
            thread.start()
        except Exception as e:
            print(e.args)