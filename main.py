class MotionPicture:
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self.isnotplaying = True

    def play(self):
        print(f"\n🎬 Playing '{self.title}' directed by {self.director}.")
        self.isnotplaying = False

    def pause(self):
        print(f"⏸ Paused '{self.title}'.")
        self.isnotplaying = True

    def get_info(self):
        print(f"\nTitle: {self.title}\nDirector: {self.director}")


class Movie(MotionPicture):
    def __init__(self, title, director, duration, genre):
        super().__init__(title, director)
        self.duration = duration
        self.genre = genre

    def get_duration(self):
        print(f"Duration: {self.duration} minutes")

    def watch_trailer(self):
        print(f"🎞 Watching trailer of the movie '{self.title}'...")

    def recommend_similar(self):
        print(f"If you like '{self.title}', you might also enjoy other {self.genre} movies.")


class Series(MotionPicture):
    def __init__(self, title, director, seasons, current_episode):
        super().__init__(title, director)
        self.seasons = seasons
        self.current_episode = current_episode

    def get_seasons(self):
        print(f"Number of Seasons: {self.seasons}")

    def next_episode(self):
        self.current_episode += 1
        print(f"⏭ Now watching Episode {self.current_episode} of '{self.title}'...")

    def skip_intro(self):
        print("⏩ Skipping intro... Enjoy the episode!")


class Documentary(MotionPicture):
    def __init__(self, title, director, topic, narrator, statistics):
        super().__init__(title, director)
        self.topic = topic
        self.narrator = narrator
        self.statistics = statistics

    def get_topic(self):
        print(f"Topic: {self.topic}")

    def narrate(self):
        print(f"🎙 Narrating the documentary '{self.title}' with {self.narrator}...")

    def show_statistics(self):
        print(f"📊 Statistics for '{self.title}':")
        print(f" Viewer Impact: {self.statistics['impact']}%")
        print(f" Avg Rating: {self.statistics['rating']}/10")
        print(f" Featured in {self.statistics['festivals']} festivals")


class ShortFilm(MotionPicture):
    def __init__(self, title, director, length, award_won):
        super().__init__(title, director)
        self.length = length
        self.award_won = award_won

    def get_length(self):
        print(f"Short film length: {self.length} minutes")

    def film_festival(self):
        print(f"🎟 '{self.title}' is featured at a short film festival!")

    def show_award(self):
        print(f"🏆 '{self.title}' won the '{self.award_won}' award!")


# Collections
movie_films = [
    Movie("Heneral Luna", "Jerrold Tarog", 118, "Historical"),
    Movie("Kita Kita", "Sigrid Andrea Bernardo", 85, "Romance"),
    Movie("Goyo: Ang Batang Heneral", "Jerrold Tarog", 120, "Historical"),
    Movie("On The Job", "Erik Matti", 120, "Crime"),
    Movie("Four Sisters and a Wedding", "Cathy Garcia-Molina", 120, "Drama"),
    Movie("BuyBust", "Erik Matti", 120, "Action")
]

series_films = [
    Series("Ang Probinsyano", "Malou Sevilla", 7, 1),
    Series("Encantadia", "Mark Reyes", 4, 1),
    Series("Pangako Sa 'Yo", "Rory B. Quintos", 2, 1),
    Series("Be Careful With My Heart", "Jon S. Rivera", 6, 1),
    Series("Forevermore", "Jerry Lopez Sineneng", 1, 1),
    Series("The General's Daughter", "Millee O'Brian", 2, 1)
]

