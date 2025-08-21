# 🔹 Projet 1 : Calculateur de notes

# 👉 Objectif : Créer un programme qui gère les notes des étudiants avec des fonctions.

# Consignes :

# Crée une fonction ajouter_note(liste, note) qui ajoute une note dans une liste.

# Crée une fonction moyenne_notes(liste) qui retourne la moyenne des notes.

# Crée une fonction note_max(liste) qui retourne la meilleure note.

# Dans le programme principal, demande à l’utilisateur d’entrer plusieurs notes, puis affiche la liste des notes, la moyenne et la meilleure note.


# fonction qui demande le nom 

# def Press():
#     print("Bienvenue dans ll'appli de note")
# Press()


# note_list = []

# def ajouter_notes():
   
#     note = input("entrez la note obtenue : ")
#     noteOOB = note_list.append(note)
#     print(noteOOB)
# print("la note est : ",note_list)
# ajouter_notes()
    

# def moyenne():
    
#     print(f"la note moyenne est {min(note_list)}")
# moyenne()

# def Maxnote():
#     print(f"la meilleure note est {max(note_list)}")
# Maxnote()


# # la solution 

# # -*- coding: utf-8 -*-

# def demander_nom():
#     """
#     Demande et retourne le nom de l'étudiant.
#     """
#     nom = input("Veuillez entrer le nom de l'étudiant : ")
#     return nom

# def ajouter_note(liste_notes, note):
#     """
#     Ajoute une note à la liste des notes.

#     Args:
#         liste_notes (list): La liste contenant les notes.
#         note (float): La note à ajouter.
#     """
#     # On s'assure que la note est un nombre avant de l'ajouter
#     try:
#         note_float = float(note)
#         if 0 <= note_float <= 20: # On peut supposer une échelle de 0 à 20
#             liste_notes.append(note_float)
#             print(f"Note {note_float} ajoutée.")
#         else:
#             print("Erreur : Veuillez entrer une note entre 0 et 20.")
#     except ValueError:
#         print("Erreur : Veuillez entrer une valeur numérique valide.")

# def moyenne_notes(liste_notes):
#     """
#     Calcule et retourne la moyenne des notes dans la liste.

#     Args:
#         liste_notes (list): La liste des notes.

#     Returns:
#         float: La moyenne des notes, ou 0 si la liste est vide.
#     """
#     if not liste_notes: # Vérifie si la liste est vide pour éviter une division par zéro
#         return 0
#     total = sum(liste_notes)
#     moyenne = total / len(liste_notes)
#     return moyenne

# def note_max(liste_notes):
#     """
#     Trouve et retourne la note la plus élevée dans la liste.

#     Args:
#         liste_notes (list): La liste des notes.

#     Returns:
#         float: La note maximale, ou None si la liste est vide.
#     """
#     if not liste_notes: # Vérifie si la liste est vide
#         return None
#     return max(liste_notes)

# # --- Programme Principal ---
# if __name__ == "__main__":
#     # Initialisation
#     notes_etudiant = []
#     nom_etudiant = demander_nom()

#     print("\n--- Saisie des notes ---")
#     print("Entrez les notes une par une. Tapez 'fin' lorsque vous avez terminé.")

#     # Boucle pour demander les notes à l'utilisateur
#     while True:
#         saisie = input("Entrez une note (ou 'fin' pour arrêter) : ")

#         if saisie.lower() == 'fin':
#             break # Sort de la boucle si l'utilisateur tape 'fin'
#         else:
#             ajouter_note(notes_etudiant, saisie)

#     # Affichage des résultats
#     print("\n--- Résultats pour l'étudiant : {} ---".format(nom_etudiant))

#     if notes_etudiant: # On vérifie qu'il y a au moins une note
#         # 1. Afficher la liste complète des notes
#         print(f"Liste des notes : {notes_etudiant}")

#         # 2. Calculer et afficher la moyenne
#         moyenne = moyenne_notes(notes_etudiant)
#         # On utilise :.2f pour formater la moyenne avec 2 décimales
#         print(f"Moyenne des notes : {moyenne:.2f}")

#         # 3. Trouver et afficher la meilleure note
#         meilleure_note = note_max(notes_etudiant)
#         print(f"Meilleure note : {meilleure_note}")
#     else:
#         print("Aucune note n'a été entrée.")

#     print("\n--- Fin du programme ---")



    # 2projet 

    # 🔹 Projet 2 : Convertisseur de devises

