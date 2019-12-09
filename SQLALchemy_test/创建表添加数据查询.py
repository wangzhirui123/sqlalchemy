# -*- coding: utf-8 -*-
__author__ = 'Px'

import sys
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import Column,ForeignKey,Integer,String
from sqlalchemy import or_,and_
reload(sys)
sys.setdefaultencoding('utf8')

conn_url = 'mysql://root:123456@localhost:3306/testa?charset=utf8'
engine = create_engine(conn_url,encoding='utf8',echo=True)
Base = declarative_base(engine)

class Dep(Base):

    __tablename__ = 'dep'

    id = Column(Integer,primary_key=True,autoincrement=True)
    dname = Column(String(length=50))

class Emp(Base):

    __tablename__ = 'emp'

    id = Column(Integer,primary_key=True,autoincrement=True)
    ename = Column(String(32),index=True)
    dep_id = Column(Integer,ForeignKey('dep.id'))


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)

# drop_db()
# init_db()
#
session = sessionmaker(bind=engine)
pool = session()
#
# pool.add_all([
#     Dep(dname='技术'),
#     Dep(dname='销售'),
#     Dep(dname='市场'),
#     Dep(dname='人事')
# ])
#
# pool.add_all([
#     Emp(ename='张三',dep_id='1'),
#     Emp(ename='里斯',dep_id='2'),
#     Emp(ename='王武',dep_id='3'),
#     Emp(ename='赵留',dep_id='4'),
#
# ])
#
# pool.commit()


# def search_1():
#     '''条件filter_by只能传参数,x=x'''
#     sql = pool.query(Emp).filter_by(ename='王武').all()
#     for i in sql:print i.ename

def search_2():
    '''filter传的是表达式,逗号分隔,默认为and'''
    sql = pool.query(Emp).filter(Emp.id>0,Emp.ename =='里斯').all()
    for i in sql:print i.ename


def search_3():
    '''filter between()之间'''

    res = pool.query(Emp).filter(Emp.id.between(1,4),Emp.ename=='里斯').all()
    for i in res:print i.id



def search_4():
    '''in_'''
    res = pool.query(Emp).filter(Emp.id.in_([1,2,3,4])).all()
    for i in res:print i.ename



def search_5():
    '''~not'''
    res = pool.query(Emp).filter(~Emp.id.in_([1,2,3])).all()
    for i in res:print i.ename



def search6():
    '''and_'''
    res = pool.query(Emp).filter(and_(Emp.id==2,Emp.ename=='里斯')).all()
    for i in res:print i.id

search6()

def search_6():
    '''or_'''

    res = pool.query(Emp).filter(or_(Emp.id==4,Emp.ename=='王武')).all()
    for i in res:print i.ename



def search_7():
    '''连表'''
    res = pool.query(Dep,Emp).all()
    for i in res:
        print i[1].ename



def update_data():
    sql = pool.query(Emp).filter(Emp.id>2).update({"ename":"张三"})
    pool.commit()


update_data()