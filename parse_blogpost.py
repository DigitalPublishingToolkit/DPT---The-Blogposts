#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Script aims at converting a Wordpress (DPT blog) blog-post into Markdown document

Input: plain-text file contantaining the url of the posts

'''
import os, subprocess, re, glob
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
            

def vimeo_api(video_id):
    api = 'http://vimeo.com/api/v2/video/{}.json'.format(video_id)
    request = urllib2.urlopen(api)
    jsonp = json.loads(request.read() )[0]
    poster = jsonp.get('thumbnail_large')
    url = jsonp.get('url')
    return (url, poster)


def post_videos(iframes):
    for iframe in iframes:
        src = iframe.attrib['src']
        if 'vimeo' in src:
            vimeo_id = (src.split('/'))[-1]
            url, poster = vimeo_api(vimeo_id)

        elif 'youtube' in src:
            youtube_id = (src.split('/'))[-1]
            poster = 'http://img.youtube.com/vi/{}/0.jpg'.format(youtube_id)
            url = 'https://www.youtube.com/watch?v={}'.format(youtube_id)
        anchor = lxml.etree.Element('a', attrib={'href':url}, nsmap=None)
        img = lxml.etree.SubElement(anchor, 'img', attrib={'src':poster, 'class': 'video'}, nsmap=None)
#        new_heading.text = heading_text
        parent = iframe.getparent()
        parent.replace(iframe, anchor)


def post_imgs(images):
    for img in images:
        '''Download img in original size; save in imgs/ change <img> src to match'''    
        src = img.attrib['src']

        #get the url of original img
        if re.match(regex_imgsresize, src):
            src_path, src_ext = (re.findall(regex_imgsresize, src))[0]
            src = src_path + src_ext 
            print 'IMG SRC',src

        wget_img = 'wget --quiet -P imgs {} --quiet'.format(src)        
        subprocess.call(wget_img, shell=True)   
        path, filename = os.path.split(src)
        newpath = os.path.join('../../imgs', filename)
        img.attrib['src'] = newpath
        if 'class' in img.attrib:
            img_class = img.attrib['class']

        parent = (img.xpath('..'))[0] #Note:complicated due to captions as paragraphs #esier to give an empty href to the wrapping <a> 
        if parent.tag is 'a' and img_class != 'video': # disable <a> wrapping <img>
            parent.attrib['href']=""


def post_clean_html(article):
    # remove unnecessary elements
    elements_to_remove = '//br | .//a[@class="footnote"] | .//div[@class="footnotes"] | .//em[not(normalize-space()) and not(*)] | .//i[not(normalize-space()) and not(*)] | .//b[not(normalize-space()) and not(*)] | .//strong[not(normalize-space()) and not(*)]'
    rm_els = article.xpath(elements_to_remove)
    for el in rm_els:
        el.getparent().remove(el)


        
def post2markdown(tree): # keep only the <article> content - where blogpost actualy is 
    
    article = (tree.xpath('//article'))[0]
    header = (tree.xpath('//header[@class="article-header"]'))[0]
    p_blog = (article.xpath('.//p[@id="breadcrumb"]'))[0] # contains: "Blog:"

    header.remove(p_blog)
    if (article.xpath('.//footer')):
        footer = (article.xpath('.//footer'))[0]        
        article.remove(footer)

    # lower headings: h1 -> h2, ...
    headings = ['//h1', '//h2', '//h3', '//h4']
    headings_dict = {'h1':"", 'h2':"", 'h3':"", 'h4':""}
    post_lower_headings(headings, headings_dict, article)

    iframes =  article.xpath('//iframe')
    post_videos(iframes) # videos: replace video's iframe with <a><img>

    images = (article.xpath('.//img'))
    post_imgs(images)
    
    post_clean_html(article)
        
    # get info
    date = ((article.xpath('//time'))[0]).attrib['datetime']
    author = (article.xpath('//a[@rel="author"]'))[0].text    
    title = (article.xpath('//h2[@class="entry-title single-title"]'))[0].text

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
    --template markdown.template \
    --variable title="{t}" \
    --variable author="{a}" \
    --variable date="{d}" \
    tmp_article.html \
    -o "{mdfile}"'.format(t=title , a=author, d=date, mdfile=md_filename)
    subprocess.call(pandoc, shell=True) 
    clean_markdown(md_filename)
#    os.remove('index.html')


def wget_post(url, section):
    '''
    Download post
    Parse post's tree
    Get Metadata
    Save content to Markdown file inside docs/section/file.md 
    '''    
    wget = 'wget --quiet {}'.format(url)        
    subprocess.call(wget, shell=True) # download as index.html
    input_file = open('index.html', "r") # open and parse
    parsed = lxml.html.parse(input_file)
    article = parsed.xpath('//article')[0]

#    print parsed
#    print article
    # post2markdown(parsed)
    date, author, title = post2markdown(parsed)
    author = author.encode('utf-8')
    title = title.encode('utf-8')    
    print date, author, title
    md_filename = "docs/{section}/{date}-{file}.md".format( section=section, date=date, file=title.replace(" ", "_")) 
    pandoc(date, author, title, md_filename)

    

def clean():
    '''
    Remove previously stored posts and images
    '''
    imgs = glob.glob('imgs/*')
    docs = glob.glob('docs/*/*')
    all_files = imgs + docs
    for f in all_files:
        os.remove(f)
    
clean()
post_urls='posts_urls.txt' #os.path.abspath(sys.argv[1])
post_urls_file = open(post_urls, 'r')
for line in post_urls_file.readlines():
    if line:
        url, section = (line.split(" ")  )
        section = section.replace('\n', '')
        print 'URL:', url, section
        wget_post(url, section)
        os.remove('index.html')
        print 
        

#print html

        #print html# article
