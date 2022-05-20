import os
from typing import Any
import pymysql

LOAD_PATH = "../test_mysql/employees.sql"

def connection() -> Any:
  return pymysql.connect(
    host        =   "192.168.176.3",
    user        =   os.environ.get("MYSQL_USER"),
    port        =   3306,
    password    =   os.environ.get("MYSQL_ROOT_PASSWORD"),
    # database    =   os.environ.get("employees")
  )


def main():

  cnn = connection()
  with cnn:
    cnn.cursor().execute("source employees.sql")
    cnn.commit()

  """ with cnn:
    with open(LOAD_PATH, 'r') as f:
      cnn.cursor().execute(f.read())
      cnn.commit() """


if __name__ == "__main__":
  main()
