import requests

def read_token():
    f = open("token.txt")
    return f.read()

ORIGIN = "https://graph.facebook.com/"
TOKEN = f"&access_token={read_token()}"

def search(location):
    QUERY = f"search?type=place&center={'56.151564, 10.201814'},distance=100&fields=about,name,fun_count,rating_count,category_list"
    URL = f"{ORIGIN}{QUERY}{TOKEN}"
    data_set = []
    return get_and_return(URL, data_set)
    
def get_and_return(url, data_set):
    r = requests.get(url).json()
    for place in r["data"]:
        data_set.append(place)
    if "next" in r["paging"]:
        get_and_return(r["paging"]["next"], data_set)
    return data_set


print(search("Aarhus"))
