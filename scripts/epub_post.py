#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys, zipfile, os, shutil, glob, textwrap, re
from os.path import join
from xml.etree import ElementTree as ET
import html5lib
import argparse
from django.utils.html import urlize

"""
(C) 2014 Andre Castro

License: [GPL3](http://www.gnu.org/copyleft/gpl.html)
"""

"""
Script enhances the EPUB created from from Pandoc conversion to EPUB3, namely:

* Removes <sub> from footnotes, since these interferes with the iPad response; relies on CSS instead 
* Replaces back arrows - '↩' - with work 'back'
* add class='bloglink' to blog icon images - for CSS a:hover
* makes cover linear inside content.opf <spine>

"""

filename = sys.argv[1]
# unzip ePub
fh = open(str(filename), 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    outpath = "temp"
    z.extract(name, outpath)
fh.close()
temp_dir="temp/"
os.remove(temp_dir+'mimetype') # delete mimetype (will be added later with epub.writestr)



def fn_rm_sup(tree, element): # Removes Footnotes <sub>
    for fn in tree.findall(element):
        for child in list(fn):
            if child.tag == 'sup':                
                number = child.text
                fn.remove(child)
                fn.text=number


def replace_fn_links(tree, element): #replace back arrows with work "back"
    for tag in tree.findall(element):
        if tag.text is not None:
            text=(tag.text).encode('utf-8')
            if text == '↩':#'&#8617;':
                tag.text = 'back'

   
# def figure(tree, element): # insert <div> inside <figure> tp wrap <img>
#     for tag in tree.findall(element):
#         figure = tag.find('./figure')
#         img = tag.find('./img')  # find child elements' atrib
#         img_src = img.get('src')
#         figcaption = tag.find('./figcaption') #to img alt & figcaption text
#         if figcaption is not None:
#             figcaption_txt = figcaption.text
#         else:
#             figcaption_txt = ""
#         tag.clear() # clear child elements
#         new_fig = ''' <figure>
#   <div class="fig">	      
#   <img class="fig" src="{src}"
#   alt="{caption}" />
#   </div>
#   <figcaption>{caption}</figcaption>
# </figure>
# '''.format(src=(img_src.encode('utf-8')), caption=(figcaption_txt.encode('utf-8'))) # new children
#         new_fig = new_fig.replace('&', '&amp;')
#         new_fig_tag = ET.fromstring(new_fig)
#         tag.extend(new_fig_tag) # insert into figure

def spine(filename): # makes cover & title page linear is <spine>
    tree = ET.parse(filename)
    ET.register_namespace('epub', 'http://www.idpf.org/2007/ops')
    spine = tree.find('.//{http://www.idpf.org/2007/opf}spine')
    manifest = tree.find('.//{http://www.idpf.org/2007/opf}manifest')
    guide = tree.find('.//{http://www.idpf.org/2007/opf}guide')
    cover = ET.SubElement(guide, 'reference', attrib={'href':'cover.xhtml','title':'Cover','type':'title'}) # add cover as 1st page in guide
    for child in spine.getchildren():
        if child.attrib['idref'] == 'cover_xhtml'or child.attrib['idref'] == 'title_page_xhtml':            
            (child.attrib).pop("linear")
    for child in guide.getchildren():
        print "GUIDE:", ET.tostring(child)
    return tree


# add cover as text to guide: <reference href="cover.xhtml" title="Cover" type="title" />
            

        
def save_html(content_dir, content_file, tree ):
    doctype = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n'
    html = ET.tostring(tree,  encoding='utf-8', method='xml')
    html = doctype + html
    xhtml_file = open(content_dir + content_file, "w") 
    xhtml_file.write(html) 
    xhtml_file.close()


temp_ls=os.listdir("temp/")
temp_ls.sort()

    
def parse_biosfile(bios_file): #parse bibliography at the end
    for f in temp_ls: 
        if f==bios_file: 
            filename = "temp/"+f
            bios = open(filename, "r") 
            bios_tree = html5lib.parse(bios, namespaceHTMLElements=False)
            return bios_tree

def rm_author_link(tree, element, bios_file):
    bios_tree = parse_biosfile(bios_file)
    for p in tree.findall(element): # author's name - ".//p/a[@title]" //<a>author name<a/>
        anchors = p.findall('./a[@title]')
        if p.text  and anchors:            
            by = p.text.encode('utf-8')
            if "By" in by:
                author = anchors[0].text
                tail = anchors[0].tail
                print "Author:", author

                post_author = (author.encode('utf-8'))                
                post_author = post_author.replace('í','i')
                post_author_snake=post_author.replace(" ", "_")            
                # grab from bios_parsed section w/ title= author name
                author_realname = (((bios_tree.findall( './/section[@title="{}"]/h3'.format(post_author)))[0]).text)
                
                p.set('class', 'author')
                
                p.remove(anchors[0])
                # append bold
                bold = ET.SubElement(p, 'b')
                bold.text = author_realname
                bold.tail = tail
                bold.set('title', author_realname)

        
    
def authors(tree, element, bios_file, post_file): # bios on each post; and links to them
    bios_tree = parse_biosfile(bios_file)
    for anchor in tree.findall(element): # author's name - ".//p/a[@title]" //<a>author name<a/>
       if anchor.get('title'):
        title = anchor.get('title') # @title:"Post by ..."
        if 'Posts by' in title:                
            post_author = (anchor.text.encode('utf-8'))                
            post_author = post_author.replace('í','i')
            post_author_snake=post_author.replace(" ", "_")            
            # grab from bios_parsed section w/ title= author name
            bios_section = (bios_tree.findall( './/section[@title="{}"]'.format(post_author)))[0]
            # insert that bio at the bottom of current tree
            post_section = (tree.findall('.//section[@class="level1 entry-title single-title"]'))[0]
            #change the bios section id to the nickname
            bios_section.set('id', post_author_snake) 
            anchor.set('href', '#'+post_author_snake)            
                        
            # append bio to post <article>            
            ET.SubElement(post_section, 'hr')
            post_section.append(bios_section) 

            # add back button to bio
            post_id = post_section.get('id')
            print post_id
            back = ET.SubElement(bios_section, 'a',{'href':post_file} )
            back.text = "back"


def video_links(tree, element):
    for figcaption in tree.findall(element): # author's name - ".//figcaption
        if 'Video: ' in figcaption.text:
            caption = figcaption.text
            print caption
            url = caption.replace('Video: ', '')
            figcaption.text = 'Video: '
            link = ET.SubElement(figcaption, 'a', {'href':url})
            link.text = url

url_regex = '.*http[s]?://.*' # any url 
                
def urlize_text(tree, element):
    for tag in tree.findall(element):
        if tag.text is not None:
            text=(tag.text).encode('utf-8')
            text=urlize(text, nofollow=False)

bios_file='ch121.xhtml'

for f in temp_ls: #loop epub contained files     
    if f!=bios_file and f[:2]=='ch' and f[-6:]==".xhtml": # all ch*.xhtml        
        filename = "temp/"+f
        xhtml = open(filename, "r") 
        xhtml_parsed = html5lib.parse(xhtml, namespaceHTMLElements=False)
        fn_rm_sup(xhtml_parsed, './/a[@class="footnoteRef"]')
        replace_fn_links(xhtml_parsed, './/li/p/a')        
#        authors(xhtml_parsed, ".//p/a[@title]", bios_file, f)
        rm_author_link(xhtml_parsed, ".//p", bios_file)
        video_links(xhtml_parsed, ".//figcaption")
        urlize_text(xhtml_parsed, './/p')
        urlize_text(xhtml_parsed, './/li')
        
        save_html(
            content_dir=temp_dir,
            content_file=f,
            tree=xhtml_parsed )
        
    elif f == 'content.opf': # the opf
        filename = "temp/"+f
        xhtml = open("temp/"+f, "r")
        tree = spine(filename)
        ET.register_namespace('', 'http://www.idpf.org/2007/opf')
        tree.write(filename, encoding='utf-8', xml_declaration='True' )

#    elif f == 'title_page.xhtml':
#        os.remove("temp/title_page.xhtml")
#        shutil.copy("title_page.xhtml", "temp/title_page.xhtml")
        
        
# Step 3: zip epub
epub = zipfile.ZipFile("book-processed.epub", "w")
epub.writestr("mimetype", "application/epub+zip")
temp_dir = "temp"

def fileList(source):
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            matches.append(os.path.join(root, filename))
    return matches

dirlist=fileList(temp_dir)

for name in dirlist:
    path = name[5:] # removes 'temp/'
    epub.write(name, path, zipfile.ZIP_DEFLATED)
epub.close()


# Step 4: clean up: rm temp zipname
shutil.rmtree(temp_dir)

print
print "** Processed EPUB: book-processed.epub was generated without errors **"



'''
  <guide>
    <reference href="nav.xhtml" title="Digital Publishing Toolkit: the Blog Posts" type="toc" />
    <reference href="cover.xhtml" title="Cover" type="cover" />
          <reference href="cover.xhtml" title="Cover" type="title" />
  </guide>

'''
