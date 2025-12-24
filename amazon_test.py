import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_amazon():
    current_hour = datetime.now().hour
    
    if not (15 <= current_hour < 18):
        print(f"TASK BLOCKED: Current time is {current_hour}:00. Required: 15:00-18:00.")
        return

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.amazon.in")
        search_term = "Wooden Home Decor" 
        
        search_box = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.ENTER)

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2 a span")))
        products = driver.find_elements(By.CSS_SELECTOR, "h2 a span")
        
        electronic_keywords = ["DIGITAL", "ELECTRIC", "LED", "BATTERY", "USB", "CHARGING", "POWER"]
        
        selected_element = None
        selected_title = ""

        print("--- FILTERING PROCESS STARTED ---")

        for item in products:
            title = item.text.strip()
            if not title:
                continue
            
            first_letter = title[0].upper()
            if first_letter in ['A', 'B', 'C', 'D']:
                print(f"Skipping (Letter {first_letter}): {title[:40]}...")
                continue
            
            if any(word in title.upper() for word in electronic_keywords):
                print(f"Skipping (Electronic): {title[:40]}...")
                continue

            selected_element = item
            selected_title = title
            break

        if selected_element:
            print(f"MATCH FOUND: {selected_title}")
            
            driver.execute_script("arguments[0].scrollIntoView();", selected_element)
            time.sleep(1)
            selected_element.click()

            driver.switch_to.window(driver.window_handles[-1])

            final_page_title = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text
            
            print("--- VERIFICATION ---")
            if selected_title[:10] in final_page_title:
                print("SUCCESS: Product Page Details Verified.")
            else:
                print("FAILURE: Page details do not match.")
        else:
            print("No product found matching all criteria.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    run_amazon()