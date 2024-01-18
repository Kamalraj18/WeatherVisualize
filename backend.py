import requests


apikey = "e8dc2622dc22273cd345e0c642995fb7"

def get_data(place,forcast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={apikey}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_value = 8*forcast_days
    filtered_data = filtered_data[:nr_value]
    return filtered_data


if __name__ == "__main__":
    get_data(place="Tokyo",forcast_days=3)

