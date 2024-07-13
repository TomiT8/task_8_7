# todo regex

# todo Task 1
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

# todo Task 2
# Napis funkciu, ktora dostane na vstupe string a rozhodne, ci je to validna emailova adresa
# definujme si znaky basic = {vsetky pismena anglickej abecedy} | {vsetky cislice} | {.}
# emailova adresa je validna, pokial obsahuje aspon jeden znak z mnoziny `basic`, za ktorym nasleduje zavinac '@',
# dalej znovu aspon jeden znak z `basic - {.}` (bez bodky), bodka (.) a aspon 2 znaky anglickej abecedy.
# Disclaimer - toto nie je definicia realnej validnej emailovej adresy, iba velmi podobna definicia.
# Najlepsie je pouzivat v praxi validatory z uz naimplementovanych kniznic.

"""
import re

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

# todo Task 2.1
# Napis funkciu, ktora dostane text a vrati z neho zoznam vsetkych emailovych adries

"""
import re
text = "Find email: some valid ones tomas.jasko@gmail.com, adam.jasko@gmail.com and some invalid ones @gmail.com, tomasjasko@gmail.c_com."

pattern = r"[a-zA-Z0-9\.]+@[a-zA-Z0-9]+\.+[a-z]{2,}"

matches = re.findall(pattern, text)
print(matches)
"""

# todo Task 3
# Napis funkciu, ktora dostane datum v stringu a skontroluje, ci je vo formate mm-dd-yyyy. Ak nie, vratime None.
# Ak ano, prevedieme ho na format dd/mm/yyyy a vratime ho ako vysledok.

# todo
#  1. riešenie

"""
date_test = [
    "10-31-2024",       # True
    "31-10-2024",
    "10-31-202",
    "jan-31-2024",
    "10.31.2024",
    "8-7-1990",         # True
    "02-31.2024",
    "02-29-2024",        # True
    "02-29-2023"
]
def date_string(dstr):
    parts = dstr.split("-")

    if len(parts) != 3:
        return False

    month, day, year = parts

    for part in parts:
        if not (month.isdigit() and day.isdigit() and year.isdigit()):
            return False
        if not 1 <= int(month) <= 12:
            return False
        if int(month) == 2:
            if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
                if not 1 <= int(day) <= 29:
                    return False
            else:
                if not 1 <= int(day) <= 28:
                    return False
        if int(month) in [1, 3, 5, 7, 8, 10, 12] and not (1 <= int(day) <= 31):
            return False
        if int(month) in [4, 6, 9, 11] and not (1 <= int(day) <= 30):
            return False
        if len(str(year)) != 4:
            return False
    return f"{day}/{month}/{year}"

valid_dates = []

for dstring in date_test:
    result = date_string(dstring)
    if result:
        print(f"{dstring} - True")
        valid_dates.append(result)
    else:
        print(f"{dstring} - False")
print()
print()
for valid_date in valid_dates:
    print(valid_date)
"""

# todo
#  2. riešenie

"""
from datetime import datetime

date_test = [
    "10-31-2024",  # True
    "31-10-2024",
    "10-31-202",
    "jan-31-2024",
    "10.31.2024",
    "8-7-1990",  # True
    "02-31.2024",
    "02-29-2024",  # True
    "02-29-2023"
]
def date_string(dstr):
    try:
        datetime.strptime(dstr, "%m-%d-%Y")
        month, day, year = dstr.split('-')
        return f"{day}/{month}/{year}"
    except ValueError:
        return False

valid_dates = []

for dstring in date_test:
    result = date_string(dstring)
    if result:
        print(f"{dstring} - True")
        valid_dates.append(result)
    else:
        print(f"{dstring} - False")
print()
print()
for valid_date in valid_dates:
    print(valid_date)
"""

# todo Task 4
# Napis funkciu, ktora vrati vsetky webove adresy zo stringu vo formate
# https://{hocico}<whitespace>
# alebo
# http://{hocico}<whitespace>
# Ak mas cas navyse, mozes si skusit napisat taky regex, ktory korektne validuje celu URL.

"""
import re

test = [
    "https://{hocico}<whitespace>",  # True
    "http://{hocico}<whitespace>",  # True
    "httpe://{hocico}<whitespace>",
    "http:/{hocico}<whitespace>",
    "http//{hocico}<whitespace>"
]

def web_search(textlist):
    pattern = r'https?:\/\/\S+\s'
    matches = []
    for text in textlist:
        found = re.findall(pattern, text)
        matches.extend(found)
    return matches

print(web_search(test))
"""

# Task 5
# Napis funkciu, ktora dostane na vstupe string a zisti, ci sa jedna o IPv4 adresu.
# IPv4 adresa je vo formate {cislo v rozmedzi 0-255}.{cislo v rozmedzi 0-255}.{cislo v rozmedzi 0-255}.{cislo v rozmedzi 0-255}

"""
test = ["192.168.1.1", "256.168.1.1"]
def is_valid_ipv4(ipv4):
    parts = ipv4.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True

for ip in test:
    print(f"{ip} - {is_valid_ipv4(ip)}")
"""
