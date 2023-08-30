from digidevice import location


def get_my_location() -> (float, float, float):
    """
    Retrieves the current geographic coordinates (latitude, longitude and altitude).

    Returns:
        tuple: A tuple containing the latitude, longitude and altitude as float values.
    """
    loc = location.Location()
    return loc.position


def main():
    print(get_my_location())


if __name__ == '__main__':
    main()


