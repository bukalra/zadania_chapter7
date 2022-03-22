from readline import set_pre_input_hook
import random

class Movie:
    def __init__(self, title, release_year, genre, views,type):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = views
        self.type = type
    def play(self, view_num = 1):
        self.views += view_num
    def __str__(self):
        return f'{self.title} ({self.release_year})'

class Serie(Movie):
    def __init__(self, seasons, episodes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episodes = episodes
        self.seasons = seasons

    def play(self, view_num = 1):
        self.views += view_num
    def __str__(self):
        _episode = random.choice(self.episodes)
        _season = random.choice(self.seasons)
        if int(_season) <10 and (_episode <10):
            return f'{self.title} S0{_season}E0{_episode}'
        elif int(_season) <10:
            return f'{self.title} S0{_season}E{_episode}'
        elif int(_season) <10:
            return f'{self.title} S{_season}E0{_episode}'

library = [
Movie(title='Shawshank', release_year =1994, genre='drama',views=10, type = 'M'),
Movie(title='Forest Gump', release_year=1994, genre='comedy',views=19,type = 'M'),
Movie(title='The Shining', release_year=1980, genre='psychological',views=34,type = 'M'),
Movie(title='Troy', release_year=2004, genre='historical',views = 33,type = 'M'),
Movie(title='Cast Away', release_year=2000, genre='survival drama',views=14,type = 'M'),
Serie(title='Band Of Brothers', release_year=2001, genre='war drama', views=11,type = 'S', seasons= [1], episodes=[1,2,3,4,5,6,7,8,9,10]),
Serie(title='The Witcher', release_year=2020, genre='fantasy', views=18,type = 'S', seasons=[1,2],episodes=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]),
Serie(title='House of Cards', release_year=2017, genre='political fiction', views=22,type = 'S', seasons=[1,2,3,4,5,6],episodes=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,3,24]),
Serie(title='Black Mirror', release_year=2016, genre='fantasy', views=55,type = 'S', seasons=[1,2,3],episodes=[1,2,3,4,5,6,7,8,9,10,11,12])
]


top_views = []
sorted_top_views = []

def get_movies():
    movies = []
    for item in library:
        if item.type == 'M':
            movies.append(item.title)
    return sorted(movies)

def get_series():
    series = []
    for item in library:
        if item.type == 'S':
            series.append(item.title)
    return sorted(series)

def search(name):
    for item in library:
        if item.title == name:
            return f'Movie avaialble in the library: {item.title}'
    return None
           
def generate_views():
    random_title = random.choice(library).title
    for item in library:
        if random_title == item.title:
            item.views += random.choice(range(1,100))
        return item.views

def multiplication():
    i = 0
    while i < 10:
        generate_views()
        i+=1
        return None

def top_titles(quantity):
    library.sort(key=lambda x:x.views)
    i = 1 
    movie_rank = ''
    for movie in library[::-1]:
        if i <= quantity:
            movie_rank +=  (f'{i}.{movie.title} with {movie.views} views\n')
        else:
            break
        i += 1 
    return movie_rank
        
if __name__ == "__main__":
    quantity = int(input('How many most viewed movies do you want to list?'))
    #name = input('what movie do you look for?')
    item = top_titles(quantity)
    #item = top_titles(quantity)
    print(item)

