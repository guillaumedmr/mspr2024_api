from geopy.geocoders import Nominatim

def ville_plus_proche(coordonnees):
    # Initialisation du géocodeur
    geolocator = Nominatim(user_agent="ville_plus_proche")

    # Récupération des coordonnées
    latitude, longitude = coordonnees

    # Recherche de la ville la plus proche
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    ville = location.raw['address'].get('city', '')
    if not ville:
        ville = location.raw['address'].get('town', '')
    if not ville:
        ville = location.raw['address'].get('village', '')
    if not ville:
        ville = location.raw['address'].get('municipality', '')
    if not ville:
        ville = location.raw['address'].get('county', '')

    return ville
