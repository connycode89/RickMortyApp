# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:38:47 2022

@author: Conor Donovan
"""

#%%
import requests
BASE_URL = 'https://rickandmortyapi.com/api/'

#%%
def get_request(url):
    resp = requests.get(url)
    data = resp.json()
    return data

def get_api_categories():
    cats = get_request(BASE_URL)
    return cats

#%%
def get_all_json_data(base_dict):
    dict2 = {key: get_request(base_dict[key]) for key in base_dict}
    print(dict2)

d = get_api_categories()
get_all_json_data(d)
