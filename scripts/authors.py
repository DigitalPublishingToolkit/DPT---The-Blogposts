#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

file_authors = open('scripts/all_authors.txt', 'r')
authors = []

for line in file_authors.readlines():
    author = line.replace("author: ", "")
    author = author.replace("\n ", "")
    if author not in authors:
        authors.append(author)

authors.sort()
for author in authors:
    print author
