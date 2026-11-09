# Lab 11 - Customer Dictionary & Lookup
# Name: Yashvini Jamnadas
# ISM2411 - Fall 2026
#
# Reflection
# 1. I'd use .get() when a key might be missing, like an optional field such as
#    a phone number, so the program keeps running with a default value. I'd use
#    bracket notation when the key has to be there, like a customer's name,
#    because a crash tells me right away that the data is broken. My rule of
#    thumb: optional data gets .get(), required data gets brackets.
#
# 2. Building a summary dictionary reminds me of a pivot table or SUMIF in
#    Excel, where you total sales by a category like region. The Python version
#    is better for large datasets because it runs the same way on a million rows
#    as on ten, and I can rerun it on new data without rebuilding anything.


# Exercise 1: One customer
print("--- Exercise 1: One customer ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2: Update and add
print("\n--- Exercise 2: Update and add ---")
customer["phone"] = "813-555-0123"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)


# Exercise 3: Safe lookup
print("\n--- Exercise 3: Safe lookup ---")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught: the key", error, "does not exist")


# Exercise 4: Iterate
print("\n--- Exercise 4: Iterate ---")
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping without .items() only gives you the keys, not the values.
# To get a value that way, you have to look it up with customer[key].
for key in customer:
    print(key)


# Exercise 5: Lookup table
print("\n--- Exercise 5: Lookup table ---")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
purchase = 200
tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
final_price = purchase * (1 - discount)
print("Tier:", tier)
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")


# Exercise 6: List of dicts
print("\n--- Exercise 6: List of dicts ---")
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Ben", "tier": "silver"},
    {"name": "Carla", "tier": "bronze"},
]
purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} | {c['tier']} | discount on $300: ${discount_amount:.2f}")


# Exercise 7: Nested catalog
print("\n--- Exercise 7: Nested catalog ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} (only {info['stock']} left)")


# Exercise 8: Sales by region
print("\n--- Exercise 8: Sales by region ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")
