
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
        co2ValperGram = co2_index_per_g * weight
        return True, co2ValperGram
    else:
        print(f'No such document: {name}')
        return False, ''