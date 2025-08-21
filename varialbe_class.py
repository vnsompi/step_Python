# -*- coding: utf-8 -*-

class Personne:
    """
    Représente une personne avec un nom et un âge.
    """
    # Ceci est une variable de classe, partagée par toutes les instances de Personne.
    espece_etre_vivant = "Humain (Mammifère Homo sapiens)"

    def __init__(self, nom: str = "", age: int = 0):
        """
        Constructeur de la classe Personne.
        S'exécute lors de la création d'un nouvel objet Personne.
        """
        self.nom = nom  # Crée une variable d'instance : nom
        self.age = age  # Crée une variable d'instance : age

        # Si aucun nom n'est fourni lors de la création, on le demande.
        if self.nom == "":
            self.demander_nom()
        
        print(f"--- Objet Personne '{self.nom}' créé. ---")

    def se_presenter(self):
        """
        Affiche les informations de la personne.
        """
        info_personne = f"Bonjour, je m'appelle {self.nom}"

        if self.age != 0:
            info_personne += f", j'ai {self.age} ans"
        
        print(info_personne)

        # On peut ajouter une condition pour vérifier si la personne est majeure.
        if self.age >= 18:
            print("Je suis majeur(e).")
        elif self.age > 0:
            print("Je suis mineur(e).")

    def demander_nom(self):
        """
        Demande à l'utilisateur d'entrer un nom pour la personne.
        """
        self.nom = input("Quel est le nom de la personne ? ")

# --- Utilisation de la classe Personne ---
if __name__ == "__main__":
    # Crée une première personne en fournissant les informations directement
    personne1 = Personne("Jean", 30)
    personne1.se_presenter()
    print(f"Espèce : {Personne.espece_etre_vivant}\n")

    # Crée une deuxième personne sans fournir de nom, le programme le demandera
    personne2 = Personne(age=16)
    personne2.se_presenter()
    print(f"Espèce : {Personne.espece_etre_vivant}\n")
