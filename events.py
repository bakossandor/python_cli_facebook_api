import requests

def read_token():
    f = open("token.txt")
    return f.read()


URL = "https://graph.facebook.com/"
QUERY="me"
FIELDS = "?fields=id,name"
TOKEN = f"&access_token={read_token()}"

r = requests.get(f"{URL}{QUERY}{FIELDS}{TOKEN}")
print(str(r.text))
