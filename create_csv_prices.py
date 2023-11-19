import csv
from calculate_costs import provigo_info
from instacart_web_scraping import instacart_info

ing1 = ['canola oil', 'olive oil', 'balsamic vinegar', 'white vinegar']
ing2 = ['rice vinegar', 'ketchup', 'mayonnaise','dijon mustard']
ing3 = ['soy sauce', 'chili paste', 'hot sauce', 'cayenne pepper']
ing4 = ['cumin', 'coriander', 'oregano', 'paprika']
ing5 = ['rosemary', 'thyme leaves', 'cinnamon', 'cloves']
ing6 = ['allspice', 'ginger', 'nutmeg','chili powder']
ing7 = ['curry powder', 'vanilla extract', 'canned black beans', 'canned chickpeas']
ing8 = ['olives', 'peanut butter', 'canned tomatoes', 'tomato paste']
ing9 = ['salsa', 'canned tuna fish', 'couscous', 'regular pasta']
ing10 = ['rice', 'baking powder', 'baking soda', 'brown sugar'] 
ing11 = ['cornstarch', 'all-purpose flour', 'granulated sugar', 'honey']
ing12 = ['butter', 'cheddar cheese', 'feta cheese', 'parmesan cheese']
ing13 = ['mozzarella cheese', 'eggs', 'milk', 'plain yogurt'] 
ing14 = ['blackberries', 'blueberries', 'peaches', 'strawberries']
ing15 = ['broccoli', 'corn', 'peas', 'spinach']
ing16 = ['garlic', 'onions', 'potatoes', 'dried raisins']
ing17 = ['dried apples', 'dried apricots', 'almonds', 'peanuts'] 
ing18 = ['sunflower seeds', 'chicken', 'salt', 'pepper']
ing19 = ['pork', 'beef', 'orange', 'turkey']
ing20 = ['bacon', 'coconut', 'mushrooms', 'beets']
ing21 = ['fennel seeds', 'lamb', 'shrimp', 'white bread']
ing22 = ['baguette', 'wholegrain bread', 'sourdough bread', 'naan bread']
ing23 = ['avocado oil', 'sesame oil', 'sunflower oil', 'apple cider vinegar']
ing24 = ['yellow mustard', 'basil', 'dill', 'sage']
ing25 = ['tarragon', 'cardamom', 'turmeric', 'lentils']
ing26 = ['quinoa', 'barley', 'penne pasta', 'fusilli pasta']
ing27 = ['farfalle pasta', 'spaghetti', 'maple syrup', 'gouda cheese']
ing28 = ['swiss cheese', 'goat cheese', 'walnuts', 'pecans']
ing29 = ['chia seeds', 'flaxseeds', 'cranberries', 'dates']
ing30 = ['salmon', 'lamb chops', 'pita bread', 'almond milk']
ing31 = ['coconut milk', 'bell peppers', 'zucchini', 'asparagus']
ing32 = ['mango', 'pineapple', 'kiwi', 'pesto sauce']
ing33 = ['hummus', 'carrots', 'celery', 'leeks']
ing34 = ['artichokes', 'brussels sprouts', 'cauliflower', 'eggplant']
ing35 = ['kale', 'radish', 'cabbage', 'green beans']
ing36 = ['cucumber', 'apple', 'pear', 'pickle']
ing37 = ['chocolate', 'candy', 'frozen pizza', 'banana']


#Give big list of common ingredients to provigo_info
data = instacart_info(ing18, "adonis")

def make_csv(store_name, data):
    csv_file = store_name+'.csv'

    # Write the dictionary to a CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['Ingredient', 'Price', 'Quantity', 'Unit Price', 'Unit', 'Url'])
        
        # Write the data
        for ingredient, info in data.items():
            writer.writerow([ingredient, info['Price'], info['Quantity'], info['UnitPrice'], info['Unit'], info['Url']])

    print(f'CSV file "{csv_file}" created successfully.')
    

def append_to_csv(store_name, additional_data):
    csv_file = store_name + '.csv'

    # Open the CSV file in append mode
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)

        # Append the new data to the file
        for ingredient, info in additional_data.items():
            writer.writerow([ingredient, info['Price'], info['Quantity'], info['UnitPrice'], info['Unit'], info['Url']])

    print(f'Data appended to CSV file "{csv_file}" successfully.')
    

# make_csv("adonis", data)
append_to_csv("adonis", data)


