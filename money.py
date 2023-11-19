import csv
import os

DATA_BASE_PATH = "./data/"
FILENAMES = ["adonis.csv", "metro.csv"]
FILEPATHS = [DATA_BASE_PATH + filename for filename in FILENAMES]


def get_ingredients(filepath) -> list:
    with open(filepath, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        ingredients = []
        for row in reader:
            ingredients.append(row)
            # add file basename to each row as "source"
            ingredients[-1]["source"] = os.path.basename(filepath).split(".")[0]
        return ingredients


# https://spoonacular.com/food-api/docs#Convert-Amounts
# for converting between different units of things


# def get_cheapest_ingredients(ingredients: list) -> list:
#     cheapest_ingredients = []
#     for ingredient in ingredients:
#         if not cheapest_ingredients:
#             cheapest_ingredients.append(ingredient)
#         else:
#             for i, cheapest_ingredient in enumerate(cheapest_ingredients):
#                 if ingredient["name"] == cheapest_ingredient["name"]:
#                     if float(ingredient["price"]) < float(cheapest_ingredient["price"]):
#                         cheapest_ingredients[i] = ingredient
#                 else:
#                     cheapest_ingredients.append(ingredient)
#     return cheapest_ingredients


if __name__ == "__main__":
    ingredients = []
    for filepath in FILEPATHS:
        if not os.path.exists(filepath):
            print(f"Error: File `{filepath}` does not exist")
            exit(1)
        else:
            ingredients.extend(get_ingredients(filepath))

    for ingredient in ingredients:
        print(ingredient)
