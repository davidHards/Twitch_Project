# coding: utf-8
'''
Twitch API RESTful program game data
Date: 21/11/2018
Author: David Hards
Web Crawler for Twitch collects top games data, runs every 15 mins collecting
game data, stores the results in a csv file.

'''
import csv
import requests
import json
import time
import os.path

# top games pagination
tAfter = 'data'
# top games results
tResults = 'data'
timestr = time.strftime("%d%m%Y-%H%M%S")
path = 'E:/UG_Project_Data/'
file = timestr + '-topGames'
completeName = os.path.join(path, file + ".csv")

# This method gets top 100 games once, and stores results in csv file
def topGames():

    global tAfter
    global tResults

    url = 'https://api.twitch.tv/helix/games/top?first=100'
    headers = {
        'Client-ID': 'c736zvttjs86skjv8uwg3p3cr49f8o',
    }

    req = requests.get(url, headers=headers)
    json_response = json.loads(req.content)
    tAfter = json_response['pagination']['cursor']
    tResults = json_response['data']
    index = int(len(json_response['data']))

    with open(completeName, 'w', newline='', encoding='utf-8-sig') as f:
        x=0
        w = csv.DictWriter(f, tResults[x].keys())
        w.writeheader()
        for x in range(index):
            w.writerow(tResults[x])
    return

# This method gets next 100 games, and repeats to end of list, stores results csv file
def moreTopGames():

    global tAfter
    global tResults

    url = 'https://api.twitch.tv/helix/games/top?first=100&after=' + tAfter
    headers = {
        'Client-ID': 'c736zvttjs86skjv8uwg3p3cr49f8o',
    }

    req = requests.get(url, headers=headers)
    json_response = json.loads(req.content)
    try:
        tAfter = json_response['pagination']['cursor']
    except:
        print("no pagination")
        return
    tResults = json_response['data']
    index = int(len(json_response['data']))

    try:
        with open(completeName, 'a', newline='', encoding='utf-8-sig') as f:
            x=0
            w = csv.DictWriter(f, tResults[x].keys())
            for x in range(index):
                w.writerow(tResults[x])
    except:
        print("no more games")
        return
    return

if __name__ == '__main__':
    topGames()
    i = 1
    while i < 25:
        print(i)
        moreTopGames()
        i += 1
        time.sleep(6)
