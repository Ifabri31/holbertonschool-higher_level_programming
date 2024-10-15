#!/usr/bin/env python3
import requests
import csv

def fetch_and_print_posts():
    solicitud = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {solicitud.status_code}")
    
    if solicitud.status_code == 200:
        posts = solicitud.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    solicitud = requests.get('https://jsonplaceholder.typicode.com/posts')

    if solicitud.status_code == 200:
        response_json = solicitud.json()

        with open('posts.csv', mode='w', encoding='utf-8', newline='') as i:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(i, fieldnames=fieldnames)
            writer.writeheader()
            
            for post in response_json:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
