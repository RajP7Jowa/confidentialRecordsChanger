import pandas as pd
from faker import Faker
from pprint import pprint
import numpy as np
from random import randint

class SaveHistorical:
    fake = Faker()
    def readExcelFile(self):
        try:
            return pd.read_csv("input.csv")
        except Exception as e:
            print("[Read Excel] Unable to read file -",str(e))
            return False

    # Function for filtering the data 
    def filterDataAndCalculateRatio(self, filteredData, objectChange):
        try:
            for index, row in filteredData.iterrows():
                    fullNme = self.fake.name()
                    first_last_name = fullNme.replace("Mr.","").split(" ")

                    filteredData.loc[index, objectChange["FirstName"]] = first_last_name[0]
                    filteredData.loc[index, objectChange["LastName"]] = first_last_name[1]
                    
                    # filteredData.loc[index, objectChange["Name"]] =fullNme
                    filteredData.loc[index, objectChange["Email"]] =(first_last_name[0]+"."+first_last_name[1]+"@xyz.com").lower()
                    filteredData.loc[index, objectChange["Addr"]] =self.fake.address()
                    filteredData.loc[index, objectChange["Mobile"]] = "("+str(randint(700, 999))+")"+str(randint(700, 999))+"-"+str(randint(7000, 9999))

                    
            filteredData.to_csv('output.csv',index=False,header=False, quoting=1)
            
            return True
        except Exception as e:
            print("Error change -",str(e))
        return False


    def PreparingDataOfHistorical(self, objectChange):
        if (self.filterDataAndCalculateRatio(self.readExcelFile(), objectChange)):
                return True
        return False


if __name__ == '__main__':
    try:
        objectChange = {"Name":"FieldName", "Addr":"address","Mobile":"phone", "FirstName":"first_name","LastName":"last_name","Email":"email" }
        p = SaveHistorical()
        p.PreparingDataOfHistorical(objectChange)
        
    except Exception as e:
        print("[calculateRatioOfYear] process break - ", str(e))