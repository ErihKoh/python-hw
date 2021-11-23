from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://'
                       'postgres:hellga1408@smartbot.ci4kh2fdklto.eu-west-3.rds.amazonaws.com:5432/NoteBook')
Session = sessionmaker(bind=engine)


