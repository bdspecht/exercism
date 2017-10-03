'''
Function that checks if a given string is an isogram
'''

def is_isogram(string):
    '''
    Args:
        string - String to check
    Returns:
        True or False if the string being checked is considered an isogram
    '''
    string_list = [c.lower() for c in string if c.isalnum()]

    return len(set(string_list)) == len(string_list)
