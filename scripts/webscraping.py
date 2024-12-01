from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

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
    "Metro": ".product-page-filter",
    "Loblaws": ".chakra-linkbox",
    "No Frills":".chakra-linkbox",
    "T&T Supermarket": ".item-root-ADb"
}


def parse_data(store, product):
    # set up selenium stuff
    # Example:
    # {"Whole Wheat Bread": [price], "Whole Grain Bread: [price]"}
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = webdriver.ChromeService(executable_path="scripts/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(get_url(store, product))
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector_dict[store])) 
    )

    related_items = {}
    number_products = 3
    count = 0

    if store == "Walmart":
        #fill this out later
        return
        
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
    #elif store == "Loblaws":
    # elif store == "No Frills":
    # elif store == "T&T Supermarket":
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