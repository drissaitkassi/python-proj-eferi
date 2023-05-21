#Écrivez une fonction factorial récursive qui calcule la factorielle
#d'un nombre donné (exemple : 4! = 1 × 2 × 3 × 4 = 24).

def factorial(number):
    if number == 1 :
        return 1
    else:
        return number * factorial(number-1)

print(factorial(5))