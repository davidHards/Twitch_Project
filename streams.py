# coding: utf-8
'''
Twitch API RESTful program stream data
Date: 21/11/2018
Author: David Hards
Web Crawler for Twitch streams, runs for 15 mins collecting
Stream Data, stores the results in a csv file.

'''
import csv
import requests
import json
import time
import os.path

# stream pagination
sAfter = 'data'
# stream results
sResults = 'data'
timestr = time.strftime("%d%m%Y-%H%M%S")
path = 'E:/UG_Project_Data/'
file = timestr + '-streamData'
completeName = os.path.join(path, file + ".csv")

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

    with open(completeName, 'w', newline='', encoding='utf-8-sig') as f:
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
        with open(completeName, 'a', newline='', encoding='utf-8-sig') as f:
            x=0
            w = csv.DictWriter(f, sResults[x].keys())
            for x in range(index):
                w.writerow(sResults[x])
    except:
        print("no more streams")
        return
    return

if __name__ == '__main__':
    getStreams()
    i = 1
    while i < 140:
        print(i)
        moreStreams()
        i += 1
        time.sleep(6)
