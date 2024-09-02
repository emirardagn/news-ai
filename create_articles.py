import requests
from bs4 import BeautifulSoup
import ollama
import time
import pyautogui
from selenium import webdriver

url = "https://www.google.com/search?q=ai+news&sca_esv=87cd9f5db8b9fddc&sca_upv=1&tbm=nws&sxsrf=ADLYWIIgTdfC4G7lXkZYiFpq91G8qKxXyA:1723099882057&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwi3sYej5-SHAxWLQvEDHdGeA-YQpwV6BAgEEA0&biw=1854&bih=961&dpr=1"
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
each_urls_links = soup.find_all('a')

filtered_links = [item.get('href') for item in each_urls_links if 'url' in item.get('href')]
filtered_links = [item for item in filtered_links if 'google.com' not in item]


final_output =""


for link in filtered_links:
    link = link[7:]
    link = link.split("&sa")[0]
    try:
        response = requests.get(link)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(strip=True)
        req = f'summarize this news,minimum 150 words, write only the summarization, do not add additional comments so i can directly copy and paste to my blog, text: {text}'
        output = ollama.generate(model="gemma2",prompt=req)
        summary = output["response"]
        
        req = f"translate this to turkish: {summary}"
        output = ollama.generate(model="gemma2",prompt=req)
        summary = output["response"]
        final_output += f"{summary}\nHaberin detayı: {link}\n**********\n"
        print(link)
        

    except:
        _=1

with open("current_posts.txt", 'w', encoding='utf-8') as file:
    file.write(final_output)
print("done")

import bert
bert


