import json
import requests #biblioteca para fazer requisições HTTP

# 2
class URLResError(Exception):
    
    def __init__(self, url, code) -> None:
        self.__url = url
        self.__code = code
    
    def __str__(self) -> str:
        return f"URLResError {self.__url} {self.__code}"

# 1 
def computeWinRate(data):
    wrs = dict()
    for user in data:
        try:
            uname = user["full_name"]
            wr = user["victories"]/user["plays"]
            wrs[uname] = "{:.2f}".format(wr)
        except TypeError as te:
            print(f"TypeError {te}")
        except ZeroDivisionError as ze:
            print(f"{ze} at user {uname}")
            wrs[uname] = "NaN";
        except KeyError as ke:
            print(f"KeyError: {ke} missing at {user}")
    return wrs

# retorna um JSON com os dados dos usuários
url = "https://raw.githubusercontent.com/grellert/jsonbin/master/players.json"

# 2
try:
    res = requests.get(url)
    sc = res.status_code
    if sc != 200:
        raise URLResError(url, sc)
    else:
        usersData = json.loads(res.content)
except json.JSONDecodeError as je:
    print(je)

    
print(computeWinRate(usersData))

    