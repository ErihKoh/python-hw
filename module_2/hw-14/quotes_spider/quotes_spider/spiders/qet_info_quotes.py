import scrapy
import re
from quotes_spider.items import QuotesSpiderItem


def replace_quotes(my_str):
    return re.sub("^\s+|\n|\r|“|”|”\s+$", '', my_str)


class QetInfoQuotesSpider(scrapy.Spider):
    name = 'qet_info_quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        for quote in response.xpath("/html//div[@class='quote']"):
            item = QuotesSpiderItem()

            item["keyword_name"] = quote.xpath("div[@class='tags']/a/text()").getall(),
            item["author_name"] = quote.xpath("span/small/text()").get(),
            item["quote_text"] = replace_quotes(quote.xpath("span[@class='text']/text()").get()),
            item["author_url"] = "https://quotes.toscrape.com/" + response.xpath("//span/a/@href").get()
            yield item

        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)
