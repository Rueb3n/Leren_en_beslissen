import json
import time 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import product

productList = []
#productdata = product.productdata()

# open file
with open('data/payments.json') as json_data:
    
    # laad data
    data = json.load(json_data)
    # neem alleen relevante data
    for element in data:
        try:
            productid = element["products"][0]["_id"]["$oid"]
        except: 
            productid = 0
        user = element["state"]["by"]
        tijd = element["state"]["on"]["time"]
        datum = element["state"]["on"]["date"]
        typeId = element["description"]
        if productid == '57c2b4cb7672fa9201fa0aa9': #'57cd87343068d0401719d1b3': < hok fris #'57cd872a3068d0401719d1a3': < hokbier
            productList.append({"user id":user,"tijd":tijd+datum,"beschrijving":typeId})
            print typeId+" "+datum+" "+tijd
        #print productList
    # plt.hist(productList);
    # plt.show()
print len(productList)

