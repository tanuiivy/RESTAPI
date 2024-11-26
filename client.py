import requests

BASE_URL = "http://127.0.0.1:5000"

def add_product(name, description, price):
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(f"{BASE_URL}/products", json=payload)
    if response.status_code == 201:
        print("Product added:", response.json())
    else:
        print("Failed to add product:", response.json())

def get_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        print("Products retrieved:", response.json())
    else:
        print("Failed to retrieve products:", response.json())

if __name__ == "__main__":
    # Adding products
    add_product("Laptop", "High-performance laptop", 999.99)
    add_product("Smartphone", "Latest model smartphone", 799.49)
    
    # Retrieving products
    get_products()

