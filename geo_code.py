import requests


def read_token():
    f = open("geocode.txt")
    return str(f.read()).split(",")

ORIGIN = "https://geocoder.api.here.com/6.2/geocode.json"
APP_ID = f"?app_id={read_token()[0]}"
APP_CODE = f"&app_code={read_token()[1]}"

def city_location(city):
    try:
        r = requests.get(f"{ORIGIN}{APP_ID}{APP_CODE}&searchtext={city}")
        coords = r.json()["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]
        return [coords["Latitude"], coords["Longitude"]] if coords else False
    except:
        return False