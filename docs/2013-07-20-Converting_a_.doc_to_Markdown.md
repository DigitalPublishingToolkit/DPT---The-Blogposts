---
title: Converting a .doc to Markdown
author: Silvio Lorusso
date: 2013-07-20
...

# Converting a .doc to Markdown {.entry-title .single-title itemprop="headline"}

By [Silvio
Lorusso](http://networkcultures.org/digitalpublishing/author/silviolorusso/ "Posts by Silvio Lorusso"),
July 20, 2013 at 4:55 pm.

This posts gathers the preliminary reflections on including Markdown
into the publishing workflow of INC. INC often receives papers and
articles in .doc format. That’s why it is necessary to test the
possibilities for automated conversion from .doc to Markdown.



![](imgs/lodi-doc-in-libreoffice.png)
.doc as rendered by LibreOffice



The test document chosen is in .doc format and it contains:

-   Basic formatting (e.g. bold and italic);
-   Footnotes;
-   References;
-   Blockquotes;
-   Hyperlinks;
-   Images.

# First Method: Textutil (Mac only) + Pandoc

The first method employs the command line tool **textutil** (only
available on Mac), to convert the document to HTML, and the command line
tool [Pandoc](http://johnmacfarlane.net/pandoc/).

The advantage of this method is the fact that it only requires a
one-liner:`textutil -convert html file.doc -stdout | pandoc -f html -t markdown -o file.md`

### Outcomes



![](imgs/lodi-markdown-mou.png)
Resulting Markdown as rendered by Mou



**Pros**

-   Basic formatting is preserved;

**Cons**

-   Images are missing;
-   Line breaks are converted into backslashes;
-   Footnotes are put at the end of the document without keeping the
    link within the text;
-   No formatting for blockquotes;
-   There is formatting for hyperlinks, but is not compatible with
    Markdown.

# Second Method: LibreOffice (4.0.4.2) + Pandoc

The second methods consists in exporting the .doc to XHTML via
LibreOffice and then…

### Outcomes



![](imgs/lodi-html-from-libreoffice.png)
The test document converted to HTML via LibreOffice



The HTML code outputted by LibreOffice has a CSS style applied in a
paragraph-specific way, this makes it pretty unreadable.

The HTML is then converted to Markdown via
Pandoc:`pandoc file.html -f html -t markdown -o file.md`

**Pros**

-   Hyperlinks are preserved;

**Cons**

-   Basic formatting is not preserved;
-   Images are included in the markdown but formatted as text, making
    the file impossible to open;
-   There is formatting for footnotes, but is not compatible with
    Markdown.
-   No formatting for blockquotes;
-   There is formatting for hyperlinks, but is not compatible with
    Markdown.

# Conclusions

The first method, Textutil (Mac only) + Pandoc, seems to be more
convenient time-wise. However it is still necessary to add images,
blockquotes, footnotes by hand. Furthermore hyperlinks need to be
reformatted and slashes needs to be deleted.
