import geocoder
def get_my_location()->(float, float):
    """
    Returns the latitude and longitude of the user's current location.
    :return: [float, float]
    :rtype: list
    """
    g = geocoder.ip('me')
    return g.current_result.latlng

def main():
    print(get_my_location())

if __name__ == '__main__':
    main()


