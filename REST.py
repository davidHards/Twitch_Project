# coding: utf-8
'''
Twitch API RESTful program
Date: 21/11/2018
Author: David Hards
Web Crawler for Twitch streams and top games, runs for 15 mins collecting
Stream Data, stores the results in a csv file. Also stores top games once in
a csv file

'''
import csv
import requests
import json
import time

# stream pagination
sAfter = 'data'
# stream results
sResults = 'data'
# top games results
tResults = 'data'
timestr = time.strftime("%d%m%Y-%H%M%S")

# This method gets top 100 games once, and stores results in csv file
def topGames():

    global tResults

    url = 'https://api.twitch.tv/helix/games/top?first=100'
    headers = {
        'Client-ID': 'c736zvttjs86skjv8uwg3p3cr49f8o',
    }

    req = requests.get(url, headers=headers)
    json_response = json.loads(req.content)
    tResults = json_response['data']
    index = int(len(json_response['data']))

    with open(timestr + '-topGames.csv', 'w', encoding='utf-8-sig') as f:
        x=0
        w = csv.DictWriter(f, tResults[x].keys())
        w.writeheader()
        for x in range(index):
            w.writerow(tResults[x])
    return

# This method gets top 100 streams once, and stores results in csv file
def getStreams():

    global sAfter
    global sResults

    url = 'https://api.twitch.tv/helix/streams?first=100'
    headers = {
        'Client-ID': 'c736zvttjs86skjv8uwg3p3cr49f8o',
    }

    req = requests.get(url, headers=headers)
    json_response = json.loads(req.content)
    sAfter = json_response['pagination']['cursor']
    sResults = json_response['data']
    index = int(len(json_response['data']))

    with open(timestr + '-streamData.csv', 'w', encoding='utf-8-sig') as f:
        x=0
        w = csv.DictWriter(f, sResults[x].keys())
        w.writeheader()
        for x in range(index):
            w.writerow(sResults[x])
    return

# This method gets next 100 streams, adds results to csv file and repeats
def moreStreams():

    global sAfter
    global sResults

    url = 'https://api.twitch.tv/helix/streams?first=100&after=' + sAfter
    headers = {
        'Client-ID': 'c736zvttjs86skjv8uwg3p3cr49f8o',
    }

    req = requests.get(url, headers=headers)
    json_response = json.loads(req.content)
    sAfter = json_response['pagination']['cursor']
    sResults = json_response['data']
    index = int(len(json_response['data']))

    try:
        with open(timestr + '-streamData.csv', 'a', encoding='utf-8-sig') as f:
            x=0
            w = csv.DictWriter(f, sResults[x].keys())
            for x in range(index):
                w.writerow(sResults[x])
    except:
        print("no more streams")
        return
    return

if __name__ == '__main__':
    topGames()
    getStreams()
    i = 1
    while i < 140:
        print(i)
        moreStreams()
        i += 1
        time.sleep(6)
