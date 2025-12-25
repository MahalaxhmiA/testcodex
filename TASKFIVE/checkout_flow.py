import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automate_full_flow():
    current_hour = datetime.now().hour
    BYPASS_FOR_TESTING = True 

    if not BYPASS_FOR_TESTING and not (18 <= current_hour < 19):
        print(f"TERMINATED: Time requirement unmet. Current hour: {current_hour}")
        return

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    driver.maximize_window()

    try:
        driver.get("https://www.amazon.in")
        
        search = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search.send_keys("Smartwatch")
        search.submit()

        price_whole = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))).text
        price_amount = float(price_whole.replace(',', ''))

        if price_amount <= 500:
            print(f"STOP: Price ₹{price_amount} <= 500.")
            return
        
        print(f"VALIDATED: ₹{price_amount}")

        driver.find_element(By.CSS_SELECTOR, "h2 a").click()
        driver.switch_to.window(driver.window_handles[-1])

        add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
        add_to_cart.click()

        time.sleep(2) 
        driver.get("https://www.amazon.in/gp/cart/view.html")
        checkout = wait.until(EC.element_to_be_clickable((By.NAME, "proceedToRetailCheckout")))
        checkout.click()

        print("SUCCESS: Flow complete.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    automate_full_flow()