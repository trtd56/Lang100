# coding: utf-8

from Q30 import mapping_list

for data in mapping_list:
    if data["pos"] == "動詞":
        print data["surface"]
