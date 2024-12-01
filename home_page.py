import streamlit as st
import pandas as pd
from scripts import db_manager as db
import string
import random

loading_fun = [
    "Hunting for ",
    "Fetching ",
    "Running after ",
    "Sprinting for ",
    "Browsing aisles for ",
    "Scavenging for ",
    "Cooking up "
]
st.logo(
    image = "assets/large_logo.png",
    size = "large",
    icon_image = "assets/small_logo.png"
)

title = "Grocery Running 🏃‍♂️"

st.set_page_config(
        page_title=title,
)

st.title(title)

tab1, tab2 = st.tabs(["Enter Info", "Final List"])

tab1.write("Enter your shopping list in the sidebar to get started!")

# tab1.text_input("Your Location:", key = "location")


selected_locs = tab1.multiselect(
    'Which stores are you willing to visit?',
    db.local_supermarkets
)

grocery_list = pd.DataFrame(
    {
        "groceries": [""],
    }
)

st.sidebar.title("Shopping List 🛒")

# Manage the grocery list on the side
edited_grocery_list = st.sidebar.data_editor(
    grocery_list,
    column_config={
        "groceries": st.column_config.TextColumn(
            "Grocery List",
            help = "Add items from your grocery list here!",
            width = "medium",
            required = True
        )
    },
    num_rows = "dynamic",
    hide_index = True,
)

final_list_items = []

##### Coded by CHATGPT #####

def fetch_and_cache_options(grocery, selected_locs):
    cache_key = f"grocery_options_{grocery}_{'_'.join(selected_locs)}"

    if cache_key not in st.session_state:
        # Fetch options from the database if not already cached
        options = db.get_grocery_options(grocery, selected_locs)
        st.session_state[cache_key] = options  # Save it in session state
        print(f"Fetching options for {grocery} from the database...")
    else:
        print(f"Using cached options for {grocery}...")
    
    return st.session_state[cache_key]  # Return the cached options


##### End of code by Chat GPT ####

def display_options():
    id = 0
    for grocery in edited_grocery_list["groceries"]:
        grocery = grocery.strip()
        if grocery and selected_locs:
            tab1.header(string.capwords(grocery))
            with st.spinner(random.choice(loading_fun) + string.capwords(grocery)):
                grocery_options = fetch_and_cache_options(grocery, selected_locs)
                edited_options = tab1.data_editor(
                    grocery_options,
                    key = f"candidate-groceries-{id}",
                    hide_index = True
                )
                for option in edited_options.itertuples():
                    if(option.Finalize):
                        final_list_items.append(
                            {
                                'Item_Name': option.Item_Name,
                                'Price': option.Price,
                                'Store': option.Store
                            }
                        )
        id += 1

display_options()

tab1.write("Finished selecting groceries? Head over to the 'final list' tab to view your grocery list!")

tab2.dataframe(
    final_list_items,
    column_config={
        'Item_Name': 'Item Name',
        'Price': 'Price',
        'Store': 'Store',
    },
    hide_index = True,
    width = 1000
)

