from readline import set_pre_input_hook
import random

library = [
{'title':'Shawshank', 'release_year':'1994', 'genre':'drama','views':10},
{'title':'Forest Gump', 'release_year':'1994', 'genre':'comedy','views':19},
{'title':'The Shining', 'release_year':'1980', 'genre':'psychological','views':122},
{'title':'Troy', 'release_year':'2004', 'genre':'historical','views':33},
{'title':'Cast Away', 'release_year':'2000', 'genre':'survival drama','views':14},

{'title':'Band Of Brothers', 'release_year':'2001', 'genre':'war drama', 'views':11, 'seasons':[1],'episodes':[1,2,3,4,5,6,7,8,9,10]},
{'title':'The Witcher', 'release_year':'2020', 'genre':'fantasy', 'views':18, 'seasons':[1,2],'episodes':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]},
{'title':'House of Cards', 'release_year':'2017', 'genre':'political fiction', 'views':22, 'seasons':[1,2,3,4,5,6],'episodes':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,3,24]},
{'title':'Black Mirror', 'release_year':'2016', 'genre':'fantasy', 'views':55, 'seasons':[1,2,3],'episodes':[1,2,3,4,5,6,7,8,9,10,11,12]},
]

movies = []
series = []
top_views = []

class Movie:
    def __init__(self, title, release_year, genre, views):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = views
    def play(self, view_num = 1):
        self.views += view_num
    def __str__(self):
        return f'{self.title} ({self.release_year})'

class Serie(Movie):
    def __init__(self, season_number, episode_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
    def play(self, view_num = 1):
        self.views += view_num
    def __str__(self):
        if int(self.season_number) <10 and (self.episode_number) <10:
            return f'{self.title} S0{self.season_number}E0{self.episode_number}'
        elif int(self.season_number) <10:
            return f'{self.title} S0{self.season_number}E{self.episode_number}'
        elif int(self.episode_number) <10:
            return f'{self.title} S{self.season_number}E0{self.episode_number}'

def get_movies():
    for item in library:
        if len(item)==4:
            movies.append(item['title'])
    return(sorted(movies))

def get_series():
    for item in library:
        if len(item)==6:
            series.append(item['title'])
    return(sorted(series))

def search(name):
    i= 0 
    for item in library:
        i += 1
        if len(item) == 6 and item['title']==name:
            print(f'The serie available in the base {item}')
            break
        elif len(library) == i:
            print('The serie is not available in the base')
        else:
            print('Searching...')
           
def generate_views():
    random_title = random.choice(library)['title']
    for item in library:
        if random_title == item['title']:
            item['views'] += random.choice(range(1,100))
            print(item['title'])

def multiplication():
    i = 0
    while i < 10:
        generate_views()
        i+=1

sorted_top_views = []
quantity = int(input('How many best view movies/series do you want to display?'))
def top_titles():
    top_views = sorted(library, key=lambda d: d['views'])
    i=1
    for i, item in enumerate(top_views[-1:-quantity-1:-1]):
        print(f'{i+1}.{item["title"]} with {item["views"]} views')
        
top_titles()



'''serie = Serie(title= 'Band Of Brothers', release_year = '2002', genre = 'war drama', season_number = '12', 
episode_number= '9')
movie = Movie(title=library[0]['title'], release_year=library[0]['release_year'], genre=library[0]['genre'])'''
