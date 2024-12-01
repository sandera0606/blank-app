import time
import random
import pickle
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from scripts import bypass_bot_test
# import bypass_bot_test

stores = ["Zehrs", "Real Canadian Superstore", "Loblaws", "No Frills"]

def get_url(store, product):
    url_dict = {
        "Zehrs": f"https://www.zehrs.ca/search?search-bar={product}&sort=price-desc&page=1",
        "Real Canadian Superstore": f"https://www.realcanadiansuperstore.ca/search?search-bar={product}&sort=newest-desc&page=1",
        "Loblaws": f"https://www.loblaws.ca/search?search-bar={product}&sort=recommended&page=1&promotions=Price%2520Reduction",
        "No Frills": f"https://www.nofrills.ca/search?search-bar={product}",
        "Fortinos": f"https://www.fortinos.ca/search?search-bar={product}&page=1&dietaryCallouts=organic"
    }
    return url_dict[store]

selector_dict = {
    "Zehrs": "chakra-linkbox",
    "Real Canadian Superstore": "chakra-linkbox",
    "Loblaws": "chakra-linkbox__overlay",
    "No Frills":"chakra-linkbox",
    "Fortinos": "chakra-linkbox__overlay",
}

############################ Beginning of CHATGPT use ############################

def manage_cookies(driver, cookie_file):
    try:
        # Load cookies from file only if they match the current domain
        with open(cookie_file, "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                # Add the cookie only if the domain matches the current domain
                if cookie['domain'] in driver.current_url:
                    driver.add_cookie(cookie)
    except (FileNotFoundError, EOFError):  # Catch both file not found and empty file errors
        print(f"Cookie file {cookie_file} not found or is empty. Proceeding without loading cookies.")

    # Save cookies after loading the page
    with open(cookie_file, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

def parse_data(store, product):
    # set up selenium stuff

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('referer=https://www.google.com')
    options.add_argument(f'user-agent={random.choice(bypass_bot_test.user_agents)}')

    service = ChromeService(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    # Visit URL and manage cookies
    driver.set_window_size(1080, 800)
    driver.get(get_url(store, product))

    manage_cookies(driver, f"{store}_cookies.pkl")

    WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.CLASS_NAME, selector_dict[store]))
    )

############################ End of CHATGPT Use ############################

    related_items = {}
    number_products = random.randrange(1,4) #retrieves the three top items from each grocery store page
    count = 0

    if store == "Zehrs":
        products = driver.find_elements(By.CLASS_NAME, selector_dict[store])
        for product in products:
            if count >= number_products:
                break
            price = product.find_element(By.CSS_SELECTOR, '.chakra-text.css-1yftjin').text
            name = product.find_element(By.CLASS_NAME, 'chakra-heading').text
            related_items[name] = price
            count += 1
        
    elif store == "Real Canadian Superstore":
        products = driver.find_elements(By.CLASS_NAME, selector_dict[store])
        for product in products:
            if count >= number_products:
                break
            name = product.find_element(By.CLASS_NAME, 'chakra-heading').text
            price = product.find_element(By.CSS_SELECTOR, '.chakra-text.css-1yftjin').text
            related_items[name] = price
            count += 1
    
    elif store == "Loblaws":
        products = driver.find_elements(By.CLASS_NAME, selector_dict[store])
        for product in products:
            if count >= number_products:
                break
            price = product.find_element(By.CSS_SELECTOR, '.chakra-text.css-1yftjin').text
            name = product.find_element(By.CLASS_NAME, 'chakra-heading').text
            related_items[name] = price
            count += 1

    elif store == "No Frills":
        products = driver.find_elements(By.CLASS_NAME, selector_dict[store])
        for product in products:
            if count >= number_products:
                break
            name = product.find_element(By.CLASS_NAME, 'chakra-heading').text
            price = product.find_element(By.CSS_SELECTOR, '.chakra-text.css-1yftjin').text
            related_items[name] = price
            count += 1
    
    elif store == "Fortinos":
        products = driver.find_elements(By.CLASS_NAME, selector_dict[store])
        for product in products:
            if count >= number_products:
                break
            name = product.find_element(By.CLASS_NAME, 'chakra-heading').text
            price = product.find_element(By.CSS_SELECTOR, '.chakra-text.css-1yftjin').text
            related_items[name] = price
            count += 1

    else:
        raise TypeError("Invalid store")
    
    driver.quit()
    return related_items
        
def get_groceries_by_store(product, selected_locs): #retrieves top three products per page, given the product name and selected grocery stores
    grocery_data = {}
    for store in selected_locs:
        grocery_data[store] = parse_data(store, product)
    return grocery_data
