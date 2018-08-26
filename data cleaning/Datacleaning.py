
import pandas as pd
from pullData import pullData



class Datacleaning():

    def __init__(self):
        pass


    def separatecommaString(self, item):

        result = pd.DataFrame()

        for i in range(1, len(item)):
            result[i] = [item[i].split(",")]

        result= result.transpose()
        return result




    def getcity(self, str):
        strs = str.split(",")
        for c in strs:
            if "city" in c:
                return c

