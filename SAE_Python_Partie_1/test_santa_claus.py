def test_dictionary_cities():
    assert dictionary_cities([])=={}
    assert dictionary_cities(["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63])=={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466715, 'Lille': 203.67224282542662}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367429894, 'Lille': 558.5472363339595}, 'Marseille': {'Paris': 661.8616554466715, 'Lyon': 275.87965367429894, 'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}
    print("Test OK")
test_dictionary_cities()


def test_distance_cities():
    distances={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466715,
                    'Lille': 203.67224282540448}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367429894, 
                    'Lille': 558.5472363339516}, 'Marseille': {'Paris': 661.8616554466715, 'Lyon': 275.87965367429894, 
                    'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282540448, 'Lyon': 558.5472363339516, 
                    'Marseille': 834.0220261600157}}
    assert distance_cities ("Marseille", "Paris" ,distances)==661.8616554466852
    assert distance_cities("Villetaneuse", "Paris", distances)== -1
    assert distance_cities("Paris", "Paris", distances)==0
    print ("TEST : OK !")
test_distance_cities()



def test_tour_length():
    distances={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466715,
                    'Lille': 203.67224282540448}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367429894, 
                    'Lille': 558.5472363339516}, 'Marseille': {'Paris': 661.8616554466715, 'Lyon': 275.87965367429894, 
                    'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282540448, 'Lyon': 558.5472363339516, 
                    'Marseille': 834.0220261600157}}
    
    assert tour_length([ "Paris", "Lyon"],distances)==789.0113668595314
    assert tour_length(["Paris", "Lyon", "Marseille", "Lille"],distances)==1708.0796060895232
    print ("TEST : OK !")
test_tour_length()


def test_closest_city():
    distances={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466715,
                    'Lille': 203.67224282540448}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367429894, 
                    'Lille': 558.5472363339516}, 'Marseille': {'Paris': 661.8616554466715, 'Lyon': 275.87965367429894, 
                    'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282540448, 'Lyon': 558.5472363339516, 
                    'Marseille': 834.0220261600157}}
    
    assert closest_city("Paris",["Marseille", "Lyon"], distances)==1
    assert closest_city("Paris",["Lille", "Lyon"],distances)==0
    print ("TEST : OK !")  
test_closest_city()


def test_tour_from_closest_city():
    distances={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466715,
                    'Lille': 203.67224282540448}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367429894, 
                    'Lille': 558.5472363339516}, 'Marseille': {'Paris': 661.8616554466715, 'Lyon': 275.87965367429894, 
                    'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282540448, 'Lyon': 558.5472363339516, 
                    'Marseille': 834.0220261600157}}
    
    assert tour_from_closest_city("Marseille",distances)==['Marseille', 'Lyon', 'Paris', 'Lille']
    assert tour_from_closest_city("Paris",distances)==['Paris', 'Lille', 'Lyon', 'Marseille']
    print ("TEST : OK !")  
test_tour_from_closest_city()



def test_best_tour_from_closest_city():
    assert best_tour_from_closest_city({'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466715,
                    'Lille': 203.67224282540448}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367429894, 
                    'Lille': 558.5472363339516}, 'Marseille': {'Paris': 661.8616554466715, 'Lyon': 275.87965367429894, 
                    'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282540448, 'Lyon': 558.5472363339516, 
                    'Marseille': 834.0220261600157}})
    print("Test OK")
test_best_tour_from_closest_city()



def test_reverse_part_tour():
    tour=["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"]
    
    assert reverse_part_tour(tour, 0, 1)==[ "Belfort", "Agen", "Cahors", "Dijon", "Épinay", "Fréjus","Grenoble", "Hyères"]
    assert reverse_part_tour(tour, 2, 5)==["Agen", "Belfort", "Fréjus", "Épinay", "Dijon", "Cahors"," Grenoble", "Hyères"]
    print ("TEST : OK !")  
test_reverse_part_tour()



def test_inversion_length_diff():
    distances={'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466715,
                    'Lille': 203.67224282540448}, 'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367429894, 
                    'Lille': 558.5472363339516}, 'Marseille': {'Paris': 661.8616554466715, 'Lyon': 275.87965367429894, 
                    'Lille': 834.0220261600157}, 'Lille': {'Paris': 203.67224282540448, 'Lyon': 558.5472363339516, 
                    'Marseille': 834.0220261600157}}
    tour=["Marseille", "Lyon", "Paris", "Lille"]
    ind_b=1
    ind_e=2
    
    assert inversion_length_diff(distances, tour, ind_b, ind_e) == -740-8569952808871
    print ("TEST : OK !")
test_inversion_length_diff()



def test_better_inversion():
    assert better_inversion({
    'Marseille': {'Lyon': 275.87965367429894, 'Paris': 661.8616554466715, 'Lille': 834.0220261600157},
    'Lyon': {'Marseille': 275.87965367429894, 'Paris': 394.5056834297657, 'Lille': 558.5472363339516},
    'Paris': {'Marseille': 661.8616554466715, 'Lyon': 394.5056834297657, 'Lille': 203.67224282540448},
    'Lille': {'Marseille': 834.0220261600157, 'Lyon': 558.5472363339516, 'Paris': 203.67224282540448}
}, ['Marseille', 'Lyon', 'Lille', 'Paris'])==False
    assert better_inversion({
    'Marseille': {'Lyon': 275.87965367429894, 'Paris': 661.8616554466715, 'Lille': 834.0220261600157},
    'Lyon': {'Marseille': 275.87965367429894, 'Paris': 394.5056834297657, 'Lille': 558.5472363339516},
    'Paris': {'Marseille': 661.8616554466715, 'Lyon': 394.5056834297657, 'Lille': 203.67224282540448},
    'Lille': {'Marseille': 834.0220261600157, 'Lyon': 558.5472363339516, 'Paris': 203.67224282540448}
}, ["Marseille", "Paris", "Lyon", "Lille"])

print("Test OK")
test_better_inversion()




def test_best_obtained_with_inversions():
    assert best_obtained_with_inversions({
    'Marseille': {'Lyon': 275.87965367429894, 'Paris': 661.8616554466715, 'Lille': 834.0220261600157},
    'Lyon': {'Marseille': 275.87965367429894, 'Paris': 394.5056834297657, 'Lille': 558.5472363339516},
    'Paris': {'Marseille': 661.8616554466715, 'Lyon': 394.5056834297657, 'Lille': 203.67224282540448},
    'Lille': {'Marseille': 834.0220261600157, 'Lyon': 558.5472363339516, 'Paris': 203.67224282540448}
}, ["Marseille", "Paris", "Lyon", "Lille"])==["Marseille", "Lyon", "Lille", "Paris"]

    print("Test OK")
test_best_obtained_with_inversion()



