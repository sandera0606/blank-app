import streamlit as st
import pandas as pd
from scripts import db_manager as db

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
    hide_index = True
)