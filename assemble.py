#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Script aims to:
* assemble under a single markdown file - Bloposts.md - all the posts collected under docs/
* Bloposts.md will respect docs folder structure:
    Digital Publishing ToolKit - The Blog Posts/
    Reflections/
    Reports/
    Tools/
* Directories will become heading 1
* Files will become heading 2

'''


import os, re
regex_img = re.compile('(\!\[.*\]\()\.\.\/\.\./(.*)(\))')


md_all = open('Blogposts.md', 'w')
md_all.write('')
md_all.close()

md_all = open('Blogposts.md', 'a') #'a' = append


dirs = ([name for name in os.listdir("docs/")])
dirs.sort()


for directory in dirs:    
    print directory
    h1 = "\n# {} \n".format(directory)
    md_all.write(h1)
    
    for post in os.listdir("docs/{}".format(directory)):
        print post
        md_post = open("docs/{}/{}".format(directory, post), 'r')

        md_post_content = md_post.readlines()
        content = ""
        for line in md_post_content:

            # if re.search(regex_img, line): # re.search() checks for matches anywhere in the string
            #     found = re.findall(regex_img, line)
            #     print found

                
            content = content + line
        md_all.write(content)
        

md_all.close()
