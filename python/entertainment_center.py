import fresh_tomatoes
import media

# As I imported media.py I can create instances of Movie class.
# I'm creating 4 instances, each for one of my favorite's movies.
# As defined in media.py class Movie has 4 instance variables:
# name, description,url to poster, url to trailer

interstellar = media.Movie("interstellar",
						   "A story about cosmsos, love and time",
						   "http://upload.wikimedia.org/wikipedia/en/thumb/b/bc/I"+
						   "nterstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
						   "http://www.youtube.com/watch?v=0vxOhd4qlnA")


special_attention = media.Movie("In the area of special attention",
						   		"A story about brave russian soldiers",
						   		"http://www.kinopoisk.ru/images/film_big/45650.jpg",
						   		"http://www.youtube.com/watch?v=P-0AfY9YE6c")

bridge_to_terabithia = media.Movie("Bridge to terabithia",
						  		   "A story about boy and girl in wonderland",
						   		   "http://upload.wikimedia.org/wikipedia/en/thumb/b/"
						   		   "bd/Bridgetoterabithiaposter.jpg/220px-Bridgetotera"
						   		   "bithiaposter.jpg",
						   		   "http://www.youtube.com/watch?v=t42b2t2KXsg")

bourne_identity = media.Movie("Bourne identity",
							  "Spy story about Bourne, Jason Bourne",
							  "http://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Bour"
							  "neIdentityfilm.jpg/220px-BourneIdentityfilm.jpg",
							  "http://www.youtube.com/watch?v=FpKaB5dvQ4g")

# Now I can make list of my instances and pass it to open_movies_page() function,
# defined in fresh_tomatoes.py, where index.html will be parsed and finally maked.

movies = [interstellar,special_attention,bridge_to_terabithia,bourne_identity]

fresh_tomatoes.open_movies_page(movies)
				   