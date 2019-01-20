import requests
from auth import read_token
from geo_code import city_location

#show the places and choose to select events

ORIGIN = "https://graph.facebook.com/"
TOKEN = f"&access_token={read_token()}"
LIMIT = 50

def search(city):
    LOCATION = city_location(city)
    QUERY = f"search?type=place&center={LOCATION[0]},{LOCATION[1]},distance=1000&fields=about,name,fun_count,rating_count,category_list&limit={LIMIT}"
    URL = f"{ORIGIN}{QUERY}{TOKEN}"
    return get_and_return(URL, [])
    
def get_and_return(url, data_set):
    r = requests.get(url).json()
    print(r)
    for place in r["data"]:
        data_set.append(place)
    # if "next" in r["paging"]:
    #     get_and_return(r["paging"]["next"], data_set)
    return data_set


print(search("Aarhus"))
