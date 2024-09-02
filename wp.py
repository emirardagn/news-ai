import requests
from requests.auth import HTTPBasicAuth



def send_to_wp(title,content,status="publish"):
    data = {
        "title": title,
        "content": content,
        "status": status,
        "categories": [216]
    }


    response = requests.post(wp_url, auth=HTTPBasicAuth(wp_username, wp_password), json=data)


    if response.status_code == 201:
        print("Yazı başarıyla oluşturuldu")
    else:
        print(response.status_code, response.text)



