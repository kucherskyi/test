# -*- coding: utf-8 -*-
'''
    Hi. This is a tool to collect tweets.

'''
import oauth2
import json
import auth
import time
import user


print "Hi! Are You registered?"

if input('1 for YES \n2 for NO \n :') == 1:
    user.registered()
else:
    user.register()


# This function defines a word and location to search
def ur():

    tweetword = str(raw_input('Choose word to search: '))
    locale_user = str(raw_input('Choose locale: '))
    if len(locale_user) <= 2:
        locale_user = 'ua'

    tweeturl = 'https://api.twitter.com/1.1/search/tweets.json?q=' + \
               tweetword + '&count=100&locale=' + locale_user
    return tweeturl


# This is function to authentificate to Twitter
def oauth_req(url, key, secret,
              http_method="GET",
              post_body="",
              http_headers=None):

    consumer = oauth2.Consumer(key=auth.authkey, secret=auth.authsecr)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)

    resp, content = client.request(url,
                                   method=http_method,
                                   body=post_body,
                                   headers=http_headers)
    return content


# This function writes search results to file
def filewrite(strem, tweetid):

    # Filename is the same as username with .txt extension
    file = open(str(user.username)+'.txt', 'a')
    file.write(str(user.username + '\n'))
    for item in strem['statuses']:
        idtweet = str(item['id'])+'L'
        if id not in tweetid:
            tweetid.append(idtweet)
            tweetitself = 'User ' + item['user']['screen_name'].encode('utf8')\
                          + ' posted ' + '\n' + item['text'].encode('utf8')\
                          + ' at ' + item['created_at'].encode('utf8')\
                          + '\n' + '-'*40 + '\n'
            file.write(tweetitself)
        else:
            pass
    file.close()


# This function defines time to watch and does all the job.
def work():

    z = input('Time to watch in sec: ')
    # Ugly hack to make sure that file is empty
    fileToWrite = open(str(user.username) + '.txt', 'w')
    fileToWrite.close()
    tweetid = []
    coun = 0
    while coun <= z:
        co = json.loads(oauth_req(ur, auth.tokenkey, auth.tokensecret))
        filewrite(co, tweetid)
        time.sleep(5)
        coun += 1
    print "Your file has been saved"

if user.loginStatus is True:
    ur = ur()
    work()
else:
    print user.loginStatus
    print 'Something went wrong :('
