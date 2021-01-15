from scrapy import cmdline

name = "single_process_spider"
cmdline.execute(['scrapy', 'crawl', name, '-a', 'start=0'])
