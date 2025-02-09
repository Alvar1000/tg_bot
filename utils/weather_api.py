import requests

def get_current_temp(city):
    API_KEY = "5d17cfddc212ca44869ba673d30088f4"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={API_KEY}&q={city}&units=metric"

    try:
        response = requests.get(complete_url)
        data = response.json()

        if response.status_code != 200:
            return f"Ошибка: {data.get('message', 'Неизвестная ошибка')}"

        return data["main"]["temp"]

    except requests.exceptions.RequestException as e:
        return f"Ошибка соединения: {e}"