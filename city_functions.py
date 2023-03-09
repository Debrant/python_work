def get_city_listing(city, country, population=0):
    """Generate a neatly formated name."""
    if population:
        city_listing = city.title() + ", " + country.title() + ", Population: " + str(population) 
    else:
        city_listing = city.title() + ", " + country.title()
    return city_listing
