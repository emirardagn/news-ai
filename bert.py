from transformers import BertModel, BertTokenizer
from sklearn.metrics.pairwise import cosine_similarity



model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')




def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True, padding='max_length')
    outputs = model(**inputs)
    cls_embedding = outputs.last_hidden_state[:, 0, :].detach().numpy()
    return cls_embedding
def find_distance(text1,text2):
    embedding1 = get_bert_embedding(text1)
    embedding2 = get_bert_embedding(text2)
    similarity = cosine_similarity(embedding1, embedding2)
    return ({similarity[0][0]})

"""with open("current_posts.txt", 'r', encoding='utf-8') as file:

    curr = file.read()
curr = (curr.split("**********"))

with open("all_posts.txt", 'r', encoding='utf-8') as file:

    all = file.read()
all = (all.split("**********"))

curr = (curr[0:-1]) 
all = (all[0:-1])"""



"""for i in range (len(curr)):
    best = 0
    t1 = curr[i]
    for j in range (len(all)):
        
        t2 = all[j]
        dist = float(find_distance(t1,t2).pop())
        if(dist > best):
            best = dist
    
    if (best < 0.98):
        print(i,"yok, eklenebilir",best)
        with open("all_posts.txt", 'a', encoding='utf-8') as file:
            file.write(t1)
        req = f"bu özete başlık ver, sadece başlığı yaz böylece direkt kopyalayabileyim: {t1}"
        title = ollama.generate(model="gemma2",prompt=req)["response"]
        wp.send_to_wp(title,t1)"""