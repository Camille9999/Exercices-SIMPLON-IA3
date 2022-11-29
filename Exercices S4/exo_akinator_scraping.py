import pandas as pd
from bs4 import BeautifulSoup
import requests


df = pd.read_csv('akinator IA3 - Feuille 1.csv')
films = df['Film préféré'].tolist()
film_year = {}

for film in films:
    page = requests.get(f"https://www.imdb.com/find?q={film}")
    soup = BeautifulSoup(page.content, 'html.parser')
    film_year[film] = int(soup.find(class_="ipc-metadata-list-summary-item__li").get_text())

print(film_year)
