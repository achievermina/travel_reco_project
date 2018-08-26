#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
import json
import pandas as pd
import csv
import configparser

class database:

    def __init__(self):
        print("database")

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

    def insert_citydata(self, items):
        query = """
                            INSERT INTO table_city (
                                city_id, city_name, description, rating
                             ) VALUES (
                                %s, %s, %s, %s
                            )
                        """

        for i in items:
            binding = (i["city_id"], i["city_name"], i["description"], i["rating"])

            cur = self.conn.cursor()
            cur.execute(query, binding)
            self.conn.commit()

        print("finish input")

    def insert_poidata(self, items2):

        query = """
                    INSERT INTO table_poi (
                        poi_id, poi_name, city_name, marker, categories, poi_parents_id
                    ) VALUES (
                          %s, %s, %s, %s, %s, %s
                    )
                """


        for j in items2:
            binding = (j["poi_id"], j["poi_name"], j["city_name"], j["marker"], ','.join(j['categories']), ','.join(j['poi_parents_id']))

            with self.conn.cursor() as cursor:
                cursor.execute(query, binding)
                self.conn.commit()

        print("insert to database success")


    def insert_csv(self, inputquery, path):

        query = inputquery

        with open(path) as csv_data:

            data = csv.reader(csv_data)
            for rows in data:
                with self.conn.cursor() as cursor:
                     cursor.execute(query,tuple(rows))
                     self.conn.commit()

        print("insert to database success")


    def insert_dataframe(self, inputquery, df):

        query = inputquery

        for j in df.itertuples():
            with self.conn.cursor() as cursor:
                     cursor.execute(query,j)
                     self.conn.commit()

        print("insert to database success")

