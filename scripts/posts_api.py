#! /usr/bin/env python
# -*- coding: utf-8 -*-

###3
# Generate a list with all existing posts from http://networkcultures.org/digitalpublishing/
####

import html5lib, urllib2, json, pprint, subprocess


posts_urls = open('posts_urls.txt', 'w' )

def api_request(url):    
    request = urllib2.urlopen(url)
    jsonp = json.loads(request.read() )
    
    for i, entry in enumerate(jsonp):
        link =  entry['link']
        print link
        posts_urls.write(link)
        posts_urls.write("\n")
        
api_request('http://networkcultures.org/digitalpublishing/wp-json/posts?filter[posts_per_page]=1000')
posts_urls.close()
