import requests


def get_weather_forecast(place):
    url_template = 'https://wttr.in/{}'
    payload = {
        'lang': 'ru',
        'TnMq': '',
    }
    response = requests.get(url_template.format(place), params=payload)
    response.raise_for_status()
    return response.text


def main():
    places = ('Лондон', 'SVO', 'Череповец')
    for place in places:
        print(get_weather_forecast(place))


if __name__ == '__main__':
    main()
