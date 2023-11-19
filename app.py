from flask import Flask, render_template, request, jsonify, redirect
from flask_caching import Cache
import requests
from dotenv import load_dotenv
import os
import image_recognition

load_dotenv()

# complex search: query -> title, id
# Search Recipes by Ingredients (findByIngredients): ingredients -> title, id, ingredients (all), likes
# Get Recipe Information (ID input): ID -> title, id, ingredients (all)


# Search recipes
# https://api.spoonacular.com/recipes/complexSearch
# query, cuisine, excludeCuisine, diet, intolerances, equipment, includeIngredients, excludeIngredients, type
# query: offset, number, results (contains title and id), totalResults

# Search recipes by ingredients
# https://api.spoonacular.com/recipes/findByIngredients
# id, image, imageType, likes, missedIngredientCount, missedIngredients, title, unusedIngredients, usedIngredientCount, usedIngredients
# query: ingredients, number, limitLicense, ranking, ignorePantry


app = Flask(__name__)


# Spoonacular
SPOONACULAR = os.getenv("SPOONACULAR_API_KEY")

# Spoonacular API endpoint
SPOONACULAR_COMPLEX_SEARCH = "https://api.spoonacular.com/recipes/complexSearch"
FIND_BY_INGREDIENTS_URL = "https://api.spoonacular.com/recipes/findByIngredients"
# "https://api.spoonacular.com/recipes/{id}/analyzedInstructions" # to add
# https://api.spoonacular.com/recipes/{id}/priceBreakdownWidget.json

# Use the "filesystem" cache type with a specified cache directory

cache = Cache(app, config={"CACHE_TYPE": "filesystem", "CACHE_DIR": "./cache"})
# cache = Cache(app, config={"CACHE_TYPE": "simple"})


@app.route("/")
def index():
    return render_template("index.html")


# use the max ready time because people wanna know how long it takes to cook shit

# https://spoonacular.com/food-api/docs#Summarize-Recipe
# add this to every recipe card
# then expand using some whatever thing that I can think of later


# todo: make there be 9 of them
# cached version for API savings + speediness
def get_recipes_api(ingredients, user_input):
    cached_response = cache.get(ingredients)
    if cached_response is not None:
        print(f"\n\n----- Serving response for {ingredients} from cache -----\n\n")
        return cached_response

    params = {
        "apiKey": SPOONACULAR,  # always required
        "ingredients": user_input,
    }

    response = requests.get(FIND_BY_INGREDIENTS_URL, params=params)
    if response.status_code == 200:
        # 'id', 'title', 'image', 'imageType', 'usedIngredientCount', 'missedIngredientCount',
        # 'missedIngredients', 'usedIngredients', 'unusedIngredients', 'likes'
        recipes = response.json()
        print(f"Caching recipes for {ingredients}")
        cache.set(ingredients, recipes)
        print(recipes)
        return recipes
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return f"Error: {response.status_code} - {response.text}"


@app.route("/recipes/<ingredient>", methods=["POST"])
def get_recipes(ingredient):
    print(ingredient)
    if request.method == "POST":
        user_input = request.form["ingredient_input"]
        print(f"user_input: '{user_input}'")
        recipes = get_recipes_api(ingredient, user_input)
        return render_template("recipes.html", recipes=recipes)


def recipe_for_image_caption_api(user_input):
    cached_response = cache.get(user_input)
    if cached_response is not None:
        print(f"\n\n----- Serving response for {user_input} from cache -----\n\n")
        return cached_response

    print(f"Getting recipes for {user_input} (not cached)")
    params = {
        "apiKey": SPOONACULAR,  # always required
        "query": user_input,  # the one they chose as most likely from among the predictions
        "addRecipeInformation": "true",
    }
    response = requests.get(SPOONACULAR_COMPLEX_SEARCH, params=params)

    if response.status_code == 200:
        recipes = response.json()

        # also cache the complex search results
        print(f"Caching recipes for {user_input}")
        cache.set(user_input, recipes)

        recipes = recipes["results"]  # id, title, image, imageType
        print("recipes:", recipes)
        recipe_ids = list(map(lambda r: r["id"], recipes))
        recipes_info = [get_id_info(ID) for ID in recipe_ids]
        print(f"Caching recipes_info for {user_input}")
        cache.set(user_input, recipes_info)

        return recipes_info
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return f"Error: {response.status_code} - {response.text}"


def cplx_search_api(user_input):
    cached_response = cache.get(user_input)


