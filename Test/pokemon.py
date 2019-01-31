import requests
import json

def main():
    req = requests.get('http://pokeapi.co/api/v2/pokemon/3/')
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    print("Pokemon Name: " + json_response['name'])

if __name__ == '__main__':
    main()
