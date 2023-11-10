import validators

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