def get_id_info(id):
    # cached_response = cache.get(str(id))
    cached_response = None
    print(f"The cache name is {str(id)} which gets saved as `idk`")
    if cached_response is not None:
        print(f"\n\n----- Serving response for {str(id)} from cache -----\n\n")
        return cached_response

    params = {
        "apiKey": SPOONACULAR,  # always required
        "id": id,
    }
    response = requests.get(
        f"https://api.spoonacular.com/recipes/{id}/information", params=params
    )
    if response.status_code == 200:
        recipe_info = response.json()
        print(f"Caching recipe_info for {id}")
        # cache.set(str(id), recipe_info)
        return recipe_info
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return f"Error: {response.status_code} - {response.text}"


@app.route("/recipesbyimage", methods=["POST"])
def recipe_for_image_caption():
    if request.method == "POST":
        data = request.get_json()
        user_input = data.get("food_input")
        recipes_info = recipe_for_image_caption_api(user_input)

        # get recipes by food
        return render_template("recipesbyfood.html", recipes=recipes_info)


# TODO: integrate this into the search
cuisines = [
    "African",
    "Asian",
    "American",
    "British",
    "Cajun",
    "Caribbean",
    "Chinese",
    "Eastern European",
    "European",
    "French",
    "German",
    "Greek",
    "Indian",
    "Irish",
    "Italian",
    "Japanese",
    "Jewish",
    "Korean",
    "Latin American",
    "Mediterranean",
    "Mexican",
    "Middle Eastern",
    "Nordic",
    "Southern",
    "Spanish",
    "Thai",
    "Vietnamese",
]


@app.route("/recipesbyfood/<query>", methods=["POST"])
@cache.cached()  # TODO: implement persistent caching for the data but not the html
def get_recipe_by_food(query):
    print(f"query: `{query}`")
    if request.method == "POST":
        user_input = request.form["food_input"]

        params = {
            "apiKey": SPOONACULAR,  # always required
            "query": user_input,
            "addRecipeInformation": "true",
        }

        # get recipes by food
        response = requests.get(SPOONACULAR_COMPLEX_SEARCH, params=params)
        if response.status_code == 200:
            print("raw json:")
            print(response.json())
            print("raw json:")
            recipes = response.json()["results"]  # id, title, image, imageType
            print("recipes:", recipes)
            recipe_ids = list(map(lambda r: r["id"], recipes))
            recipes_info = [
                requests.get(
                    f"https://api.spoonacular.com/recipes/{ID}/information",
                    {"apiKey": SPOONACULAR, "id": ID},
                ).json()
                for ID in recipe_ids
            ]
            return render_template(
                "recipesbyfood.html", recipes=recipes_info
            )  # passed arguments MUST be jsons
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return f"Error: {response.status_code} - {response.text}"


@app.route("/upload", methods=["POST"])
def upload():
    # get the uploaded file
    file = request.files["file"]

    if file.filename != "":
        filepath = f"./data/uploads/{file.filename}"
        os.makedirs("./data/uploads", exist_ok=True)
        print(f"Saving file to `{filepath}`")
        file.save(filepath)

        # Your existing code to process the image
        response = image_recognition.process_and_caption(filepath)
        if response is None:
            return "Error: No response from image_recognition.process_and_caption"
        elif "segmentation_results" not in response:
            return "Error: No segmentation_results in response from image_recognition.process_and_caption"

        print("response:")
        print(response)
        seg_results = response["segmentation_results"]  # type: ignore

        unique_responses = remove_duplicates(seg_results)
        print("responses:")
        print(unique_responses)
        print("end responses")

        return render_template("predict.html", dishes=unique_responses)
    else:
        return "Error: No file selected"


def remove_duplicates(predictions):
    # Create a dictionary to store unique food items with the highest probability
    unique_food_items = {}

    for prediction in predictions:
        food_name = prediction["recognition_results"][0]["name"]
        prob = prediction["recognition_results"][0]["prob"]

        # Check if the food item is already in the dictionary
        if food_name in unique_food_items:
            # If the current probability is higher, update the dictionary
            if prob > unique_food_items[food_name]["prob"]:
                unique_food_items[food_name] = {"prob": prob, "prediction": prediction}
        else:
            unique_food_items[food_name] = {"prob": prob, "prediction": prediction}

    # Extract the unique predictions from the dictionary
    unique_predictions = [item["prediction"] for item in unique_food_items.values()]

    return unique_predictions


@app.route("/submit_selection", methods=["POST"])
def submit_selection():
    if request.method == "POST":
        # get the selected dish
        selected_dish = request.form["selected_dish"]
        print(f"selected_dish: '{selected_dish}'")

        # Call Spoonacular API to get recipes based on user input
        params = {
            "apiKey": SPOONACULAR,  # always required
            "ingredients": selected_dish,
        }

        response = requests.get(FIND_BY_INGREDIENTS_URL, params=params)

        if response.status_code == 200:
            recipes = response.json()
            print(f"recipes: {recipes}")
            return render_template("recipes.html", recipes=recipes)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return f"Error: {response.status_code} - {response.text}"


if __name__ == "__main__":
    app.run(debug=True)
