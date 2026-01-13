# Vector Product Search

This project demonstrates a **product similarity search using vector embeddings**.

---

## Features

- Generate fake product data (500 products, including edge cases)
- TF-IDF embeddings for product names
- Store embeddings in MySQL
- Perform vector similarity search
- AWS Lambda compatible search logic (optional deployment)

---

## Tech Stack

- Python
- MySQL (local Workbench or RDS)
- TF-IDF (scikit-learn)
- AWS Lambda (optional)
- pandas, numpy

---

## Instructions to Run Locally

1️⃣ **Clone Repository**

```bash
git clone https://github.com/pavannkumar1000/vector-product-search.git
cd vector-product-search

2️⃣ Create Python Virtual Environment & Install Dependencies

python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt

3️⃣ Create MySQL Database

CREATE DATABASE IF NOT EXISTS product_search;
USE product_search;

-- Create table
SOURCE sql/create_products_vectors.sql;

4️⃣ Generate Product CSV

python scripts/generate_products.py

5️⃣ Insert Products + Vectors into MySQL

python scripts/embed_products.py

6️⃣ Verify

SELECT * FROM products_vectors LIMIT 5;

Instructions for AWS Deployment (Optional)

1️⃣ S3 – Store products.csv (optional)
2️⃣ RDS MySQL – Create instance, run SQL table
3️⃣ Lambda – Upload lambda_handler.py
4️⃣ Set environment variables: DB_HOST, DB_USER, DB_PASS, DB_NAME

Note: Full AWS deployment is optional. Core functionality works locally.

Vector Similarity Logic

Product names converted to TF-IDF vectors

Query vector generated using same TF-IDF model

Similarity computed using cosine similarity

Example in Python:

from sklearn.metrics.pairwise import cosine_similarity

similarities = cosine_similarity(query_vector, product_vectors)
top_5 = similarities.argsort()[0][-5:][::-1]


Assumptions:

TF-IDF is sufficient for small product dataset

Vector column stored as JSON in MySQL

Query product may have typos – TF-IDF captures similarity based on word overlap

Edge Case Handling

Similar product names (e.g., "Apple iPhone 14" vs "Apple iPhone 14 Pro")

Typo product names included in dataset (e.g., "Samzung Galaxy S21")

Random variants generated to reach 500 products

Folder Structure
vector-product-search/
├── data/            # CSV files
├── scripts/         # Python scripts (generate, embed)
├── sql/             # MySQL schema
├── lambda/          # Lambda handler code
├── README.md
├── requirements.txt
└── .gitignore
