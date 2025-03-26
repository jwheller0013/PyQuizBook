def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    pass  # implement me
    return dict(zip(keys, values))

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    pass  # implement me
    d3 = d1 | d2
    return d3

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    #
    pass  # implement me
    result = {}
    for i in lst:
        result[i] = d1
    return result

def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #
    pass  # implement me
    return {x: datadict[x] for x in keylist}

def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    pass
    for x in keylist:
        datadict.pop(x)
    return datadict

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    pass
    return key in datadict or key in datadict.values()

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    pass
    return min(ddd, key=ddd.get)

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    pass
    return max(ddd, key=ddd.get)