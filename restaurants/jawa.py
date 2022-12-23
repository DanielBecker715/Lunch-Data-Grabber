#!/usr/bin/env python3
import createJSON

restaurantName="Jawa"
address="Wendenstraße 29, 20097 Hamburg"
openingTime="Montag bis Freitag von 11:30 - 15:00 Uhr"
website = "https://www.jawa-restaurant.de/"


createJSON.createRestaurant(restaurantName, address, openingTime, website)

#TODO Create a database connection
#TODO Get all menus from the restaurant and write it to json

# createJSON.addMenu(restaurantName,
#     number="",
#     dish="",
#     desc="",
#     price="",
#     allergens="")