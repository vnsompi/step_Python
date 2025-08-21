# les variables 


age  = 20

sentences = " my name is vainqueur"

sara, dio, mike =  12,34,45
print(sara)
print(dio)
print(mike)

# others kind 
name, age = "avi", 22

print("my name is : ",name)
print("and i'm : ",age)

# arithmetique operators 

sim1 = 34
sim2 = 12

print(" the addition of these numbers is :",sim1 + sim2)
print( "The sum is:",sim1 * sim2)
print( "the rest  of the divide is :",sim1 / sim2)
# thi is module
print("the remaining is :",sim1 % sim2)


# strings 
sent1 = "today is a beautifull day"
print(sent1)

first_name = "Nsompi"
last_name = "jainn"
print(first_name + " "+  last_name )

sen = "avi was playing "
print("this is  the le,gth 's word match : ", sen[0:3])


# placeholders in sring

sentence = " %s %s was the president of the United state"

print(sentence % ("barack", "Obama"))


# %s is for string and %d is for integer 
sentences = "%s is %d years old "
print(sentences % ('avi', 23))

# f string  means format string 

n ="avi"
print(f"hello",{n})


# EXECISE 
a = 15
b = 30 
sum = a + b 
ret = sum /2

print(f"the answers is : ", {sum}  ) 
print(f"the resulte  is : ", {ret}  ) 

# 2  Initialize two variables and use arithmetic operators to add, 
# subtract, multiply, divide, and find the remainder.

numb1 = 40
numb2 = 4

print(numb1 + numb2)
print(numb1 - numb2)
print(numb1 * numb2)
print(numb1 / numb2)
print(numb1 % numb2)


# 3  Create a variable called name and store your name in it as a string.

blame = "vainqueur" 
print(blame)

# 4  Create three variables in one line and assign each one a different food item.
usa,drc,france = "pizza", "charwama", "pasta"
print(usa)
print(drc)
print(france)

# 5. Print out "Hello" ten times using arithmetic operators.
print("hello " * 10 )

# 6. Set your name and age variables in one line with multiple assignment

nale, aged = "vainqueur", '12'
print(nale + " " +aged)

# 7.  Create two strings and then create a third variable combining 
# both of the two original strings.

pen = 'black'
pencil = "white"
combinPen = pen + " " + pencil
print(combinPen)

# 8. Create a string and print the fourth letter of the word.
sa = "beautifull"
print(f"This is the fouth letters", {sa[4]})

# 9. Create a string and print the letters from index 0 to 5.
print(sa[0:5])

# 10.  Create a variable and print all the letters from the first index until the end.
print(sa[1:])


# introduction to list 

shopping = ["apples","oranges", "bananas", "cheese" ]
# index 0 or zero 
print(shopping[0])
print(shopping[1])
print(shopping[2])
print(shopping[3])

# updete 
shopping.append("juice")
# :change  data

shopping[1] = "Ccersie"
# delete 
del shopping[2]

print(shopping)

shopping_list2 = ['bread', 'jam', 'butter']
print(shopping_list2 + shopping)

print(shopping * 2)

List_num = [1,2,3,4,5]
# show the highest  number
print(max(List_num))

# show the lowest  number 
print(min(List_num))

# dictionary in python 

student  = {
    'bob': 12,
    "erich": 23,
    "rachel": 45
}

print(student)

student["bob"] = 15
print(student)

del student['erich']
print(student)

print(len(student))

# introduction to tuples 

# tuples are imutable 
tup= ("orange", "apples", "bananas")
# tuples can't be change anymore 
# dans le type tuple il n'y pas de rang 0
tup[0]  
print(tup)

# EXECISE 
# 1. Create a list of names and print the second item.

foo = ["orange", "mangoes", "juice"]
print(foo[2])

# 2.Create a list of sports and then replace the second item with another sport.
sport = ['footer', "soccer", 'player']
sport[2] = "manager"
print(sport)

# 3. Create a list containing numbers and delete the fifth number from the array.
numbers = [23,45,89,2,24,12]
del numbers[5]
print(numbers)

# 4. Create two lists of numbers and merge them.
l1 = [2,4,6,8]
l2 = [3,4,6,8]
l3 = l1 + l2
print(l3)

# 5. Create a list of numbers and find the length, minimum, and maximum.
print("the length of this array is :",len(l3))
print("the highest value of this array is : ",max(l3))
print("the lowest value is : ", min(l3))

