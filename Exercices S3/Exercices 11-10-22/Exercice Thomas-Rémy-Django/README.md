# **Exercice Django, Rémy et Thomas**

Vous êtes data analyste pour SFS (Simplon Financial Services). Un collègue  a besoin de votre aide pour retrouver les méthodes inscrites dans un fichier main.py avec pour objectif d'analyser un dictionnaire d'entreprise.

## **Informations**

Le dictionnaire est structuré comme cela :
- `company_name` (*string*) le nom de l'entreprise
- `price` (*number*) le prix de l'action en €
- `company_partners` (*list*) les entreprises partenaires
- `stock` (*number*) quantité d'action disponible

&nbsp;

**Elements fournis** :
- Le dictionnaire des entreprises ``data_company.py``
- Un fichier ``main.py`` avec les méthodes inscrite


**Contraintes** :
- ``main.py`` : **Interdiction** de modifier les paramètres d'une méthodes
- ``data_company.py`` : **Interdiction** de modifier la liste à la main
- La bibliothèque **pandas n'est pas autorisé**
- **/!\ Les méthodes doivent être déclarées dans un autre fichier /!\\**

&nbsp;

---
&nbsp;
## **Exercices**

### **Exercice 1 :**
Créer la fonction ``filter_price`` qui affiche le nom des entreprises et le prix de leur action, pour les entreprises qui ont une action supérieur à 500€,
&nbsp;

Format attendu : ``Company name : [company_name], price : [price]``

&nbsp;

### **Exercice 2 :**
Créer la fonction ``find_partners`` qui retourne une liste classée par ordre alphabétique de toutes les ``company_partners`` qui sont présentes (sans doublons).

&nbsp;

### **Exercice 3 :**
Créez la fonction ``average_price`` qui retourne la valeur moyenne de toutes les actions.

&nbsp;

### **Exercice 4 :**
`company_partners` représente comment sont divisées les actions de chaque entreprise pour les partenaires.

*exemple*:
```
{
    'company_name': 'Nunc PC',
    'price': 102,
    'company_partners': ['Sibelius', 'Adobe', 'Chami'],
    'stock': 12
}
```
Dans ce cas :
- **Nunc PC** possède 50% des actions (**12** / 2 = **6**)
- **Sibelius, Adobe et Chami** se divisent équitablement les 50% restant (**6** / 3 = 2 actions par entreprise)

soit :
- **Nunc PC** : 6 actions
- **Sibelius** : 2 actions
- **Adobe** : 2 actions
- **Chami** : 2 actions



**Avec ces indications, créez la fonction ``companies_stock`` qui retourne le nombre d'actions que chaque ``company_partners`` possèdent.**
&nbsp;
&nbsp;


Format attendu : **dictionnaire**
```
{
    'company_name': [Nom de l'entreprise],
    'stock': [Nombre d'actions]
}
```


&nbsp;
&nbsp;
&nbsp;

(**SUPER QUESTION BONUS:** *déterminez la valeur de chaque ``company_partners`` grâce à la question du dessus et à la valeur de chaque action*)
