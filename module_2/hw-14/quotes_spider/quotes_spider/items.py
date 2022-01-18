# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesSpiderItem(scrapy.Item):
    keyword_name = scrapy.Field()
    author_name = scrapy.Field()
    quote_text = scrapy.Field()
    author_url = scrapy.Field()
