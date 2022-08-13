import requests


def get_air_temp(user_ip):
    url1 = "http://ip-api.com/json/{}".format(
        user_ip) if user_ip and user_ip not in ["0.0.0.0", "::1", "127.0.0.1"] else "http://ip-api.com/json"
    r = requests.get(url1).json()
    # print(r)
    location = {
        "lat": r['lat'],
        "lon": r['lon'],
        "city": r['city'],
        "region": r['region'],
        "countryCode": r['countryCode']
    }
    url2 = "https://api.openweathermap.org/data/2.5/weather?q={},{},{} \
        &appid=95a77bc86522876229ff64adad24253e&units=imperial".format(location['city'], location['region'], location['countryCode'])
    r2 = requests.get(url2).json()
    return r2.get('main', {}).get("temp", 0)
