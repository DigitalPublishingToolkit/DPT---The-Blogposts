---
title: Markdown to Indesign with Pandoc (via ICML)
author: Silvio Lorusso
date: 2014-10-8
...

# Markdown to Indesign with Pandoc (via ICML) {.entry-title .single-title itemprop="headline"}

By [Silvio
Lorusso](http://networkcultures.org/digitalpublishing/author/silviolorusso/ "Posts by Silvio Lorusso"),
October 8, 2014 at 5:37 pm.

![](imgs/Screen-Shot-2014-10-08-at-17.29.26.png)

![](imgs/Screen-Shot-2014-10-08-at-17.02.19.png)

As part of the hybrid workflow for the Institute of Network Cultures
developed by the INC subgroup, I started a collaboration with Italian
graphic designer [Roberto Arista](http://projects.robertoarista.it/) in
order to write and collect scripts that facilitate the process of
importing HTML into InDesign.

This [set of
scripts](https://github.com/roberto-arista/fromHTMLtoXML_InDesignFlavour)
pre-processes HTML files, preserving such entities like headers,
paragraphs, italics, footnotes, tables, images, etc. Some of these steps
are summarised
[here](http://networkcultures.org/digitalpublishing/2014/05/import-html-into-indesign-via-xml/).
The scripts do so by converting the HTML files into an InDesign-friendly
XML structure and employing its *Import XML* function.

While such procedure is pretty good at maintaining the underlying
structure of the text (Paragraph and Character Styles are almost
automatically generated), it still has some imperfections. For instance,
an InDesign script called
[ReFoot](http://www.indiscripts.com/post/2010/04/refoot-convert-markup-text-into-indesign-footnotes)
was modified to generate footnotes declared with a XML-compatible
markup. The problem is that footnotes’ inner styles (italic, bold) are
lost. At the same time, yet no solution is provided to keep images or at
least their position.

Since May 2014, [pandoc](http://johnmacfarlane.net/pandoc/), an
open-source ”universal document converter”, is able to produce outputs
as ICML files. [ICML files](http://www.fileinfo.com/extension/icml) are
generally managed by InCopy, Adobe’s own word processor meant to
integrate with Adobe InDesign.

One of the advantage of using pandoc to obtain ICML is the fact that no
intermediate format is needed – HTML in our previous procedure.
Therefore we can directly use our Markdown source files. Here’s the
syntax to convert one document:

    pandoc -s -f markdown -t icml -o my.icml my.md

-   **-s** option, which stands for “standalone”, produces output with
    an appropriate header and footer;
-   **-f** option, which stands for “from”, is followed by the source
    format;
-   **-t** option, which stands for “to”, is followed by the output
    format;
-   **-o** option, which stands for “output”, is followed by the output
    filename, **my.icml** in above example;
-   **my.md**, in the above example, is the source filename.

The generated ICML file is then imported into InDesign with
**File\>Place**. In order to test the output, I used [this
file](http://networkcultures.org/digitalpublishing/wp-content/uploads/sites/26/2014/10/Astrid.icml_.zip),
derived from the [Society of the Query
Reader](http://networkcultures.org/blog/publication/society-of-the-query-reader-reflections-on-web-search/).

Both Paragraph Styles and Character Styles are automatically generated.

Here’s a tentative list of preserved entities:

-   bold;
-   italic;
-   blockquotes:
-   footnotes;
-   headers;
-   paragraphs;
-   tables;
-   lists.

In addition, a placeholder for each image is created.

In this sense, pandoc seems to provide a pretty robust conversion system
that straightforwardly connects the production and editing of Markdown
structured text and the design phase in the Adobe InDesign environment.
