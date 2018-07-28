country = ['England', 'France', 'Netherlands', 'Spain', 'Italy', 'Denmark', 'Germany', 'Poland', 'Norway', 'Sweden']
city = ['London', 'Paris', 'Amsterdam', 'Madrid', 'Roma', 'Copenhagen', 'Berlin', 'Warsaw', 'Oslo', 'Stockholm']


place = input("Check if your place is in one of these lists!")
if place == city or country:
    if place in country and city:
        print("This place is in both the lists!")
    elif place in country:
        print("This place is in list of countries.")
    elif place in city:
        print("This place is in list of cities.")
    elif place not in country or city:
        print("No list for this place")
    else:
        print("i don't know.")
