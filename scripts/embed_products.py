import pandas as pd
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
import json

#  Read CSV
df = pd.read_csv("data/products.csv")

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df['product_name'])

# Convert vectors to list
vector_list = vectors.toarray().tolist()

#  Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="1234",       #Mysql local password  
    database="product_search"
)

cursor = conn.cursor()

#  Insert into products_vectors
for idx, row in df.iterrows():
    product_id = int(row['product_id'])
    product_name = row['product_name']
    vector_json = json.dumps(vector_list[idx])

    sql = "INSERT INTO products_vectors (product_id, product_name, vector) VALUES (%s, %s, %s)"
    cursor.execute(sql, (product_id, product_name, vector_json))

conn.commit()
cursor.close()
conn.close()

print("✅ All products inserted into MySQL with vectors")
