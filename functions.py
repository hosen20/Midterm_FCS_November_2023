import validators
import requests
from bs4 import BeautifulSoup
import time


def validateURL():
    user_url = input("please enter url: ")
    while (not validators.url(user_url)):
        print("\n")
        user_url = input("please enter url: ")
    return user_url

def add_tab(tabs):
    user_url = validateURL()
    title = input("please input title: ")
    print("\n")
    tabs.append({title:user_url})



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


