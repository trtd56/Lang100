import requests
from Q28 import Dic

def json_search(json_data):
    ret_dict = {}
    for k, v in json_data.items():
        if isinstance(v, list):
            for e in v:
                ret_dict.update(json_search(e))
        elif isinstance(v, dict):
            ret_dict.update(json_search(v))
        else:
            ret_dict[k] = v
    return ret_dict

if __name__=="__main__":
    url = "https://en.wikipedia.org/w/api.php"
    payload = {"action": "query",
               "titles": "File:{}".format(Dic[u"国旗画像"]),
               "prop": "imageinfo",
               "format": "json",
               "iiprop": "url"}
    json_data = requests.get(url, params=payload).json()
    print(json_data)
    print(json_search(json_data)["url"])
