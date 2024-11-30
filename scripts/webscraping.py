import requests #allows for https requests 
from bs4 import beautifulsoup #html parsing 
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

#metro: (f"https://www.metro.ca/en/online-grocery/search?filter={product}")

#walmart: (f"https://www.walmart.ca/en/search?q={product}")

#loblaws: (f"https://www.loblaws.ca/search?search-bar={product}")

#nofrills: (f"https://www.nofrills.ca/search?search-bar={product}")


url_dict = {
    "Walmart": "https://www.walmart.ca/en/search?q="+product,
    "Metro": "https://www.metro.ca/en/online-grocery/search?filter="+product,
    "Loblaws": "https://www.loblaws.ca/search?search-bar="+product,
    "No Frills": "https://www.nofrills.ca/search?search-bar="+product,
    "T&T Supermarket": "https://www.tntsupermarket.com/eng/search.html?query="+product
}

stores = ["Walmart", "Metro", "Loblaws", "No Frills", "T&T Supermarket"]

def parse_data(stores, product, url):
    for store in stores: 
        if store == url.dict.values():
            pass 

def get_
for store, url in url_dict.items():
