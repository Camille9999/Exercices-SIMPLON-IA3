import pandas as pd
import requests

df = pd.read_csv('akinator IA3 - Feuille 1.csv')
animals = [*set(df['Animal totem'].tolist())]

pictures_of_animals = {}

for animal in animals:
    url = f"https://pixabay.com/api/?key=30681142-ea26c481685397e592373e675&q={animal}&lang=fr"
    response_API = requests.get(url)
    data = response_API.json()
    pictures_of_animals[animal] = data["hits"][0]["largeImageURL"]

print(pictures_of_animals)
