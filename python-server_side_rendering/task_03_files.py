#!/usr/bin/python3
"""Flask application that displays product data from JSON or CSV."""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename):
    """Read and return a list of products from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def read_csv(filename):
    """Read and return a list of products from a CSV file."""
    products = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


@app.route('/products')
def products():
    """Render products from a JSON or CSV source, optionally filtered."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv'):
        return render_template(
            'product_display.html', error='Wrong source')

    if source == 'json':
        data = read_json('products.json')
    else:
        data = read_csv('products.csv')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error='Product not found')

        data = [product for product in data if product['id'] == product_id]

        if not data:
            return render_template(
                'product_display.html', error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
