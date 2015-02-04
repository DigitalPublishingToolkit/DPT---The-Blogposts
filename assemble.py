#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Script aims to:
* assemble under a single markdown file - Bloposts.md - all the posts collected under docs/

'''


import os, re, glob
regex_img = re.compile('(\!\[.*\]\()\.\.\/\.\./(.*)(\))')


md_all = open('Blogposts.md', 'w')
md_all.write('')
md_all.close()

md_all = open('Blogposts.md', 'a') #'a' = append


md_posts = glob.glob('docs/*.md')
md_posts.sort()
md_posts.reverse()

for post in md_posts:
    print post
    md_post = open(post, 'r')
    md_post_content = md_post.readlines()
    content = ""
    for i, line in enumerate(md_post_content):

        if i > 4: # prevent YAML to go to be concat
            content = content + line
        
    md_all.write(content)
        

md_all.close()
