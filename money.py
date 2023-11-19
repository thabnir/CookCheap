import csv
import os

CSV_PATH = "./data/adonis.csv"

def read_ingredients(filepath):
    with open (filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        ingredients = []
        for row in reader:
            ingredients.append(row)
        return ingredients





if __name__ == "__main__":
    ingredients = read_ingredients(CSV_PATH)
    print(ingredients)