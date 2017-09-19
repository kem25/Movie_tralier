import media
import fresh_tomatoes

"""Instantiating movie object-tangled"""
tangled = media.Movie("Tangled",
                      "Story About A Lost Princess",
                      "https://upload.wikimedia.org/wikipedia/en/a/a8/Tangled_poster.jpg",   # noqa
                      "https://www.youtube.com/watch?v=ip_0CFKTO9E")

# Instantiating movie object-tangled
minions = media.Movie("Minions",
                      "Story about Minions",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",   # noqa
                      "https://www.youtube.com/watch?v=eisKxhjBnZ0")

# Instantiating movie object-lor
lord_of_the_rings = media.Movie("Lord Of The Rings",
                                "Story based on fantasy novel-The Hobbit",
                                "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # noqa
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")

# Instantiating movie finding_dory
finding_dory = media.Movie("Finding Dory",
                           "A story about finding Dory",
                           "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",  # noqa
                           "https://www.youtube.com/watch?v=3JNLwlcPBPI")

# Instantiating movie object-inception
inception = media.Movie("Inception",
                        "Story of a Thief who steals corporate secrets",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

# Instantiating movie object-insideout
inside_out = media.Movie("Inside Out",
                         "Story about the voices inside a little girl's head",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=seMwpP0yeu4")

"""input list of movies to open_movie_page function defined in tomato.py"""
movies = [tangled, minions, lord_of_the_rings,
          finding_dory, inception, inside_out]
fresh_tomatoes.open_movies_page(movies)
