import json
# with open("data_json","r") as file:
#      data = json.load(file)

with open("talabalar_json","r") as f:
     talaba = json.load(f)

print(type(talaba))
