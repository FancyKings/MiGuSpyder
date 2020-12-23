import re

if __name__ == '__main__':
    text = "原著小说最新章节，官场出版小说，第一章，咪咕阅读><meta name="
    sss = re.search(r"第[^*?]章", text)
    print(sss.group())


"""
        context_string = ""
        contexts = response.xpath("/html/body/section[3]/div[2]/p")
        for each in contexts:
            if not None:
                context_string += each.xpath('./text()').extract_first()
                context_string += '\n\n'
        save_item['content_text'] = context_string
        save_item['page_link'] = response.request.url
        self.logger.debug("Chapter Content" + save_item['content_text'])
        self.logger.debug("Chapter page_link" + save_item['page_link'])
"""