from flask import Flask, request
from flask_cors import CORS
from co2_index_table import return_all_available_ingredients, calculate_food_item_co2_index, calculate_ingredient_co2_index

app = Flask(__name__)
# cors = CORS(app, resources={r"*": {"origins": "https://landing-page-xu26by35cq-ew.a.run.app"}})
# cors = CORS(app, resources={r"*": {"origins": "https://pr230-ui-xu26by35cq-ew.a.run.app"}})
cors = CORS(app, resources={r"*": {"origins": "http://localhost:8080"}})


@app.route('/', methods=['POST'])
def calculate_carbon_index_of_food_item():
    """returns the carbon weight in grams of a single food item
        params:
            type: dict
            fomat: {"name": "ingredient name", "weight"; 0.5}
        return:
            type: str
            format: "0.2"
    """
    try:
        req = request.get_json()
        ingredient = req.get('name', '')
        weight = req.get('weight', 0)

        if ingredient != '' and weight != 0:
            return str(calculate_ingredient_co2_index(ingredient, weight))
        else:
            return "Record not found", 400 

    except Exception as e:
        return f"unable to calculate food item index, error {str(e)}"


@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    try:
        req_data = request.get_json()
        print(req_data)

        #ingredients = return_all_available_ingredients()
        
        return ""
        #return { i : ingredients[i] for i in range(0, len(ingredients) ) }
    except Exception as e:
        return f"unable to get ingredients list, error: {str(e)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)                