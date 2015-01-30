#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Script aims to:
* assemble under a single markdown file - Bloposts.md - all the posts collected under docs/

'''


import os, re
regex_img = re.compile('(\!\[.*\]\()\.\.\/\.\./(.*)(\))')


md_all = open('Blogposts.md', 'w')
md_all.write('')
md_all.close()

md_all = open('Blogposts.md', 'a') #'a' = append



md_posts = os.listdir("docs/")
md_posts.sort()
md_posts.reverse()

for post in md_posts:
    print post
    md_post = open("docs/{}".format(post), 'r')
    md_post_content = md_post.readlines()
    content = ""
    for line in md_post_content:

        # if re.search(regex_img, line): # re.search() checks for matches anywhere in the string
        #     found = re.findall(regex_img, line)
        #     print found


        content = content + line
    md_all.write(content)
        

md_all.close()
