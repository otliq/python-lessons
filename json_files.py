import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# json_data = json.dumps(data)

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)

with open("data_json","w") as file:
     json.dump(data,file)

with open("talabalar_json","w") as f:
    json.dump(talaba_json,f)
