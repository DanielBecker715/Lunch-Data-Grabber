import json

jsonOutputFilePath = r"C:/edeka/restaurantMenu.json"

#JSON TEMPLATE 
dictionary = {
    "restaurant-name": "Jawa",
    "address": "Wendenstraße 29, 20097 Hamburg",
    "opening-time": "Montag bis Freitag von 11:30 - 15:00 Uhr",
    "website": "https://www.jawa-restaurant.de/",
    "menu": [
        {
        "number":"M1",
        "dish":"Bakmie goreng sayur",
        "desc":"Bratnudeln mit Ei und Gemüse",
        "price":"5,90€",
        "allergens":""
        },
    ]
}

def createRestaurant(restaurantName, address, openingTime, website):
    print("")

def addMenu(restaurantName ,number, dish, desc, price, allergens):
    dictionary["menu"].append({ "number":f"{number}", "dish":f"{dish}", "desc":f"{desc}", "price":f"{price}", "allergens":f"{allergens}" })

def createJsonFile():
    global jsonOutputFilePath
    # convert into JSON:
    file = open(jsonOutputFilePath, 'w', encoding='utf-8')
    file.write(json.dumps(dictionary, indent=4))
    print(f"File {jsonOutputFilePath} updated")
    file.close()