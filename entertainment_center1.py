#https://classroom.udacity.com/courses/ud036
import media
import fresh_tomatoes

truman_show = media.Movie("Truman Show",
                        "Truman Burbank in Seaheaven watched with Omnicamera",
                        "https://upload.wikimedia.org/wikipedia/en/c/cd/Trumanshow.jpg",
                        "https://www.youtube.com/watch?v=ktId707bSUQ")

#print(truman_show.storyline)

the_grinch = media.Movie("The Grinch",
                     "The Grinch looks like Santa Claus but He is Burglarer",
                     "https://upload.wikimedia.org/wikipedia/en/e/e7/How_the_Grinch_Stole_Christmas_film_poster.jpg",
                     "https://www.youtube.com/watch?v=iZPV3-_xiso")

#print(the_grinch.storyline)
#the_grinch.show_trailer()

starwar_I = media.Movie("Star War I", 
                             "Origin of Anakin Skywalker",
                             "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",
                             "https://www.youtube.com/watch?v=bD7bpG-zDJQ")

series_of_unfortunate_event = media.Movie("Series of the Unfortunate Events",
                          "Stories of Baudelaire Orphan Family",
                          "https://upload.wikimedia.org/wikipedia/en/3/31/A_Series_of_Unfortunate_Events_Logo.jpg",
                          "https://www.youtube.com/watch?v=Tup-5yOcJuM")

queen_gambit = media.Movie("Queen Gambit",
                                "Story of Chess woman player as world champion",
                                "https://upload.wikimedia.org/wikipedia/en/d/db/TheQueensGambit.jpg",
                                "https://www.youtube.com/watch?v=kwrQzTz16w4")

beautiful_mind = media.Movie("Beautiful mind",
                           "Story of World Economist named John Nash",
                           "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                           "https://www.youtube.com/watch?v=9wZM7CQY130")   

movies = [truman_show, the_grinch, starwar_I, series_of_unfortunate_event, queen_gambit, beautiful_mind]
fresh_tomatoes.open_movies_page(movies)
