from typing import List
import csv
from sygic_city2 import sygic_api
from sql2 import database


def main():
## Calling class
    s = sygic_api()
    db = database()

##city info data to Database
    result2 = s.get_cityinfos()
    db.insert_citydata(result2)

## Save CSV file for city-info

keys = result2[0].keys()
with open('city_info.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(result2)






if __name__ == "__main__":
    main()










