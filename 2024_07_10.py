# todo - Správce kontextu (správca kontextu)
# https://journey.study/v2/learn/courses/10302/modules/26102/units/9/materials/44447

# with

# Vytvorenie vlastného správcu

# tu bol task -> Vlastní správca kontextu jako funkce

# todo - Generátory a iterátory
## Iterace
## Iterovanie cez veľkú kolekciu
## Iterátor
## Generátor


# todo Task 1
# Napis generator `even_numbers()`, ktory bude generovat donekonecna parne (sude) cisla

"""
def even_numbers():
    x = 0
    while True:
        yield x
        x += 2

generator = even_numbers()

for i in range(10):
    print(next(generator))
"""

# todo Task 2
# Napis generator `my_range(start, stop=None, step=1), ktory sa sprava rovnako ako funkcia range

# todo Task 3
# Napis generator `fib()`, ktory bude donekonecna generovat cisla fibonnaciho postupnosti

# todo Task 4
# Napis generator `read_file(file_name)`, ktory otvori subor `file_name` a bude
# postupne vracat jeho riadky

# todo Task 5
# Napis generator `randgen(start, end)`, ktory bude donekonecna generovat nahodne cisla
# v intervale <start, end>.

# todo Task 6
# Napis generatory `map` a `filter`, ktore sa spravaju ako builtin funkcie `map` a `filter`

"""
def my_map(f, iterable):
    for item in iterable:
        yield f(item)

def to_lower(x):
    return x.lower()

strings = ['Mama', 'OTEC', 'seSTra', 'braT']
lower_string = map(to_lower, strings)
print(list(lower_string))
"""

"""
def my_filter(f, iterable):
    for item in iterable:
        if f(item):
            yield item

def is_odd(x):
    return x%2 != 0

numbers = [1, 2, 3, 4, 5]
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))
"""