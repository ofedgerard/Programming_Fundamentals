"""
Author: Gerard Ortiz
Date: 9/27/2026
Tier Level: Base

Description:
This program stores, displays, and analyzes a personal list of movies. Movies are stored
as a dictionary containing title(string), year(int), genre(s)(string), and rating(float)
"""

# starter data. a list of dictionaries of 5 movies
current_movie_list = [
    {
        "title": "Insidious 1", 
        "year": 2010, 
        "genres": ["horror", "supernatural"], 
        "rating": 6.2
    },
    {
        "title": "Insidious: Chapter 2", 
        "year": 2013, 
        "genres": ["horror", "supernatural"], 
        "rating": 6.6
    },
    {
        "title": "Insidious: Chapter 3", 
        "year": 2015, 
        "genres": ["horror", "supernatural"], 
        "rating": 5.1
    },
    {
        "title": "Insidious: The Last Key", 
        "year": 2018, 
        "genres": ["horror", "supernatural"], 
        "rating": 5.8
    },
    {
        "title": "Insidious: The Red Door", 
        "year": 2023, 
        "genres": ["horror", "supernatural"], 
        "rating": 5.7
    }
]

# this functions takes no arguments. asks the user to input a movie title, year, genres, and rating.
# returns the user inputs in the correct data type
def collect_movie():
    while True:
        try:
            title = input("\n"+"Movie title: ").title()
            year = int(input("Year: "))
            genres = input("Genres(separate with ','): ").title().strip().split(",")
            rating = round(float(input("Rating: ")),2)
            return title, year, genres, rating
        except ValueError or TypeError:
            print("Input was not valid. Please try again")

#Formats and returns the user input from collect_movie() to the dictionary format
def create_movie(title, year, genres, rating):
    new_movie = {
        "title": title[:30], 
        "year": year, 
        "genres": genres, 
        "rating": rating
    }
    return new_movie

# Takes the movie list of dictionaries anda heading value. prtins a header and
# formated display of the movies
def display_movies (movies, heading):
    print("\n"+ heading, "\n"+"-"*68)
    if movies != []:
            print(f"{'Title':<30}{'Year':<10}{'Genres':<20}  {'Rating':<10}")
            for collection in movies:
                title = collection["title"]
                year = int(collection["year"])
                genres = "/".join(collection["genres"])
                rating = collection["rating"]
                print(f"{title:<30}{year:<10}{genres:<20}  {rating:<10}")
    else:
        print("No movies in this collection")
    return

# takes a movie list and an n-value. sorts the list by rating in descending order and returns 
# the top n movies
def find_top(movies, n):
    #rating = movies["rating"]
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True) 
    return sorted_movies[:n]

# takes a the movie list of dictinoaries and takes the average using a for loop.
# retruns the average rating
def get_average_rating(movies):
    movie_rating_average = 0
    movie_rating_lenght = 0
    total_rating = 0
    if movies != []:
        for collection in movies:
            rating = collection["rating"]
            total_rating += rating
            movie_rating_lenght += 1
        movie_rating_average = total_rating/movie_rating_lenght
        return round(float(movie_rating_average),2)
    else:
        return round(float(movie_rating_average),1)

# Main section

# Initiates heading 1 and calls display_movie() on the started data
heading_1 = "Your Movie Collection"
display_movies(current_movie_list,heading_1)

# Uses a for loop and calls on collect_movie() and passes output to create_movie()
# appends the output from _create_movie() to the started_data
print("\n"+"Enter 2 Movies") 
for i in range(2):
    title, year, genres, rating = collect_movie()
    new_movie = create_movie(title, year, genres, rating)
    current_movie_list.append(new_movie)

# intiates deading 2.Sorts the appended movie list by year and 
# calls on display_movie() to display the appended movie list
heading_2 = "All Movies Sorted by Year"
current_movie_list.sort(key=lambda x: x["year"], reverse=True)
display_movies(current_movie_list, heading_2)

# intiates heading 3. Calls on find_top() to find the top 3 rated movies
# calls on display_movies() to display the top 3 movies 
heading_3 = "Top 3 Rated Movies"
sorted_movies = find_top(current_movie_list, 3)
display_movies(sorted_movies, heading_3)

# calls on get_average_rating() to get the average rating the appended movie list.
# prints the output of the get_average_rating() on a new line
print("\n"+"Collection average rating: ",get_average_rating(current_movie_list))
