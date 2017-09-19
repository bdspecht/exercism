def is_isogram(string):
    if len(set(string)) == len(string):
        return True
    else:
        return False
