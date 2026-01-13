import mysql.connector
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

# 1️⃣ Connect to MySQL
def get_products_from_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          
        password="1234",          
        database="product_search"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT product_id, product_name, vector FROM products_vectors")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convert vector JSON to list
    products = []
    for r in rows:
        products.append({
            "product_id": r[0],
            "product_name": r[1],
            "vector": json.loads(r[2])
        })
    return products

# 2️⃣ Lambda handler (simulate API call)
def lambda_handler(event, context=None):
    # event = {"query": "Apple iPhone 14"} 
    query = event.get("query", "")
    if not query:
        return {"error": "Query is required"}

    # 3️⃣ Load all product names
    products = get_products_from_db()
    product_names = [p["product_name"] for p in products]

    # 4️⃣ Fit TF-IDF on all products (including query)
    vectorizer = TfidfVectorizer()
    vectorizer.fit(product_names + [query])

    # 5️⃣ Transform query vector
    query_vec = vectorizer.transform([query]).toarray()

    # 6️⃣ Compute cosine similarity
    similarities = []
    for p in products:
        prod_vec = vectorizer.transform([p["product_name"]]).toarray()
        sim = cosine_similarity(query_vec, prod_vec)[0][0]
        similarities.append((sim, p["product_name"]))

    # 7️⃣ Sort by similarity (descending)
    similarities.sort(reverse=True, key=lambda x: x[0])

    # 8️⃣ Return top 5
    top5 = [name for score, name in similarities[:5]]

    return {"query": query, "top5": top5}

# 🔹 Example local test
if __name__ == "__main__":
    result = lambda_handler({"query": "Apple iPhone 14"})
    print(result)
