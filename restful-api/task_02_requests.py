"""
This module consumes and processes data from the JSONPlaceholder API.
It includes functions to print post titles and save post data to a CSV file.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their status code.
    If successful, iterates and prints out the titles of all the posts.
    """
    url = "https://typicode.com"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder.
    If successful, structures id, title, and body into a list of dictionaries
    and writes it to a CSV file named posts.csv.
    """
    url = "https://typicode.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Structure the required keys using list comprehension
        structured_data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]
        
        # Write to CSV using DictWriter
        fieldnames = ["id", "title", "body"]
        with open("posts.csv", mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
