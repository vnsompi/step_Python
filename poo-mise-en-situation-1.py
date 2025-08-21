# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        if self.genre:
            print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
            print("Genre : Masculin")
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
            print()
        else:
            print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
            print("Genre : Feminin")
            if self.EstMajeur():
                print("Je suis majeure")
            else:
                print("Je suis mineure")
            print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25, True)  # voici là ou il a l'erreur 
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()


# selon moi on pourrait faire une fonction qui retoune deja 
#  en disant bonjour je m'appele vainquer j'ai 21 ans , je suis du gente masculin et je suis majeur 
# au lieu de faire un peu repeter le code 

# et en appelant la fonction sepresenter() il va voir si la condition est respecter pour soit afficher 
# celui du mineur ou majeur  