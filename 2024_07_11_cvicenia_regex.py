# todo
#   1. Extrahovanie Emailových Adries
#   Úloha: Nájsť všetky emailové adresy v texte.

"""
import re

text = "Kontaktujte nás na info@example.com alebo support@my-domain.org."

def extract_email(text):
    pattern = r'[a-zA-Z0-9\.\-\_]@[a-zA-Z0-9\.\-\_]+\.[a-zA-Z0-9]{2,}'
    email = re.findall(pattern, text)
    return email

print(extract_email(text))
"""

# todo
#   2. Overenie Formátu Telefónneho Čísla
#   Úloha: Skontrolovať, či daný reťazec zodpovedá formátu telefónneho čísla (napr. +421 123 456 789).

"""
import re

phone_number = "+421 123 456 789 and 00421 123 456 789, +421123456789, 00421123456789 is valid and 123-456-7890 is invalid"

def ph_number(phone_number):
    pattern = r'(\+421|00421)\s\d{3}\s\d{3}\s\d{3}|(\+421|00421)\d{9}'
    return [match.group().replace("00421", "+421").replace(" ","") for match in re.finditer(pattern, phone_number)]

print(ph_number(phone_number))
"""

# todo
#   3. Získanie URL Adries z Textu
#   Úloha: Nájsť všetky URL adresy v texte.

"""
import re

text = "Navštívte naše stránky na https://example.com alebo https://www.example.org/path."

def extract_url(text):
    pattern = r'https:\/\/[a-zA-Z0-9\.-]+\.[a-zA-Z]{3,}\/?[a-zA-Z]*'
    return re.findall(pattern, text)

print(extract_url(text))
"""

# todo
#   4. Vyhľadávanie a Nahradenie Všetkých Čísel v Texte
#   Úloha: Nahradiť všetky čísla v texte s textom "NUMBER".

"""
text = "V tomto texte sú čísla ako 123, 456 a 789."

def number_replace(text):
    return re.sub(r'\d+', "NUMBER", text)

print(number_replace(text))
"""

# todo
#   5. Overenie Platnosti Dátumu v Formáte RRRR-MM-DD
#   Úloha: Skontrolovať, či daný reťazec zodpovedá formátu dátumu (napr. 2024-07-13).

"""
from datetime import datetime

text = "2024-07-13"
text = "2024-13-40"

def email_control(text):
    try:
        datetime.strptime(text,"%Y-%m-%d")
        month, day, year = text.split('-')
        return True
    except ValueError:
        return False

print(email_control(text))
"""