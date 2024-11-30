import pandas as pd

# replace with location.get_local_supermarkets() or something
local_supermarkets = ["Metro", "T&T Supermarket", "Loblaws", "Walmart", "No Frills"]

# For testing:
# Replace with something webscraping
eggs = {
    "Walmart": {"Quail Eggs": 1, "Organic Chicken Eggs": 5000, "Free Range": 30},
    "Sobeys": {"Duck Eggs": 18},
    "Costco": {"Eggs": 5},
    "T&T Supermarket": {"Marinated Egg Snack": 80, "Tea Eggs": 40},
}

def get_grocery_options(item, selected_locs): # take a string "item" as input later
    rows = []
    # call function to make item list with provided found groceries by grocery store
    #    and grocery stores, with the format of eggs above
    # replace "eggs" with whatever we scraped
    for store in eggs:
        if store in selected_locs:
            for product, price in eggs[store].items():
                rows.append(
                    {
                        'Finalize': False,
                        'Item_Name': product,
                        'Price': price,
                        'Store': store
                    }
                )
    return pd.DataFrame(rows)
