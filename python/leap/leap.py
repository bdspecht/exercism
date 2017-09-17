def is_leap_year(year):
    '''
    Args:
      year - Year to check
    Returns:
      True/False depending on if the provider year is considered a leap year
    ''' 
    # Every year that is evenly divisible by 4 and not divisible by 100
    if year % 4 == 0 and year % 100 != 0:
        return True 
    # Unless divisible by 400
    elif year % 400 == 0:
        return True
    else:
        return False

    
