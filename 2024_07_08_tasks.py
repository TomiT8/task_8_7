# todo - task1 - pickle
# import pickle
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greeting(self):
#         return f"Ahoj, volám sa {self.name} a mám {self.age} rokov."
#
# person = Person("Tomáš", 34)
#
# with open("person.pkl", "wb") as file:
#     pickle.dump(person, file)
#
# with open("person.pkl", "rb") as file:
#     loaded_person = pickle.load(file)
#
# print(loaded_person.greeting())




# todo - task2 - csv

from typing import List
from dataclasses import dataclass
import csv


@dataclass
class Movie:
    MovieID: int
    Title: str
    Genre: str
    Rating: float
    Year: int


def read_movies_csv(file_name):
    movies = []
    with open(file_name, mode='r') as filecsv:
        reader = csv.reader(filecsv)
        for row in reader:
            movie = Movie(
                MovieID=int(row[0]),
                Title=row[1],
                Genre=row[2],
                Rating=float(row[3]),
                Year=int(row[4])
            )
            movies += [movie]
    return movies

# file_name = 'movies.csv'
# movies = read_movies_csv(file_name)
# for movie in movies:
#     print(movie)


def filter_movies(movies: List[Movie], genre: str):
    filtered_movies = []
    for movie in movies:
        if movie.Genre.lower() == genre.lower():
            filtered_movies.append(movie)
    return filtered_movies

file_name = 'movies.csv'
movies = read_movies_csv(file_name)

# Filtruj filmy podľa žánru "Action"
filtered_movies = filter_movies(movies, 'Action')

# Výpis:
for movie in filtered_movies:
    print(movie)

