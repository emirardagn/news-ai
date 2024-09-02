import find_news as fn
import requests
from bs4 import BeautifulSoup
import ollama
from translate import Translator
import json

translator = Translator(to_lang="tr")
news = fn.find_news()

for new in news:
    try:
        response = requests.get(new["link"])
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(strip=True)
        req = f'summarize this news,minimum 150 words, write only the summarization, do not add additional comments so i can directly copy and paste to my blog,if you think this news doesnt belong enough information or not related with ai just write !None!. text: {text}'
        output = ollama.generate(model="gemma2",prompt=req)
        summary = output["response"]
        new['sum'] = summary
    except Exception as e:
        print(new,e)

news = [item for item in news if "sum" in item]
with open("output.json", "w") as json_file:
    json.dump(news, json_file, indent=4)

