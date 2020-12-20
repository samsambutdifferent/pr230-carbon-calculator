
def calculate_equivalent_values(carbon_value, db):
    '''intakes carbon value returns carbon equivalents
        params:
            type: float
        return:
            type: array[dict{}]
            format: [{"name": "name of equivalent type", "value": 20, "units": "equivalnt units"},...]
    '''
    equivalents = []
    docs = db.collection(u'equivalency_conversion_factors').stream()
    for doc in docs:
        dic = doc.to_dict()
        equivalents.append({'value': dic.get('value') * carbon_value, 'name': dic.get('type'), 'unit': dic.get('unit')})

    return(equivalents)