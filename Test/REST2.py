# coding: utf-8
import csv
import requests
import json
import time

after = 'data'
results = 'data'
runOnce = 1
'''
# This method lists top 20 games
def top20Games():

    headers = {
        'Client-ID': 'c736zvttjs86skjv8uwg3p3cr49f8o',
    }

    req = requests.get('https://api.twitch.tv/helix/games/top', headers=headers)
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    print(json.dumps(json_response, indent=4))
'''

def loLStreams():
    url = 'https://api.twitch.tv/helix/streams?game_id=21779'
    headers = {
        'Client-ID': 'c736zvttjs86skjv8uwg3p3cr49f8o',
    }
    req = requests.get(url, headers=headers)
    #print("HTTP Status Code: " + str(req.status_code))
    json_response = json.loads(req.content)
    after = json_response['pagination']['cursor']
    index = int(len(json_response['data']))
    with open('mycsvfile.csv', 'w', encoding='utf-8-sig') as f:
        x=0
        w = csv.DictWriter(f, json_response['data'][x].keys())
        w.writeheader()
        #w.writerow(json_response['data'][6])
        for x in range(index):
            w.writerow(json_response['data'][x])
    return (after)

def loLStreams1(after):

    url = 'https://api.twitch.tv/helix/streams?game_id=21779&after=' + after
    headers = {
        'Client-ID': 'c736zvttjs86skjv8uwg3p3cr49f8o',
    }

    req = requests.get(url, headers=headers)
    print(req.content)
    #print("HTTP Status Code: " + str(req.status_code))

    json_response = json.loads(req.content)
    print(json.dumps(json_response, indent=4))
    after = json_response['pagination']['cursor']
    return (after)

# Opens csv file and creates headers with first entry
def csvWriter1(my_dict, runOnce):
    with open('mycsvfile.csv', 'w') as f:
        w = csv.DictWriter(f, my_dict.keys())
        if runOnce == 1:
            w.writeheader()
            runOnce = 0
            w.writerow(my_dict)
        else:
            w.writerow(my_dict)
    return(my_dict, runOnce)

def csvWriter2(my_dictn):
    with open('mycsvfile.csv', 'w') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writeheader()
        w.writerow(my_dict)

if __name__ == '__main__':
    after = loLStreams()
    '''
    print (after, 'test')
    i = 1
    while (i < 100):
        i=+1
        after = loLStreams1(after)
        time.sleep(3)
    '''
