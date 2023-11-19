from difflib import SequenceMatcher
import pandas as pd

# Example dataset 
ingredient_prices = pd.DataFrame({
    'Ingredient': ['ingredient1', 'ingredient2', 'ingredient3'],
    'Store1': [1.0, 2.0, 3.0],
    'Store2': [1.2, 1.8, 2.5],
    'Store3': [0.8, 2.2, 3.2]
})

# Example list of recipes with ingredients
recipes = {
    'RecipeA': ['ingredient1', 'ingredient2'],
    'RecipeB': ['ingredient2', 'ingredient3'],
    'RecipeC': ['ingredient1', 'ingredient3']
}

def calculate_recipe_price(recipe, prices_df):
    # Calculate the cheapest price for each ingredient in the recipe
    ingredient_prices = prices_df[prices_df['Ingredient'].isin(recipe)].set_index('Ingredient')
    cheapest_prices = ingredient_prices.min(axis=1)

    # Calculate the total price for the recipe
    total_price = cheapest_prices.sum()

    return total_price, cheapest_prices

def generate_recipe_cost_output(recipes, prices_df):
    for recipe_name, ingredients in recipes.items():
        total_price, ingredient_prices = calculate_recipe_price(ingredients, prices_df)

        print(f"{recipe_name}: Price - ${total_price:.2f}")
        print("Ingredients:")
        for ingredient, price in ingredient_prices.items():
            print(f"- {ingredient}: ${price:.2f}")

# Example usage
generate_recipe_cost_output(recipes, ingredient_prices)




# def similarity_ratio(s1, s2):
#     return SequenceMatcher(None, s1, s2).ratio()

# def find_matching_ingredient(ingredient_to_find, ingredient_list):
#     # Find ingredient with highest similarity ratio
#     matches = [(ingredient, similarity_ratio(ingredient_to_find, ingredient)) for ingredient in ingredient_list]
#     best_match = max(matches, key=lambda x: x[1])

#     # Threshold for similarity ratio
#     threshold = 0.3
#     if best_match[1] >= threshold:
#         return best_match[0]
#     else:
#         return None

# Example usage
# ingredient_to_find = "coriander"
# ingredient_list = ["cilantro", "coriander leaves", "Chinese parsley", "dhania"]

# matched_ingredient = find_matching_ingredient(ingredient_to_find, ingredient_list)

# if matched_ingredient:
#     print(f"The matched ingredient for '{ingredient_to_find}' is '{matched_ingredient}'.")
# else:
#     print(f"No match found for '{ingredient_to_find}'.")
