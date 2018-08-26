import pymysql
import json
import pandas as pd
import configparser
from sqlalchemy import create_engine
from sqlalchemy import Table

class pullData:
    def __init__(self):
        print("connect database")


        config = configparser.ConfigParser()
        config.read('config.ini')
        config.sections()
        dblogin = config["db"]

        self.conn = pymysql.connect(
            host=dblogin["host"],
            port=int(dblogin["port"]),
            user=dblogin["user"],
            passwd=dblogin["pwd"],
            db=dblogin["dbname"],
            charset="utf8",
            init_command="SET SESSION time_zone='Asia/Seoul'")


    def pull_data(self):

        with self.conn.cursor() as cursor:
            query = "SELECT * FROM table_poi"
            cursor.execute(query)
            result = cursor.fetchall()

        df = pd.read_sql_query(query, self.conn)
        column_header = df.columns.tolist()

        return df


if __name__ == "__main__":
    p = pullData()
    p.pull_data()

