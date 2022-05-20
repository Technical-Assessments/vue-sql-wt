import os
from typing import Any
import pymysql

LOAD_PATH = "../test_mysql/employees.sql"

def connection() -> Any:
  return pymysql.connect(
    host        =   os.environ.get("MYSQL_HOST"),
    # user        =   os.environ.get("MYSQL_USER"),
    port        =  int(os.environ.get("MYSQL_PORT")),
    # password    =   os.environ.get("MYSQL_ROOT_PASSWORD"),
  )


def main():

  cnn = connection()

  with cnn:
    with open(LOAD_PATH, 'r') as f:
      cnn.cursor().execute(f.read())
      cnn.commit()


if __name__ == "__main__":
  main()
