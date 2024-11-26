from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for storing products
products = []

# POST /products: Add a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    # Validate input
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input data"}), 400
    if not isinstance(data['price'], (float, int)):
        return jsonify({"error": "Price must be a number"}), 400

    # Create product
    new_product = {
        "id": len(products) + 1,
        "name": data['name'],
        "description": data['description'],
        "price": float(data['price'])
    }
    products.append(new_product)
    return jsonify(new_product), 201

# GET /products: Retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)

