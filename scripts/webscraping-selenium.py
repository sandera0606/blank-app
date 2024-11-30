from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

selector_dict = {
    "Walmart": ".product-title",
    "Metro": ".default-product-tile",
    "Loblaws": ".chakra-linkbox",
    "No Frills":".chakra-linkbox",
    "T&T Supermarket": ".item-root-ADb"
}


def parse_data(store, product):
    related_items = {}
    # Example:
    # {"Whole Wheat Bread": [price], "Whole Grain Bread: [price]"}
    number_products = 3
    count = 0

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(get_url(store, product))
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector_dict[store])) 
    )

    if store == "Walmart":
        products = driver.find_elements(By.CSS_SELECTOR, selector_dict[store])
        for product in products:
            if count >= number_products:
                break
            name = product.find_element(By.CSS_SELECTOR, 'head-title').text
            price = product.find_element(By.CSS_SELECTOR, 'product-price').text
            related_items[name] = price
            count += 1
        print(related_items)
        
    elif store == "Metro":
        products = driver.find_elements(By.CSS_SELECTOR, selector_dict[store])
        for product in products:
            if count >= number_products:
                break
            name = product.find_element(By.CSS_SELECTOR, 'head__title').text
            price = product.find_element(By.CSS_SELECTOR, 'pricing__sale-price').text
            related_items[name] = price
            count += 1
        print(related_items)
    elif store == "Loblaws":
        products = driver.find_elements(By.CSS_SELECTOR, selector_dict[store])
        for product in products:
            if count >= number_products:
                break
            name = product.find_element(By.CSS_SELECTOR, 'head__title').text
            price = product.find_element(By.CSS_SELECTOR, 'pricing__sale-price').text
            related_items[name] = price
            count += 1
        print(related_items)

    elif store == "No Frills":
        products = driver.find_elements(By.CSS_SELECTOR, selector_dict[store])
        for product in products:
            if count >= number_products:
                break
            name = product.find_element(By.CSS_SELECTOR, 'chakra-heading css-').text
            price = product.find_element(By.CSS_SELECTOR, 'price-product-tile').text
            related_items[name] = price
            count += 1
        print(related_items)
    elif store == "T&T Supermarket":
        products = driver.find_elements(By.CSS_SELECTOR, selector_dict[store])
        for product in products:
            if count >= number_products:
                break
            name = product.find_element(By.CSS_SELECTOR, 'item-name--yq').text
            price = product.find_element(By.CSS_SELECTOR, 'item-priceBox-OeM').text
            related_items[name] = price
            count += 1
        print(related_items)
    # else:
    #     raise TypeError("Invalid store")
    driver.quit()
    return related_items
        



def get_groceries_by_store(product, selected_locs):
    grocery_data = {}
    for store in selected_locs:
        grocery_data[store] = parse_data(store, product)
    return grocery_data

parse_data("Metro", "Eggs")