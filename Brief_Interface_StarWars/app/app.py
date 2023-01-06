import streamlit as st
import requests


option = st.selectbox(
    'What category are you interested in?',
    ('', 'People', 'Films', 'Starships', 'Vehicles', 'Species', 'Planets'))

keyword = st.text_input('Would you like to specify your request?')

results = []
c = 1

if option:

    while True:
        page = requests.get(f"https://swapi.dev/api/{option.lower()}/?page={c}").json()
        results += page['results']
        if not page['next']: break
        c += 1

    selected = []
    category = 'title' if option == 'Films' else 'name'

    people = ['name','gender','birth_year']
    film = ['title','director','producer','release_date']
    starship = ['name','model','manufacturer','hyperdrive_rating','starship_class']
    vehicle = ['name','model','manufacturer','vehicle_class']
    species = ['name','language','classification','designation']
    planet = ['name','diameter','climate','gravity','terrain','population']

    option_to_list = {
        'People' : people,
        'Films' : film,
        'Starships' : starship,
        'Vehicles' : vehicle,
        'Species' : species,
        'Planets' : planet
    }

    for result in results:
        if keyword.lower() in result[category].lower():
            selected.append(result)

    st.write(f'#### {len(selected)} results')
    st.write('\n')

    for item in selected:
        st.write(f'### {item[option_to_list[option][0]]}')
        for element in option_to_list[option][1:]:
            name = element.capitalize().replace('_', ' ')
            st.write(f'- **{name}** : {item[element]}')
        st.write('\n')
