import phonenumbers
from phonenumbers import geocoder
from art import *
import opencage
tprint("Created    by    yousef")
print("This osint tool for phonenumbers")
number1 = input("Enter your number without +:")
number = ("+"+number1)
phnumber =phonenumbers.parse(number)
location = geocoder.description_for_number(phnumber, "en")
print(location)
from phonenumbers import carrier
service = phonenumbers.parse(number)
print(carrier.name_for_number(service, "en"))

from opencage.geocoder import OpenCageGeocode
key ='07b1284701c84013bdf1b22d31e786a0'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
lat = results[0] ['geometry']['lat']
lng = results[0] ['geometry']['lng']
print(lat,lng)
print("Godebye!!")
