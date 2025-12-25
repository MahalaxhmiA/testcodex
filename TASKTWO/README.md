# README

This project is an automated testing tool designed for Amazon India. It verifies user eligibility based on identity, time, and purchase value.

## Requirements and Rules

1. **Username Validation**: The user identity must be exactly 10 alphanumeric characters.
2. **Time Restriction**: The script is locked to run only between 6:00 PM and 7:00 PM (18:00 - 19:00).
3. **Price Verification**: The cart must contain multiple items with a total value exceeding 2,000 INR.

## How to Run

1. **Install Dependencies**:
   Open your terminal and run:
   pip install selenium

2. **Run the Script**:
   python amazon_cart_test.py

## Project Logic



- **Pre-Check**: The script validates the username length and format, and checks the system time before launching the browser.
- **Automation**: It opens the browser, searches for specific products, adds them to the cart, and handles any warranty pop-ups.
- **Calculation**: It navigates to the cart page, extracts the subtotal string, cleans the numerical data, and performs a mathematical check.



## Test Scenarios

- **Username 'autonaye10'**: Valid (10 characters).
- **Username 'autonaye'**: Invalid (Only 9 characters - Script will stop).
- **Total > 2000**: Script reports SUCCESS.
- **Total <= 2000**: Script reports FAILURE.