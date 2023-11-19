import json
from provigo_web_scraping import *
from instacart_web_scraping import *
import csv
from fuzzywuzzy import fuzz

# def get_list_ingredients(json_data):
#     '''returns a list of the names of all ingredients needed for one recipe'''
#     data = json.loads(json_data)

#     missed_ingredients = [ingredient['name'] for ingredient in data['recipes'][0]['missedIngredients']]

#     used_ingredients = [ingredient['name'] for ingredient in data['recipes'][0]['usedIngredients']]
#     all_ingredients = missed_ingredients + used_ingredients

#     print(all_ingredients)

#     return all_ingredients


def get_all_ingredients(recipe):
    """returns a list of the names of all ingredients needed for one recipe"""

    all_ingredients = []

    missed_ingredients = recipe.get("missedIngredients", [])
    for ingredient in missed_ingredients:
        name = ingredient.get("name")
        if name:
            all_ingredients.append(name)

    used_ingredients = recipe.get("usedIngredients", [])
    for ingredient in used_ingredients:
        name = ingredient.get("name")
        if name:
            all_ingredients.append(name)
    return all_ingredients


# Given a list of ingredients needed, output a dictionary with all of their info


def provigo_info(all_ingredients):
    """(list of strings) --> dict

    provigo_info(['egg', 'non-fat yogurt', 'baking soda'])

    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    provigo = {}

    for ingredient in all_ingredients:
        url = get_url_provigo(ingredient, driver)
        if not isinstance(url, str):
            continue
        name, info = get_info_provigo(url, driver)
        # If we cannot find a produce, don't include in the dictionary TODO null vs -1
        if name == "null":
            continue
        provigo.update({name: info})
    driver.quit()
    return provigo


# a = provigo_info(['egg', 'apple', 'patate'])


def convert_price_to_float(price_str):
    cleaned_price_str = price_str.replace("$", "").replace(",", ".")
    try:
        return float(cleaned_price_str)
    except ValueError:
        # Handle the case where the conversion fails (e.g., if the price is '-1' or other non-numeric value)
        return 0.0


def get_total_cost_grocery_list(grocery_list):
    """{{'Egg': {'Price': '4.29', 'Quantity': '100g', 'Url': 'bob.com'},

    {'Peanut': {'Price': '7', 'Quantity': '100g', 'Url': 'nuts.com'}} --> float

    """

    total_price = 0.0

    for item in grocery_list.values():
        if not isinstance(item["Price"], float):
            continue
        total_price += item["Price"]
    print(total_price)

    return round(total_price, 2)


def load_csv(file_path):
    # Load the CSV file into a dictionary with product names as keys and prices as values
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return {row[0].lower(): float(row[1]) for row in reader}


def find_similar_product(ingredient, products):
    # Use fuzzy matching to find a similar product
    best_match = None
    highest_score = 0
    for product in products:
        score = fuzz.ratio(ingredient.lower(), product.lower())
        if score > highest_score:
            highest_score = score
            best_match = product
    if highest_score < 0.6:
        return False
    return best_match


def get_total_cost_grocery_list_csv(grocery_list, csv_file, grocery_store, scrap):
    total_price = 0.0
    unfound_ingredients = []

    products_and_prices = load_csv(csv_file)

    # Go through each item in grocery list and search for it in the csv file, if not found, add to unfound_ingredients
    for ingredient in grocery_list:
        similar_product = find_similar_product(ingredient, products_and_prices.keys())

        if similar_product:
            total_price += products_and_prices[similar_product]
        else:
            unfound_ingredients.append(ingredient)

    # If we cannot find it then call get_total_cost_grocery_list(instacart_info(unfound_ingredients, grocery_store))
    if scrap and len(unfound_ingredients) < 4:
        total_price += get_total_cost_grocery_list(
            instacart_info(unfound_ingredients, grocery_store)
        )

    return round(total_price, 2)


# a = get_total_cost_grocery_list_csv(['mango', 'pineapple', 'kiwi', 'pesto sauce', "computer"], 'adonis.csv', 'adonis', False)
# print(a)


def get_cost_all_recipes(json_file):
    """recipe_prices = {id: price}"""

    data = json.loads(json_file)
    recipe_prices = {}
    recipe_book = data["recipes"]

    for recipe in recipe_book:
        recipe_id = recipe["id"]
        list_ingredients = get_all_ingredients(recipe)
        cost = get_total_cost_grocery_list(provigo_info(list_ingredients))
        recipe_prices.update({recipe_id: cost})

    return recipe_prices


def sort_increasing(recipe_prices):
    sorted_recipe_costs = dict(sorted(recipe_prices.items(), key=lambda item: item[1]))
    return sorted_recipe_costs


# recipe_costs = {637161: 25.01, 641411: 39.85, 637160: 2.01}

# print(sort_increasing(recipe_costs))

# print(get_cost_all_recipes(json_data))


# data = json.loads(json_data)

# # print(data["recipes"][0])

# # print(type(data["recipes"][0]))

# recipe_book = data['recipes']

# for recipe in recipe_book:

#     recipe_id = recipe['id']

#     print(recipe_id)
