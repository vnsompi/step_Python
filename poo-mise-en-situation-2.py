# POO EXERCICE DE MISE EN SITUATION 2
class Personne:
    def __init__(self, nom: str, age:int):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age   # crée une variable d'instance : age

        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 23)
personne1.SePresenter()

personne1 = Personne("Emilie", 34)
personne1.SePresenter()


# MON AVIS 

# la fonction isMajeur a une condition en lui mais n'est en mesure 
# de sorti un message une fois cette condition executer 
# il faut delocaliser  les output  puis cree une fonction 
# complet qui peut en meme temps sortir 
# et effectuer si il est majeur ou mineur et dans la fonction
#   se presenter on ne fera qu'appeler les deux soit IsMajeur()  soit IsMineur()
