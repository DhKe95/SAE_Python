def distance(long1, lat1, long2, lat2):
    """retourne la distance entre les points (long1, lat1) et (long2, lat2)"""
    lat1 = d2r(lat1)
    long1 = d2r(long1)
    lat2 = d2r(lat2)
    long2 = d2r(long2)
    R = 6370.7
    d = R*arccos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long2-long1))
    return d





#Question 1

def dictionary_cities(villes):
    distances_villes = {}
    i = 0
    while i < len(villes):
        city1 = villes[i]
        long1, lat1 = villes[i + 1], villes[i + 2]
        distances_villes[city1] = {}

        j = 0
        while j < len(villes):
            if i != j:
                city2 = villes[j]
                long2, lat2 = villes[j + 1], villes[j + 2]
                dist = distance(long1, lat1, long2, lat2)
                distances_villes[city1][city2] = dist

            j += 3

        i += 3

    return distances_villes




#Question 2

def distance_cities(city1, city2, distances):

    if city1 in distances:

        if city2 in distances[city1]:

            return distances[city1][city2]


    return -1.0
    





#Question 3

def tour_length(tour, distances):

    if len(tour) < 2:
        return 0.0

    total_length = 0.0

    i = 0
    while i < len(tour) - 1:
        total_length += distance_cities(tour[i], tour[i + 1], distances)
        i += 1

    first_city = tour[0]
    last_city = tour[-1]
    total_length += distance_cities(last_city, first_city, distances)

    return total_length







#Question 5

def closest_city(city, cities, distances):
    
    if city not in distances or not cities:
        return -1

    min_distance = float('inf')
    closest_index = -1
    index = 0

    while index < len(cities):
        other_city = cities[index]
        if other_city in distances[city]:
            distance = distances[city][other_city]
            if distance < min_distance:
                min_distance = distance
                closest_index = index
        index += 1

    return closest_index



#Question 6

def tour_from_closest_city(start_city, distances):
    tour = [start_city]

    while len(tour) < len(distances):
        current_city = tour[-1]
        

        min_distance = float('inf')
        closest_city = None
        for city in distances[current_city]:
            if city not in tour:
                distance = distances[current_city][city]
                if distance < min_distance:
                    min_distance = distance
                    closest_city = city
        

        tour.append(closest_city)

    return tour





#QUESTION 7 

def best_tour_from_closest_city(distances):
    all_tours = []
    cities = list(distances.keys())

    i = 0
    while i < len(cities):
        start_city = cities[i]
        tour = tour_from_closest_city(start_city, distances)
        all_tours.append(tour)
        i += 1

    best_tour = all_tours[0]
    min_length = tour_length(best_tour, distances)

    i = 1
    while i < len(all_tours):
        current_length = tour_length(all_tours[i], distances)
        if current_length < min_length:
            best_tour = all_tours[i]
            min_length = current_length
        i += 1

    return best_tour







#QUESTION 9

def reverse_part_tour(tour, ind_b, ind_e):
    if ind_b < 0 or ind_e >= len(tour) or ind_b >= ind_e:

        return


    tour[ind_b:ind_e + 1] = reversed(tour[ind_b:ind_e + 1])





#QUESTION 10

def inversion_length_diff(distances, tour, ind_b, ind_e):

    if ind_b < 0 or ind_e >= len(tour) or ind_b >= ind_e:
        print("Indices invalides")
        return 


    tour_copie = tour.copy()


    while ind_b < ind_e:
        tour_copie[ind_b], tour_copie[ind_e] = tour_copie[ind_e], tour_copie[ind_b]
        ind_b += 1
        ind_e -= 1


    longueur_originale = long_tour(villes, tour)


    longueur_modifiee = long_tour(villes, tour_copie)


    return longueur_originale - longueur_modifiee





#QUESTION 11

def better_inversion(distances, tour):
    i = 0
    improved = False

    while i < len(tour) - 1 and not improved:
        j = i + 1

        while j < len(tour):

            diff = inversion_length_diff(distances, tour, i, j)


            if diff > 0:
                tour[i:j + 1] = reversed(tour[i:j + 1])
                improved = True

            j += 1

        i += 1

    return improved, tour.copy()





#QUESTION 12


def best_obtained_with_inversions(distances, tour):
    nb_inversions = 0
    improved = True

    while improved:
        improved = False
        best_diff = 0

        for ind_b in range(len(tour)):
            for ind_e in range(ind_b + 1, len(tour)):
                diff = inversion_length_diff(distances, tour, ind_b, ind_e)

                if diff > best_diff:
                    best_diff = diff
                    best_indices = (ind_b, ind_e)
                    improved = True

        if improved:
            ind_b, ind_e = best_indices
            # Appliquer l'inversion qui a donné la meilleure amélioration
            tour[ind_b:ind_e + 1] = reversed(tour[ind_b:ind_e + 1])
            nb_inversions += 1

    return nb_inversions, tour



