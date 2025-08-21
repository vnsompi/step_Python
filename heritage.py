
class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur", pseudo, "/ Points de vie :", health, "/ Attaque :", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.attack)


# Exemple d'utilisation :
player = Player("Graven", 20, 2)
player.damage(5)
print(player.get_pseudo(), "a maintenant", player.get_health(), "points de vie.")


class Warrior:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.armor = 3
        print("Bienvenue au joueur", pseudo, "/ Points de vie :", health, "/ Attaque :", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):


        return self.attack

    def damage(self, damage):
        self.health -= damage


    def attack_player(self, target_player):
        target_player.damage(self.attack)


# Exemple d'utilisation :
player = Player("Graven", 20, 2)
player.damage(5)
print(player.get_pseudo(), "a maintenant", player.get_health(), "points de vie.")





# polymorphisme

class Animal:
    def Se_deplacer(self):
        pass

class Chien(Animal):
    def Se_deplacer(self):
        print("courir")
      
class Dauphin(Animal):
    def Se_deplacer(self):
        print("nager")
      
class Aigle(Animal):
    def Se_deplacer(self):
        print("voltiger")

     
c = Chien()
c.Se_deplacer()


class Animal:
    def se_deplacer(self):
        print("Je me déplace d'une certaine manière.")


class Chien(Animal):
    def se_deplacer(self):
        print("Je marche et je cours.")


class Dauphin(Animal):
    def se_deplacer(self):
        print("Je nage dans l'eau.")


class Aigle(Animal):
    def se_deplacer(self):
        print("Je vole dans le ciel.")


class A:
    def comment_se_deplace(self, a: Animal):
        a.se_deplacer()


# Exemple d'utilisation
obj = A()
obj.comment_se_deplace(Animal())
obj.comment_se_deplace(Chien())
obj.comment_se_deplace(Dauphin())
obj.comment_se_deplace(Aigle())
