import re
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
    def number_of_episodes(self):
        for counter1, item in enumerate(self.episodes):
            continue
        for counter2, item in enumerate(self.seasons):
            continue
        return (counter1+1)*(counter2+1)
    #func that allows to print a class instance as a string. The aim of the excercise in point 4 wants us to display serie as a string and presend the information about some particular episode. As the libraty list doesn't keep all series episodes as individual instance the function generate dummy information about some randomly picked espisode. 
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
Serie(title='Band Of Brothers', release_year=2001, genre='war drama', views=11,type = 'S', seasons= [1], episodes=[1,2,3]),
Serie(title='The Witcher', release_year=2020, genre='fantasy', views=18,type = 'S', seasons=[1,2],episodes=[1,2]),
Serie(title='House of Cards', release_year=2017, genre='political fiction', views=22,type = 'S', seasons=[1,2,3,4],episodes=[1,2,3,4,5]),
Serie(title='Black Mirror', release_year=2016, genre='fantasy', views=55,type = 'S', seasons=[1,2,3],episodes=[1,2,3,4])
]

top_views = []
sorted_top_views = []

#movie searching func
def get_movies():
    movies = []
    for item in library:
        if item.type == 'M':
            movies.append(item.title)
    return movies

#series searching func
def get_series():
    series = []
    for item in library:
        if item.type == 'S':
            series.append(item.title)
    return series

#funk that look for movie or serie by entered name
def search(name):
    for item in library:
        if item.title == name:
            return item
    return None

#func that generate views for randomly chosen movie
def generate_views():
    random_title = random.choice(library).title
    for item in library:
        if random_title == item.title:
            item.views += random.choice(range(1,100))
        return item

#func that multiplies execution of generate_views() by 10
def multiplication():
    i = 0
    while i < 10:
        generate_views()
        i+=1
    return None

#func that list the given number of most viewed movies or series
def top_titles(quantity):
    library.sort(key=lambda x:x.views)
    item = library[::-quantity]
    return item

#add_item() supplementaly func that helps to add number of seasons and expiodes to the class instance of the serie Class 
def add_suplementary(a):
    i=1
    item_table = []
    for item in range(1,a):
        item_table.append(item)
    return item_table

#func that is responsible for adding series to the library
def add_item():
    next = 'yes'
    print('dodawanie')
    while next == 'yes': 
        print('paaaart 2 ')   
        library.append(Serie(title=input('Serie title: '), release_year=input('Serie release year: '), genre=input('Serie genre: '),views=0, type='S', seasons=add_suplementary(a = int(input('Number of seasons: '))), episodes=add_suplementary(a = int(input('Number of episodes: ')))))
        next = input('Do you want to add another serie: (yes/no) ')
    return library


#function that triggers actions
def to_do(action):  
    if action == '1':
        name = input('Write down the movie/serie name:\n')
        result = search(name)
        result2 = search(name).number_of_episodes()
        if result == None:
            print('There is no movie/serie you search for in the library\n')
        elif result.type == "M":
            print(f'The movie {result} is available in the library\n')
        elif result.type == "S":
            print(f'The serie {result} is available in the library and consis of {result2} episodes\n')
    elif action == '2':
        result = get_movies()
        print ('The list of available movies:\n')
        for movie in result:
            print (movie)
        print('\n')
    elif action == '3':
        result = get_series()
        print ('The list of available series:\n')
        for movie in result:
            print (movie)
        print('\n')
    elif action == '4':
        quantity = int(input('\n\nWrite down the number of most viewed movies/series you want to display:'))
        result = top_titles(quantity)
        for counter, movie in enumerate(result):
            print(f'{counter+1}.{movie} views: {movie.views}')
    elif action == '5':
        add_item()
        print('Series added successfully')
  
    elif action == '6':
        quantity = int(input('\n\n'))
        result = top_titles(quantity)

    elif action == 'exit':
        return True
    else:
        return False

#main program logic
action = ''
print('Welcome to Movies Library\n')
generate_views()
multiplication()

while to_do(action) != True:
    action = str(input('\nAvailable options:\n1. Search movies/series by name\n2. List all available movies\n3. List all available series\n4. Display most viewed movies\n5. Add series to the library \n Type "exit" to exit  \n'))