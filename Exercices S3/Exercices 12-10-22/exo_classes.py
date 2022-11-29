############################################################

#Vous etes en alternance chez @construitstapiscine, et vous avez récupéré le dossier de votre collegue
#Vous avez récupéré le dossier de votre collegue

############################################################

# Partie 1 : Debugage

# Une partie du document a pris le café et maintenant le code est bugé
# Debugez le code afin que celui ci affiche le volume et la surface de la piscine


class Piscine:
    def __init__(self, longueur, largeur, hauteur):
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur

    def calcul_volume(self):
        volume = self.longueur * self.largeur * self.hauteur
        return volume

    def calcul_surface(self):
        surface = self.longueur * self.largeur + 2 * self.hauteur * (self.longueur + self.largeur)
        return surface

    def resultat(self):
        return f"Le volume de la piscine est de {self.calcul_volume()}m3 et la surface est de {self.calcul_surface()}m2"

########################################

# Cette partie n'est pas bugée, ne pas y toucher

p1 = Piscine(10,5,7)
print(p1.resultat())

# Resultat attendu : "Le volume de la piscine est de 350 m3 et la surface est de 260 m2"

######################################

# Partie 2 : Arguments

# Une nouvelle piscine doit etre construite

# Vous devez faire en sorte que ce code retourne la valeur suivante : "Le volume de la piscine est de 27 m3 et la surface est de 51 m2"

# Cependant !
# vous ne devez pas rajouter de lignes de code
# Vous ne devez pas modifier l'ordre des arguments dans l'appel de "Piscine"
# Vous ne devez pas modifier leur valeurs numeriques

##############

p2 = Piscine(hauteur=1, longueur=9, largeur=3)
print(p2.resultat())

#############

# BONUS :

# Instruction : Codez la méthode "whaaat" de la class "Fonction" afin que celle ci retourne les resultats "#"

class Fonction:
    def whaaat(self, a, b, c=1):
        return a / b + c
