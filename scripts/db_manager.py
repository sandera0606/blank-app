import pandas as pd
from scripts import webscraper

# replace with location.get_local_supermarkets() or something
local_supermarkets = ["Real Canadian Superstore", "Loblaws", "Zehrs", "No Frills", "Fortinos"]

def get_grocery_options(product, selected_locs): # take a string "item" as input later
    rows = []
    product_options = webscraper.get_groceries_by_store(product, selected_locs)
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
