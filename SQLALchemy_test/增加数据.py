# -*- coding: utf-8 -*-
__author__ = 'Px'

import sys
import datetime
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer,String,Text,DateTime,Date
from sqlalchemy.orm.session import sessionmaker
reload(sys)
sys.setdefaultencoding('utf8')


connurl = 'mysql://root:123456@localhost/mysql?charset=utf8'
engine = create_engine(connurl,encoding='utf-8',echo=True)
Base = declarative_base(engine)
sessions = sessionmaker(bind=engine)
session = sessions()

class ProxyIp(Base):
    __tablename__ = 't_ProxyIp'

    id = Column(Integer,primary_key=True,autoincrement=True)
    Ip = Column(String(length=20),unique=True)
    HttpType = Column(String(length=10))
    CheckTime = Column(DateTime)
Base.metadata.create_all()
ip = ProxyIp(Ip='192.168.1.2',HttpType='http',CheckTime=datetime.datetime.today())
session.add(ip)
session.commit()
session.refresh(ip)
session.close()


