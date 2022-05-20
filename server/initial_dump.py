import os
import pymysql
from typing import Any


def connection() -> Any:
  return pymysql.connect(
    user        =   os.environ.get("MYSQL_USER"),
    port        =   int(os.environ.get("MYSQL_PORT")),
    password    =   os.environ.get("MYSQL_ROOT_PASSWORD"),
    database    =   os.environ.get("MYSQL_DATABASE")
  )


def main():
    cnn = connection()
    with cnn:
        with cnn.cursor() as cursor:
            query = "SELECT * FROM employees LIMIT 10"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)

if __name__ == "__main__":
  main()
