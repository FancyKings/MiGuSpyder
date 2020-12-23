# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MiGuScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    chapter_no = scrapy.Field()
    content_text = scrapy.Field()
    page_link = scrapy.Field()
    pass
