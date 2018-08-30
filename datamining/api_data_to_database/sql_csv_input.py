from typing import List
import csv
from sygic_city2 import sygic_api
from sql2 import database
import pandas as pd


def main():
## Calling class
    db = database()


##Airport ID
    inputQuery ="""
                    INSERT INTO table_airport (
                        city_id, city_name, airport_id
                    ) VALUES (
                          %s, %s, %s
                    )
                """
    path = '/Users/mina/Dropbox/dropbox_project/code/UScityinfo_airportcode2.csv'

    db.insert_csv(inputQuery, path)


##GetCityID from POI
    inputQuery2 ="""INSERT INTO table_poi_cityid(
                        city_id, city_name
                    ) VALUES (
                          %s, %s
                    )"""


    path2 = '/Users/mina/Dropbox/dropbox_project/csv/poi_cityid_add2.csv'

    db.insert_csv(inputQuery2,path2)

if __name__ == "__main__":
    main()