documentary_films = [
    Documentary("The Kingmaker", "Lauren Greenfield", "Political", "Lauren Greenfield",
                {"impact": 91, "rating": 8.2, "festivals": 15}),
    Documentary("Aswang", "Alyx Ayn Arumpac", "Social Issues", "Alyx Ayn Arumpac",
                {"impact": 88, "rating": 8.5, "festivals": 10}),
    Documentary("Call Her Ganda", "PJ Raval", "True Crime", "PJ Raval",
                {"impact": 84, "rating": 7.8, "festivals": 12}),
    Documentary("Lakbayan", "Jasmine Ng", "Indigenous Peoples", "Jasmine Ng",
                {"impact": 79, "rating": 7.5, "festivals": 9}),
    Documentary("War Is a Tender Thing", "Diana Markosian", "Conflict", "Diana Markosian",
                {"impact": 86, "rating": 8.1, "festivals": 11}),
    Documentary("The Cleaners", "Hans Block", "Digital Media", "Hans Block",
                {"impact": 89, "rating": 8.4, "festivals": 13})
]

short_films = [
    ShortFilm("Tokwifi", "Carla Pulido Ocampo", 20, "Best Short Film - QCinema"),
    ShortFilm("Nakaw", "Arvin Belarmino", 13, "Audience Choice Award"),
    ShortFilm("The Leaving", "Don Josephus Raphael Eblahan", 15, "Special Jury Prize"),
    ShortFilm("Pusong Bato", "Michael V.", 9, "Best Actor Award"),
    ShortFilm("Mga Anak ng Kamote", "Benedict Mique Jr.", 15, "Best Screenplay"),
    ShortFilm("Bakaw", "Rea Molina", 17, "Cinemalaya Best Short")
]


def show_options(item):
    if isinstance(item, Movie):
        print("1. Play\n2. Get Info\n3. Get Duration\n4. Watch Trailer\n5. Recommend Similar\n6. Back")
    elif isinstance(item, Series):
        print("1. Play\n2. Get Info\n3. Get Seasons\n4. Next Episode\n5. Skip Intro\n6. Back")
    elif isinstance(item, Documentary):
        print("1. Play\n2. Get Info\n3. Get Topic\n4. Narrate\n5. Show Statistics\n6. Back")
    elif isinstance(item, ShortFilm):
        print("1. Play\n2. Get Info\n3. Get Length\n4. Film Festival\n5. Show Award\n6. Back")


def interact_with_film(film):
    while True:
        show_options(film)
        action = input("Choose action: ")

        if action == "1":
            if film.isnotplaying:
                film.play()
            else:
                pauseit = input("It's currently playing. Pause it? (y/n): ").lower()
                if pauseit == "y":
                    film.pause()
                    print("Paused.")
                else:
                    print("Continuing playback.")
        elif action == "2":
            film.get_info()
        elif action == "3":
            if isinstance(film, Movie):
                film.get_duration()
            elif isinstance(film, Series):
                film.get_seasons()
            elif isinstance(film, Documentary):
                film.get_topic()
            elif isinstance(film, ShortFilm):
                film.get_length()
        elif action == "4":
            if isinstance(film, Movie):
                film.watch_trailer()
            elif isinstance(film, Series):
                film.next_episode()
            elif isinstance(film, Documentary):
                film.narrate()
            elif isinstance(film, ShortFilm):
                film.film_festival()
        elif action == "5":
            if isinstance(film, Movie):
                film.recommend_similar()
            elif isinstance(film, Series):
                film.skip_intro()
            elif isinstance(film, Documentary):
                film.show_statistics()
            elif isinstance(film, ShortFilm):
                film.show_award()
        elif action == "6":
            break
        else:
            print("Invalid option.")


def main():
    collections = {
        "1": ("Movies", movie_films),
        "2": ("TV Series", series_films),
        "3": ("Documentaries", documentary_films),
        "4": ("Short Films", short_films)
    }

    film_type = input('Select film type: \n("1" for Movies, "2" for Series, "3" for Documentaries, "4" for Short Films): ')
    if film_type not in collections:
        print("Invalid selection.")
        return

    category, films = collections[film_type]
    print(f"\n{category.upper()} COLLECTION:")
    for i, film in enumerate(films, 1):
        print(f"{i}. {film.title} by {film.director}")

    while True:
        choice = input("\nEnter film number to explore or 'q' to quit: ")
        if choice.lower() == 'q':
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(films):
                interact_with_film(films[idx])
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a number or 'q' to quit.")


if __name__ == "__main__":
    main()
