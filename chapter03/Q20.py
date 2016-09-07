import json

f = open('jawiki-country.json')
lines = f.readlines()
f.close()

for l in lines:
    json_data = json.loads(l)
    if json_data["title"]=="イギリス":
        text = json_data["text"]

TEXT = text

if __name__=="__main__":
    print(text)


