import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def run_task_four():
    # Standard setup
    driver = webdriver.Chrome()

    try:
        # Step 1: Open Amazon Home
        driver.get("https://www.amazon.in")
        
        print("\n!!! ACTION REQUIRED !!!")
        print("1. Search for any product (e.g., 'Mobiles').")
        print("2. Stay on the results page.")
        print("Waiting 20 seconds for you...")
        
        time.sleep(20) # This gives you time to actually find a page that works

        # Step 2: Grab the price of the first item on the screen
        price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
        current_price = price_element.text
        
        print("\n" + "="*30)
        print("SUCCESS: TASK FOUR")
        print(f"Detected Price: ₹{current_price}")
        print("="*30)

        # Step 3: Trigger the notification alert
        driver.execute_script(f"alert('NOTIFICATION: Price tracked at ₹{current_price}')")
        time.sleep(5)

    except Exception as e:
        print(f"Error: Could not find a price on this page. Make sure prices are visible.")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_task_four()