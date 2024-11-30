import streamlit as st
import pandas as pd
from scripts import db_manager as db
import string

title = "Grocery Running 🏃‍♂️"

st.set_page_config(
        page_title=title,
)

st.title(title)

tab1, tab2 = st.tabs(["Enter Info", "Final List"])

tab1.write("Enter your shopping list in the sidebar to get started!")

tab1.text_input("Your Location:", key = "location")


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

def display_options():
    id = 0
    for grocery in edited_grocery_list["groceries"]:
        grocery = grocery.strip()
        if grocery and selected_locs:
            tab1.header(string.capwords(grocery))
            edited_options = tab1.data_editor(
                db.get_grocery_options(grocery, selected_locs),
                key = "candidate-groceries-" + str(id),
                hide_index = True
            )
            for option in edited_options.itertuples():
                if(option.Finalize):
                    final_list_items.append(option)
        id += 1

display_options()

tab1.write("Finished selecting groceries? Head over to the 'final list' tab to view your grocery list!")

tab2.dataframe(
    final_list_items
)