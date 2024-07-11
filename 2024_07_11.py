# todo regex
# Task 1
# Napis funkciu, ktora dostane na vstupe text a vrati v zozname vsetky telefonne cisla
# s ceskou predvolbou +420, ktore sa v texte nachadzaju. Predpokladaj, ze za predvolbou
# moze nasledovat iba prave 9 cislic

"""
import re
text = "Find tel. number: some valid ones +420123456789, +420987654321 and some invalid ones +420123, +42098765432199999999999."

pattern = r"\+420\d{9}\b"

matches = re.findall(pattern, text)
print(matches)
"""

# Task 2
# Napis funkciu, ktora dostane na vstupe string a rozhodne, ci je to validna emailova adresa
# definujme si znaky basic = {vsetky pismena anglickej abecedy} | {vsetky cislice} | {.}
# emailova adresa je validna, pokial obsahuje aspon jeden znak z mnoziny `basic`, za ktorym nasleduje zavinac '@',
# dalej znovu aspon jeden znak z `basic - {.}` (bez bodky), bodka (.) a aspon 2 znaky anglickej abecedy.
# Disclaimer - toto nie je definicia realnej validnej emailovej adresy, iba velmi podobna definicia.
# Najlepsie je pouzivat v praxi validatory z uz naimplementovanych kniznic.

import re

"""
test = [
    "tomas.jasko@gmail.com",
    "tomasjasko8@gmail.co",
    "tomas.invalid@gmail",
    "tomas.jasko@gmail.c",
    "tomasjasko@gmail.c_com",
    "@gmail.com"
]

# basic   = r"^[a-zA-Z0-9\.]"
# basic_p = r"^[a-zA-Z0-9]"
pattern = r"^[a-zA-Z0-9\.]+@[a-zA-Z0-9]+\.+[a-z]{2,}$"

for email in test:
    match = re.match(pattern, email)
    is_valid = match is not None
    print(f"{email} - {is_valid}")
"""

# Task 2.1
# Napis funkciu, ktora dostane text a vrati z neho zoznam vsetkych emailovych adries

import re
text = "Find email: some valid ones tomas.jasko@gmail.com, adam.jasko@gmail.com and some invalid ones @gmail.com, tomasjasko@gmail.c_com."

pattern = r"^[a-zA-Z0-9\.]+@[a-zA-Z0-9]+\.+[a-z]{2,}$"

matches = re.findall(pattern, text)
print(matches)