# 6. Create a dictionary of students and scores and print out a student’s score.
school = {
    "elie": 31,
    "moldavie":56,
    "julie":43,
    "Sarah": 23
}
print(school)

# 7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
auto = {
    "erick": 45,
    "soul": 23,
    "emile":12
}
auto.pop("emile")
print(f" the value ifthe remover is :", auto)

# 8. Create a dictionary of names and ages and then print out all the keys and values
noun = {
    "vainqueur": "architecture",
    "emile": "singer",
     "Josua": "developper"
}
print(noun)
# 9. Create a tuple of your favorite movies
tupeue = {"person of interest", "24h chrono", "Shooter"}
print(tupeue)

# 10. Create a tuple and print all the items from the first to third index.
tup = [1,3,4,5,6,56]
print(tup[1:4])

# correstion 
data = {"Rachel": 17, "Rahul": 61, "Anna": 15}
print(data.keys)
print(data.values)
# **************************************************************************************************************
# condition statement 

if 5 > 3 :
    print("food")
# this condition is true 

# when thee condition is false 
if 5 < 3 :
    print("food")
else:
    print("glass")

# condition with + > < == !=

if 5 == 3:  
    print("hello")
# we use this to compare values 

age = 16
if age <= 15:
    print("you're younger")
elif age ==16:
    print("you are 16 ")
elif age ==17:
    print("you are 17 ")
else:
    print("you are oldeer than 16")



age = 13
if age <13:
    print("you are a child")
elif age >= 13 and age <18:
    print("your are a teeneger")
else:
    print('you are an adult')

# other kind og condition 
if 5 > 3 or 2 < 1 :
    print("hello")


# for loop  repeat things 

list1 = ["apples", "banans", "orange"]
tup1 = (2,4,6)

for i in list1:
    print(i)

for i in tup1:
    print(tup1)

# the 2 is the incommet  factor 
# the 2 means that we will iterate only between pairs numbers 
for i in range(0, 20, 2):
        print(i)

#the first 5 mean that the iteration will start to this number 
for i in range(5, 50, 5):
        print(i)

for i in range(0, 5):
     for j in range(0, 3):
          print(i * j)
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# while loop 
# keeps executed as long the condition is true 
# use break in while loops 
# continue will skip the value on which the iteartion was stopped 

c = 0 
print("this ")
while c < 5:
     c = c + 1
     if c == 4:
          print("breath")
          pass
     print(c)


# Try and Except 
# how to use it 

try:
     if name > 3:
          print("goo")
except:
     print("An error was detected in your code ")


# function in python 
#  with the def( ) keyword 
def hello_word():
     print("holly")

hello_word()

def greeting(name):
     print("hi " + name + " !")

greeting("vainqueur")


def add(numb1, numb2):
     return numb1 + numb2


def mul(numb1, numb2):
     return numb1 * numb2

print(mul(add(1, 3), add(4, 8)))

# built_in  pyrhon function 
print(abs(-23))

# boolean function 
print(bool(0))

print(dir('hello'))
# this function show all the function request 

print(help("hello".upper))

sent = "print('girl')"
eval(sent)
eval(sent)
# girl 
# eval going to print  the contenu of variable called sent 
# it"s will print all this out  

print("hello " + str(100))
# with this methode we can concatinate string with integer
print(int("123") + 345)
print(float("123"))
print(float("123") + 0.23)

# EXERCISE 
print("***************************************************************")
def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

# Exemple
print(calculate_factorial(5))  # Résultat attendu : 120

print("***************************************************************")

def calculate_factorial(number):
    if number == 0 or number == 1:  # Cas de base
        return 1
    else:
        return number * calculate_factorial(number - 1)

# Exemple
print(calculate_factorial(5))  # Résultat attendu : 120

print("***************************************************************")
def calculate_add(number):
    factorial = 2
    for i in range(1, number + 1):
        factorial += i
    return factorial
print(calculate_add(5)) 


def somm(n):
     b = 3
    #  j'itère maintenant 
     for i in range(1, n -1 ):
      b -= i
      return b 
print(somm(7))


# OPP Classes and Objects 

class Person:
    def __init__(self,name,age): 
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
        
p1 = Person("bob", 22)
print(p1.getAge())
print(p1.getName())

# class inherance 


























 
