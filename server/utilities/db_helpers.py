import os
import pymysql
from pymysql.connections import Connection
from pymysql.cursors import DictCursor


user      : str = os.environ["MYSQL_USER"]
port      : int = int(os.environ["MYSQL_PORT"])
password  : str = os.environ["MYSQL_ROOT_PASSWORD"]
database  : str = os.environ["MYSQL_DATABASE"]


def connection() -> Connection:
    return pymysql.connect(
        user        =     user,
        port        =     port,
        password    =     password,
        database    =     database,
        cursorclass =    DictCursor
    )


def SQLSelect(query: str):
    with connection() as cnn:
        with cnn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
