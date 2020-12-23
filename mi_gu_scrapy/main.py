from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute(
        'scrapy crawl mi_gu -o x.csv'.split())

    # cmdline.execute(
    #     'scrapy crawl mi_gu -o codesList.json -s JOBDIR=cache/spyder_cache_migu'.split())
