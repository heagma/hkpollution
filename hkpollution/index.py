
import os
import requests
import sys
from argparse import ArgumentParser

parser = ArgumentParser(description='Get the Air pollution in HK')
parser.add_argument("-d", "--district", help="The district to get the pollution for. Use it with '-' or oneword if the district has more than 1 word. Ex: tuen-mun")
args = parser.parse_args()

quality = {"good": 50, "Moderate": 100, "Sensitive": 150, "Unhealthy": 200, "Very unhealthy": 300, "Poisoning": 301}
siglas = {"pm25": "Particulate Matter 2.5", "co": "Carbon Monoxide", "no2": "Nitrogen Dioxide", "o3": "Ground-Level Ozone", "pm10": "Particular Matter 10", "p": "Pressure", "so2": "Sulfur Dioxide"}

def api_work():
    """Work with the api file and catch errors if does not exist, also
    define the url to get the data.

    Parameters: None
    Return: a request object
    """
    try:
        api_key_file = open(os.path.join(os.getcwd(), "hkpollution", "api_details.txt"))
    except FileNotFoundError as err:
        print(f"error: {err}")
        sys.exit(1)
    else:
        with api_key_file:
            api_key = api_key_file.readline()

    if not api_key:
        print("Error: no 'API KEY' provided")
        sys.exit(1)
    url = f"https://api.waqi.info/feed/hongkong/{'-'.join(args.district.split())}/?token={api_key}"
    res = requests.get(url)
    return res

api_work()


if api_work().status_code != 200:
    print(f"Error talking to weather provider: {res.status_code}")
    sys.exit(1)
else:
    data = api_work().json()


def indices():
    """ Get the most used index of the Air Quality
    Parameters: None
    Return: a List of indexes
    """
    print(f"******{data['data']['city']['name']:^4{4}}******")
    print("\n")
    aq = "Total Air Quality"
    all_index = []
    for k, v in quality.items():
        if data["data"]["aqi"] in range(v+1):
            print(f"{aq:{2}{2}} -> {data['data']['aqi']:{2}} --------> {k:{2}}" )
            break
    for j, g in data["data"]["iaqi"].items():
        if j in siglas:
            print(f"{siglas[j]:{2}{2}} :  {g['v']:{1}}")
            all_index.append((j,g))
    
    return all_index

indices()

#print("Details: ")
#print(data)