from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine


keywords_quotes_association = Table('quote_keyword', Base.metadata,
                                    Column('quote_id', Integer, ForeignKey('quote.id')),
                                    Column('keyword_id', Integer, ForeignKey('keyword.id'))
                                    )


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    author_name = Column(String)
    author_url = Column(String)
    # quotes = relationship('Quote', backref='author')

    def __init__(self, author_name, author_url):
        self.author_name = author_name
        self.author_url = author_url

    def __repr__(self):
        return f'{self.author_name}'


class Keyword(Base):
    __tablename__ = "keyword"
    id = Column(Integer, primary_key=True)
    keyword_name = Column('keyword_name', String(30), unique=True)
    quotes = relationship('Quote', secondary='quote_keyword',
                          lazy='dynamic', backref="keyword")

    def __init__(self, keyword_name):
        self.keyword_name = keyword_name

    def __repr__(self):
        return f'{self.keyword_name}'


class Quote(Base):
    __tablename__ = "quote"
    id = Column(Integer, primary_key=True)
    quote_text = Column(String)
    author = Column(String, ForeignKey('author.author_name'))
    keywords = relationship("Keyword", secondary='quote_keyword', lazy='dynamic', backref="quote")

    def __init__(self, quote_text, author):
        self.quote_text = quote_text
        self.author = author

    def __repr__(self):
        return f'{self.quote_text}'
