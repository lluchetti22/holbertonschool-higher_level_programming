#!/usr/bin/python3
"""Flask application that displays product data from JSON, CSV, or SQL."""
import csv
import json
import sqlite3
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


def read_sql(product_id=None):
    """Read and return a list of products from the SQLite database.

    Args:
        product_id (int): If provided, filter results to this id.

    Returns:
        list: A list of product dictionaries.
    """
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    if product_id is not None:
        cursor.execute(
            'SELECT id, name, category, price FROM Products WHERE id = ?',
            (product_id,))
    else:
        cursor.execute('SELECT id, name, category, price FROM Products')

    rows = cursor.fetchall()
    conn.close()

    return [
        {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
        for row in rows
    ]


@app.route('/products')
def products():
    """Render products from a JSON, CSV, or SQL source, optionally filtered."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template(
            'product_display.html', error='Wrong source')

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error='Product not found')

    if source == 'sql':
        try:
            data = read_sql(product_id)
        except sqlite3.Error:
            return render_template(
                'product_display.html', error='Error handling database')
    else:
        if source == 'json':
            data = read_json('products.json')
        else:
            data = read_csv('products.csv')

        if product_id is not None:
            data = [p for p in data if p['id'] == product_id]

    if product_id is not None and not data:
        return render_template(
            'product_display.html', error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
