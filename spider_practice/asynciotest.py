import asyncio
import requests
import aiohttp
from bs4 import BeautifulSoup
import datetime
from io import BytesIO
urls = [f'https://www.umei.cc/bizhitupian/diannaobizhi/{i}.htm' for i in range(1, 5)]

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    "referer": "https://www.umei.cc/bizhitupian/diannaobizhi/",
    'cookie': 'Hm_lvt_19d597dda6fff717a20d276fa907bd17=1612023293; Hm_lpvt_19d597dda6fff717a20d276fa907bd17=1612023301'
}


def getImgUrl():
    img_urls = []
    for url in urls:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        imgs = soup.find('div', class_='TypeList').find_all('img')
        for img in imgs:
            img_urls.append(img.attrs['src'])
    return img_urls


def normalDowloader(img_urls):
    for url in img_urls:
        img_name = url.split('/')[-1]
        bin_img = requests.get(url).content
        file = open(f"normalDownload/{img_name}", 'wb')
        file.write(bin_img)
        file.close()


async def download(url):
    async with aiohttp.ClientSession() as s:
        async with await s.get(url=url, headers=headers) as response:
            image_name = url.split("/")[-1]
            bin_image = await response.content.read()
            return {'image_name': image_name, 'content': bin_image}


def writer(task):
    image = task.result()
    image_name = image['image_name']
    content = image['content']
    file = open(f"asyncioDownload/{image_name}", 'wb' )
    file.write(content)
    file.close()


def asyncDownloader(img_urls):
    loop = asyncio.get_event_loop()
    tasks = []
    for img_url in img_urls:
        t = download(img_url)
        task = loop.create_task(t)
        task.add_done_callback(writer)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))



if __name__ == '__main__':
    img_urls = getImgUrl()
    start_time = datetime.datetime.now()
    print("开始下载图片，时间：", start_time)
    # normalDowloader(img_urls=img_urls)
    asyncDownloader(img_urls=img_urls)
    over_time = datetime.datetime.now()
    print("图片下载结束，时间：", over_time)
    print("总用时：", (over_time - start_time).seconds, "秒")