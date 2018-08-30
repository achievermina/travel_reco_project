#from typing import List
import csv
from sygic_city2 import sygic_api
from sql2 import database
import pandas as pd


def main():
## Calling class
    s = sygic_api()
    db = database()

##city location data to Database
    data = s.get_cityLocation()

    data = pd.DataFrame.from_dict(data)

    data.to_csv('city_location2.csv',encoding='utf-8')
    print(data)


## Save CSV file for city-location

keys = result2[0].keys()
with open('city_locations.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(result2)



if __name__ == "__main__":
    main()
