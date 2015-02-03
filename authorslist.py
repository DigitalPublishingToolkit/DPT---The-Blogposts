#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Scrape the name of all authors that wrote the posts = of docs/*.md
'''

import glob
authors_file = open('authors.txt', 'w' )
authors_list = []
def all_docs():
    docs = glob.glob('docs/*')
    docs.remove('docs/imgs')
    all_docs = docs

    return all_docs

def authors(all_docs):
    for doc in all_docs:
        print doc
        doc_file = open(doc, 'r')
        doc_txt = doc_file.readlines()
        if  'author' in doc_txt[2]: 
            author = doc_txt[2].replace('author: ', '')        
            if author not in authors_list:
                authors_list.append(author)

        print authors_list

        for name in authors_list:                
            print name
            authors_file.write(name)


            
docs = all_docs()
authors(docs)
authors_file.close()


