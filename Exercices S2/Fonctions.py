from random import randint
from BDD import *
import csv



def random_emoji(lst):
    for i in lst: i['emoji'] = emoji[randint(0,11)]
    return lst

#apprenants = random_emoji(apprenants)


def icone_prenom(lst):
    for i in lst:
        if len(i['Prénom']) < 6: i['Icone'] = icone[0]
        elif 5 < len(i['Prénom']) < 8: i['Icone'] = icone[1]
        else: i['Icone'] = icone[2]
    return lst

apprenants = icone_prenom(apprenants)


def emoji_personnalisee(lst):
    for i in lst: i['emoji'] = emoji_animaux[i['Animal']]
    return lst

apprenants = emoji_personnalisee(apprenants)


def repartitionHF(lst):
    H, F = 0, 0
    for i in lst:
        if i['Sexe'] == 'M': H +=1
        else: F += 1
    return f'Parmis les apprenants, {H} sont des hommes et {F} sont des femmes.'

#repartitionHF(apprenants)


def personnes_inspirantes(lst):
    print('Entrer votre prénom :')
    prenom = input()
    pi = []
    status = True
    while status:
        status = False
        print("Entrez le nom d'une personne qui vous inspire :")
        temp = input()
        pi.append(temp)
        print("Y-a-t-il quelqu'un d'autre que vous trouvez inspirant ? Y/N")
        if input() == 'Y': status = True
    for i in lst:
        i['Personnes inspirantes'] = ''
        if i['Prénom'] == prenom:
            i['Personnes inspirantes'] = pi
            break
    return lst


#apprenants = personnes_inspirantes(apprenants)
#dictionnarylist_2_csv(apprenants)

def row_reader(key):
    with open('apprenants_bdd.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['Prénom'], row[key])

#row_reader('Personnes inspirantes')



import pandas as pd


df = pd.DataFrame(apprenants)
df.to_csv('apprenants.csv', sep = ';')

print(df)
