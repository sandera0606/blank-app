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

if "generate_clicked" not in st.session_state:
    st.session_state.generate_clicked = False

def generate_options():
    st.session_state.generate_clicked = True

def degenerate_options():
    st.session_state.generate_clicked = False

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
    hide_index = True,
    on_change = degenerate_options
)

st.button(
    label = "Generate Options", 
    type = "primary", 
    help = "Finished selecting stores? Generate options!",
    on_click = generate_options
)

if st.session_state.generate_clicked:
    for grocery in edited_grocery_list["groceries"]:
        grocery = grocery.strip()
        if grocery and selected_locs:
            st.header(string.capwords(grocery))
            grocery_options = db.get_grocery_options(grocery, selected_locs)
            grocery_options


