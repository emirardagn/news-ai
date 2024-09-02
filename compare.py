import json
import bert as bt
import wp 
from googletrans import Translator
translator = Translator()
with open('output.json', 'r') as file:
    news = json.load(file)
try:
    with open("all_news.json", "r") as json_file:
        hist = json.load(json_file)
except FileNotFoundError:
    hist = []



for i in range(len(news)):
    best = 0
    for j in range(len(hist)): #all_news'a göre editleyeceğiz
        title_distance = float(bt.find_distance(news[i]["title"],hist[j]["title"]).pop())
        sum_distance = float(bt.find_distance(news[i]["sum"],hist[j]["sum"]).pop())
        best = max(best, sum_distance, title_distance)
    #there is no similar
    if best <0.87:
        #make translate
        title = translator.translate((news[i]["title"]), dest='tr')
        content = translator.translate((news[i]["sum"]), dest='tr')
        content = content.text +"\nHaber linki:"+ news[i]["link"]
        wp.send_to_wp(title.text,content)
        hist.append(news[i])

    else:
        print(news[i]["title"], "zaten var", best)

with open("all_news.json", "w") as json_file:
    json.dump(hist, json_file, indent=4)