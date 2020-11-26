from flask import Flask, request
from flask_cors import CORS
from co2_index_table import calculate_ingredients_co2_index, calculate_ingredient_co2_index
import os
from dotenv import load_dotenv
load_dotenv()
UI_URL = os.getenv("UI_URL")

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": UI_URL}})


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
            passed, value = calculate_ingredients_co2_index(ingredients)
            if passed:
                return str(value), 200
            else:
                return "Record not found", 400 
        else:
            return "Malformed request", 400 

    except Exception as e:
        print(f"unable to calculate food item index, ERROR: {str(e)}")
        return f"unable to calculate food item carbon index"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)                