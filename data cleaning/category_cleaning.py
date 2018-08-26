import pandas as pd
import sys
sys.path.insert(0,'/Users/mina/Dropbox/dropbox_project/code')
from code.api_data_to_database.sql2 import database

df = pd.read_csv("/Users/mina/Dropbox/dropbox_project/csv/table_category_final_view.csv",  index_col=None, encoding = "ISO-8859-1")

## delete null category
df = df[pd.notnull(df['category_name'])]

## Keep top3 categories
df = df.groupby(['city_name']).head(3)
df= df[['city_name', 'category_name']]


cityid =pd.read_csv("/Users/mina/Dropbox/dropbox_project/csv/poi_cityid_add2.csv",  index_col=None, encoding = "ISO-8859-1")

## city id to dict
cityid_dict = dict(zip(cityid['city_name'], cityid['city_id']))

## add new column by mapping city_name
df['city_id']= df['city_name'].map(cityid_dict)


## insert to db

db= database()
query ="""INSERT INTO table_category_final2(
                        city_name, category_name, city_id
                    ) VALUES (
                          %s, %s, %s
                    )"""


path2 = '/Users/mina/Dropbox/dropbox_project/csv/cityid_category.csv'
db.insert_csv(query, path2)


