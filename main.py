import random

import matplotlib.pyplot as plt

langas, grafikas = plt.subplots()

# x = [1,2,3]
# y = [2,3,4]
# fig, ax = plt.subplots()
# ax.plot(x,y)
# plt.show()
# A) Duotas sąrašas x=[1,2,3,4,5,6,7,8,9]
# Viename lange, skirtinguose grafikuose atvaizduokite x
# 2, x ⋅ 3, x ⋅ a, čia a - įvedamas vartotojo.
# Panaudokite skirtingas spalvas, linijų tipus.

# x = [1,2,3,4,5,6,7,8,9]
# a = float(input("Įveskite skaičių a: "))
#
# y1 = [i**2 for i in x]
# y2 = [i*3 for i in x]
# y3 = [i*a for i in x]
#
# plt.plot(x, y1, color='blue', linestyle='-', marker='o', label='$x^2$')
# plt.plot(x, y2, color='red', linestyle='--', marker='s', label='x * 3')
# plt.plot(x, y3, color='green', linestyle='-.', marker='^', label=f'x * {a}')
#
#
# plt.show()

# Duoti sąrašai x = [1,2,3,4,5], y1=[2,2,0,0,2], y2 = [4,3,2,1,-1], y3 =
# [2,4,9,16,25], y4 = [-1,1,-1,1,-1]
# Atvaizduokite viename lange, skirtinguose grafikuose x~y1, x~y2,
# x~y3, x~y4 grafikus. Pirmasis grafikas - linijinis, antrasis - taškinis,
# trečiasis - linija su duomenų taškais, ketvirtasis - brūkšninis.
# Spalvos visų turi būti skirtingos. Grafikai, ašys turi turėti pavadinimus

# x = [1,2,3,4,5]
# y1 = [2,2,0,0,2]
# y2 = [4,3,2,1,-1]
# y3 = [2,4,9,16,25]
# y4 = [-1,1,-1,1,-1]
#
# plt.plot(x, y1, color='blue', linestyle='-', label='y1 (linijinis)')
# plt.scatter(x,y2, color='red', label='2 (taškinis)')
# plt.plot(x, y3, color='green', linestyle='--', marker='o', label='y3 (linija + taškai)')
# plt.bar(x, y4, color='yellow', label='y4 (brūkšninis)')
#
# plt.title("Skirtingi grafikai")
#
# plt.xlabel("x ašis")
# plt.ylabel("y ašis")
#
# plt.legend()
# plt.show()

# Sugeneruoti sąrašą x, turintį 101 elementą (nuo 0 iki 100).
# Sukurti antrą sąrašą, kuriame būtų skaičiai, pakelti kvadratu, iš pirmojo sąrašo (x2)
# Sukurti trečiąjį sąrašą, kuriame skaičiai būtų pakelti kvadratu ir
# padauginti iš atsitiktinai sugeneruoto skaičiaus (x2 ⋅ a).
# Sugeneruoti 100-to elementų ilgio sąrašą iš atsitiktinių skaičių.
# Visus šiuos sąrašus atvaizduoti grafike. Grafikas turi turėti
# pavadinimą, pavadintos ašys, pakeisti šriftų dydžiai.

x = list(range(101))
x2 = [i**2 for i in x]
a = random.randint(1,5)
x3 = [i*a for i in x2]

random_values = [random.randint(1,500) for i in range(100)]
# print(random_values)

plt.plot(x, x2, label='$x^2$', color='blue', linestyle='-')
plt.plot(x, x3, label=f'$x^2$ * a (a={a:.2f})', color='green', linestyle='--')
plt.plot(x[:100], random_values, label='Atsitiktiniai skaičiai', color='red', linestyle=':')

plt.title("Skirtingų skaičių sąrašų palyginimas", fontsize=16)
plt.xlabel("x reikšmės", fontsize=14)
plt.ylabel("y reikšmės", fontsize=12)

plt.legend(fontsize=10)
plt.show()