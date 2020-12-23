import scrapy, re, os
# -*- coding: utf-8 -*-

from mi_gu_scrapy.items import MiGuScrapyItem


class MiGuSpider(scrapy.Spider):
    name = 'mi_gu'
    allowed_domains = ['wap.cmread.com']
    # https://wap.cmread.com/r/533088210/533088212.htm
    start_urls = ['https://wap.cmread.com/r/l/r.jsp?ln=127_614323__2_1_&at=1&nid=381939562&purl=%2Fr%2Fl%2Fr.jsp%3Fat%3D1%26nid%3D381939562%26bid%3D533088210%26cid%3D533088213&bid=533088210&vt=3&cid=533088212']

    def parse(self, response):
        save_item = MiGuScrapyItem()
        save_item['chapter_no'] = response.xpath("//div[@class='charpterName']/text()").extract_first()
        self.logger.debug("Chapter No." + save_item['chapter_no'])
        context_string = ""
        contexts = response.xpath('//div[@class="charpterContent"]/p')
        for each in contexts:
            if not None:
                one_line = each.xpath('./text()').extract_first()
                if str(one_line) != None and str(one_line) != "None":
                    context_string += str(one_line)
        save_item['content_text'] = context_string
        save_item['page_link'] = response.request.url
        self.logger.debug("Chapter Content" + save_item['content_text'])
        self.logger.debug("Chapter page_link" + save_item['page_link'])

        yield save_item

        next_page = 'https://wap.cmread.com' + str(response.xpath('//div[@class="charpterBox"]/a[3]/@href').extract_first())
        yield scrapy.Request(next_page, callback=self.parse)
