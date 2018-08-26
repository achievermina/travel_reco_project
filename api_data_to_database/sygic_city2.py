#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pandas as pd
import csv

print("sygic process")

city_list = []


class sygic_api:
    def __init__(self):
        print("api init")
        self.path = "https://api.sygictravelapi.com/1.0/en/places/list"
        self.header = {
            "x-api-key": "hxZOIRuA3y2TTsxnKtZIi9Fs8yAdQEmp9aq691Bw"
        }


##City detail
    def get_cityinfos(self):
        param = "ids=city:186|city:377|city:366|city:361|city:10891|city:364|city:320|city:363|city:362|city:311|city:414|city:10452|city:508|city:3804|city:1773|city:2550|city:10887|city:1816|city:1839|city:1595|city:1661|city:360|city:1844|city:1649|city:367|city:1853|city:418|city:397|city:1820|city:10520|city:4931|city:3885|city:1771|city:1752|city:365|city:140240|city:493|city:10553|city:1843|city:1809|city:401|city:1723|city:4490"
        response = requests.get(f"https://api.sygictravelapi.com/1.0/en/places?{param}", headers= self.header)
        js_data = response.json()

        lst = js_data['data']['places']

        items = []

        for item in lst:
            item_info = {
                "city_id": item["id"],
                "city_name": item["name"],
                "description": item["perex"],
                "rating": item["rating"]
            }

            items.append(item_info)

        print("request success")
        return items

    ##City detail
    @property
    def get_cityLocation(self):
        param = "ids=city:186|city:377|city:366|city:361|city:10891|city:364|city:320|city:363|city:362|city:311|city:414|city:10452|city:508|city:3804|city:1773|city:2550|city:10887|city:1816|city:1839|city:1595|city:1661|city:360|city:1844|city:1649|city:367|city:1853|city:418|city:397|city:1820|city:10520|city:4931|city:3885|city:1771|city:1752|city:365|city:140240|city:493|city:10553|city:1843|city:1809|city:401|city:1723|city:4490"
        response = requests.get(f'https://api.sygictravelapi.com/1.0/en/places?{param}'.format(param=param), headers=self.header)

        js_data = response.json()

        lst = js_data['data']['places']

        items3 = []

        for item in lst:
            item_info = {
                "city_id": item["id"],
                "city_name": item["name"],
                "LAT": item["location"]['lat'],
                "LNG": item["location"]['lng']
            }

            items3.append(item_info)
            print(items3)
        data = pd.DataFrame.from_dict(items3)
        data.to_csv('city_location.csv',encoding='utf-8')

        print("request success")
        return items3

    # poi list
    def get_poilist(self, parents, level, limit):

        path = "https://api.sygictravelapi.com/1.0/en/places/list"
        header = {
            "x-api-key": "hxZOIRuA3y2TTsxnKtZIi9Fs8yAdQEmp9aq691Bw"
        }

        parameters2 = {
            'parents': parents,
            'level': level,
            'limit': limit,
        }

        response2 = requests.get(url=path, headers=header, params=parameters2)
        js_data2 = response2.json()

        lst2 = js_data2['data']['places']
        items2 = []

        for item in lst2:
            item_info2 = {
                "poi_id": item["id"],
                "poi_name": item["name"],
                "city_name": item["name_suffix"],
                "marker": item["marker"],
                "categories": item["categories"],
                "poi_parents_id": item["parent_ids"]
            }

            items2.append(item_info2)

        print("request success")
        return items2


if __name__ == "__main__":
    main()