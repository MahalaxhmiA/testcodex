import time
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TARGET_USER = "autonaye10"
ITEMS = ["SSD Drive", "Monitor"]
TEST_MODE = True

def run_amazon_automation():
    if len(TARGET_USER) != 10 or not TARGET_USER.isalnum():
        print(f"TERMINATED: '{TARGET_USER}' is invalid. Use 10 letters/numbers only.")
        return

    current_hour = datetime.now().hour
    if not TEST_MODE and current_hour != 18:
        print(f"TERMINATED: It is currently {datetime.now().strftime('%H:%M')}.")
        print("This script only functions between 6:00 PM and 7:00 PM.")
        return

    print(f"Starting automation for: {TARGET_USER}")
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    
    try:
        for product_name in ITEMS:
            driver.get("https://www.amazon.in")
            
            search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
            search_box.clear()
            search_box.send_keys(product_name)
            search_box.submit()

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h2 a"))).click()

            wait.until(lambda d: len(d.window_handles) > 1)
            driver.switch_to.window(driver.window_handles[-1])

            wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button"))).click()
            
            time.sleep(2)
            try:
                driver.find_element(By.ID, "attachSiNoCoverage").click()
            except:
                pass
            
            print(f"Added to cart: {product_name}")
            
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        driver.get("https://www.amazon.in/gp/cart/view.html")
        
        price_element = wait.until(EC.presence_of_element_located((By.ID, "sc-subtotal-amount-buybox")))
        
        final_price = float(re.sub(r'[^\d.]', '', price_element.text))

        print("\n" + "="*40)
        print(f"VERIFICATION REPORT")
        print(f"User Name: {TARGET_USER}")
        print(f"Final Cart Total: ₹{final_price}")
        
        if final_price > 2000:
            print("ELIGIBILITY: SUCCESS - Cart is above ₹2000.")
        else:
            print("ELIGIBILITY: FAILED - Cart is ₹2000 or below.")
        print("="*40 + "\n")

    except Exception as e:
        print(f"An error occurred during testing: {e}")
    
    finally:
        print("Automation finished. Closing browser in 30 seconds...")
        time.sleep(30)
        driver.quit()

if __name__ == "__main__":
    run_amazon_automation()