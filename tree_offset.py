tree_details = {'tree_name' : 'maritime pine',
               'tree_cost':  17, #subscription
                'tree_co2e' : 300,
                'tree_life' : 13,
                'tree_yearly_c02e' : 23.1, #300/13
                'tree_co2e_per_pound' : 17.6} #300/17


def calculate_offset_cost(meal_co2e_kg, offset=1):
    """returns the number of meals off set by by kg of co2e
    """
    
    one_pound_offsets = tree_details['tree_co2e_per_pound'] * offset / meal_co2e_kg
    
    return one_pound_offsets