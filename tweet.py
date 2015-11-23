# -*- coding: utf-8 -*-

import oauth2
import json
import httplib2
from auth import *
import time
import sys


def ur():
    tweetword = str(raw_input('Choose word to search: '))
    locale_user = str(raw_input('Choose locale: '))
    if len(locale_user) <=2:
        locale_user = 'ua'

    tweeturl = 'https://api.twitter.com/1.1/search/tweets.json?q='+tweetword+'&count=100&locale='+ locale_user
    return tweeturl

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=authkey, secret=authsecr)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)

    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content


def filewrite(strem,tweetid):
    file = open('name.json','a')
    for item in strem['statuses']:
        id = str(item['id'])+'L'
        if id not in tweetid:
            tweetid.append(id)
            tweetitself = 'User '+item['user']['screen_name'].encode('utf8')+ ' posted ' \
                        + item['text'].encode('utf8')+\
                        ' at '+item ['created_at'].encode('utf8')+'\n'+'_'*80 +'\n'
            file.write(tweetitself)
            print tweetitself
            print '_'*80 +'\n'

        else:
            pass
    file.close()
    #return tweetitself
ur = ur()
def work():
    z = input('Time to watch in sec: ')
    file = open('name.json','w')
    file.close()
    tweetid = []
    coun = 0
    while  coun <= z:
        co = json.loads(oauth_req(ur, tokenkey, tokensecret))
        filewrite(co,tweetid)
        time.sleep(5)
        coun +=1
    print "Your file has been saved"

work()
