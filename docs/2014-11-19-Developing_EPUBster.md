---
title: Developing EPUBster
author: Marc de Bruijn
date: 2014-11-19
...

# Developing EPUBster {.entry-title .single-title itemprop="headline"}

By [Marc de
Bruijn](http://networkcultures.org/digitalpublishing/author/marcdebruijn/ "Posts by Marc de Bruijn"),
November 19, 2014 at 3:26 pm.

[![epubster-04](imgs/epubster-04.png)]()

With *EPUBster* (for lack of a better name) we tried to develop a web
application allowing publishers to edit and create EPUBs. We us the term
‘publisher’ very loosely in this instance, also referring to developers,
designers or editors. *EPUBster* was partly developed for Amsterdam
based publisher Valiz and designers Meeus Ontwerpt in order for them to
create a series of books titled “Context Without Walls”. Their feedback
at various points prompted some of the design and implementation
decisions. As such the application is intended as a general purpose tool
for generating EPUBs, but incorporating some very specific features,
such as support for multiple indices.

The application can be broken down in a few components:

-   A very simple metadata editor offering just the necessary fields as
    defined in the EPUB standard;
-   Section or chapter editor, used for rearranging and deleting
    chapters in an EPUB;
-   Content editor allowing the user to manipulate the text of a
    section/chapter;
-   Options to add a book cover and CSS styling.

After creating an edition, filling in the required metadata and creating
some chapters, the user is then able to generate or preview an EPUB
based on the inputted data.

The same components used to build the application are represented in the
user interface. The interface allows the publisher to author a
publication step-by-step, from primary information and metadata input in
the first tab of EPUBster to adding a cover as the last step of the
process. To assist the user with the creation of a publication and
provide a flexible workflow, one can switch between tabs and components
of the application. This allows for a non-lineair workflow and the
possibility of adding chapters to a publication or change the design by
adding different CSS-files at a later stage.

## The Application

At the time we decided to build the application using a PHP framework,
*CakePHP*. Having developed multiple applications using the framework,
*CakePHP* proved to be a familiar environment allowing us to rapidly
prototype the features of the application. One of the downsides of
CakePHP is the slowness of the framework compared to other offerings and
the reliance on what’s often called “automagic” in Cake’s documentation.
As our recent experiences with the *Laravel* framework, partly built on
*Symfony*, have been very positive, the initial choice for *CakePHP* as
a foundation doesn’t seem as straightforward at this point.

One of the restrictions that guided the development process was the
requirement that the application should run on very common server
hardware. As a lot of webhosting environments are of the “shared
hosting” variety, making use of shell programs was out of the question.
It would be relatively simple to build a web GUI on top of *calibre*’s
command line interface or a document converter like *pandoc*. Instead we
relied on PHP libraries for most of the generative features of the web
application. Asbjorn Grandt’s
[*PHPePub*](https://github.com/Grandt/PHPePub) forms the core of the
application and was packaged, with some modifications, as a Cake plugin
in order to receive content from *EPUBster*’s MySQL database containing
the publication data.

At first we focussed on processing Markdown formatted text as input for
the various chapters/sections in a publication. After storing the
Markdown text in a database this is then converted to HTML and
subsequently processed by *PHPePub*. The conversion is done using the
[*Markdown Extra*](https://michelf.ca/projects/php-markdown/extra/)
library packaged as Cake plugin [by Maury M.
Marques](https://github.com/maurymmarques/markdown-cakephp).*WYSIWYG*
(What You See Is What You Get) orientated approach, while still
supporting Markdown. The *WYSIWYG* editor is an extended version of Davi
Ferreira’s [*Medium
Editor*](https://github.com/daviferreira/medium-editor). As the editor
manipulates HTML directly, no conversion is necessary prior to
generating an EPUB. Due to the fact that the editor uses HTML5’s
*contenteditable* behaviour there is support for parsing rich text
pasted from text editors and word processors. Bolds, italics, colours,
etc. will be pasted as HTML in a *contenteditable* element. This
introduces several problems however, as some word processors (notably
*Microsoft Word*) wrap formatted text in tags with a lot of style
attributes, resulting in a lot of undesirable and superfluous markup
when generating an EPUB. Stripping the unwanted markup (font-families,
line-height, etc.), while leaving the desirable elements (bold, italic,
etc.) in place took some modification of the *Medium Editor*’s codebase.

In earlier versions of the application it was only possible to preview a
draft edition by generating an EPUB, downloading the file to the user’s
harddrive and previewing said file in an ereader like *calibre* or
*iBooks*. To provide a more immediate way to preview draft editions we
decided to implement a JavaScript EPUB viewer. *ReadiumJS* seemed like a
natural choice, as the project is backed by several large publishers and
the *International Digital Publishing Forum*, the curators of the EPUB
standard. However at the time of implementation, *ReadiumJS* – which is
still in heavy development – proved to be too unstable for production
use. Instead we opted for
[*epub.js*](https://github.com/futurepress/epub.js/) by Fred Chasen, an
actively developed JavaScript library comparable to *ReadiumJS* which
offers a more robust experience. When a user previews an edition in
*EPUBster* an EPUB is generated on the fly and rendered in the browser
using *epub.js*.

The current version of *EPUBster* [is available on
GitHub](https://github.com/DigitalPublishingToolkit/epubster). As it
stands the application should be considered of alpha quality and could
do with a lot more testing and polish. Testing of the EPUBs generated by
the application on several ereading devices should be a priority, for
example, should development on the application continue in some for or
other. However, it should currently be possible to create a
fully-fledged EPUB 3 without much trouble using the tools provided by
*EPUBster*.



[![epubster-02](imgs/epubster-02.png)]()
[![epubster-05](imgs/epubster-05.png)]()
[![epubster-07](imgs/epubster-07.png)]()
[![epubster-04](imgs/epubster-041.png)]()
[![epubster-06](imgs/epubster-06.png)]()
[![epubster-08](imgs/epubster-08.png)]()
[![epubster-03](imgs/epubster-03.png)]()


