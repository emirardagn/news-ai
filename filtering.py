import json
import ollama

with open('output.json', 'r') as file:
    news = json.load(file)

for new in news:
    req = f'do you think the title that i will give it to you includes any political,advertisal or swearing, if so just return 1, else 0:{new["title"]}, return only the number that you think cause i will use your output as input'
    output = ollama.generate(model="gemma2", prompt=req, options={"num_ctx": 5000})
    new["pass"]= int(output["response"])

news = [item for item in news if item["pass"] != 1]

with open("output.json", "w") as json_file:
    json.dump(news, json_file, indent=4)