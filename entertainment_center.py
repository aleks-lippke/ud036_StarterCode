import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=Ny_hRfvsmU8")

avatar = media.Movie("Avatar",
                     "A story of a boy and his toys that come to life",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

star_wars = media.Movie("Star Wars: The Last Jedi",
                        "The Resistance prepares to battle the First Order",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY")

hunger_games = media.Movie("Hunger Games", "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, school_of_rock, ratatouille, star_wars,
          hunger_games]
fresh_tomatoes.open_movies_page(movies)
