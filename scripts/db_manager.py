import pandas as pd
from webscraping import get_groceries_by_store

# replace with location.get_local_supermarkets() or something
local_supermarkets = ["Metro", "T&T Supermarket", "Loblaws", "Walmart", "No Frills"]

# # For testing:
# # Replace with something webscraping
# eggs = {
#     "Walmart": {"Quail Eggs": 1, "Organic Chicken Eggs": 5000, "Free Range": 30},
#     "Sobeys": {"Duck Eggs": 18},
#     "Costco": {"Eggs": 5},
#     "T&T Supermarket": {"Marinated Egg Snack": 80, "Tea Eggs": 40},
# }

def get_grocery_options(product, selected_locs): # take a string "item" as input later
    rows = []
    product_options = get_groceries_by_store(product, selected_locs)
    for store in product_options:
        if store in selected_locs:
            for product, price in product_options[store].items():
                rows.append(
                    {
                        'Finalize': False,
                        'Item_Name': product,
                        'Price': price,
                        'Store': store
                    }
                )
    return pd.DataFrame(rows)
