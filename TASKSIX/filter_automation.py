import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_filter_task():
    current_hour = datetime.now().hour
    BYPASS_TIME = True 

    if not BYPASS_TIME and not (15 <= current_hour < 18):
        print(f"TERMINATED: Requirement 3PM-6PM not met. Current hour: {current_hour}")
        return

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    driver.maximize_window()

    try:
        driver.get("https://www.amazon.in")
        
        search = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search.send_keys("Watch")
        search.submit()

        rating_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@aria-label='4 Stars & Up']//a")))
        rating_filter.click()
        
        price_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '2,000')]")))
        price_filter.click()

        time.sleep(3)
        products = driver.find_elements(By.CSS_SELECTOR, "h2 a span")
        
        found_match = False
        for item in products[:5]:
            brand_title = item.text
            if brand_title.upper().startswith('C'):
                print(f"MATCH FOUND: {brand_title}")
                found_match = True
                break
        
        if not found_match:
            print("NO MATCH: No brands starting with 'C' found.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        time.sleep(60)
        driver.quit()

if __name__ == "__main__":
    run_filter_task()