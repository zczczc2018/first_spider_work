import multiprocessing
from scrapy.utils.log import configure_logging
from scrapy import cmdline



configure_logging()


def start_spider(start, i):
    commad = 'scrapy crawl single_process_spider -a start=%s' % start
    print("爬虫%s开始运行" % i)
    cmdline.execute(commad.split())


if __name__ == "__main__":
    starts = [0, 20, 40, 60, 80, 100, 120, 140]
    process_size = 1
    pool = multiprocessing.Pool(processes=process_size)
    i = 1
    for start in starts:
        result = pool.apply_async(start_spider, args=(start, i))
        i += 1
    pool.close()
    pool.join()
    if result.successful():
        print("爬取结束")

