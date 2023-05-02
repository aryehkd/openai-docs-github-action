def kmToMiles(val):
    """
    This function converts kilometers to miles.
    
    :param val: a numeric value representing the number of kilometers to be converted
    :type val: float
    :return: the equivalent number of miles as a float
    """
    conv_fac = 0.621371
    miles = val * conv_fac
    return miles

def milesToKm(val):
    """
    This function converts distances in miles to kilometers.
    
    Args:
        val (float): The distance in miles to be converted.
    
    Returns:
        float: The distance in kilometers after conversion.
    """
    conv_fac = 1.60934
    km = val * conv_fac
    return km
