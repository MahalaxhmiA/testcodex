import time
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

FORBIDDEN_CHARS = ['A', 'C', 'G', 'I', 'L', 'K']
TEST_MODE = True

def run_profile_test():
    current_hour = datetime.now().hour
    if not TEST_MODE and not (12 <= current_hour < 15):
        print(f"TERMINATED: Current hour is {current_hour}. Test window is 12 PM - 3 PM.")
        return

    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.amazon.in")
        
        print("ACTION: Please navigate to the page where your profile name is visible.")
        print("Waiting 20 seconds for page to load...")
        time.sleep(20)

        try:
            name_element = driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
            full_text = name_element.text
            profile_name = full_text.replace("Hello, ", "").strip()
        except:
            print("ERROR: Could not find profile name on screen. Check if you are logged in.")
            return

        print(f"Detected Profile Name: {profile_name}")

        found_chars = [char for char in FORBIDDEN_CHARS if char in profile_name.upper()]

        print("\n" + "="*40)
        print("PROFILE VALIDATION REPORT")
        print(f"User Name: {profile_name}")
        
        if not found_chars:
            print("RESULT: SUCCESS - No forbidden characters (A,C,G,I,L,K) found.")
        else:
            print(f"RESULT: FAILED - Found forbidden characters: {found_chars}")
        print("="*40 + "\n")

    except Exception as e:
        print(f"System Error: {e}")
    finally:
        print("Closing browser in 10 seconds...")
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    run_profile_test()