import csv
from calculate_costs import provigo_info

print("HEYYYY")
# data = provigo_info(["apple", "cream", "cheese"])
# print(data)
a={'Egg Creations original': {'Price': 4.29, 'Quantity': '500 g', 'UnitPrice': 0.86, 'Unit': '100g', 'Url': 'https://www.provigo.ca/egg-creations-original/p/20820690001_EA'}, 'Yogourt biologique nature 2 %': {'Price': 4.99, 'Quantity': '650 g', 'UnitPrice': 0.77, 'Unit': '100g', 'Url': 'https://www.provigo.ca/yogourt-biologique-nature-2/p/20316485010_EA'}, '-1': {'Price': '-1', 'Quantity': '-1', 'UnitPrice': '-1', 'Unit': '-1', 'Url': 'https://www.provigo.ca/raisins-secs-de-smyrne/p/20647009_EA'}, 'Petits pains à la cannelle': {'Price': 5.79, 'Quantity': '9x30.0 g', 'UnitPrice': 2.14, 'Unit': '100g', 'Url': 'https://www.provigo.ca/petits-pains-la-cannelle/p/20563813_EA'}, 'Muffins au chocolat et bananes': {'Price': 7.49, 'Quantity': '600 g', 'UnitPrice': 1.25, 'Unit': '100g', 'Url': 'https://www.provigo.ca/muffins-au-chocolat-et-bananes/p/21283357_EA'}, 'Carottes, sac de 3 lb': {'Price': 2.99, 'Quantity': '1.362 kg', 'UnitPrice': 0.22, 'Unit': '100g', 'Url': 'https://www.provigo.ca/carottes-sac-de-3-lb/p/20600927001_EA'}}
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

make_csv("provigo", a)