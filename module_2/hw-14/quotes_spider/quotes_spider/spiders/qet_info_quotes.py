import scrapy


class QetInfoQuotesSpider(scrapy.Spider):
    name = 'qet_info_quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
