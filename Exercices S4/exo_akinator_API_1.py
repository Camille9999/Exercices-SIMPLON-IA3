import pandas as pd
import requests


df = pd.read_csv('akinator IA3 - Feuille 1.csv')
usernames = df['github name'].tolist()

username_name = {}

id = "Camille9999"
token = "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"

for username in usernames:
    response_API = requests.get("https://api.github.com/users/"+username, auth=(id, token))
    data = response_API.json()
    username_name[username] = data['name']

print(username_name)
