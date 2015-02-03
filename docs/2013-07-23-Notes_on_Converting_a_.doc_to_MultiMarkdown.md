---
title: Notes on Converting a .doc to MultiMarkdown
author: Silvio Lorusso
date: 2013-07-23
...

# Notes on Converting a .doc to MultiMarkdown {.entry-title .single-title itemprop="headline"}

By [Silvio
Lorusso](http://networkcultures.org/digitalpublishing/author/silviolorusso/ "Posts by Silvio Lorusso"),
July 23, 2013 at 6:34 pm.

As stated in a [previous
post](http://networkcultures.org/digitalpublishing/2013/07/converting-a-doc-to-markdown/),
there is no direct and straightforward tool to convert a .doc to
Markdown. Of course the same goes for MultiMarkdown (MMD). In this post
I’ll document the process adopted to convert the file, which is partly
automated, partly manual. As a test document I use an
[article](http://networkcultures.org/digitalpublishing/wp-content/uploads/sites/26/2013/07/lodi.doc)
that has the following features:



[Mou](http://mouapp.com/) for Mac as editor because it’s a freeware.
**Metadata** I start adding the standard metadata as suggested in the
[MMD’s guide](http://fletcher.github.io/peg-multimarkdown/).

    Title:             This is the Title of the Article  
    Author:            Author Name  
    Affiliation:       https://twitter.com/AuthorName  
    Date:              2013  
    Base Header Level: 1  
    Copyright:         All Rights Reserved
     In addition to the standard metadata (that are not mandatory), it is possible to add any custom metadata that is needed. Considering that the aim of this would be to have source files to publish articles to different formats such as ePub and PDF, some metadata and attributes can be borrowed from the 

[specifications of
IPDF](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm) for ePUB. An
example could be the attribute “file as” used to normalise names.

    Title:             This is the Title of the Article  
    Author:            John Doe  
    Author File As:    Doe, John  
    Affiliation:       https://twitter.com/AuthorName   
    Date:              2013  
    Base Header Level: 1  
    Copyright:         All Rights Reserved
    Subject:           Internet  
    Description:       This is a long description of the article
                       on more than one line  
    Publisher:         Institute of Network Cultures  
    Type:              Article  
    Language:          English
     The fact that attributes are linked to the main metadata (as "file-as" to "author") adds a level of complexity to the organization of the document and the possible validation of it. The set of "linked" metadata should be of course put one next to another and this can't be shown through a blank line that would signify the end of the metadata part. 

**Content** I get the content, with a basic formatting, using **Pandoc**
in conjunction with **textutil** (Mac only) as described more in detail
[here](http://networkcultures.org/digitalpublishing/2013/07/converting-a-doc-to-markdown/):

**Headlines** I can now paste the content of “file.md” into the file in
which I set the metadata. In the case of this test document, the
headlines were simply set in bold; so I needed to correct that. From:

    **Title**
    **Subtitle**
     To: 


    #Title
    ##Subtitle

**Footnotes** Converting footnotes is pretty annoying because they’re
all at the end of the documents but the relative numbers, both in the
actual text and outside, are stripped. So I need to find each footnote
in the .doc and recreate it in the .md:

    Here is some text containing a footnote.[^somesamplefootnote]

    [^somesamplefootnote]: Here is the text of the footnote itself.
     Due to the fact that this is done by hand, it is likely that there are mistakes. Generally when this happens the amount of footnotes does not correspond. 

**Hyperlinks** Hyperlinks are easy to add if they are provided with the
“http:” or “www” part. In this case a simple regular expression allows
to add them:

    <&> That makes this: 

    http://exampleurl.com to this: 

    &#60;http://exampleurl.com/&#62; Unfortunately Mou doesn't support Regular Expression so I did this with 

[Coda](https://panic.com/coda/). The regular expression was tested in
real time on [RegExr](http://gskinner.com/RegExr/).
([Here’s](http://net.tutsplus.com/tutorials/other/8-regular-expressions-you-should-know/)
a good starter to Regular Expressions) **Blockquotes** Blockquotes
aren’t indicated in any way in the converted document, so it’s necessary
to find them in the original .doc and adding a “\>” symbol at the
beginning.

**Images** Images are stripped in the converted document; they are added
manually in the following way.

    ![This is the figure caption][fig_id]

    [fig_id]: mmd.png "This is where the title goes" height=45px width=120px

**References** MultiMarkdown provides support for basic citations but,
considering that INC publications have references that are not directly
“linked” within the text (because there are footnotes for that), an
unordered list is probably the easiest solution. Still declaring that
the list is the set of reference would be useful for data retrieval. An
easy way to do so would be adding an HTML comment.

    &#60!--references--&#62
    * Young, Tim. ‘My Book’, 2011. 
    * Doe, John. ‘Book’, 2010.

## Conclusions The resulting MMD document can be downloaded

[here](http://networkcultures.org/digitalpublishing/wp-content/uploads/sites/26/2013/07/trial.md),
while the output in HTML can be downloaded
[here](http://networkcultures.org/digitalpublishing/wp-content/uploads/sites/26/2013/07/trial.html).
The process to convert a .doc to MultiMarkdown is not straightforward
and has some levels of complexities due to the fact there is no single
tool able to do the conversion in a satisfying way. Several passages
between different softwares are needed and some prior knowledge is
required. Furthermore the conversion requires a good amount of hand
labour, in particular regarding the formatting of the footnotes.
