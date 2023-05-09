# importowanie potrzebnych modułów
from collections import defaultdict
import random

# przykładowe dane o restauracjach (nazwa, lokalizacja, rodzaj kuchni, ocena, cena)
restaurants = [
    ("Restauracja A", "Warszawa", "Włoska", 4.5, 3),
    ("Restauracja B", "Kraków", "Meksykańska", 4.0, 2),
    ("Restauracja C", "Gdańsk", "Azjatycka", 4.8, 4),
    ("Restauracja D", "Wrocław", "Polska", 4.2, 3),
    ("Restauracja E", "Poznań", "Francuska", 4.6, 4),
    ("Restauracja F", "Kraków", "Włoska", 4.1, 2),
    ("Restauracja G", "Warszawa", "Azjatycka", 4.7, 4),
    ("Restauracja H", "Wrocław", "Meksykańska", 3.9, 2),
    ("Restauracja I", "Gdańsk", "Francuska", 4.4, 4),
    ("Restauracja J", "Poznań", "Polska", 4.3, 3)
]

# funkcja do wyboru najlepszej restauracji za pomocą algorytmu AHL
def choose_restaurant(location, cuisine, price_range, user_ratings):
    # przygotowanie słownika dla każdej restauracji, w celu przechowywania liczby trafień
    restaurants_hits = defaultdict(int)

    # liczba losowych prób do wyboru najlepszej restauracji
    num_trials = 100

    # pętla, która wywołuje AHL wielokrotnie i zlicza wyniki
    for i in range(num_trials):
        # losowe ustawienie wagi dla każdego kryterium
        location_weight = random.uniform(0, 1)
        cuisine_weight = random.uniform(0, 1)
        price_range_weight = random.uniform(0, 1)
        user_ratings_weight = random.uniform(0, 1)

        # AHL - przypisanie punktów dla każdej restauracji na podstawie wag
        for restaurant in restaurants:
            if restaurant[1] == location and restaurant[2] == cuisine and restaurant[4] == price_range:
                # punkty za trafienie kryteriów użytkownika
                hits = 1

                # punkty za ocenę użytkownika (1-5)
                hits += user_ratings_weight * restaurant[3]

                # punkty za każde kryterium wagowe
                hits += location_weight
                hits += cuisine_weight
                hits += price_range_weight

                # zwiększenie liczby trafień dla danej restauracji
                restaurants_hits[restaurant] += hits

    # wybór restauracji z najwyższą ilością trafień
    best_restaurant = max(restaurants_hits, key=restaurants_hits.get)

    # zwrócenie najlepszej restauracji
    return best_restaurant[0]


