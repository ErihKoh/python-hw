from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from quotes_spider.models import Author, Quote, Keyword, db_connect, create_table
from quotes_spider.items import QuotesSpiderItem


class QuotesSpiderPipeline:
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.authors = set()
        self.keywords = set()

    def process_item(self, item, spider):

        if isinstance(item, QuotesSpiderItem):
            isExist_author = item["author_name"]
            if isExist_author not in self.authors:
                author = Author(author_name=item["author_name"], author_url=item["author_url"])
                self.session.add(author)
                self.authors.add(item["author_name"])

            quote = Quote(item["quote_text"], item["author_name"])
            self.session.add(quote)

            if "keyword_name" in item:
                for keyword_name in item["keyword_name"]:
                    keyword = Keyword(keyword_name=keyword_name)
                    exist_keyword = self.session.query(Keyword).filter_by(keyword_name=keyword.keyword_name).first()
                    if exist_keyword is not None:
                        keyword = exist_keyword
                        self.session.add(keyword)

                    quote.keywords.append(keyword)
            return item

    def close_spider(self, spider):
        try:
            self.session.commit()
        except:
            self.session.rollback()
        finally:
            self.session.close()


class DuplicatesPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        exist_quote = session.query(Quote).filter_by(quote_text=item["quote_text"]).first()
        session.close()
        if exist_quote:
            raise DropItem("Duplicate item found: %s" % item["quote_content"])
        else:
            return item
