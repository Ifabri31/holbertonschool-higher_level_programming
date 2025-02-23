import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if response.status_code == 200:
        print("Status code: 200")
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()         
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})