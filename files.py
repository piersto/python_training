import json


f = open('C:\Users\Pierre\Desktop\new 12.json')
try:
    res = json.load(f)
except:
    pass


f.close()

print(res)
