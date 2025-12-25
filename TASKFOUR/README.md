# TASK FOUR: Price Monitoring & Notification System

## Objective
Automate a system that monitors product prices on Amazon.in and triggers a browser notification when a price is detected.

## Features
- **Manual Handshake Logic**: To bypass Amazon's aggressive bot detection, the script allows 20 seconds for the user to navigate to a product search page.
- **Dynamic Extraction**: Uses Selenium to locate and extract the price from the `a-price-whole` class.
- **Notification Trigger**: Uses JavaScript injection to create an immediate browser-based alert popup when the price is found.

## How to Run
1. Ensure Selenium is installed: `python -m pip install selenium`
2. Run the script: `python price_monitor.py`
3. When the browser opens, search for a product (e.g., "Mobiles").
4. Wait for the terminal to print the detected price and for the browser alert to appear.

## Error Handling
- The script includes a `try-except` block to catch instances where Amazon might block the request or the price element is missing.