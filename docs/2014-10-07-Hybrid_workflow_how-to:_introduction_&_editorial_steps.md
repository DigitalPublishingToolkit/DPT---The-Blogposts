---
title: Hybrid workflow how-to: introduction & editorial steps
author: Miriam Rasch
date: 2014-10-07
...

# Hybrid workflow how-to: introduction & editorial steps {.entry-title .single-title itemprop="headline"}

By [Miriam
Rasch](http://networkcultures.org/digitalpublishing/author/michael/ "Posts by Miriam Rasch"),
October 7, 2014 at 2:57 pm.

The hybrid workflow described below is developed by the [Institute of
Network Cultures](http://networkcultures.org) within the Digital
Publishing Toolkit. The research into this workflow was aimed at making
the transition from a print-centered publication process towards a
digital and print (hybrid) publication process. We ask the question: how
to handle documents so publication on different platforms is possible?
This means we don’t go into appropriate styles of writing or ways of
designing epublications vis-à-vis paper books.

Creating a workflow that is both structured and flexible enough to cater
for the different choices made is a key step towards an efficient
electronic or hybrid publishing strategy. The hybrid workflow we propose
here is based on the need for publishing across different mediums, while
keeping the majority of the work process in-house instead of
outsourcing.

Instead of ‘adding’ the digital publication at the end of an existing
workflow, based on the printed book as end result as is often done by
publishers, the workflow should be adjusted and made efficient and
practical towards hybrid publishing in an earlier stage. From-scratch
development of each publication format is thus replaced by single
source, multi format publishing.

The old, ‘traditional’ workflow is centered around the paper book
production, which basically means that it is centered around an InDesign
file. This file or the PDF that goes to the printer is the final
document that can be archived. The new, ‘hybrid’ workflow, is centered
around the archive file in Markdown, which is used as the basis for
publications in different output formats. A Markdown-oriented workflow
is both easy to use and open to many possibilities.

This manual is divided into three parts, one for each ‘role’ in the book
production process: editor, print book designer, and ebook developer.
Below you’ll find the editorial steps – the first in the process. For
the print design and ebook development see the respective blogposts for
print book designer steps and ebook developer steps (to be published
shortly).

Please note that the description below starts at a point which in
reality is not the beginning of the publication trajectory, namely when
an author hands in the definitive manuscript – so after the editing and
rewriting process has been rounded off. Should the author already be
working in Markdown format, this will change the workflow. However, in
our experience manuscripts are mainly produced in Microsoft Word and
delivered in .doc or .docx.

NB: An important step preceding the publication trajectory lies in the
formulation of the in-house style guide, where authors and editors can
find the requirements for the manuscript. This style guide must be
adapted according to the hybrid workflow as an absolute start. This
issue will be taken up in another blogpost.

So how small edition, low budget publishing houses can implement the new
workflow is what we will turn to now.

## What is needed in preparation:

**1. Install Pandoc** ([installation
page](http://www.johnmacfarlane.net/pandoc/installing.html)). Pandoc is
working in the so-called command line mode and not in a user interface
environment. Hence you can’t ‘open’ the program and don’t see an icon.

Windows: To start pandoc type cmd in the RUN (also called ‘search
programs and files’ in the start panel which can be found under the MS
window icon down in the toolbar), this will enable you to start the
command mode. You get a white/black window saying C:useryourusername\>.
There you type pandoc (enter) and the same line reappears, waiting for
pandoc input (see further below).

Mac: To use pandoc open the Terminal from your Utilities folder in your
Applications folder, or through the search bar in the top right of your
screen. Pandoc will be used to convert files in the steps below. *Note:
Pandoc does not work on older Mac operating systems*.

**2. Install a Markdown editor**. For Mac, use for example
[Mou](http://25.io/mou/) or [MacDown](http://macdown.uranusjr.com/); for
Windows, [MarkdownPad](http://markdownpad.com/).

*What is Markdown?* John Gruber, developer of Markdown, describes
Markdown on [his website](http://daringfireball.net/projects/markdown/)
as follows: ‘Markdown allows you to write using an easy-to-read,
easy-to-write plain text format, then convert it to structurally valid
XHTML (or HTML).’ Markdown is a way to process plain, unformatted text
with human-readable formatting symbols. That means that Markdown doesn’t
use HTML style tags to format, such as \<b\> for bold or \ to
mark-up the author name, but rather \#, \* and \_.

## Notes on working in Terminal

-   Delete: If you like to delete parts of your text you need to use
    your cursor and backspace. It is not possible to select parts of the
    text and delete it nor can you move in the text by selecting a spot
    with your mouse.
-   Go back: you can go back to earlier commands with the up arrow
-   Refresh: Close window and open a new one
-   You know that your command worked if you do not get an error.

## Editorial steps

You receive a digital document containing the definitive manuscript from
an author. We’ll name this file Jane\_Writer\_def.doc.

STEP 1: Open the file in Microsoft Word.

STEP 2: Convert the document to docx-format by saving it as
Jane\_Writer\_def.docx.

STEP 3: Apply header styling in the Word-document. Use header 1 for
title and author, header 2 for section title, header 3 for level below,
et cetera. Header styling is found in the Toolbar of Microsoft Word
under ‘Styles’ – click on the icon and select the right style. Or go to
the menu and select ‘View’ and ‘Styles’ under Toolbox and work from the
pop-up panel.

STEP 4: Save.

STEP 5: Convert the docx to Markdown using pandoc (for an elaborate user
manual, see the [pandoc
website](http://www.johnmacfarlane.net/pandoc/)):

-   Pandoc is a command-line tool. There is no graphic user interface.
    So, to use it, you’ll need to open a terminal window (see above).
-   Create a subfolder in your Documents folder called ‘pandoc-test’.
    For Windows, put this under C:usersyournamedocuments (in many cases
    this is the default directory). This is the folder where we’ll store
    and retrieve documents to be converted and which are made by pandoc.
-   Put the docx-document you want to convert in this folder called
    pandoc-test. In this case: Jane\_Writer\_def.docx.
-   Go to the terminal and type cd Documents. This means the terminal
    will ‘change directory’ to the Documents folder.
-   Now type cd pandoc-test. The terminal will change directory to the
    folder within the Documents folder called pandoc-test. Now you can
    work with the documents in there.
-   On Mac, type ls [l as in lima, referring to ‘list’], on Windows dir
    to get a list of files in the current folder. The
    Jane\_Writer\_def.docx should be listed.
-   To convert the file from docx to markdown, type the following into
    the terminal: pandoc Jane\_Writer\_def.docx -f docx -t
    markdown -s -o Jane\_Writer\_def.md
-   The filename Jane\_Writer\_def.docx tells pandoc which file to
    convert, -f docx -t markdown, so from docx to markdown. The -s
    option says to create a ‘standalone’ file, with a header and footer,
    not just a fragment. And the -o Jane\_Writer\_def.md says to put the
    output in a file named Jane\_Writer\_def.md. (Note: in Mac you can
    copy-paste the command, in Windows you can’t copy-paste.)
-   Check that the file was created by typing ls or dir again. You
    should see Jane\_Writer\_def.md.

STEP 6: Open the Markdown editor that you installed (Mou or
Markdownpad), navigate to the pandoc-test directory and open the file
you just created using pandoc, Jane\_Writer\_def.md. The file will now
be opened in the markdown editor. You see two panels. The left panel is
the markdown format which we use to work in, the right panel is the
rendering of the coded panel into a user-readable-form. (You can also
try to type ‘open Jane\_Writer\_def.md’ in the terminal to open the
file.)

STEP 7: Check the Markdown file after conversion: are the headers still
marked, is there no funny formatting in the text, are the blockquotes
and italics preserved, for example in the references?

STEP 8: We use a template document showing how the formatting should be
applied in a correct way and which metadata to add. The text can be
copied into this document template, the format adjusted where needed
(for instance title, author name, headings, references, notes, the table
and the image). Save the file as Jane\_Writer\_final.md by choosing
‘duplicate’.

STEP 9: Add metadata information. Below is an example of relevant
metadata used by the INC:

    #Metadata

    Pr-id: project
    P-id: publication series
    A-id: number within the series
    Type (formerly called Item): type of the item
    Book-type: anthology or monograph
    Anthology item: TOC, article, index etc.
    Item-id: unique no.
    Article-title: title of the article
    Article-status: submitted, under review, accepted
    Author: name(s) of author(s)
    Author-email: corresponding address
    Author-bio: about the author
    Abstract: short description of the article (100 words)
    Keywords: 50 keywords for search and indexing
    Rights: Creative Commons etc. 

STEP 12: Save the final Markdown file into an archive folder. This is
the document that can be send to the print designer and epub developer
to work with in the production of the print book and ebook.

## Images

Check format of the images: is the quality good enough for print? Scale
images to smaller size for e-book publication. Store the images and send
to designer and developer.

## Corrections

Corrections form a large part of the editor’s workflow. How to handle
them will be the subject of a separate blogpost.
