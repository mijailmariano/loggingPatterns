import random
import subprocess
from datetime import datetime, timedelta

import logging
import auxiliary_module

# create a logger file to log the output
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)


logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')


def analyze_customer_data(customer_id, date_range, product_category=None):
    def fetch_customer_info(cust_id):
        # Simulate fetching customer information from a database
        customers = {
            1: {"name": "Alice", "email": "alice@example.com", "loyalty_level": "Gold"},
            2: {"name": "Bob", "email": "bob@example.com", "loyalty_level": "Silver"},
            3: {"name": "Charlie", "email": "charlie@example.com", "loyalty_level": "Bronze"}
        }
        return customers.get(cust_id, {"name": "Unknown", "email": "unknown@example.com", "loyalty_level": "None"})

    def generate_purchase_history(start_date, end_date, category=None):
        # Simulate generating purchase history
        categories = ["Electronics", "Clothing", "Books", "Home & Garden"]
        history = []
        current_date = start_date
        while current_date <= end_date:
            if random.random() < 0.7:  # 70% chance of a purchase on any given day
                purchase = {
                    "date": current_date,
                    "category": category or random.choice(categories),
                    "amount": round(random.uniform(10, 500), 2)
                }
                history.append(purchase)
            current_date += timedelta(days=1)
        return history

    def calculate_customer_value(purchase_history):
        # Calculate customer value based on purchase history
        total_spent = sum(purchase["amount"] for purchase in purchase_history)
        avg_purchase = total_spent / len(purchase_history) if purchase_history else 0
        frequency = len(purchase_history) / ((date_range[1] - date_range[0]).days + 1)
        return total_spent * frequency * (avg_purchase / 100)

    # Main function logic
    customer_info = fetch_customer_info(customer_id)
    
    if not customer_info["name"]:
        raise ValueError(f"Customer with ID {customer_id} not found")

    purchase_history = generate_purchase_history(date_range[0], date_range[1], product_category)
    
    if product_category and not any(purchase["category"] == product_category for purchase in purchase_history):
        raise ValueError(f"No purchases found for category: {product_category}")

    customer_value = calculate_customer_value(purchase_history)

    # Perform some "complex" analysis
    loyalty_multiplier = {"Gold": 1.5, "Silver": 1.2, "Bronze": 1.0, "None": 0.8}
    adjusted_value = customer_value * loyalty_multiplier[customer_info["loyalty_level"]]

    result = {
        "customer_id": customer_id,
        "name": customer_info["name"],
        "email": customer_info["email"],
        "loyalty_level": customer_info["loyalty_level"],
        "total_purchases": len(purchase_history),
        "total_spent": sum(purchase["amount"] for purchase in purchase_history),
        "customer_value": customer_value,
        "adjusted_value": adjusted_value
    }

    return result

# Example usage:
# start_date = datetime(2023, 1, 1)
# end_date = datetime(2023, 12, 31)
# result = analyze_customer_data(1, (start_date, end_date), "Electronics")

#%%
print(f'{"text":.^40}')