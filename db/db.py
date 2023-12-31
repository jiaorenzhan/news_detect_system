import os
import pandas as pd
from sqlalchemy import create_engine
import pymysql

engine = create_engine('mysql+pymysql://root:123456@192.168.56.101:3306/library')  # 这里直接使用pymysql连接,echo=True，会显示在加载数据库所执行的SQL语句。


def get_models():

    # sql 命令
    sql_cmd = "SELECT name  FROM books "

    df = pd.read_sql_table(table_name='books', con=engine)
    return df


def get_datasets():
    # sql 命令
    sql_cmd = "SELECT name  FROM book_sort "

    df = pd.read_sql(sql=sql_cmd, con=engine)
    return df
