# from config import appid
appid = ""


def get_air_temp(user_ip):
    url1 = "http://ip-api.com/json/{}".format(user_ip)
    location = {}
    url2 = "https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude=minutely,hourly,daily,alerts&appid={}" \
        .format(location.lat, location.lon, appid)
    w_data = {}
    return 0
