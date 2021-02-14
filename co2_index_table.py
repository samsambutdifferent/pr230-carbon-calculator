
def calculate_ingredients_co2_index(ingredientList, db):
    '''
        Sum together all co2 values to get total
    '''
    totalSum = 0
    for item in ingredientList:
        passed, value = calculate_ingredient_co2_index(item.get('name'), item.get('weight'), db)
        if passed:
            totalSum += value
            continue
        else:
            return False, totalSum
    return True, totalSum
        

def calculate_ingredient_co2_index(name, weight, db):
    '''
        Get c02 per gram value from co2 index table
    '''
    doc = db.collection(u'carbon_index').document(name).get()

    if doc.exists:
        doc_data = doc.to_dict()
        co2_index_per_g = doc_data.get('co2_index_per_g')
        co2ValperGram = co2_index_per_g * float(weight)
        return True, co2ValperGram
    else:
        print(f'No such document: {name}')
        return False, ''



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

    print("here2")

    doc = db.collection(u'co2e_index').document(name).get()
    
    if doc.exists:
        doc_data = doc.to_dict()
        print(doc_data)
        default = doc_data["default"]
        print(default)
        value = doc_data[default]

        co2e_val_per_gram = value * float(weight)

        return True, co2e_val_per_gram
    else:
        raise ValueError(f"no such document {name} in co2e_index table")
        return False, ''