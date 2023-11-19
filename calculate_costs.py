import json
from provigo_web_scraping import *
from instacart_web_scraping import *

json_data = """{
   "recipes":[
      {
         "id":637161,
         "title":"Carrot and Banana Snacking Cake",
         "image":"https://spoonacular.com/recipeImages/637161-312x231.jpg",
         "imageType":"jpg",
         "usedIngredientCount":2,
         "missedIngredientCount":5,
         "missedIngredients":[
            {
               "id":1123,
               "amount":1.0,
               "unit":"large",
               "unitLong":"large",
               "unitShort":"large",
               "aisle":"Milk, Eggs, Other Dairy",
               "name":"egg",
               "original":"1 large egg",
               "originalName":"egg",
               "meta":[
                  
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/egg.png"
            },
            {
               "id":1001116,
               "amount":0.5,
               "unit":"cup",
               "unitLong":"cups",
               "unitShort":"cup",
               "aisle":"Milk, Eggs, Other Dairy",
               "name":"non-fat yogurt",
               "original":"1/2 cup non-fat plain yogurt",
               "originalName":"non-fat plain yogurt",
               "meta":[
                  "plain"
               ],
               "extendedName":"plain non-fat yogurt",
               "image":"https://spoonacular.com/cdn/ingredients_100x100/plain-yogurt.jpg"
            },
            {
               "id":18372,
               "amount":1.0,
               "unit":"teaspoon",
               "unitLong":"teaspoon",
               "unitShort":"tsp",
               "aisle":"Baking",
               "name":"baking soda",
               "original":"1 teaspoon baking soda",
               "originalName":"baking soda",
               "meta":[
                  
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/white-powder.jpg"
            },
            {
               "id":2010,
               "amount":1.0,
               "unit":"teaspoon",
               "unitLong":"teaspoon",
               "unitShort":"tsp",
               "aisle":"Spices and Seasonings",
               "name":"cinnamon",
               "original":"1 teaspoon cinnamon",
               "originalName":"cinnamon",
               "meta":[
                  
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/cinnamon.jpg"
            },
            {
               "id":9299,
               "amount":0.5,
               "unit":"cup",
               "unitLong":"cups",
               "unitShort":"cup",
               "aisle":"Produce",
               "name":"raisins",
               "original":"1/2 cup raisins",
               "originalName":"raisins",
               "meta":[
                  
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/raisins.jpg"
            }
         ],
         "usedIngredients":[
            {
               "id":9040,
               "amount":1.0,
               "unit":"large",
               "unitLong":"large",
               "unitShort":"large",
               "aisle":"Produce",
               "name":"banana",
               "original":"1 large banana",
               "originalName":"banana",
               "meta":[
                  
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/bananas.jpg"
            },
            {
               "id":11124,
               "amount":1.0,
               "unit":"cup",
               "unitLong":"cup",
               "unitShort":"cup",
               "aisle":"Produce",
               "name":"carrots",
               "original":"1 cup carrots",
               "originalName":"carrots",
               "meta":[
                  
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"
            }
         ],
         "unusedIngredients":[
            
         ],
         "likes":3
      },
      {
         "id":641411,
         "title":"Delicious RAW Macadamia Zucchini GREEN Smoothie",
         "image":"https://spoonacular.com/recipeImages/641411-312x231.jpg",
         "imageType":"jpg",
         "usedIngredientCount":2,
         "missedIngredientCount":8,
         "missedIngredients":[
            {
               "id":11477,
               "amount":10.0,
               "unit":"servings",
               "unitLong":"servings",
               "unitShort":"servings",
               "aisle":"Produce",
               "name":"zucchini",
               "original":"of a zucchini (unpeeled)",
               "originalName":"of a zucchini (unpeeled)",
               "meta":[
                  "unpeeled"
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/zucchini.jpg"
            },
            {
               "id":93607,
               "amount":1.0,
               "unit":"cup",
               "unitLong":"cup",
               "unitShort":"cup",
               "aisle":"Milk, Eggs, Other Dairy",
               "name":"almond milk",
               "original":"1 cup of almond milk (see recipe below)",
               "originalName":"almond milk (see recipe below)",
               "meta":[
                  "(see recipe below)"
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/almond-milk.png"
            },
            {
               "id":12131,
               "amount":0.2,
               "unit":"cup",
               "unitLong":"cups",
               "unitShort":"cup",
               "aisle":"Baking",
               "name":"macadamia nuts",
               "original":"1/5 cup of raw macadamia nuts",
               "originalName":"raw macadamia nuts",
               "meta":[
                  "raw"
               ],
               "extendedName":"raw macadamia nuts",
               "image":"https://spoonacular.com/cdn/ingredients_100x100/macadamia-nuts.png"
            },
            {
               "id":9200,
               "amount":1.0,
               "unit":"",
               "unitLong":"",
               "unitShort":"",
               "aisle":"Produce",
               "name":"orange",
               "original":"1 peeled orange",
               "originalName":"peeled orange",
               "meta":[
                  "peeled"
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/orange.png"
            },
            {
               "id":10011457,
               "amount":1.0,
               "unit":"cup",
               "unitLong":"cup",
               "unitShort":"cup",
               "aisle":"Produce",
               "name":"spinach",
               "original":"1 cup of spinach",
               "originalName":"spinach",
               "meta":[
                  
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/spinach.jpg"
            },
            {
               "id":9184,
               "amount":0.5,
               "unit":"cup",
               "unitLong":"cups",
               "unitShort":"cup",
               "aisle":"Produce",
               "name":"honeydew melon",
               "original":"1/2 cup of honeydew melon (frozen)",
               "originalName":"honeydew melon (frozen)",
               "meta":[
                  "frozen",
                  "()"
               ],
               "extendedName":"frozen honeydew melon",
               "image":"https://spoonacular.com/cdn/ingredients_100x100/honeydew.png"
            },
            {
               "id":9087,
               "amount":3.0,
               "unit":"",
               "unitLong":"",
               "unitShort":"",
               "aisle":"Dried Fruits",
               "name":"dates",
               "original":"3 dates",
               "originalName":"dates",
               "meta":[
                  
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/dates.jpg"
            },
            {
               "id":11667,
               "amount":1.0,
               "unit":"teaspoon",
               "unitLong":"teaspoon",
               "unitShort":"tsp",
               "aisle":"Health Foods",
               "name":"spirulina …so much more",
               "original":"1 teaspoon spirulina (b 12 and other b vitamins, vitamins a-d and even k) …so much more.",
               "originalName":"spirulina (b 12 and other b vitamins, vitamins a-d and even k) …so much more",
               "meta":[
                  "(b 12 and other b vitamins, vitamins a-d and even k)"
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/spirulina-powder.jpg"
            }
         ],
         "usedIngredients":[
            {
               "id":11124,
               "amount":2.0,
               "unit":"",
               "unitLong":"",
               "unitShort":"",
               "aisle":"Produce",
               "name":"carrots",
               "original":"2 carrots (depending on how thick you want your smoothie)",
               "originalName":"carrots (depending on how thick you want your smoothie)",
               "meta":[
                  "thick",
                  "(depending on how you want your smoothie)"
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"
            },
            {
               "id":9040,
               "amount":1.0,
               "unit":"",
               "unitLong":"",
               "unitShort":"",
               "aisle":"Produce",
               "name":"banana",
               "original":"1 banana",
               "originalName":"banana",
               "meta":[
                  
               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/bananas.jpg"
            }
         ],
         "unusedIngredients":[
            
         ],
         "likes":1
      }
   ]
}"""

