import random
import pandas as pd

# Base product categories
electronics = [
    "Apple iPhone 14", "Apple iPhone 14 Pro", "Apple iPhone 13",
    "Samsung Galaxy S21", "Samsung Galaxy S22",
    "OnePlus 11", "OnePlus Nord",
    "Sony WH-1000XM5 Headphones",
    "Dell XPS 13 Laptop",
    "HP Pavilion Laptop"
]

fashion = [
    "Nike Running Shoes",
    "Adidas Sports Shoes",
    "Puma Sneakers",
    "Levis Blue Jeans",
    "U.S. Polo T-Shirt",
    "Ray-Ban Sunglasses"
]

groceries = [
    "Aashirvaad Atta 5kg",
    "Tata Salt 1kg",
    "Fortune Sunflower Oil 1L",
    "Maggi Noodles Pack",
    "Amul Butter 500g"
]

# Intentional typos (edge cases)
typos = [
    "Samzung Galaxy S21",
    "Appl iPhone 14",
    "Nik Running Shoes",
    "Adiddas Sports Shoes",
    "Tatta Salt 1kg"
]

all_base_products = electronics + fashion + groceries

products = []

product_id = 1

# Add base products
for name in all_base_products:
    products.append({
        "product_id": product_id,
        "product_name": name
    })
    product_id += 1

# Add typo products
for name in typos:
    products.append({
        "product_id": product_id,
        "product_name": name
    })
    product_id += 1

# Generate remaining random products to reach 500
while len(products) < 500:
    base = random.choice(all_base_products)
    variant = random.choice([
        "New Edition", "2024 Model", "Pro", "Plus", "Mini"
    ])
    generated_name = f"{base} {variant}"

    products.append({
        "product_id": product_id,
        "product_name": generated_name
    })
    product_id += 1

# Create DataFrame
df = pd.DataFrame(products)

# Save to CSV
df.to_csv("data/products.csv", index=False)

print("✅ products.csv generated with", len(df), "products")
