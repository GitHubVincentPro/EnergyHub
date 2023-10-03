import requests

def get_forecast():
response = requests.get("http://localhost:5000/forecast")
return response.json()