# def get_list_ingredients(json_data):
#     '''returns a list of the names of all ingredients needed for one recipe'''
#     data = json.loads(json_data)
    
#     missed_ingredients = [ingredient['name'] for ingredient in data['recipes'][0]['missedIngredients']]
#     used_ingredients = [ingredient['name'] for ingredient in data['recipes'][0]['usedIngredients']]

#     all_ingredients = missed_ingredients + used_ingredients
#     print(all_ingredients)
#     return all_ingredients

def get_all_ingredients(recipe):
    '''returns a list of the names of all ingredients needed for one recipe'''
    all_ingredients = []

    # Extract ingredients from missedIngredients
    missed_ingredients = recipe.get("missedIngredients", [])
    for ingredient in missed_ingredients:
        name = ingredient.get("name")
        if name:
            all_ingredients.append(name)

    # Extract ingredients from usedIngredients
    used_ingredients = recipe.get("usedIngredients", [])
    for ingredient in used_ingredients:
        name = ingredient.get("name")
        if name:
            all_ingredients.append(name)

    return all_ingredients

#Given a list of ingredients needed, output a dictionary with all of their info
def provigo_info(all_ingredients):
    '''(list of strings) --> dict
    provigo_info(['egg', 'non-fat yogurt', 'baking soda'])
    '''
    provigo = {}
    for ingredient in all_ingredients:
        url = get_url_provigo(ingredient, driver)
        if not isinstance(url, str):
            continue
        name, info = get_info_provigo(url, driver)
        #If we cannot find a produce, don't include in the dictionary
        if name == -1:
            continue
        provigo.update({name: info})
    
    return provigo
# a = provigo_info(['egg', 'apple', 'patate'])

def convert_price_to_float(price_str):
    cleaned_price_str = price_str.replace('$', '').replace(',', '.')

    try:
        return float(cleaned_price_str)
    except ValueError:
        # Handle the case where the conversion fails (e.g., if the price is '-1' or other non-numeric value)
        return 0.0  
    
def get_total_cost_grocery_list(grocery_list):
    '''{{'Egg': {'Price': '4.29', 'Quantity': '100g', 'Url': 'bob.com'},
    {'Peanut': {'Price': '7', 'Quantity': '100g', 'Url': 'nuts.com'}} --> float
    '''
    total_price = 0.0
    for item in grocery_list.values():
        if not isinstance(item['Price'], float):
            continue
        total_price += item['Price']
    print(total_price)                         
    return round(total_price,2)

# a = get_total_cost_grocery_list(a)
# print("Total grocery list cost: $" + str(a))

#TODO, actually figure this out
def get_cost_per_portion(grocery_list):
    total_price = sum(convert_price_to_float(item['Price'])*item["UnitPrice"] for item in grocery_list.values())

def get_cost_all_recipes(json_file):
    '''recipe_prices = {id: price}'''
    data = json.loads(json_file)
    recipe_prices = {}
    recipe_book = data['recipes']
    for recipe in recipe_book:
        recipe_id = recipe['id']
        list_ingredients = get_all_ingredients(recipe)
        cost = get_total_cost_grocery_list(provigo_info(list_ingredients))
        recipe_prices.update({recipe_id: cost})
    return recipe_prices

def sort_increasing(recipe_prices):
    sorted_recipe_costs = dict(sorted(recipe_prices.items(), key=lambda item: item[1]))
    return sorted_recipe_costs

recipe_costs = {637161: 25.01, 641411: 39.85, 637160: 2.01}
print(sort_increasing(recipe_costs))
# print(get_cost_all_recipes(json_data))

# data = json.loads(json_data)
# # print(data["recipes"][0])
# # print(type(data["recipes"][0]))
# recipe_book = data['recipes']
# for recipe in recipe_book:
#     recipe_id = recipe['id'] 
#     print(recipe_id)
