import requests
city = input("Введите город: ")
url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

weather_data = requests.get(url).json()
temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
wind_speed = round(weather_data['wind']['speed'])
humidity = round(weather_data['main']['humidity'])
weather_description = weather_data['weather'][0]['description']
print('Сейчас в городе', city, '-', weather_description.capitalize())
print('В данный момент температура составляет',str(temperature), '°C')
print('Ощущается как', str(temperature_feels), '°C')
print('Ветер', str(wind_speed), 'м/с')
print('Влажность', str(humidity), '%')

