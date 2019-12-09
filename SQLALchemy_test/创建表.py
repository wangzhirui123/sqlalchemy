# -*- coding: utf-8 -*-
__author__ = 'Px'

import sys

from sqlalchemy import Column
from sqlalchemy.types import Integer,DateTime,Date,Text,String
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base

reload(sys)
sys.setdefaultencoding('utf8')

connurl = 'mysql://root:123456@localhost/mysql?charset=utf8'
engine = create_engine(connurl,encoding='utf-8',echo=True)
Base = declarative_base(bind=engine)

class ProxyIp(Base):
    __tablename__ = 't_ProxyIp'

    id = Column(Integer,primary_key=True,autoincrement=True)
    Ip = Column(String(length=20),unique=True)
    HttpType = Column(String(length=10))
    CheckTime = Column(DateTime)

Base.metadata.create_all()

