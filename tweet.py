 # -*- coding: utf-8 -*-
 
import oauth2
import json
import httplib2

tweeturl = 'https://api.twitter.com/1.1/search/tweets.json?q=asd&count=100&locale=ua'
authsecr = "4A4sePR2HorfqT5DXTph7NOrqzqkU0kQbeaUcrTs4Nh2KI6aOS"
authkey = "Y2W7ofIwUhV8X6c9YnASKoTHZ"
tokenkey = '2330051484-z3UMoyMg3BoEQMsVQeCzVyzdyhbgamwuXYEff0O'
tokensecret = 'gkglDuRt1fOBAxpH6jQB91qnH9E6QdyXDQRLTQ9m8deLi'
proxy = httplib2.ProxyInfo(3, '127.0.0.1', 8888) #HTTP Proxy Type (3)


def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    lenn=0
    minlen = 0
    consumer = oauth2.Consumer(key=authkey, secret=authsecr)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    client.proxy_info = proxy
    client.disable_ssl_certificate_validation = True
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    file = open('list.json','w')
    file.write(content)
    file.close()
    file = open('list222.json','w')
    with open('list.json') as data_file:    
        data = json.load(data_file)
    for item in data['statuses']:
        if len(item [u'user'][u'screen_name']) > lenn:
            lenn = len(item [u'user'][u'screen_name'])
        else:
            minlen = lenn - len(item [u'user'][u'screen_name'])
        file.write(str(item [u'id'])+ ' ' +  item [u'user'][u'screen_name'] + (' ' * (minlen+1)) + item [u'created_at'] +'\n')
        print str(item [u'id'])+ ' ' +  item [u'user'][u'screen_name']
    file.close()
    #print str(item [u'id'])+ ' ' + 
    #userId.append(str(resp_body[u'statuses']))
    #print resp_body
    #print client.proxy_info()
 
home_timeline = oauth_req(tweeturl, tokenkey, tokensecret)


