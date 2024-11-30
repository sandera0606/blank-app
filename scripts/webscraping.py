import requests #allows for https requests 
import beautifulsoup #html parsing 
import re 

store_names = [] #will be the store name like costco, metro, t&t, etc
products = [] #

random_locations = ["costco", "walmart", "t&t"]
random_products = ["eggs", "beef", "yep"]

#walmart price parsing: <span class="w_q67L">current price $6.88</span>

product = "" #insert the same of the products 

#t&t: (f"https://www.tntsupermarket.com/eng/search.html?query={product}") 
#filter by item-price-zRu
#<div class="item-price-zRu"><span>$</span><span>12</span><span>.</span><span>99</span></div>
for store in store_names:
<a link-identifier="6000191268613" class="w-100 h-100 z-1 hide-sibling-opacity  absolute" target="" href="/en/ip/Gray-Ridge-Premium-Large-White-Eggs/6000191268613?selectedSellerId=0&amp;from=/search"><span class="w_q67L">Gray Ridge Premium Large White Eggs, 18 Count </span></a>