
import json

# with open("students.json","r") as json_file:
#      data = json.load(json_file)

# for item in data['student']:
    # print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")

# Faylni Pythonda oching va konsolga maqolaning sarlavhasi (title) va qisqa matnini (extract) chiqaring:

with open("api-result.json") as file:
    data = json.load(file)

print(data['query']['pages']['13801']['title'])
print(data['query']['pages']['13801']['extract'])