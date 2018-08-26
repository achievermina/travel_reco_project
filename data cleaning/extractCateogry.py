from pullData import pullData
import pandas as pd
from Datacleaning import Datacleaning
import pymysql
import configparser

p= pullData()
d = Datacleaning()
df = p.pull_data()




#Merge to the previous table
df[u'poi_parents_id'] = d.separatecommaString(df[u'poi_parents_id'])
df[u'categories'] = d.separatecommaString(df[u'categories'])

#ListToMultipleRows(df_cleaning,u'categories')
#Category table
s2 = df.set_index(u'city_name')[u'categories'].apply(pd.Series).stack()
s2 = s2.reset_index()
s2.columns = ['city_name','index_no','category_name']


#category_id
print(s2.category_name.unique())
values_dict = {'sightseeing':1, 'discovering':2, 'relaxing':3, 'doing_sports':4, 'hiking':5,
       'traveling':6, 'shopping':7, 'going_out':8, 'eating':9, 'playing':10,
       'sleeping':11,'':12}
s2['category_id'] = s2['category_name'].map(values_dict)

## Save CSV file for cateogry
s2.to_csv('category.csv',sep='\t')





##SQL insert final version
config = configparser.ConfigParser()
config.read('config.ini')
config.sections()
dblogin = config["db"]

conn = pymysql.connect(
            host=dblogin["host"],
            port=int(dblogin["port"]),
            user=dblogin["user"],
            passwd=dblogin["pwd"],
            db=dblogin["dbname"],
            charset="utf8",
            init_command="SET SESSION time_zone='Asia/Seoul'")


query = """ INSERT INTO table_category(
            city_name, `index`, category_name, category_id)values(
            %s,%s,%s,%s
            )
"""


s3 = list(s2.itertuples(index=False, name=None))
converted_tuple_list = [(item[0], int(item[1]), item[2], int(item[3])) for item in s3]

for items in converted_tuple_list:

    with conn.cursor() as cursor:
        cursor.execute(query,items)
        conn.commit()


print("insert to database success")
