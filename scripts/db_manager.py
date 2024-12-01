import pandas as pd
from webscraping import get_groceries_by_store

# replace with location.get_local_supermarkets() or something
local_supermarkets = ["Real Canadian Superstore", "T&T Supermarket", "Loblaws", "Zehrs", "No Frills"]

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
