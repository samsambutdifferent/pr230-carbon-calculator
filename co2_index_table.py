
def calculate_ingredients_co2e_index(ingredientList, db):
    '''
        Sum together all co2 values to get total
    '''
    totalSum = 0
    for item in ingredientList:
        passed, value = calculate_co2e_value(db, item.get('name'), item.get('weight'))
        if passed:
            totalSum += value
            continue
        else:
            return False, totalSum
    return True, totalSum
        


def calculate_co2e_value(db, name, weight, select_type=None):
    '''
        Get c02 per gram value from co2 index table
    '''

    select_type = select_type if select_type is not None else "default"

    doc = db.collection(u'co2e_index').document(name).get()
    
    if doc.exists:
        doc_data = doc.to_dict()
        default = doc_data["default"]
        value = doc_data[default]

        co2e_val_per_gram = value * float(weight)

        return True, co2e_val_per_gram
    else:
        raise ValueError(f"no such document {name} in co2e_index table")
        return False, ''