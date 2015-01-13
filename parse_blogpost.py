#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Script aims at converting a Wordpress (DPT blog) blog-post into Markdown document

Input: plain-text file contantaining the url of the posts

TO DO: 
* remove hyperlinks wrap images
* if a video: <video> <iframe> - 
** get poster
** replace these elements with: <a hre=video_url><img src="poster> 


'''
import sys, os, subprocess, re, shutil,  html5lib
import lxml.html #import ElementTree as ET
from urllib2 import unquote as unquote 




def blog2article(tree): # keep only the <article> content - where blogpost actualy is 
    article = (tree.xpath('//article'))[0]
    header = (tree.xpath('//header[@class="article-header"]'))[0]
    #remove
    footer = (article.xpath('.//footer'))[0]
    p_blog = (article.xpath('.//p[@id="breadcrumb"]'))[0] # contains: "Blog:"
    header.remove(p_blog)
    article.remove(footer)

    # empty tags # namely empty italics and bolds - to avoid complication in MD
    empty = article.xpath('.//em[not(normalize-space()) and not(*)]|.//i[not(normalize-space()) and not(*)]|.//b[not(normalize-space()) and not(*)]|.//strong[not(normalize-space()) and not(*)]')
    for node in empty:
        parent = node.getparent()
        parent.remove(node)

    # images
    images = (article.xpath('.//img'))
    for img in images:
        '''Download img; save in imgs/ change <img> src to match'''    
        src = img.attrib['src']
        wget_img = 'wget -P imgs {}'.format(src)        
        subprocess.call(wget_img, shell=True)   
        path, filename = os.path.split(src)
        newpath = os.path.join('../imgs', filename)
        img.attrib['src'] = newpath

#        shutil.copy(unquote(src), unquote(newpath))

        # remove <a> parent from <img>
        # Note:complicated due to captions as paragraphs 
        # parent = (img.xpath('..'))[0]
        # if parent.tag is 'a':             
        #     grandparent = parent.getparent()
        #     grandparent.remove(parent) # removing parent (a) also removes (img) - which is unwanted
        #     lxml.etree.SubElement(grandparent,'img', attrib={'src':newpath})



        
    # get info
    date = ((article.xpath('//time'))[0]).attrib['datetime']
    author = (article.xpath('//a[@rel="author"]'))[0].text    
    title = (article.xpath('//h1[@class="entry-title single-title"]'))[0].text    

    html_article = lxml.html.tostring(article, pretty_print=True, include_meta_content_type=True, encoding='utf-8', method='html', with_tail=False)
    html = open('tmp_article.html', 'w')
    html.write(html_article)
    html.close()
    
    return (date, author, title)

    
def clean_markdown(md_filename):
    '''remove html tags from markdown'''
    md_file = open(md_filename, 'r') 
    md_content = md_file.read()
    md_file.close()
    html_exp = re.compile(r'\<\/?[section|div|span|p].+?\>', re.DOTALL) #html elments either opening or closing tags
    html_less = re.sub(html_exp, "", md_content)
    md_file = open(md_filename, 'w') 
    md_file.write(html_less)
    md_file.close()

def md_images():
    '''
    * find all images present in the md file
    * mv those images to a single imgs/ directory
    * change the images' paths in the md file, to match their new directory
    '''

    
def pandoc(date, author, title, md_filename): 
    '''uses pandoc to convert html content  to markdown
    * include yalm metadata: title, author, date
    '''

    # how to guarantee no html tags are present in markdown
    
    md_file = open(md_filename, 'w') 
    pandoc = 'pandoc -f html -t markdown \
    --atx-headers \
    --template markdown.template \
    --variable title="{t}" \
    --variable author="{a}" \
    --variable date="{d}" \
    tmp_article.html \
    -o "{mdfile}"'.format(t=title , a=author, d=date, mdfile=md_filename)
    subprocess.call(pandoc, shell=True) # saved in tmp_content.html html
    clean_markdown(md_filename)
    os.remove('index.html')

# post -> tmp_html (tmp_article.html) -> markdown


def wget_post(url):
    wget = 'wget {}'.format(url)        
    subprocess.call(wget, shell=True) # download as index.html
    input_file = open('index.html', "r") # open and parse
    parsed = lxml.html.parse(input_file)

    date, author, title = blog2article(parsed)
    print date, author, title
    md_filename = "docs/"+ (title.replace(" ", "_")) + ".md"

    pandoc(date, author, title, md_filename)


    # need to change filename
    
    
   #    input_filename=os.path.abspath(sys.argv[1])
#    input_filename_list = input_filename.split(".") # write output based on input
    #ext = os.path.splitext(input_filename)[1]



post_urls=os.path.abspath(sys.argv[1])
post_urls_file = open(post_urls, 'r')
for url in post_urls_file.readlines():
    if url:
        print 'URL:', url
        wget_post(url)

        

#print html

        #print html# article
