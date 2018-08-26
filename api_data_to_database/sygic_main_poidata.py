from typing import List
import csv
from sygic_city2 import sygic_api
from sql2 import database

with open('/Users/mina/Dropbox/dropbox_project/backupdata/city_id3.csv') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    city_list_final = sum(your_list, [])

def main():

## Calling class
    s = sygic_api()
    db = database()

#poi info data to Database(multi) - BE CAREFUL WHEN YOU RUN THIS

    for city in city_list_final:
        result = s.get_poilist(city, "poi", "200")
        print(city, len(result))
        db.insert_poidata(result)

##poi info data to Database(one)
    #result = s.get_poilist(city_list_final, "poi", "200")
    #db.insert_poidata(result)


##Save csv file for poi list
    #keys = result[0].keys()
    #with open('city_poi_list.csv', 'w') as output_file:
        #dict_writer = csv.DictWriter(output_file, keys)
        #dict_writer.writeheader()
        #dict_writer.writerows(result)


if __name__ == "__main__":
    main()










