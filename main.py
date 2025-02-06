# print("Hello World!")

#----------------------------------

#    un = 3
#    deux = 8

#    print(un + deux)
#    print(un - deux)
#    print(un * deux)
#    print(un / deux)
#    print(un % deux)

#----------------------------------

#    user = int(input("Entrer un nombre :"))

#    if user == 0:
#        print("null")
#    elif user < 0:
#        print("inferieur")
#    else:
#        print("superier")
    
#----------------------------------
'''
user = int(input("Entrer un nombre :"))

if user % 2 == 0:
    print("pair")
else:
    print("impaire")
'''

#----------------------------------

'''
user = int(input("Saisie ton age :"))

if user >= 18:
    print('majeur')
else:
    print('mineur')
'''

#----------------------------------

'''
user = str(input("Entree votre prenom : "))

if user == 'Alice' or user == 'Bob':
    print("Bienvenue V I P")
else:
    print("Bienvenue",' ' + user)
'''

#----------------------------------

'''
un = int(input("Entree un nombre : "))
oper = input("Entree une operation (+, -, /, *, %): ")
deux = int(input("Entree un deuxieme nombre : "))

result = 0

if oper == '+':
    result = int(un + deux)
elif oper == '-':
    result = int(un - deux)
elif oper == '/':
    result = int(un - deux)
elif oper == '*':
    result = int(un - deux)
elif oper == '%':
    result = int(un - deux)

print(un, oper, deux, '=', result )
'''

#----------------------------------

'''
list = ['Alice', 'Bob', 'Shirley']

print(list)
print(len(list))
print(list[0])
print(list[1])
print(list[2])
'''

#----------------------------------

'''
list = ['Shirley', 1, 9.99, True]

print(list)

list.append("Marouan")

print(list)
'''
#----------------------------------

'''
list = ["Voiture", "moto", "velo"]

print(list)

list[1] = 'scooter'

print(list)
'''

#----------------------------------

'''
list = ["Fraise", "Pomme", "Ananas", "Grenadine", "Kiwi"]

for fruit in list:
    print(fruit)
'''

#----------------------------------

'''
user = int(input("Entrer un nombre : "))

for i in range(0, user+1):
    print(i)
'''

#----------------------------------

'''
cara = "marouan"

for i in cara:
    print(i)
'''

#----------------------------------

'''
nom = ["Jean", "Stephane", "Hamid", "Christine", "Marie"]

for i in nom:
    if i == "Hamid":
        break
    print(i)
'''

#----------------------------------  

'''
nom = ["Jean", "Stephane", "Hamid", "Christine", "Marie"]

for i in nom:
    if i == "Hamid":
        continue
    print(i)
'''

#----------------------------------

'''
i = 8

while i <= 18:
    print(i)
    i += 1
'''
#----------------------------------

'''
i = 18

while i >= 0:
    print(i)
    i -= 1
'''
#----------------------------------

'''
gens = {
    'nom' : 'Marouan',
    'age' : 18,
    'ville' : 'Bruxelles'   
}

x = list(gens.values())
print(x)
'''
#----------------------------------

'''
fruits = {
    'pomme' : 6,
    'kiwi' : 1,
    'framboise' : 9
}

x = list(fruits.values())
print(x)
print("vous avez,", x[0] + x[1] + x[2], "fruits")
'''

#----------------------------------

'''
etu1 = {
    'nom' : 'Chris',
    'age' : 19,
    'moyenne' : 17.9
}

etu2 = {
    'classe' : 'segpa',
    'annee' : 2015
}

etudiants = etu1 | etu2

print(etudiants)
'''
#----------------------------------
'''
def cal(a, b):
    w =  a + b
    x =  a - b
    y =  a * b
    z =  a / b
    return w, x, y, z

i = cal(9, 7)
print(i)
'''
#----------------------------------

'''
def user():
    
    a = int(input("entree un premier nombre : "))
    ope = input("entree une operation (+, -, *, /, %): ")
    b = int(input("entree un second nombre : "))
    
    if ope == '+':
        print(a + b)
    elif ope == '-':
        print(a - b)
    elif ope == '*':
        print(a * b)
    elif ope == '/':
        print(a / b)
    elif ope == '%':
        print(a % b)

user()
'''
#----------------------------------

'''
def maj(x):
    print(x.capitalize())
    
maj('moto')
'''

#----------------------------------


# def mdp():
#     i = 0
    
#     input("Donner le mots de passe : ")
#     while i != "python":
#         i = print(input("veuillez donner le bon mots de passe : "))
        
# mdp()


#                                        EXERCICE LOGIQUE 
#------------EXO 1-----------------


# user = int(input("Entree un nombre : "))

# def tf(user):
#     return user % 2 == 0

# result = tf(user)
# print(result)


#------------EXO 2-----------------


# def fm(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fm(n-1)
       
# fm(5)

#------------EXO 4-----------------

# def palin(mot):
#     tom = mot[::-1]
#     if mot == tom:
#         print('True')
#     else:
#         print("False")

# palin("oko")

#------------EXO 5-----------------

# liste = [5, 2, 8, 1, 6]

# liste.sort()
# print(liste)

#------------EXO 6-----------------

# borne_inf = 1 
# borne_sup = 20

# def np(borne_inf, borne_sup):
#     premier = []
#     for w in range(borne_inf, borne_sup + 1):
#         if w < 2:
#             continue
#         x = True
#         for i in range(2, w):
#             if w % i == 0:
#                 x = False
#                 break
#         if x:
#             premier.append(w)
#     return premier

# print(np(borne_inf, borne_sup))

#------------EXO 7-----------------

# def carreParfait(borne_inf, borne_sup):
#     list = []
#     for i in range(borne_inf, borne_sup + 1):
#         if int(i**0.5) * int(i**0.5) == i:
#             list.append(i)
#     return list

# borne_inf = 1
# borne_sup = 30
# print(carreParfait(borne_inf, borne_sup))
   
#------------EXO 8-----------------
# liste1 = [2, 4, 6, 8]
# liste2 = [1, 3, 5, 7]

# liste1.extend(liste2)

# liste1.sort()
# print(liste1)
#------------EXO 9-----------------

# def rl():
#     liste = [10, 20, 30, 40, 50]
#     k = 3
    
#     rlist = liste[-k:] + liste[:-k]
#     print(rlist)
    
# rl()

#------------EXO 10-----------------

# def ana(chaine1, chaine2):
#     chaine1 = chaine1.lower()
#     chaine2 = chaine2.lower()
    
#     return sorted(chaine1) == sorted(chaine2)

# chaine1 = input("Ecrivee 1 mot : ")
# chaine2 = input("Ecrivee 1 mot : ")
# print(ana(chaine1, chaine2))

#------------EXO 11-----------------

# def ch(chaines):
#     result = chaines[0]

#     for i in range(len(result)):



# chaines = ["flower", "flour", "flight"]
# ch(chaines)
