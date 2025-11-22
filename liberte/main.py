import requests
import os

def run():
    login = os.environ.get('LIBRUS_LOGIN')
    password = os.environ.get('LIBRUS_PASS')

    if not login or not password:
        raise ValueError("LIBRUS_LOGIN and LIBRUS_PASS environment variables must be set")

    login_data = {
        'action': 'login',
        'login': login,
        'pass': password
    }
    
    session = requests.Session()
    session.get("https://api.librus.pl/OAuth/Authorization?client_id=46&response_type=code&scope=mydata")
    session.post("https://api.librus.pl/OAuth/Authorization?client_id=46", login_data)
    session.get("https://api.librus.pl/OAuth/Authorization/2FA?client_id=46")

    response = session.get("https://synergia.librus.pl/rodzic/index")

    print(response.content)

if __name__ == "__main__":
    run()
