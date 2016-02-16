def get_keys(d):
    if d.non_matching_keys == None:
        return d.dict_obj.keys()
    return list(set(d.dict_obj.keys()) - set(d.non_matching_keys))

class Dict(object):

    def __init__(self, dict_obj, non_matching_keys=None):
        self.dict_obj = dict_obj 
        self.non_matching_keys = non_matching_keys

    def __eq__(self, other):
        my_keys = get_keys(self)
        other_keys = get_keys(other)

        if sorted(my_keys) != sorted(other_keys):
            return False
        
        for k in my_keys:
            v1 = self.dict_obj[k]
            v2 = other.dict_obj[k]

            if v1 != v2:
                return False

        return True
    
    def __ne__(self, other):
        return not (self.__eq__(other))
