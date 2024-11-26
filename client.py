import requests

API_URL = "http://127.0.0.1:5000/products"

# Add a new product
def add_product(name, description, price):
    data = {"name": name, "description": description, "price": price}
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        print("Product added successfully:", response.json())
    else:
        print("Failed to add product:", response.json())

# Retrieve all products
def get_products():
    response = requests.get(API_URL)
    if response.status_code == 200:
        print("List of products:")
        for product in response.json():
            print(product)
    else:
        print("Failed to retrieve products:", response.json())

if __name__ == '__main__':
    # Example usage
    add_product("Laptop", "A high-performance laptop", 1500.0)
    add_product("Mouse", "Wireless mouse", 25.5)
    get_products()
