#!/usr/bin/env python3
import createJSON
import pdftotext
import requests
import re
import os
from datetime import datetime

currentMonth = datetime.now().month
currentYear = datetime.now().year
url = f"https://www.niemerszein.de/assets/{currentYear}/{currentMonth}/Brotladen_Mahlzeit_Mittagswoche51.pdf"

HTTP_PROXY = "http://192.168.23.70:3128"
HTTPS_PROXY = "http://192.168.23.70:3128"
response = requests.get(url, proxies={ "http"  : HTTP_PROXY, "https" : HTTPS_PROXY })

#TODO Read information from pdf
#TODO Get all menus from the restaurant and write it to json

createJSON.createRestaurant(restaurantName="", address="", openingTime="", website="")
#createJSON.addMenu(restaurantName="" ,number="", dish="", desc="", price="", allergens=""):


# Load your PDF
# with open("tmp.pdf", "wb") as file:
#     file.write(response.content)
# with open("tmp.pdf", "rb") as f:
#     pdf = pdftotext.PDF(f)
#     os.unlink("tmp.pdf")
# text = "\n".join(pdf)

# found = False
# for line in text.split("\n"):
#     print(line)
#     if line.split(" ")[0] in ["MONTAG", "DIENSTAG", "MITTWOCH", "DONNERSTAG", "FREITAG", "JEDEN"]:
#         print("new Day")
#         found = True
#     if line.split(" ")[0] in ["INFOS"]:
#         break
