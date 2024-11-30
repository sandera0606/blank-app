import streamlit as st
import pandas as pd
from scripts import db_manager as db
import string

title = "Grocery Running 🏃‍♂️"
st.set_page_config(
        page_title=title,
)

st.title(title)

st.text_input("Your Location:", key = "location")


selected_locs = st.multiselect(
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

candidate_grocery_options = []
final_list_items = pd.DataFrame()

def display_options():
    id = 0
    for grocery in edited_grocery_list["groceries"]:
        grocery = grocery.strip()
        if grocery and selected_locs:
            st.header(string.capwords(grocery))
            edited_options = st.data_editor(
                db.get_grocery_options(grocery, selected_locs),
                key = "candidate-groceries-" + str(id),
                hide_index = True
            )
        id += 1

display_options()