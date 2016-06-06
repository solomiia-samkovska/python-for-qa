
import json
import requests

from requests.auth import HTTPBasicAuth

ENDPOINT = 'https://python-for-qa.herokuapp.com/login'

def read_file(file):
    with open(file, 'r') as f:
        file_str = f.read()
        return file_str

def login(usr, psw):
    response = requests.get(ENDPOINT, auth = HTTPBasicAuth(usr, psw))
    if response.status_code == 401:
        print("Client:'" + usr +"' with password:'" + psw + "' - don't have access to web service.")


def main():
    str_json = read_file('clients.json')
    json_data = json.loads(str_json)
    
    for item in json_data:
        user_name = item['name']
        password = item['password']
        login(user_name, password)


if __name__ == '__main__':
    main()
