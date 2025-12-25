# TASK FIVE: End-to-End E-commerce Automation

## Overview
This task automates the full purchase lifecycle on Amazon India, including product search, price validation, cart management, and checkout initiation.

## Requirements
- **Time Constraint**: The script is programmed to run only between 18:00 and 19:00 (6 PM - 7 PM).
- **Price Constraint**: The script validates that the selected item is priced above Rs. 500.
- **Automation Flow**: 
    1. Navigation to Amazon.in.
    2. Automated search for "Smartwatch".
    3. Price verification logic.
    4. Handling new browser tabs for product details.
    5. Automatic "Add to Cart" execution.
    6. Transition to the "Proceed to Checkout" payment screen.

## Execution
Run the script using:
```bash
python checkout_flow.py