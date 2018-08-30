import pymysql
import pandas as pd
import configparser

def get_userSelectedDays(days):
    travelDays = int(days)
    if travelDays <=2:
        userSelectedDays = "short"
    elif travelDays <=4:
        userSelectedDays = "mid"
    else:
        userSelectedDays = "long"

    return userSelectedDays


class Database:
    def __init__(self, configpath="/home/ubuntu/portfolio/mina_final_website/apps/config.ini"):
        config = configparser.ConfigParser()
        config.read(configpath)
        config.sections()
        dblogin = config["db"]
        self.querylogin = config["query"]
        self.conn = pymysql.connect(

            host = dblogin["host"],
            port = int(dblogin["port"]),
            user = dblogin["user"],
            passwd = dblogin["pwd"],
            db = dblogin["dbname"],
            charset = "utf8",
            init_command = "SET SESSION time_zone='Asia/Seoul'")

    def pullData(self, travelDay, categories):

        category_str = " "

        for c in categories:
            category_str += " or category_name LIKE '{}'".format(c)

        category_str = category_str[4:]

        query_str = self.querylogin["queryfordata"]
        query = query_str.format(category_str, travelDay)
        result = pd.read_sql_query(query, self.conn)

        return result




if __name__ == "__main__":
    pullData(eg_day, eg_categories)
    print()

