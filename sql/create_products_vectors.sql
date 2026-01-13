CREATE TABLE products_vectors (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    vector JSON NOT NULL
);
