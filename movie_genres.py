MAX = 10000

number_of_people = int(input())

movie_genres = {}

def sort_genres(genre):
    return MAX - movie_genres.get(genre)



for i in range(number_of_people):
    line = input().split()
    for j in range(len(line)-1):
        k = j + 1
        if (movie_genres.get(line[k]) == None):
            movie_genres.update({line[k]:1})
        else:
            movie_genres.update({line[k]:movie_genres.get(line[k])+1})

genres_list = list(movie_genres.keys())

genres_list.sort(key = lambda x:(sort_genres(x),x))

for genre in genres_list:
    print("{} : {}".format(genre, movie_genres.get(genre)))

