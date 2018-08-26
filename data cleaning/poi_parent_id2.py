import pandas as pd
from Datacleaning import Datacleaning
import csv

d = Datacleaning()

poi = pd.read_csv("/Users/mina/Dropbox/dropbox_project/csv/table_poi.csv",  index_col=None, encoding = "ISO-8859-1")
poi2 = poi[['city_name', 'poi_parents_id']]
poi3= poi[['city_name']]

dic=[]

##get city id
for i in poi2['poi_parents_id']:
    cityid= d.getcity(i)
    dic.append(cityid)

## Make city column to pandas series
city = pd.Series(dic)

##Insert city to poi3
poi3.insert(loc=0, column='city_id', value=city)

poi3.to_csv('poi_cityid_add2.csv', encoding='utf-8')


