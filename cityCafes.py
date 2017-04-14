"""
A small program that returns cafes that are opened given an input latitude and longitude pair. This program pulls data
from google maps api. authKeys is a file with user API keys and called in get_places when making a get request from googleapis.
"""
import authKeys as aK
import requests

key = aK.google_key

sydney = '-33.8670522,151.1957362'
logan_square = '41.929067, -87.707344'
pilsen = '41.857363, -87.666877'
loop = '41.929067, -87.707344'
vancouver = '49.258343, -123.101075'
placeTypes = ['cafe', 'food', 'gallery']


def get_places(location, typeOfPlace):
    """
    Method that returns google places based on a latidude/longitude pair.
    :param location: A latitude and longitude pair
    :param typeOfPlace: Key word on what kind of place user wants returned from get request
    :return: dictionary of places from googleapis
    """
    request_uri = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + location +'&rankby=distance&types=' + typeOfPlace + '&key=' + key
    xmldata = requests.get(request_uri)
    places = xmldata.json()['results']
    return places


def get_open_now(place):
    """
    Method that checks to see if place is opened.
    :param place: place in the form of a dictionary returned from googleapis
    :return: name of place and its address if opened and returns name of place and " is closed." if not opened.
    """
    if 'opening_hours' in place.keys():
        if 'open_now' in place['opening_hours'].keys():
            if place['opening_hours']['open_now'] == True:
                return place['name'] + ', ' + place['vicinity']
            else:
                return place['name'] + " is closed."


"""Small program that searches for cafes in the Pilsen area and returns if they are opened"""
pilsen_cafes = get_places(pilsen, 'cafe')
for cafe in pilsen_cafes:
    retstr = get_open_now(cafe)
    if retstr:
        print retstr