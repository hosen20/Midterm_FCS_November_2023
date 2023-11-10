import os
import validators
import requests
from bs4 import BeautifulSoup
import time
import json


def validateURL():
    user_url = input("please enter url: ")
    while (not validators.url(user_url)):
        print("\n")
        user_url = input("please enter url: ")
    return user_url


def get_index(tabs):
    index = eval(input("enter index: "))
    print("\n")
    while (index >= len(tabs) or index < 0):
        index = eval(input("enter index: "))
        print("\n")
    return index


def add_tab(tabs):
    user_url = validateURL()
    title = input("please input title: ")
    print("\n")
    tabs.append({title:user_url, 'nested_tabs':[]})


def get_html(url):
    headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    error = True
    ct = 0
    while(error and ct < 3):
        ct = ct + 1
        time.sleep(3)
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                error = False
                # Parse the HTML content of the page using BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")
                return soup
        except:
            error = True
    return "error"


def printMenu():
    print('''
    1. Open Tab
    2. Close Tab
    3. Switch Tab
    4. Display All Tabs
    5. Open Nested Tab
    6. Clear All Tabs
    7. Save Tabs
    8. Import Tabs
    9. Exit
    ''')


def add_nested_tab(tabs):
    index = get_index(tabs)
    title = input("enter title: ")
    print("\n")
    url = validateURL()
    tabs[index]['nested_tabs'].append({title:url})


def remove_tab(tabs):
    index = get_index(tabs)
    tabs.pop(index)


def display(tabs):
    index = get_index(tabs)
    dct = tabs[index]
    print(get_html(dct[first_key(dct)]))
    if len(dct['nested_tabs']) > 0:
        for n_dct in dct['nested_tabs']:
            print(get_html(n_dct[first_key(n_dct)]))


def first_key(dct):
    keys = dct.keys()
    keys = list(keys)
    return keys[0]


def clear(tabs):
    tabs = []


def saveTabs(tabs):
    path = input("please enter file name")
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(tabs, json_file, ensure_ascii=False, indent=4)


def loadTabs():
    path = input("enter path: ")
    print("\n")
    with open(path) as f:
        data = json.load(f)
    return data


def display_titles(tabs):
    index = get_index(tabs)
    dct = tabs[index]
    print(first_key(dct))
    if len(dct['nested_tabs']) > 0:
        for n_dct in dct['nested_tabs']:
            print(f'\t--{first_key(n_dct)}')


