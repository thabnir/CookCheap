import json
from provigo_web_scraping import *
from instacart_web_scraping import *

json_data = '''
{
   "recipes":[
      {
         "id":637161,
         "title":"Carrot and Banana Snacking Cake",
         "missedIngredients":[
            {
               "id":1123,
               "amount":1.0,
               "unit":"large",
               "aisle":"Milk, Eggs, Other Dairy",
               "name":"egg",
               "meta":[

               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/egg.png"
            },
            {
               "id":1001116,
               "amount":0.5,
               "unit":"cup",
               "aisle":"Milk, Eggs, Other Dairy",
               "name":"non-fat yogurt",
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
               "aisle":"Baking",
               "name":"baking soda",
               "meta":[

               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/white-powder.jpg"
            },
            {
               "id":2010,
               "amount":1.0,
               "unit":"teaspoon",
               "aisle":"Spices and Seasonings",
               "name":"cinnamon",
               "meta":[

               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/cinnamon.jpg"
            },
            {
               "id":9299,
               "amount":0.5,
               "unit":"cup",
               "aisle":"Produce",
               "name":"raisins",
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
               "aisle":"Produce",
               "name":"banana",
               "meta":[

               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/bananas.jpg"
            },
            {
               "id":11124,
               "amount":1.0,
               "unit":"cup",
               "aisle":"Produce",
               "name":"carrots",
               "meta":[

               ],
               "image":"https://spoonacular.com/cdn/ingredients_100x100/sliced-carrot.png"
            }
         ],
         "unusedIngredients":[

         ],
         "likes":3
      }
   ]
}
'''
def get_list_ingredients(json_data):
    '''returns a list of the names of all ingredients needed for one recipe'''
    data = json.loads(json_data)

    missed_ingredients = [ingredient['name'] for ingredient in data['recipes'][0]['missedIngredients']]
    used_ingredients = [ingredient['name'] for ingredient in data['recipes'][0]['usedIngredients']]

    all_ingredients = missed_ingredients + used_ingredients
    print(all_ingredients)
    return all_ingredients

#Given a list of ingredients needed, output a dictionary with all of their info
def provigo_info(ingredients):
    '''(list of strings) --> dict
    '''
    provigo = {}
    for ingredient in ingredients:
        url = get_url_provigo(ingredient)
        name, info = get_info_provigo(url)
        #If we cannot find a produce, don't include in the dictionary
        if name == -1:
            continue
        provigo.update({name: info})
    
    return provigo

# a = provigo_info(['egg', 'non-fat yogurt', 'baking soda', 'cinnamon', 'raisins', 'banana', 'carrots'])
# print(a)

def convert_price_to_float(price_str):
    cleaned_price_str = price_str.replace('$', '').replace(',', '.')

    try:
        return float(cleaned_price_str)
    except ValueError:
        # Handle the case where the conversion fails (e.g., if the price is '-1' or other non-numeric value)
        return 0.0  
    
def get_total_cost_grocery_list(grocery_list):
    '''{{'Egg': {'Price': '4,29 $', 'Quantity': '/ 100g', 'Url': 'bob.com'},
    {'Peanut': {'Price': '7 $', 'Quantity': '/ 100g', 'Url': 'nuts.com'}} --> float
    '''
    total_price = sum(convert_price_to_float(item['Price']) for item in grocery_list.values())
    return total_price

# a = get_total_cost_grocery_list({'Egg Creations original': {'Price': '4,29 $', 'Quantity': '/ 100g', 'Url': 'https://www.provigo.ca/egg-creations-original/p/20820690001_EA'},
#         '-1': {'Price': '-1', 'Quantity': '-1', 'Url': 'https://www.provigo.ca/yogourt-biologique-nature-2/p/20316485010_EA'},
#         'Soda gingembre, emballage de 6 mini-canettes': {'Price': '4,99 $', 'Quantity': '/ 100ml', 'Url': 'https://www.provigo.ca/soda-gingembre-emballage-de-6-mini-canettes/p/20354227001_C06'},
#         'Cannelle moulue': {'Price': '3,99 $', 'Quantity': '/ 100g', 'Url': 'https://www.provigo.ca/cannelle-moulue/p/20618677_EA'},
#         'Raisins rouges extra gros sans pépins': {'Price': '8,71 $', 'Quantity': '/ 1kg', 'Url': 'https://www.provigo.ca/raisins-rouges-extra-gros-sans-p-pins/p/20159199001_KG'},
#         'Muffins au chocolat et bananes': {'Price': '6,49 $', 'Quantity': '/ 100g', 'Url': 'https://www.provigo.ca/muffins-au-chocolat-et-bananes/p/21283357_EA'},
#         'Carottes, sac de 3 lb': {'Price': '3,99 $', 'Quantity': '/ 100g', 'Url': 'https://www.provigo.ca/carottes-sac-de-3-lb/p/20600927001_EA'}}
# )
# print("Total grocery list cost: $" + str(a))

def get_cost_per_portion(grocery_list):
    total_price = sum(convert_price_to_float(item['Price'])*item["UnitPrice"] for item in grocery_list.values())

