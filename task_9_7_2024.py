# Task 1
# Napiste 1 riadok, ktory najde najvacsiu hodnotu v zozname, kde najvacsia hodnota reprezentuje najdlhsi retazec
# array = ['banana', 'apple', 'orange', 'pineapple']

fruits = ['banana', 'apple', 'orange', 'pineapple']
print(f"Ovocie s najdlhším názvom je {max(fruits,key=lambda fruit: len(fruit))}.")

"""
Task 2
Napis funkciu, ktora na vstupe dostane cele cislo n >= 0 a vrati dictionary, kde klucmi budu cisla i a
    hodnotami funkcie, ktore beru najviac jeden argument vracaju konstantnu hodnotu 2**i, pre kazde i od 0 po n-1.
    Priklad:
        function_factory(2) ~> {0: <function object>, 1: <function object>}
    Hint:
        Pozor, aby kazda funkcia nerobila to iste!
"""

def function_factory(n):
    return {i: (lambda x: 2**x)(i) for i in range(n)}

print((function_factory(8)))