# with JONATHAN
# POO PROGRAMMATION ORIENTED OBJECT
# class 
# 

# recettes des omelette 
# la programmation imperative

# l'objet eeuf peut avoir  la taille , peut etre bio?,  peut avoir des action par ex  casser un oeuf



# def afficher_information(nom, age):
#     print(f"la personne s'appele {nom}, et son age est {age}")

# def demander_nom():
#     nom = input("Quelle est votre nom ? ")
#     return nom 

# def demander_age():
#     age = input("Quelle est votre age ?  ")
#     return  age

# nom1  = "jean"
# age1 = 23

# nom2  = "Paul"
# age2 = 43

# afficher_information(nom1, age1)
# afficher_information(nom2, age2)

# nom3 = demander_nom()
# age3 = demander_nom()

# afficher_information(nom3, age3)


# impleter en programmation orienté objet 

# Person (entite -- class)
# donnés
    # age 
    # nom
# actions
    # se presenter
    # Demander_nom (input)


# DEFINITION
class Person:
    def __init__(self, nom):
         self.nom = nom  #  creation d'une variable de l'instance 
         print("constructeur de : ",nom)

    def SePresenter(self):
        print("Bonjour je m'appelle  " + self.nom)

    # def autreFonctio(self):
    #     print(f"nom:{self.nom}")

# UTILISATION
person1 = Person("jean")   # je cree une instace de parsonne
person1.SePresenter()


# person2 = Person("BOI")   # je cree une instace de parsonne
# person3 = Person("E.F")   # je cree une instace de parsonne

# Person.SePresenter(person1)
# person2 = Person("Paul")   # je cree une deuxième  instace de parsonne
# person1.autreFonctio()


# Exercice




class Personne:
    def __init__(self,nom1, age1):

       self.nom1 = nom1
       self.age1 = age1

    def SePresenter(self):
        print(f"bonjour je m'apelle {self.nom1} et j'ai {self.age1} ans ")

    def IsMajeur(self):
        if self.age1  >= 16 :
            print(f"{self.nom1} est : Majeur par ce qu'il a {self.age1} ans  ")

        elif self.age1  <= 16 :
            print(f"{self.nom1} est : mineur  par  ce qu'il a {self.age1} ans ")
       
            
# creation de l'instance de la class 
pon1 = Personne("jean", 43)
pon2 = Personne("Elvis", 13)


# utilisation 
pon1.IsMajeur()
pon2.IsMajeur()
# homme = Personne.SePresenter(pon1)
# homme2 = Personne.IsMajeur(pon2)

       
# EXERCISE

class Student:
    def __init__(self, nom,age):

        self.nom =nom
        self.age = age

    def Sexprimer(self):
          
        self.nom =  input('quelle est votre nom !: ')
        self.age =  input('quelle est votre age !: ')

        if self.nom == "" and self.age == "":
                print("je n'est aucune information a donné")

        elif self.age == "" or self.age == 0:
                print(f"je m'appele: {self.nom}")

        else:
                print(f"JE SUIS {self.nom} et J'AI {self.age} ans ")


# creation de l'instance de Student 

bro = Student("eko", 23)
Student.Sexprimer(bro)




# PARTIES 3

# les varizaable de class




