from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

# Spoonacular API key
SPOONACULAR = os.getenv("SPOONACULAR_API_KEY")

# Spoonacular API endpoint
SPOONACULAR_API_URL = "https://api.spoonacular.com/recipes/findByIngredients"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipes", methods=["POST"])
def get_recipes():
    if request.method == "POST":
        user_input = request.form["food_input"]
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
