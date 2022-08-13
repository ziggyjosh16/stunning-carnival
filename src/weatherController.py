from config import appid
import requests
appid = ""


def get_air_temp(user_ip):
    url1 = "http://ip-api.com/json/{}".format(
        user_ip) if user_ip else "http://ip-api.com/json"
    r = requests.get(url1).json()
    location = {
        "lat": r.lat,
        "lon": r.lon
    }
    url2 = "https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=minutely,hourly,daily,alerts&appid=95a77bc86522876229ff64adad24253e \
    ".format(location.lat, location.lon)
    r = requests.get(url1).json()

    w_data = {}
    return 0
