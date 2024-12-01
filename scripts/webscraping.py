import requests #allows for https requests 
from bs4 import BeautifulSoup #html parsing 
import re 

store_names = [] #will be the store name like costco, metro, t&t, etc
products = [] #

random_locations = ["costco", "walmart", "t&t"]
random_products = ["eggs", "beef", "milk"]

#current price 

product = "" #insert the same of the products 

#t&t: (f"https://www.tntsupermarket.com/eng/search.html?query={product}") 
#filter by item-price-zRu
#<div class="item-price-zRu"><span>$</span><span>12</span><span>.</span><span>99</span></div>
# price - css_selector = "item-priceBox-OeM"


#metro: (f"https://www.metro.ca/en/online-grocery/search?filter={product}")
#price_css_selector = "pricing__sale-price"

#walmart: (f"https://www.walmart.ca/en/search?q={product}")
#product name: <span data-automation-id="product-title" class="normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy">Great Value Large Eggs, 12 Count</span>
#price - css_selector = "product-price"


#<span class="w_q67L">Great Value XL White Eggs, 12 Count<!-- --> </span>
#<span class="w_q67L">current price $4.63</span>
#<span class="w_vi_D" style="-webkit-line-clamp: 3; padding-bottom: 0em; margin-bottom: 0em;"><span data-automation-id="product-title" class="normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy">Great Value XL White Eggs, 12 Count</span></span>

#loblaws: (f"https://www.loblaws.ca/search?search-bar={product}")
#price_css_selector = "price-product-tile"

#nofrills: (f"https://www.nofrills.ca/search?search-bar={product}")




stores = ["Walmart", "Metro", "Loblaws", "No Frills", "T&T Supermarket"]

def get_url(store, product):
    url_dict = {
        "Walmart": "https://www.walmart.ca/en/search?q="+product,
        "Metro": "https://www.metro.ca/en/online-grocery/search?filter="+product,
        "Loblaws": "https://www.loblaws.ca/search?search-bar="+product,
        "No Frills": "https://www.nofrills.ca/search?search-bar="+product,
        "T&T Supermarket": "https://www.tntsupermarket.com/eng/search.html?query="+product
    }
    return url_dict[store]


def parse_data(store, product):
    related_items = {}
    # Example:
    # {"Whole Wheat Bread": [price], "Whole Grain Bread: [price]"}
    request = requests.get(get_url(store, product))
    soup = BeautifulSoup(request.text,"html5lib")
    print(get_url(store,product))
    print(soup)
    #if store == "Walmart":
        
    #elif store == "Metro":
    #elif store == "Loblaws":
    # elif store == "No Frills":
    # elif store == "T&T Supermarket":
    # else:
    #     raise TypeError("Invalid store")

    # return related_items


def get_groceries_by_store(product, selected_locs):
    grocery_data = {}
    for store in selected_locs:
        grocery_data[store] = parse_data(store, product)
    return grocery_data

parse_data("T&T Supermarket", "Eggs")