#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Script aims to:
* download Wordpress (DPT blog) blog-post
* convert downloaded pages into Markdown files.
* save Markdown files inside docs

Input files: 
* posts_urls.txt - file contantaining a list made of: "url of the posts" 
* markdown.template - template for Markdown conversion

Categories:
* Reflections
* Reports
* Tools

Relies on: Pandoc
----

Issues:
* image download
* external images
* 
* add caption: "Video: url" to video iframes 




'''

import os, subprocess, re, glob, sys
import lxml.html, html5lib
import urllib2, json

regex_imgsresize =  re.compile(r'(.*)\-\d{1,4}x\d{1,4}(\.png|\.jpg)')


def post_lower_headings(headings, headings_dict, article):
    for heading in headings: # creat a dictionary of all eading, as reference
        every_heading = article.xpath(heading)
        heading_key = heading.replace('//','') 
        headings_dict[heading_key] = every_heading
    for headings in headings_dict.keys():
        for heading in headings_dict[headings]:
            tag = heading.tag
            tag = tag[0]+str(int(tag[1])+1)
            heading_attrib = heading.attrib
            heading_text =  heading.text
            new_heading = lxml.etree.Element(tag, attrib=heading_attrib, nsmap=None)
            new_heading.text = heading_text
            parent = heading.getparent()
            parent.replace(heading, new_heading)
            

#def author():
# 									<p class="byline vcard">By <span class="author"><a href="http://networkcultures.org/digitalpublishing/author/haroldkonickx/" title="Posts by haroldkonickx" rel="author">haroldkonickx</a></span>, <time class="updated" datetime="2015-01-27" pubdate>January 27, 2015 at 2:09 pm</time>.</p>

    
            
def vimeo_api(video_id):
    api = 'http://vimeo.com/api/v2/video/{}.json'.format(video_id)
    request = urllib2.urlopen(api)
    jsonp = json.loads(request.read() )[0]
    poster = jsonp.get('thumbnail_large')
    url = jsonp.get('url')
    return (url, poster)


def img_download(src, img_type, destination):
    '''Download images save in imgs'''
    src = src.encode('utf-8')
#    blog ima

# vimeo poster

# youtube poster

    if img_type in ['blog_img', 'vimeo_poster']:
        wget_img = 'wget --quiet --no-clobber -P docs/imgs {} --quiet'.format(src)        
        subprocess.call(wget_img, shell=True)           
    elif img_type is 'youtube_poster':
        wget_img = 'wget --quiet  --no-clobber -P docs/imgs {} --quiet'.format(src)        
        subprocess.call(wget_img, shell=True)           
        mv_img = 'mv docs/imgs0.jpg docs/imgs/{} '.format(destination)
        subprocess.call(mv_img, shell=True)           


def post_videos(iframes):
    for iframe in iframes:
        src = iframe.attrib['src']
        ignore = 0 # if iframe is from vimeo or youtube: ignore=0; if iframe is NOT from vimeo or youtube: ignore=1;  
        # ignore = 0 -> frame replacement for image;
        # ignore = 1 -> frame removed;

        if 'http' not in src:
            src = src.replace('//', 'http://')            
        if 'vimeo' in src:
            vimeo_id = (src.split('/'))[-1]
            if '?' in vimeo_id:
                vimeo_id = (vimeo_id.split('?')[0])                
#            print 'Vimeo id:', vimeo_id
            url, poster_url = vimeo_api(vimeo_id)
            path, filename = os.path.split(poster_url)
            newpath = os.path.join('../../imgs', filename)
            if os.path.isfile('docs/imgs'+ filename) != True:
                img_download(poster_url, 'vimeo_poster', None) #download img if not stored
            ignore = 0
            
        elif 'youtube' in src:
            youtube_id = (src.split('/'))[-1]
            url = 'https://www.youtube.com/watch?v={}'.format(youtube_id)
            poster = 'http://img.youtube.com/vi/{}/0.jpg'.format(youtube_id)
            filename = youtube_id + '.jpg'
            newpath = os.path.join('../../imgs', filename)
#            print 'YOUTUBE', newpath
            if os.path.isfile('docs/imgs'+ filename) != True:
                img_download(poster, 'youtube_poster', filename)
            # youtube video has to change filename, otherwise they will all will be called 0.jpg
            ignore = 0            
        else: 
            ignore = 1

            
        parent = iframe.getparent()        
        if ignore == 1: 
            parent.remove(iframe)
        else:
            caption = "Video: {}".format( url ) #videolink_str            
#            anchor = lxml.etree.Element('a', attrib={'href':url}, nsmap=None)
            fig = lxml.etree.Element('figure', attrib={'class': 'video'})
            img = lxml.etree.SubElement(fig, 'img', attrib={'src':newpath, 'class': 'video', 'alt': caption}, nsmap=None)
#            figcaption = lxml.etree.SubElement(fig, 'figcaption')                
 #           figcaption.text = caption            
            parent.replace(iframe, fig)


def post_imgs(images):
    for img in images:
        '''Find imgs' original size; run def img_download to download them; change <img> src to match'''    
        src = img.attrib['src']

        if 'class' in img.attrib:
            img_class = img.attrib['class']
        else:
            img_class = ''
   
        if re.match(regex_imgsresize, src): # if image is resized, find original name
            src_path, src_ext = (re.findall(regex_imgsresize, src))[0]
            src_original = src_path + src_ext 
            src = src_original
            
        img_download(src, 'blog_img', None) #download img if not stored
        path, filename = os.path.split(src) # update image path
        newpath = os.path.join('imgs', filename)            
        img.attrib['src'] = newpath

        
        parent = (img.xpath('..'))[0]  # remove <a> wrapping <img>
        if parent.tag is 'a' and img_class != 'video': 
            grandparent = (img.xpath('../..'))[0]
            caption = (grandparent.xpath('p[@class="wp-caption-text"]'))            
            fig = lxml.etree.Element('figure')
            img = lxml.etree.Element('img')
            figcaption = lxml.etree.Element('figcaption')                

            if len(caption) > 0:
                grandparent.remove(caption[0])
                fig.insert(0, figcaption)
                figcaption.text = caption[0].text
                img.text = caption[0].text

            grandparent.remove(parent)
            grandparent.insert(0, fig)
            fig.insert(0, img)                        
            img.set('src', newpath)




