---
title: DPT Hackathon Results
author: Michael Murtaugh
date: 2014-04-30
...

# DPT Hackathon Results {.entry-title .single-title itemprop="headline"}

By [Michael
Murtaugh](http://networkcultures.org/digitalpublishing/author/michaelmurtaugh/ "Posts by Michael Murtaugh"),
April 30, 2014 at 12:49 am.

![caption](imgs/IMAG0554.jpg)

Thursday and Friday April 24 & 25 a hackathon took place at the Piet
Zwart Institute in Rotterdam. Over the course of 2 days, some of the
developers of the Digital Publishing Toolkit initiative gathered to work
on their projects and to share experiences, code and tools and discuss
the (devil-is-in-the) details of developing for digital publications.

present (left to right in photo): Michael Murtaugh, Marc de Bruijn,
Sauli Warmenhoven, Florian Cramer, Andre Castro, Kimmy Spreeuwenberg
(facilitating and taking the photo ;), , and Miriam Rasch dropped by for
a bit.



## An overview of the projects

### Marc de Bruijn / Valiz {#marc-de-bruijn---valiz}

Marc is working on an ePub generator for the Valiz publication ”Context
without Walls”. This web-based generator allows the publisher to
generate (and edit) epubs based on text structured with Markdown. The
EPUBs may be styled by selecting from a list of available styles
packages. These style packages are basically a zipped collection of CSS
and other resources like font files. Over the last couple of weeks they
have been adding functions, and a more user friendly interface. The
project can be found on the [DPT github
page](https://github.com/DigitalPublishingToolkit/epubster).

Another (future) part of the generator will be the possiblity to
generate a cover based on the CSS of the ePub.

#### The current worflow of the generator is as follows:

-   Create a new edition by filling in the mandatory form field;
-   Add the necessary sections which will form the structure of the
    edition. Sections have a title and a body of text structured with
    Markdown. The order of the sections can be changed after creating
    them;
-   A cover can be added and a style package may be chosen;
-   After all these steps have been completed an EPUB can be generated
    or previewed within the application

#### The generator already includes:

-   The possibility to use custom fonts
-   It makes sure the epub includes all the necessary metadata
-   Chapters can be ordered, each chapter is a separate HTML file
-   It is possible to view the epub in the application itself
-   They’ve added an interface to add covers to the publication
-   Possibility to choose between different CSS via an upload function
    to add custom styles is planned

#### Software used:

-   CakePHP – <http://cakephp.org/>
-   epub.js – <http://fchasen.github.io/epub.js/> epub reader in browser
    for preview functionality
-   PHPePub <https://github.com/Grandt/PHPePub>
-   <http://validator.idpf.org> Validator/ & EPUB-Checker (standalone of
    the website)

#### Problems/Issues to look into

-   At the moment the main problem is that the generator doesn’t produce
    valid EPUBs. The files can be viewed in an EPUB reader, but do not
    validate against the EPUB 3 standard
-   The usage of endnotes causes validation problems, a fix is
    forthcoming
-   The EPUBs should play nicel with major epub readers, as of yet the
    generated EPUBs do not display their cover in Apple’s iBooks, for
    example.
-   The generator might include functions to generate a cover based on
    the chosen style package, this ties into the requirements for the
    Stedelijk Museum project, where the resulting EPUB should have a
    composited cover containing artworks chosen by the user.

#### Results/Conclusions

Some progress made resolving the many validation errors, most of them
stemming from duplicate footnote IDs. The code responsible for parsing
the footnotes should be changed, this will eliminate most, if not all,
validation errors.

A first attempt at a generated EPUB cover has been made, but the
difficulties of automatically generating any sort of simple design
involving text were encountered. Text positioning and wrapping is hard,
especially in a barebones library like GD2 (ImageMagick supposedly
offers more advanced functions in this regard). Sauli proposed a
different approach using an image export of the HTML5 canvas element,
which is worth looking into as well (as javascript libraries like
paper.js or processing.js could be employed).

### Michael Murtaugh / Institute of Network Cultures (INC)

Michael as been researching the different tools/platforms that can play
a role in the Institute of Network Cultures projects workflow for hybrid
publishing, which at the same time allows to create personalized epubs.
It tries to find a balance between complex HTML based editors, and the
actual knowledge/skills publishers have to work with these tools. The
focus is on a modular approach in which different choices for tools or
programs can be made. Working the classic way from Word, and converting
this to HTML with *pandoc*, or starting from a (multi)markdown
structured document. Rather than aiming for creating (yet another) ideal
platforms, the intent is to develop flexible workflows that allow
mixed-toolsets: editors, version control and repositories, (commandline)
document converters, epub reader software. The Society of the Query
Reader, just released in print form by the INC, is being used as in
an-process test case.

Michael showed a working sketch interface for a **personalized epub
generator** for the Society of the Query online reader. The idea is that
the results from a search engine query can be compiled and downloaded to
custom epub. The essays of the reader are indexed, using the Python
search engine [Whoosh](https://bitbucket.org/mchaput/whoosh/wiki/Home).
In addition, a separate scraper script (taken from the earlier Hackathon
in Utrecht) downloads images from the SotQ2 event Flickr stream along
with their captions and adds these to the search index. The plan is to
use Calibre’s ebook-converter then to convert the search results and
linked content into a downloadable epub.

#### Current Workflow

The documents of this publication have been developed in a classic
workflow – starting from Word files collected from authors. The
following steps have already been taking to get from this stage to the
eventual digital publication: \* Conversion doc to docx by LibreOffice
(manually done) \* docx converted to HTML by Calibre’s ebook-convert
script (batch) \* Python scripts to clean up (strip "invisible" markup
like non-breaking spaces), validating and sensibly indenting the
resulting XHTML (using html5lib & ElementTree). These [scripts can be
found in the SotQ2
repo](https://github.com/DigitalPublishingToolkit/SotQ2/tree/master/scripts).

#### HTML editor?

We began with a hypothetical workflow for editing the HTML directly in
the browser using the browser’s own integrated inspection tools
(Firefox’s DOM inspector and style editor) & HTML5’s contenteditable
attribute and javascript in combination with a simple local python
webserver to save the live documents content back to the local
filesystem as an HTML file. Marc suggested we also look into using
javascript extensions such as the [medium
editor](http://daviferreira.github.io/medium-editor/) (free software
recode of the popular proprietary platform’s interface) as an example of
the "state of the art" of non-intrusive in-browser editing widgets.

In general, "live" editing of the HTML in the browser offers the
directness of "WYSIWYG" and taps into the many free software efforts to
make editing in the browser better. We discussed other possibilities
like integration with git, and some kind of simple means of applying the
various cleanup scripts (typically performed on the commandline) via
buttons in the browser interface.

This approach turned out to be contentious (Will publishers actually
work with this? It is easier to do corrections, but the structure in
html can be overwhelming. With this model you still need specialist to
help with certain problems. ) and led to a [fruitful discussion with
Florian Cramer for why a Markdown approach might be better
suited](http://networkcultures.org/digitalpublishing/2014/04/mark-me-up-mark-me-down/).

##### Problems/Issues to look into

For the SotQ front end interface, one issue is how to adjust the search
result algorithm to include images related to articles that match the
search (but are possibly not directly linked). In other words, when
searching for the term "keyword", the search results include the article
Is Small Really Beautiful? Big Search and Its Alternatives by Astrid
Mager, and then the results include images with Astrid Mager included in
their caption. The code for the proof of concept is included in the
SotQ2 repository (though not yet in a form viewable online).

### Andre Castro / INC Notebooks {#andre-castro---inc-notebooks}

Many of the INC project issues and questions overlap with Andre Castro’s
work developing epubs for the INC netbooks series from word documents.

**Problems/Questions he came accross so far:** \* Calibre converter: how
to make clear and structured conversions from docx to html? Calibre
creates a series of artifacts in the conversion process: *\* empty tags
(again)* \* Losing table of contents hierarchy

In this workflow that starts with docx there is the necessity to enforce
a style guide / protocol for the docx e.g.: Asign a style (like h6) to
blockquotes, sections tiltes as heading, so these can be seamingless
converted. And if they are not well converted one can go back to .docx
document and search for the particular style, quickly finding the
content contained under that style. Yet, this remains difficult.

-   (Libre) Open Office \>\>\> why is the html export so bad?

#### Results/Conclusions

My initial idea was to work on the preparation of the master HTML file
that will give birth to the epub.

I aimed to developed scripts to : \* clean html artifacts from calibre
conversion \* create an indented strucutred TOC – based on the document
headings the work-flow what was I aiming for:

docx –(calibre)–\> epub(html) –(clean scripts)–\> clean html

From the discussion with Florian it was clear that there was a necessity
to have as the master/source file of the book, very lean and robust,
with only the essential structure and clear to read. Markdown was an
answer, since it has a very strict syntax, readable, and when converting
a messy html into markdown it cleans it out of the calibre artifacts.

The ”’drawback”’ is that footnotes are going to be broken. They have to
be ”prepared” before hand (using a script).

To create a structured TOC I used: using calibre conversion tool:

ebook-convert IN\_FILE.docx OUT\_FILE.epub –dont-split-on-page-breaks
–pretty-print –toc-title "Table of Contents"
–level1-toc="//*[name()=’h1′]" –level2-toc="//*[name()=’h2′]"
–level3-toc="//\*[name()=’h3′]" –epub-inline-toc

The important bit is: –level1-toc="//*[name()=’h1′]"
–level2-toc="//*[name()=’h2′]" –level3-toc="//\*[name()=’h3′]" which
translates to: all the level 1 of toc = to the name of the all the
headings 1, and so forth for the other levels.

### Sauli Warmenhoven / BIS publishers

Sauli is working on a digital version of Sketching, a tutorial
publication for designers in which they learn to draw design objects. It
is divided between different exercises that refer to different skills.
Starting point of the project was to explore the possibilities of
designing a highly interactive publication using open standards like
HTML5 rather than rely on the proprietary nature of the iBooks format.
As such they decided to develop a standalone web application, and
developed, in a sense their own custom reader experience using html5 and
javascript. The exercises and skills are two separate tracks of
chapters, that are interlinked. Building their own reading application
allows us to create a custom built reader for this specific publication.

#### Tools used

*jQuery* for javascript development, with the touch events from *jQuery
Mobile* which normalizes browser implementations of javascript and touch
events and provides a consistent way of writing code. Once everything is
working, we will then package the webapplication in a platform-specific
shell using *phonegap* a mobile development framework. Phonegap allows
us to tap into device specific features, such as locking the screen
orientation.

#### Problem/Question to look into

-   HTML5 gives new possibilities for digital publishing, also compared
    to iBook/epub, but there isn’t really a clear overview of these
    possiblities and issues. A blogpost what they. html5 vs API compare
    what the possibilities or problems are? for instance Orientation:
    Javascript/CSS knows about it (but not consistent), but need API to
    lock it
-   Could we make a table of functionalities that are HTML5 vs API only
    to illustrate how this project is really pushing the boundaries of
    HTML5 + Javascript to build highly customized apps

### Florian Cramer

-   Footnote renumbering tool (linebased, doesn’t renumber it if they
    are on the same line) : this has been solved by using pandoc to
    convert from and to markdown;
-   Markdown pretty printer / tidy markdown see above; pandoc can also
    be used for this purpose

The three Toolkit sections introducing Markdown and explaining its
relative advantages and disadvantages (relative to XML, for visual and
interactive publishing, for multi-channel publishing, extensibility vs.
human readability and ease-of-use), have been written and submitted to
the GitHub repository: docs/markdown-advantages.md docs/markdown-tips.md
docs/markdown-vs-xml.md

**Results/Conclusions** \* footnote fixer also works as a numbered list
fixer. \* Markdown introductions for Toolkit reflect our discussion on
Markdown this morning \* will still write a tool to track orphaned
footnotes

See also the [Markup vs. Markdown
Discussion](http://networkcultures.org/digitalpublishing/2014/04/mark-me-up-mark-me-down/).
