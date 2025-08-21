# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
noms = []

# ici il ermet de tourner en recuperant chaque nom pour obtenir jusqu'au 3 
# mais on peut encore faire mieux

nombre_per =  3
for i in range (nombre_per):
    

 list_personne = []
# ici on boucle sur l'inscription de la personne et en le faisant on boucle 
# en meme temps sur les la presentattion  de qhaque personne 
for i in nombre_per:
  nom =   noms.append(input("nom de la personne 1  " + str(i + 1) + ":"))
  list_personne.append(Personne(nom))

for person in list_personne:
    person.SePresenter() # l'erreur se trouvait ici  par ce que la fonction se presenter a deja un print 
    # et quand on l'ajoute encore un autre print  c'est la raison pour la quelle il affiche ça 
