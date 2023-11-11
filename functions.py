import os
import validators
import requests
from bs4 import BeautifulSoup
import time
import json



# function used in choice 1
def add_tab(tabs):
    user_url = validate_url()
    title = add_title(tabs)
    tabs.append({title:user_url, 'nested_tabs':[]})

# function used in choice 2
def remove_tab(tabs):
    if len(tabs) > 0:
        index = -2
        while (index >= len(tabs) or index < -1):
            index = get_index(tabs)
        tabs.pop(index)
    else:
        print("nothing to remove, no tabs opened\n")


# function used in choice 3
def display(tabs):
    if len(tabs) == 0:
        print("nothing to display\n")
    else:
        index = -2
        while (index >= len(tabs) or index < -1):
            index = get_index(tabs)
        dct = tabs[index]
        print(get_html(dct[first_key(dct)]))
        if len(dct['nested_tabs']) > 0:
            for n_dct in dct['nested_tabs']:
                print(get_html(n_dct[first_key(n_dct)]))


# function used in choice 4
def display_titles(tabs):
    if len(tabs) == 0:
        print("no opened tabs")
    else:
        for index in range(len(tabs)):
            dct = tabs[index]
            print(first_key(dct))
            if len(dct['nested_tabs']) > 0:
                for n_dct in dct['nested_tabs']:
                    print(f'\t--{first_key(n_dct)}')


# function used in choice 5
def add_nested_tab(tabs):
    if len(tabs) == 0:
        print("no opened tabs")
    else:
        index = -2
        while (index >= len(tabs) or index < -1):
            index = get_index(tabs)
        title = add_title(tabs[index]['nested_tabs'])
        print("\n")
        url = validate_url()
        tabs[index]['nested_tabs'].append({title:url})


# function used in choice 6
def clear(tabs):
    tabs = []


# function used in choice 7
def save_tabs(tabs):
    path = ''
    while ('json' not in path):
        path = input("enter path: ")
        print("\n")
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(tabs, json_file, ensure_ascii=False, indent=4)


# function used for choice 8
def load_tabs(tabs):
    path = ''
    while ('.json' not in path):
        path = input("enter path: ")
        print("\n")
    try:
        with open(path) as f:
            data = json.load(f)
        tabs = tabs + list(data)
    except:
        print("no such path, choose choice another time")


# the following functions are helper functions


# used to get a title as input from user
def add_title(tabs):
    if (len(tabs) > 0):
        keys = []
        for dct in tabs:
            keys.append(first_key(dct))
        title = input("enter title: ")
        print('\n')
        while (title in keys):
            title = input("enter title: ")
            print('\n')
    else:
        title = input("enter title: ")
        print('\n')
    return title



# used to validate if the url provided by user is correct
def validate_url():
    user_url = input("please enter url: ")
    while (not validators.url(user_url)):
        print("\n")
        user_url = input("please enter url: ")
    return user_url


# gets index from the user
def get_index(tabs):
    index = 'not numeric'
    stop = False
    while (not stop):
        while ((not str(index).isnumeric()) and (index != '')):
            index = input("enter index: ")
            print("\n")
            try:
                index = int(index)
            except:
                pass
        if index == '':
            print("yes 1")
            return -1
        return index


# given a url it returns the HTML content
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


def print_menu():
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

# given that our dictionaries contain only 1 key, this function returns the key
def first_key(dct):
    keys = dct.keys()
    keys = list(keys)
    return keys[0]