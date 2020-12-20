from flask import Flask, request, jsonify
from flask_cors import CORS
from co2_index_table import calculate_ingredients_co2_index, calculate_ingredient_co2_index
from co2_equivalents import calculate_equivalent_values
import os
from dotenv import load_dotenv
load_dotenv()
UI_URL = os.getenv("UI_URL")

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": UI_URL}})

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()



@app.route('/', methods=['POST'])
def calculate_carbon_index():
    """returns the carbon weight in grams of a list of food items
        params:
            type: list[dict]
            fomat: [{"name": "ingredient name", "weight"; 0.5}, ..]
        return:
            type: str
            format: "0.2"
    """
    try:
        ingredients = request.get_json()
        if len(ingredients) > 0:
            passed, value = calculate_ingredients_co2_index(ingredients, db)
            if passed:
                return str(value), 200
            else:
                return "Record not found", 400 
        else:
            return "Malformed request", 400 

    except Exception as e:
        print(f"unable to calculate food item index, ERROR: {str(e)}")
        return f"unable to calculate food item carbon index"


@app.route('/calculateequivalents', methods=['POST'])
def calculate_carbon_equivalents():
    """intakes carbon value returns carbon equivalents
        params:
            type: float
        return:
            type: {equivalents:[{},...]}
            format: {equivalents:[{"name": "name of equivalent type", "value": 20, "units": "equivalnt units"},...]}
    """
    try:
        carbon_value = request.get_json()
        return jsonify(equivalents = calculate_equivalent_values(carbon_value, db))
    except Exception as e:
        print(f"unable to calculate equivalent values: {str(e)}")
        return f"unable to calculate equivalent values"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)                