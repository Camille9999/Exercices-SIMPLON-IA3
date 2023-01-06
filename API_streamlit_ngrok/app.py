import streamlit as st
import requests

drink = st.slider('% of the population having access to at least basic water services:',0,100,50, step=1)

icr = st.slider('Income composition of ressources',0.0,1.0,0.5,step=0.01)

hiv = st.number_input('Deaths per 1000 live births due to HIV/AIDS (0-4 years)',0.1,1000.0,1.0,step=0.1)

page = requests.get(f'https://024c-82-126-158-181.eu.ngrok.io/?drink={drink}&income={icr}&hiv={hiv}').json()
pred = page['prediction']

st.write(f'### Predicted life expectancy: {pred}')
