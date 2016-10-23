# coding: utf-8

from Q30 import mapping_list

for data in mapping_list:
    if data["pos"] == "名詞" and data["pos1"] == "サ変接続":
        print data["surface"]

