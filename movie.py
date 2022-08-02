import os
import json
import logging
#Import du fichier json
CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

# Recuperation des instances
def get_movies():
        movies_inst = []
        with open(DATA_FILE, "r") as f:
            movies_title = json.load(f)
        
        for movie_title in movies_title:
            movies_inst.append(Movie(movie_title))
        return movies_inst

# Creation de la classe
class Movie:
    def __init__(self, title):
        self.title = title.title()
    
    def __str__(self):
        return self.title

# Lecture et ecriture du fichier contenant les films   
    
    def _get_movies(self):
            with open(DATA_FILE, "r") as f:
                return json.load(f)         
            
    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
                json.dump(movies, f, indent=4)

# Ajout et suppression des films
    def add_to_movies(self):
        movies = self._get_movies()
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"{self.title} est deja dans la liste")
            return False

    def remove_from_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            logging.warning(f"{self.title} a ete supp de la liste")


if __name__ == "__main__":
    movies = get_movies()
    print(movies)