from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

# Spoonacular
SPOONACULAR = os.getenv("SPOONACULAR_API_KEY")

# Spoonacular API endpoint
SPOONACULAR_API_URL = "https://api.spoonacular.com/recipes/findByIngredients"
SPOONACULAR_COMPLEX_SEARCH = "https://api.spoonacular.com/recipes/complexSearch"

@app.route("/recipesbyfood", methods=["POST"])
def get_recipe_by_food():
    if request.method == "POST":
        user_input = request.form["food_input"]

        params = {
            "apiKey": SPOONACULAR, # always required
            "query": user_input,
        }

        response = requests.get(SPOONACULAR_COMPLEX_SEARCH, params=params) # get recipes by food
        if response.status_code == 200:
            recipe_names = response.json()["results"] # id, foodname, image, imageType
            recipe_ids = list(map(lambda r: r['id'], recipe_names))
            recipe_ingredients = [requests.get(f"https://api.spoonacular.com/recipes/{ID}/ingredientWidget.json",
                                               {"apiKey": SPOONACULAR, "id": ID}).json() for ID in recipe_ids]
            name_by_ingredients = [{**recipe_id, **recipe_ingredient}
                                 for (recipe_id, recipe_ingredient) in zip(recipe_names, recipe_ingredients)]
            print(name_by_ingredients)
            return render_template("recipesbyfood.html", recipes=name_by_ingredients) # passed arguments MUST be jsons
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return f"Error: {response.status_code} - {response.text}"
        
    if request.method == "POST":
        user_input = request.form["ingredients_input"]
        print(f"user_input: '{user_input}'")

        # Call Spoonacular API to get recipes based on user input
        params = {
            "apiKey": SPOONACULAR, # always required
            "ingredients": user_input,
        }

        response = requests.get(SPOONACULAR_API_URL, params=params)

        if response.status_code == 200:
            recipes = response.json()
            print(f"recipes: {recipes}")
            return render_template("recipes.html", recipes=recipes)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return f"Error: {response.status_code} - {response.text}"


if __name__ == "__main__":
    app.run(debug=True)