def post_clean_html(article):
    # remove unnecessary elements
    elements_to_remove = '//br | .//a[@class="footnote"] | .//div[@class="footnotes"] | .//em[not(normalize-space()) and not(*)] | .//i[not(normalize-space()) and not(*)] | .//b[not(normalize-space()) and not(*)] | .//strong[not(normalize-space()) and not(*)]'
    rm_els = article.xpath(elements_to_remove)
    for el in rm_els:
        el.getparent().remove(el)


        
def post2markdown(tree): # Process html; Keep only the <article> content - where blogpost actualy is 
    article = (tree.xpath('//article'))[0]
    header = (tree.xpath('//header[@class="article-header"]'))[0]
    p_blog = (article.xpath('.//p[@id="breadcrumb"]'))[0] # contains: "Blog:"
    header.remove(p_blog)
    if (article.xpath('.//footer')):
        footer = (article.xpath('.//footer'))[0]        
        article.remove(footer)
    iframes =  article.xpath('//iframe')
    post_videos(iframes) # videos: replace video's iframe with <a><img>

    images = (article.xpath('.//img'))
    post_imgs(images)
    post_clean_html(article)

    # author # add class to author wrapping <a>
    author_tag = (article.xpath('.//span[@class="author"]/a'))
#    author_tag[0].set('class', 'author')
#    author_tag[0].attrib.pop('rel')
#    author_tag[0].attrib.pop('title')
#    author_tag[0].set('title', '')

#    print lxml.html.tostring(author_tag[0])
              
    
    # get info
    date = ((article.xpath('//time'))[0]).attrib['datetime']
    author = (article.xpath('//a[@rel="author"]'))[0].text    
    title = (article.xpath('//h1[@class="entry-title single-title"]'))[0].text

    #save modified html
    html_article = lxml.html.tostring(article, pretty_print=True, include_meta_content_type=True, encoding='utf-8', method='html', with_tail=False)
    html = open('tmp_article.html', 'w')
    html.write(html_article)
    html.close()    
    return (date, author, title)

    
def clean_markdown(md_filename):
    '''remove from markdown:
    * html tags 
    * \

    '''
    md_file = open(md_filename, 'r') 
    md_content = md_file.read()
    md_file.close()

    expressions = [('\<\/?[section|div|span|p].+?\>', re.DOTALL), ('^\$', re.M)]
    for exp_flag in expressions:
        exp, flag =exp_flag
        regex = re.compile(r'{}'.format(exp), flag)
 #       allbs = re.findall(regex, md_content)
        md_content = re.sub(regex, "", md_content)

    # backslash_exp = re.compile(r'^\\$', re.M) #html elments either opening or closing tags
    # allbs = re.findall(backslash_exp, md_content)
    # print allbs
#    md_content =  re.sub(backslash_exp, "", md_content)

    md_file = open(md_filename, 'w') 
    md_file.write(md_content)
    md_file.close()

    
def pandoc(date, author, title, md_filename): 
    '''uses pandoc to convert html content  to markdown
     post -> tmp_article.html -> markdown 
    * include yalm metadata: title, author, date
    '''    
    pandoc = 'pandoc -f html -t markdown \
    --atx-headers \
    tmp_article.html \
    --template markdown.template \
    --variable title="{t}" \
    --variable author="{a}" \
    --variable date="{d}" \
    -o "{mdfile}"'.format(t=title , a=author, d=date, mdfile=md_filename)
    subprocess.call(pandoc, shell=True) 
    clean_markdown(md_filename)
#    os.remove('index.html')

def wget_post(url):
    '''
    Download post
    Parse post's tree
    Get Metadata
    Save content to Markdown file inside docs/file.md 
    '''
    wget = 'wget --quiet --no-clobber {}'.format(url)        
    subprocess.call(wget, shell=True) # download as index.html
    input_file = open('index.html', "r") # open and parse
    parsed = lxml.html.parse(input_file)
    article = parsed.xpath('//article')[0]    
    date, author, title = post2markdown(parsed)
    # date is "2014-05-27"
    date_list = date.split('-')
    day = str(format(int(date_list[-1]), '02'))
    date_list[-1] = day
    date = "-".join(date_list)
    author = author.encode('utf-8')
    title = title.encode('utf-8')    
    print date, author, title
    md_filename = "docs/{date}-{file}.md".format(date=date, file=title.replace(" ", "_")) 
    pandoc(date, author, title, md_filename)

    

def clean():
    '''
    Remove previously stored posts 
    '''
    imgs = glob.glob('docs/imgs/*')
    docs = glob.glob('docs/*')
    docs.remove('docs/imgs')
    all_files = imgs + docs
    for f in docs:
        os.remove(f)
    
#clean()
post_urls= os.path.abspath(sys.argv[1])
post_urls_file = open(post_urls, 'r')
for line in post_urls_file.readlines():
    if line:
        url = line
        print 'URL', url
        wget_post(url)
        os.remove('index.html')
        print 
        
