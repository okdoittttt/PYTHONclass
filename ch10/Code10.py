import json

custom = {
    'id':12345,
    'name':'son',
    'history':[{'date':'2022-06-02'},
               {'date':'2022-06-06'}]
}

jsonString = json.dumps(custom, indent=4)

print(jsonString)
print(type(jsonString))