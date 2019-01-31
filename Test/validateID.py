import requests
import json
import csv

def validate():

    req = requests.get('https://id.twitch.tv/oauth2/authorize?response_type=token&client_id=c736zvttjs86skjv8uwg3p3cr49f8o&redirect_uri=http://localhost&scope=analytics:read:games')
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    print(json.dumps(json_response, indent=4))

if __name__ == '__main__:':
    validate()
