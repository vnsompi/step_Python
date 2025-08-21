👉 “A course in which I learn everything about the structure of Python.”

notion sur le POO en python un concepte très important 

class Student:
    def __init__(self, name):
        self.name = name

    def Sexprimer(self):
        print(f"Bonjour, je suis {self.name} !")

# ❌ Mauvaise façon (manque 'self')
# Student.Sexprimer()

# ✅ Bonne façon
bro = Student("Djess")
bro.Sexprimer()


<!-- on peut aussi definir le type depuis la fonction d'initiation  -->

class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom  # crée une variable d'instance : nom
        self.age = age
        print("Constructeur personne " + nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        if self.age == 0:
            print("Bonjour, je m'appelle " + self.nom)
        else:
            print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18


<!-- autre cas  -->

pour eviter de dupliquer les fonctionns on cree une variable qui va stocker la valeur de si le champs de nom ou age dans me cas si il manquait 

et une fois cette fonction dans la condition  est reempli  elle sera appelé

class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom  # crée une variable d'instance : nom
        self.age = age
        print("Constructeur personne " + nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        info_personne = "Bonjour, je m'appelle " + self.nom
        if self.age == 0:
            print(info_personne)
        else:
            print(info_personne + ", j'ai " + str(self.age) + " ans")
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18





<!-- on peut aussi appele une fonction indiquant une condition bienpdeterminer  de la sorte  -->
<!-- if self.IsMajeur()  voici comment l'appelé -->

class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom  # crée une variable d'instance : nom
        self.age = age
        print("Constructeur personne " + nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        info_personne = "Bonjour, je m'appelle " + self.nom
        if self.age != 0:
            info_personne += ", j'ai " + str(self.age) + " ans"

        print(info_personne)

        if self.age != 0:
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18




        <!-- mise en situation 1 completer et simplifier  -->


class Personne:
    def __init__(self, nom: str = "", age: int = 0, genre: bool = False):
        self.nom = nom
        self.age = age
        self.genre = genre

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        
        if self.genre:
            genre_str = "Masculin"
        else:
            genre_str = "Feminin"
        print(f"Genre : {genre_str}")
        
        e_optionnel = ""
        if self.genre == False:
            e_optionnel = "e"
        
        if self.EstMajeur():
            print("Je suis majeur" + e_optionnel)
        else:
            print("Je suis mineur" + e_optionnel)

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25, True)
personne1.SePresenter()



<!--  encore simplifier  -->
def SePresenter(self):
    # Bonjour, je m'appelle Jean, j'ai 30 ans
    # Je suis majeur
    print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")

    genre_str = "Masculin" if self.genre else "Feminin"
    print(f"Genre : {genre_str}")

    e_optionnel = "" if self.genre else "e"
    
    if self.EstMajeur():
        print("Je suis majeur" + e_optionnel)
    else:
        print("Je suis mineur" + e_optionnel)
        
    print()

def EstMajeur(self):
    return self.age >= 18

personne1 = Personne("Jean", 25, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()