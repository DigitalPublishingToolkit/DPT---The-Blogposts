---
title: Importing HTML into InDesign (via XML)
author: Silvio Lorusso
date: 2014-05-15
...

# Importing HTML into InDesign (via XML) {.entry-title .single-title itemprop="headline"}

By [Silvio
Lorusso](http://networkcultures.org/digitalpublishing/author/silviolorusso/ "Posts by Silvio Lorusso"),
May 15, 2014 at 3:35 pm.

![](imgs/Screen-Shot-2014-05-15-at-15.54.29.png)

![](imgs/Screen-Shot-2014-05-15-at-15.51.56.png)

![](imgs/Screen-Shot-2014-05-15-at-15.46.26.png)

![](imgs/Screen-Shot-2014-05-15-at-15.43.21.png)

![](imgs/Screen-Shot-2014-05-15-at-15.41.37.png)

![](imgs/Screen-Shot-2014-05-15-at-15.30.22.png)

As part of the INC subgroup research, we are looking into hybrid
workflows that employ Markdown/HTML. While Markdown remains the source,
it is also used to generate HTML files that form the EPUB files.

Generally, the source files for InDesign are Word files. In the new
workflow Word files are not central anymore, instead they are only used
at the beginning of the process out of necessity.

In order to allow the designer to use InDesign, it is necessary to find
a way to import the HTML files into the project. This can be achieved by
using the **Import XML** function.

In this post I’ll go through the procedure employed to import HTML into
InDesign.

### 1. Change the Extension of Your HTML file to .xml

### 2. Keep Only the Body

In order to be able to import the file into InDesign, it is necessary to
delete the headers (eg. *\<!DOCTYPE html\>*) and the head tag. Also the
upper html tag should be deleted. Finally you will have only body of
your document, like in the following image.

### 3. Remove Redundant Line Breaks

Unlike the way browsers render HTML, InDesign will preserve every line
break that is in the document. Only the ones after headers or paragraphs
are needed, so the other ones need to be substituted with a space.

With python it is possible to do as follows:

    #!/usr/bin/env python
    # usage: clean.py myfile.xml 

    import re, sys

    source = str(sys.argv[1])

    f = open(source, 'r+')
    doc = f.read()

    cleandoc = re.sub('(?<!>)n',' ', doc)
    print(cleandoc)

The script will look for line breaks that are not preceded by a *\>*,
and will substitute them with a white space.

### 4. Import XML into InDesign

You can now import the clean file into InDesign from *File \> Import
XML*.

By checking the *Create Link* box you will be able to modify the content
of the xml file and it will be automatically updated into InDesign.

A window with the structure of your document will appear on the left. By
drag-and-dropping the body tag into the pages, the content will appear.

### 5. Create Paragraph and Character Styles

It make sense to keep the name of the style consistent with the relative
HTML tag (eg. *p* to be used with *\* tag).

### 6. Map Tags to Styles

The final step is to connect the HTML tags to the relative paragraph and
character styles. To do so click on *Map Tags to Styles*.

By clicking on *Map by Name* tags and styles will be automatically
associated.

### Notes

This procedure lacks support for images and footnotes.

(thanks to [Roberto Arista](http://projects.robertoarista.it/) for the
hints.)
