from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from quotes_spider.models import Author, Quote, Keyword, db_connect, create_table


class QuotesSpiderPipeline:
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.authors = set()
        # self.keywords = set()

    def process_item(self, item, spider):

        isExist = item["author_name"]
        if isExist not in self.authors:
            author = Author(author_name=item["author_name"], author_url=item["author_url"])
            self.session.add(author)
            self.authors.add(item["author_name"])
        # if exist_author:
        #
        # exist_author = self.session.query(Author).filter(Author.author_name == author.author_name).first()


        # quote = Quote(item["quote_text"])

        # if exist_author:
        #     quote.author = exist_author
        # else:
        #     quote.author = author
        #
        # if "keywords" in item:
        #     for keyword_name in item["keywords"]:
        #         keyword = Keyword(name=keyword_name)
        #         exist_keyword = self.session.query(Keyword).filter_by(name=keyword.name).first()
        #         if exist_keyword is not None:  # the current tag exists
        #             keyword = exist_keyword
        #
        #         quote.keywords.append(keyword)

        try:
            # self.session.add(quote)

            # self.session.add(keyword)
            self.session.commit()
        except Exception as err:
            self.session.rollback()
        finally:
            self.session.close()
            print(self.authors)

        return item

    # def close_spider(self, spider):
    #     try:
    #         self.session.add(quote)
    #         self.session.add(author)
    #         self.session.add(keyword)
    #         self.session.commit()
    #     except:
    #         self.session.rollback()
    #     finally:
    #         self.session.close()


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
