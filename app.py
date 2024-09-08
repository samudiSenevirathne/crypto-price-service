from flask import Flask, jsonify

app = Flask(__name__)

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify(status="UP"), 200

# Example endpoint: Get cryptocurrency price
@app.route('/price/<crypto>', methods=['GET'])
def get_price(crypto):
    prices = {
        "bitcoin": 50000,
        "ethereum": 3000,
        "dogecoin": 0.25
    }
    price = prices.get(crypto.lower())
    if price:
        return jsonify(crypto=crypto, price=price), 200
    else:
        return jsonify(error="Cryptocurrency not found"), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