# 👉 Objectif : Écrire un programme qui convertit une somme d’argent entre dollars ($), euros (€) et francs CFA (FCFA) à l’aide de fonctions.

# Consignes :

# Crée une fonction usd_to_cfa(montant) qui convertit les dollars en CFA (1 USD = 600 CFA).

# Crée une fonction euro_to_cfa(montant) qui convertit les euros en CFA (1 EUR = 650 CFA).

# Crée une fonction cfa_to_usd(montant) et cfa_to_euro(montant) pour l’inverse.

# Dans le programme principal, demande à l’utilisateur de choisir la devise et le montant, puis affiche le résultat.


def BienVenue():
    print("vous etes le bienvenue dans cette appli")

    print("faites un choix: ")
    print("1. usd_to_cfa: ")
    print("2. euro_to_cfa: ")
    print("3. cfa_to_usd : ")

    choix = input("choississez la devise : ")
    montant = input("Entrez le montant :")

    if  choix == "1":
        return   usd_to_cfa()
    elif choix == "2":
        return   euro_to_cfa()
    elif choix == "3":
        return cfa_to_usd()
    
    else:
        print("Erreur de choix")


    def usd_to_cfa():
            print("voici le montant avec la devise choisit est : ",montant * 600)
    usd_to_cfa() 


    def  euro_to_cfa():
            print("voici le montant  avec la devise choisit est  : ",montant * 650)
    euro_to_cfa()

    def cfa_to_usd():
            print("voici le montant  avec la devise choisit est  : ",montant / 650)
    cfa_to_usd()

BienVenue()


# -*- coding: utf-8 -*-
# correction 

# --- Définition des Fonctions de Conversion ---

# Taux de change
TAUX_USD_CFA = 600
TAUX_EUR_CFA = 650

def usd_to_cfa(montant):
    """Convertit un montant de dollars (USD) en francs CFA (CFA)."""
    return montant * TAUX_USD_CFA

def euro_to_cfa(montant):
    """Convertit un montant d'euros (EUR) en francs CFA (CFA)."""
    return montant * TAUX_EUR_CFA

def cfa_to_usd(montant):
    """Convertit un montant de francs CFA (CFA) en dollars (USD)."""
    return montant / TAUX_USD_CFA

def cfa_to_euro(montant):
    """Convertit un montant de francs CFA (CFA) en euros (EUR)."""
    return montant / TAUX_EUR_CFA

# --- Programme Principal ---
def programme_principal():
    """
    Gère le menu, les entrées utilisateur et affiche le résultat de la conversion.
    """
    print("--- Bienvenue dans le convertisseur de devises ---")
    print("Choisissez une option de conversion :")
    print("1. Dollars (USD) vers Francs CFA (CFA)")
    print("2. Euros (EUR) vers Francs CFA (CFA)")
    print("3. Francs CFA (CFA) vers Dollars (USD)")
    print("4. Francs CFA (CFA) vers Euros (EUR)")

    # Demander le choix à l'utilisateur
    choix = input("Votre choix (1-4) : ")

    # Demander le montant et gérer les erreurs de saisie
    try:
        montant_str = input("Entrez le montant à convertir : ")
        montant_float = float(montant_str)
    except ValueError:
        print("Erreur : Veuillez entrer un montant numérique valide.")
        return # Arrête la fonction si l'entrée n'est pas un nombre

    # Effectuer la conversion en fonction du choix
    resultat = 0
    devise_depart = ""
    devise_arrivee = ""

    if choix == "1":
        resultat = usd_to_cfa(montant_float)
        devise_depart = "USD"
        devise_arrivee = "CFA"
    elif choix == "2":
        resultat = euro_to_cfa(montant_float)
        devise_depart = "EUR"
        devise_arrivee = "CFA"
    elif choix == "3":
        resultat = cfa_to_usd(montant_float)
        devise_depart = "CFA"
        devise_arrivee = "USD"
    elif choix == "4":
        resultat = cfa_to_euro(montant_float)
        devise_depart = "CFA"
        devise_arrivee = "EUR"
    else:
        print("Erreur : Choix invalide. Veuillez choisir une option de 1 à 4.")
        return # Arrête la fonction si le choix est invalide

    # Afficher le résultat formaté avec 2 décimales
    print("\n--- Résultat ---")
    print(f"{montant_float:.2f} {devise_depart} = {resultat:.2f} {devise_arrivee}")
    print("------------------")


# Lancer le programme
if __name__ == "__main__":
    programme_principal()
