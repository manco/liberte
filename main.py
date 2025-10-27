import requests
import json
import yaml



                                        

def send_hello_world_post():
    credentials = None

    with open('private.yml', 'r') as file:
        credentials = yaml.load(file)

    login_data = {
        'action': 'login',
        'login': credentials.get('login'),
        'pass': credentials.get('pass')
    }
    
    session = requests.Session()
    session.get("https://api.librus.pl/OAuth/Authorization?client_id=46&response_type=code&scope=mydata")
    session.post("https://api.librus.pl/OAuth/Authorization?client_id=46", login_data)
    session.get("https://api.librus.pl/OAuth/Authorization/2FA?client_id=46")

    response = session.get("https://synergia.librus.pl/rodzic/index")

    print(response.content)

if __name__ == "__main__":
    send_hello_world_post()
