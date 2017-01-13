import json
productList = []

# open file
with open('data/products.json') as json_data:
    
    # laad data
    data = json.load(json_data)
    
    # neem alleen relevante data
    for element in data:
        prijs = element["amount"]["format"]["round"]
        soort = element["name"]
        typeId = element["type"]["id"]
        productList.append({"prijs":prijs,"soort":soort,"type":typeId})

# print de eerste        
print(productList[0])
    
    
    