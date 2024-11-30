import streamlit as st
import pandas as pd
import visual_manager

st.title("Grocery Running 🏃‍♂️")

st.text_input("Your Location:", key = "location")

supermarkets = ["Walmart", "Sobeys", "Costco", "T&T Supermarket"]

selected_locs = st.multiselect(
    'Which stores are you willing to visit?',
    supermarkets
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