import requests
import re
import wget
import os


def get_mp3_url():
    url = 'http://www.listeningexpress.com/studioclassroom/ad/'
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,\ like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
    mp3_url_parts = re.findall("\(\'.*?\.mp3", res.text)
    mp3_urls = []
    for mp3_url_part in mp3_url_parts:
        mp3_url = url + mp3_url_part.replace('(\'', '')
        mp3_urls.append(mp3_url)
    return mp3_urls


def download(urls):
    for i in range(1, len(urls)):
        file_name = wget.filename_from_url(urls[i])
        if os.path.exists('mp3/'+file_name):
            os.remove('mp3/'+file_name)
        wget.download(urls[i], './mp3/'+file_name)
    print('mp3 download complete')


if __name__ == "__main__":
    urls = get_mp3_url()
    download(urls)