from flask import Flask, render_template, request
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
        
cache = Cache(app, config={"CACHE_TYPE": "simple"})


@app.route("/")
def index():
    return render_template("index.html")

# use the max ready time because people wanna know how long it takes to cook shit

@app.route("/recipes", methods=["POST"])
@cache.cached(timeout=7200)
def get_recipes():
    if request.method == "POST":
        user_input = request.form["ingredients_input"]
        print(f"user_input: '{user_input}'")

        # Call Spoonacular API to get recipes based on user input
        params = {
            "apiKey": SPOONACULAR, # always required
            "ingredients": user_input,
        }

        response = requests.get(FIND_BY_INGREDIENTS_URL, params=params)

        if response.status_code == 200:
            # 'id', 'title', 'image', 'imageType', 'usedIngredientCount', 'missedIngredientCount',
            # 'missedIngredients', 'usedIngredients', 'unusedIngredients', 'likes'
            recipes = response.json()
            print(f"recipes: {recipes}")
            return render_template("recipes.html", recipes=recipes)
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return f"Error: {response.status_code} - {response.text}"


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
            recipes = response.json()["results"] # id, title, image, imageType
            print("recipes:", recipes)
            recipe_ids = list(map(lambda r: r['id'], recipes))
            recipes_info = [requests.get(f"https://api.spoonacular.com/recipes/{ID}/information",
                                               {"apiKey": SPOONACULAR, "id": ID}).json() for ID in recipe_ids]
            return render_template("recipesbyfood.html", recipes=recipes_info) # passed arguments MUST be jsons
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return f"Error: {response.status_code} - {response.text}"


@app.route("/upload", methods=["POST"])
@cache.cached(timeout=(3600 * 12)) #1hr * 12 # TODO: update before deployment
def upload():
    # get the uploaded file
    file = request.files["file"]


    if file.filename != "":
        filepath = f"./data/uploads/{file.filename}"
        os.makedirs("./data/uploads", exist_ok=True)
        print(f"Saving file to `{filepath}`")
        file.save(filepath)

        cache_key = f'process_image_{file.filename}'

        if cache.has(cache_key):
            print(f"Result for {file.filename} served from cache.")
            response = cache.get(cache_key)
        else:
            print(f"Computing result for {file.filename} and storing it in the cache.")
            
            # Your existing code to process the image
            response = image_recognition.process_and_caption(filepath)
            if response is None:
                return "Error: No response from image_recognition.process_and_caption"
            elif "segmentation_results" not in response:
                return "Error: No segmentation_results in response from image_recognition.process_and_caption"
            seg_results = response["segmentation_results"] # type: ignore
        
            unique_responses = []
        
            for item in seg_results:
                recognition_results = item["recognition_results"]
                if recognition_results:
                    max_prob_response = max(recognition_results, key=lambda x: x['prob'])
                    unique_responses.append(max_prob_response)

            # Store the result in the cache
            cache.set(cache_key, unique_responses, timeout=3600)  # Cache timeout is in seconds (1 hour in this example)

        # response = image_recognition.process_and_caption(filepath)
        # response contains a list of items which each have their own "recognition_results" key
        seg_results = response["segmentation_results"] # type: ignore

        unique_responses = []

        for item in seg_results:
            recognition_results = item["recognition_results"] # type: ignore
            if recognition_results:
                max_prob_response = max(recognition_results, key=lambda x: x["prob"]) # type: ignore
                unique_responses.append(max_prob_response)

        print("unique_responses:")
        for response in unique_responses:
            print(response)
        print("end unique_responses")

        return render_template("predict.html", dishes=unique_responses)
    else:
        return "Error: No file selected"


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
