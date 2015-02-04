---
title: Hybrid workflow how-to: Making automated workflows, part 1
author: Michael Murtaugh
date: 2014-10-21
...

# Hybrid workflow how-to: Making automated workflows, part 1 {.entry-title .single-title itemprop="headline"}

By [Michael
Murtaugh](http://networkcultures.org/digitalpublishing/author/michaelmurtaugh/ "Posts by Michael Murtaugh"),
October 21, 2014 at 11:53 am.

The first post in this series can be found here:[Hybrid workflow how-to:
introduction & editorial
steps](http://digitalpublishingtoolkit.org/2014/10/hybrid-workflow-how-to-introduction-editing-steps/)

As part of the [INC subgroup](http://networkcultures.org), we have been
developing a workflow that allows a flexible production of different
kinds of electronic outputs like EPUB, PDF, and [book
trailers](http://digitalpublishingtoolkit.org/2014/10/epub-trailers/)
from a sample collection of essays from the recently published [Society
of the Query](http://networkcultures.org/query/) Reader.

In part one of this tutorial, we look at using the
[pandoc](http://johnmacfarlane.net/pandoc/) tool on the command line to
convert a [markdown](http://daringfireball.net/projects/markdown/)
source that has been edited by an editor into HTML and EPUB outputs. In
addition, we will add metadata and use pandoc templates and a stylesheet
to customize the output.



This tutorial is targeted for developers or people interested in
creating automated workflows for producing EPUBs. It assumes basic
familiarity with a commandline interface (such as the Terminal
application on GNU/Linux or Mac OS X, or the command prompt in Windows).
Introductions to the commandline such as the [Designers guide to the OS
X Command
Prompt](http://wiseheartdesign.com/articles/2010/11/12/the-designers-guide-to-the-osx-command-prompt/)
can be very useful if the commandline is still new to you.

## Install pandoc

Instructions for installing pandoc on Mac, Windows, and Linux are given
on the [pandoc
website](http://johnmacfarlane.net/pandoc/installing.html).

Mac: From the [download page](https://github.com/jgm/pandoc/releases),
find the green button with a link that ends with “osx.pkg”. Download and
install this.

Debian/Ubuntu: Pandoc is available from your package manager:

``` {.sourceCode .bash}
sudo apt-get install pandoc
```

However, the version of pandoc is typically outdated. To compile the
latest and greatest, follow the instructions on the [pandoc
website](http://johnmacfarlane.net/pandoc/installing.html) under “All
platforms”. In a nutshell:

``` {.sourceCode .bash}
sudo apt-get install haskell-platform
cabal update
cabal install pandoc
```

## Prepare your workspace & tools

Unpack, checkout or copy the sample files from the [github
repository](https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader).
Open the Terminal and use the cd command to enter the “part1″ folder in
the developer section of the how-to-tutorial files.

``` {.sourceCode .bash}
git clone https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader.git

cd how-to-tutorial/developer/part1
```

As we will be working with different kinds of code (both markdown and
HTML output), it is quite important to have a good code editor to work
with. A code editor (as opposed to programs like “Simple Text” or
Microsoft Word) provides features like language-specific syntax coloring
and helpful keyboard shortcuts for say adding comments. Many code
editors exist from classical commandline editors like vi and emacs, to
graphical editors like gedit and [Sublime
Text](http://www.sublimetext.com/). Though not Free Software, [Sublime
Text](http://www.sublimetext.com/) is an excellent cross-platform code
editor with many advanced features, which is free of charge to use (in
Trial mode) indefinitely and a good example of the state of the art of
contemporary code editors in terms of features and usability.

## Use pandoc to convert a single markdown source file to HTML & EPUB

As you may have seen in Step 5 of the [Hybrid Workflow Howto for
Editors](http://digitalpublishingtoolkit.org/2014/10/hybrid-workflow-how-to-introduction-editing-steps/),
you can use the pandoc program to convert from one file format to
another (such as in that example from Word DOCX to Markdown). In this
step we use pandoc to convert an edited markdown file as it would arrive
from an editor into first HTML, and then to an EPUB.

Open the file Kylie-Jarett.md in your editor, it begins:

``` {.sourceCode .markdown}
# A Database of Intention?

Kylie Jarrett

In his 2005 study of Google, industry analyst John Battelle describes
the company’s technology as a ‘database of intentions’, ‘a massive
clickstream database of desires, needs, wants, and preferences that can
be discovered, subpoenaed, archived, tracked, and exploited for all
sorts of ends’.[^1]
```

In the terminal type the following. Note that once you type the K of the
filename you should be able to press the tab key to “auto-complete” the
name of the file:

``` {.sourceCode .bash}
pandoc Kylie-Jarrett.md 
```

By default pandoc will attempt to guess the type of the input file based
on the file extension. In this case the “.md” means that pandoc assumes
Markdown input. By default pandoc produces HTML and prints it to the
terminal rather than saving it in a file. To save it to a file, you can
use pandoc’s -o option:

``` {.sourceCode .bash}
pandoc Kylie-Jarrett.md -o test.html
```

You can also explicitly state input and output types with pandoc’s –from
and –to options. This can be useful if a filename misses a recognizable
extension:

``` {.sourceCode .bash}
pandoc --from markdown --to html Kylie-Jarrett.md -o test.html
```

In general the order of the parameter doesn’t really matter, as long as
the options precede their values, so the following would be the same:

``` {.sourceCode .bash}
pandoc -o test.html --to html --from markdown Kylie-Jarrett.md
```

Use a web browser to open the resulting file (test.html) and check the
output. It should appear as formatted HTML. However there are likely
some glitches in the text. This is because pandoc’s default HTML output
is merely a fragment, and not a complete HTML document, and some
information (such as the proper encoding of the text) is not included.
If you open test.html in your editor, you see that the file begins:

``` {.sourceCode .html}
<h1 id="a-database-of-intention">A Database of Intention?</h1>

...
```

Note that pandoc automatically assigns an id to the header. This is
useful when linking. Next, run pandoc again, this time adding the
–standalone (or -s) option:

``` {.sourceCode .bash}
pandoc essays/Kylie-Jarrett.md --standalone -o test.html
```

If you reload test.html in the browser, you should see that the
character gliches are corrected. If you look at test.html in your
editor, you see it now begins:

``` {.sourceCode .html}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  
  code{white-space: pre;}
</head>
<body>
<h1 id="a-database-of-intention">A Database of Intention?</h1>
...
```

The output now contains a proper HTML doctype and head section with,
among other things a character set, which tells the browser to interpret
the text as encoded in the utf-8 standard (Browsers by default assume
the latin-1 character set when a document doesn’t state it’s encoding
which is why the characters were being misinterpreted in the fragment).

## Add metadata to your document

In the HTML output in the previous step, the title tag in the document
is left blank. Even though the title of the essay is in the document,
it’s a level one header, pandoc doesn’t make any assumptions that that
is a title. Pandoc supports adding “metadata” (data about the document
itself).

Add the following to the first lines of the file
“essays/Kylie\_Jarrett.md”:

``` {.sourceCode .yaml}
---
title: A Database of Intention?
author: Kylie Jarrett
---
```

Now repeat the pandoc command to update the test output:

``` {.sourceCode .bash}
pandoc essays/Kylie-Jarrett.md --standalone -o test.html
```

The resulting document now looks like this:

``` {.sourceCode .html}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <meta name="author" content="Kylie Jarrett" />
  A Database of Intention?
  code{white-space: pre;}
</head>
<body>

<h1 class="title">A Database of Intention?</h1>
<h2 class="author">Kylie Jarrett</h2>

<h1 id="a-database-of-intention">A Database of Intention?</h1>


<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <meta name="author" content="Mél Hogan" />
  <meta name="author" content="M.E. Luka" />
  Polluted and Predictive, in 133 Words
  code{white-space: pre;}
</head>
```

## Customize your output with a template and a stylesheet

So how did pandoc know what to do with the title and author in your
metadata? It turns out that [pandoc has a collection of standard
templates](http://johnmacfarlane.net/pandoc/README.html#templates), or
for each output format, which it uses to produce its output.

To see pandoc’s template for producing HTML output, type the command:

``` {.sourceCode .bash}
pandoc -D html
```

The output (in part) shows:

``` {.sourceCode .html}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"$if(lang)$ lang="$lang$" xml:lang="$lang$"$endif$>
<head>
  ...
  <meta name="author" content="$author-meta$" />
endfor$
if(date-meta)$
  <meta name="date" content="$date-meta$" />
endif$
  $if(title-prefix)$$title-prefix$ - $endif$$pagetitle$
  ...
for(css)$
  <link rel="stylesheet" href="$css$" $if(html5)$$else$type="text/css" $endif$/>
endfor$
</head>
<body>
...
if(title)$

<h1 class="title">$title$</h1>
if(subtitle)$
<h1 class="subtitle">$subtitle$</h1>
endif$
for(author)$
<h2 class="author">$author$</h2>
endfor$
if(date)$
<h3 class="date">$date$</h3>
endif$

endif$
```

In the template, you can see that pandoc provides some sophisticated
tools like conditionals (if) and loops (for) to provide basic handling
for optional elements and lists author names. To customize this standard
template, make a copy of it named custom.html:

``` {.sourceCode .bash}
pandoc -D html > custom.html
```

Open the custom.html and change the display of the title and author to:

``` {.sourceCode .html}
if(title)$

  <h1 class="title">$title$</h1>
  
    &#172;
    $for(author)$
    $author$
    $endfor$
  

endif$
```

You can also see in the template that pandoc provides a number of ways
of adding custom stylesheets. The easiest is to use the –css option. So
create a new file names “styles.css” with the following:

``` {.sourceCode .css}
body {
  font-family: sans-serif;
}
#header {
    text-align: center;
}
h1 {
  margin-bottom: 0;
}
.author {
  font-weight: bold;
}
```

And now bring it all together with:

``` {.sourceCode .bash}
pandoc Kylie-Jarrett.md --standalone --template custom.html --css styles.css -o Kylie-Jarrett.html
```

## Produce an EPUB

You can easily [produce an EPUB from a markdown source with
pandoc](http://johnmacfarlane.net/pandoc/epub.html) by simply specifying
an EPUB extension to the output file. Note that the –standalone option
is implicit with an EPUB:

``` {.sourceCode .bash}
pandoc Kylie-Jarrett.md -o Kylie-Jarrett.epub 
```

To specify custom CSS with an EPUB, use the –epub-stylesheet option:

``` {.sourceCode .bash}
pandoc Kylie-Jarrett.md --epub-stylesheet styles.css -o Kylie-Jarrett.epub
```

Note that pandoc places an automatically generated table of contents as
the last page, to move this to the front use the –table-of-contents
option.

``` {.sourceCode .bash}
pandoc Kylie-Jarrett.md --epub-stylesheet styles.css -o Kylie-Jarrett.epub --table-of-contents
```

## Next time… {#next-time...}

In part 2 of this tutorial, we will work on a script to compile a
collection of essays into a single Reader EPUB.
