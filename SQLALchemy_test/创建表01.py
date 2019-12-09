# -*- coding: utf-8 -*-
__author__ = 'Px'

import sys
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer,String,Float
from sqlalchemy import Column


reload(sys)
sys.setdefaultencoding('utf8')

conn_url = 'mysql://root:123456@localhost/testa?charset=utf8'
engine = create_engine(conn_url,encoding='utf-8',echo=True)
Base = declarative_base(engine)
sessions = sessionmaker(bind=engine)
pool = sessions()
class test_table(Base):

    __tablename__ = 't_test'

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(length=50))



#Base.metadata.create_all()

def insert_data():
    name = test_table(name='张三21顶顶顶顶啊')
    pool.add(name)
    pool.commit()
    pool.refresh(name)
    pool.close()

def query_data_all():
    res = pool.query(test_table.id,test_table.name).all()
    print res

def query_data_filter():

    res = pool.query(test_table).filter(test_table.id>2,test_table.id<4).all()
    for i in res:
        print i.id,i.name



query_data_filter()



