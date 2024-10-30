import requests


def show_weather_forecast(places):
    url_template = 'https://wttr.in/{}'
    payload = {
        'lang': 'ru',
        'TnMq': '',
    }
    for place in places:
        response = requests.get(url_template.format(place), params=payload)
        response.raise_for_status()
        print(response.text)


def main():
    places = ('Лондон', 'SVO', 'Череповец')
    show_weather_forecast(places)


if __name__ == '__main__':
    main()
