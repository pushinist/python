import requests


req = requests.get('https://httpbin.org/get')
print(f"Код: {req.status_code}")
print(f"Заголовки: {req.headers}")
print(f"Текст: {req.text}")

req = requests.post('https://httpbin.org/post')
print(f"Код: {req.status_code}")
print(f"Заголовки: {req.headers}")
print(f"Текст: {req.text}")

req = requests.options('https://httpbin.org/post')
print(f"Код: {req.status_code}")
print(f"Заголовки: {req.headers}")
print(f"Текст: {req.text}")
print(f"Разрешённые заголовки: {req.headers['Allow']}")
