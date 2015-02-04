---
title: Mark me up, Mark me down!
author: Michael Murtaugh
date: 2014-04-30
...

# Mark me up, Mark me down! {.entry-title .single-title itemprop="headline"}

By [Michael
Murtaugh](http://networkcultures.org/digitalpublishing/author/michaelmurtaugh/ "Posts by Michael Murtaugh"),
April 30, 2014 at 12:50 am.

During the recent [Digitial Publishing Toolkit
hackathon](http://networkcultures.org/digitalpublishing/2014/04/dpt-hackathon-results/),
the proposal, made in the context of the INC project, for a using a
browser-based editing workflow centered on HTML as the core “document”
format was challenged in a discussion initiated by Florian Cramer who
proposed focusing instead on the Markdown format. The resulting spirited
discussion began focussed on questions of ease of use and features of
the respective approaches and ended up touching on fundamental
principles of document markup in relation to (digital) publishing.



Can editing HTML ever be something possible for “non-experts”? Or,
better said, for those whose skills do not include some working
knowledge of HTML. While web programmers, technical editors, and
designers often come to understand HTML’s particularities through their
work, publishers and copy editors tend not to. Florian argued for the
clarity of Markdown’s cleaner “structured text” format over the
idiosyncrasies of HTML. The particular needs of the INC, whose reader
publications are primarily collections of academic essays with elements
such as footnotes and references, figures and captions, was a key issue.
HTML (in its latest incarnation HTML5) lacks a firm standard for marking
up footnotes (though current standards documents do [suggest some best
practices using HTML’s existing “link” or anchor
element](http://www.w3.org/TR/html5/common-idioms.html#footnotes)). In
contrast, markdown offers an explicit and convenient syntax for
specifying footnotes (also through a kind of “best practices” extension
to the original syntax by the “multimarkdown” project which has now been
widely [embraced by many other markdown tools such as
pandoc](http://johnmacfarlane.net/pandoc/demo/example9/pandocs-markdown.html)).
Beyond just the important details related to footnotes, the ongoing
discussion revealed a number of more fundamental questions and
principles related to markup languages.

### Markup

The concept of markup exists for decades now, coming primarily from the
intersection of engineering and publishing interests to make generalized
methods for indicating structure and editorial intentions (through
“tags”) in text documents for the purposes of producing technical
documentation in a “multi-path” way. In other words, a flexible system
where the same input text files can be used to produce documentation in
a variety of languages and/or for a variety of output forms and methods
of printing. The [SGML](http://www.w3.org/MarkUp/SGML/) standard
(Standard Generalized Markup Language, 1986) formed the basis on which
Tim Berners-Lee’s [HTML](http://www.w3.org/html/) (Hypertext Markup
Language, 1989), design would form, and led to the parallel development
of [XML](http://www.w3.org/XML/) (Extensible Markup Language, 1996) to
include applications beyond web publishing.

### Markdown

> A Markdown-formatted document should be publishable as-is, as plain
> text, without looking like it’s been marked up with tags or formatting
> instructions. While Markdown’s syntax has been influenced by several
> existing text-to-HTML filters — including Setext, atx, Textile,
> reStructuredText, Grutatext, and EtText — the single biggest source of
> inspiration for Markdown’s syntax is the format of plain text email.
> [from the Markdown
> “Philosophy”](http://daringfireball.net/projects/markdown/syntax#philosophy)

Markdown was born from the online writing practices around blogger John
Gruber (2004). In its very naming, Markdown thumbs it’s nose at the
generality and extensibility promised by HTML’s markup preferring
instead to focus on human read- and write-ability. With Markdown,
writers use indentation, blank lines, and bracket text with typewriter
symbols like asterisks, brackets and parentheses according to a set of
predefined rules to indicate structural elements in a text: paragraphs,
headers, and block quotations, as well to give emphasis to text, make
links, and place images. Where Markdown lacks a feature, either custom
extensions are added (such as the notation for a footnote) or else HTML
markup can be included and which then simply “passes through” the
Markdown conversion. The Markdown system is published under a [free
software](http://daringfireball.net/projects/markdown/license) license
so others are free to contribute and re-implement it’s functionality in
their own software, which has led to the format being included in a
large number of tools and platforms.

Markdown’s less-is-more approach privileges readability over the
extensible functionality of markup, and as a result favors writing in a
“clean” and inherently “rawer” stage of development. Ideally this allows
text writing to be focussed and maximally editable while leaving open a
range of possible options in terms of how the text can then be further
manipulated (laid out, combined, reformatted) or used by other people
with other tools. Despite its initial design for publishing HTML, it’s
minimalist approach produces text sources that are inherently “open to
interpretation” and thus suitable to a variety of uses. In a sense,
where markup provides its flexibility through an explicit layering of
tags, markdown “leaves space” for other uses by omission.

### Performing the text

During the discussion, we arrived at the useful metaphor of comparing
sheet music to a recording of its musical performance. While technically
possible to use audio analysis to convert an audio recording into sheet
music, the process is inherently prone to error. Any musical performance
in fact includes many more nuances (slight rhythmic variations,
differences of interpretation, the expressiveness of each performer not
to mention the details of the audio registration itself).

In this metaphor, the audio recording is like an HTML document, and
could equally be the WYSIWYG output of a word processor like Word, or a
PDF document. While technically possible to convert any of these formats
into markdown, the process is inherently likely to produce errors. Like
the recorded performance, a published representation is rich, loaded
with extra information particular to its context (page layout,
interactivity, the subtleties of typography and spacing). These
documents lack the simpler structure of a markdown source of the same
text (where such subtleties simply cannot be expressed). Like the sheet
music, the markdown requires the additional skills of the performer to
“bring it to life” in an actual performance. The skills of the designer
or web programmer are thus engaged to make form-specific adaptations or
interpretations of the “source” text to make a particular rendering.

### The limits of markdown & the needs for flexible notation

For all the benefits of markdown, there are some important factors to
consider as limitations. By enforcing a kind of “content vs
presentation” separation Markdown privileges traditional/academic
textual writing where the assumption is that visual presentation flows
unproblematically and deterministically from the text. Following the
metaphor of musical notation, many kinds of music, from improvisational
to serial music, would be ill-served when primarily written and
expressed in traditional musical staff notation. Particular modes of
expression demand particular forms of notation. One can imagine a
multitude of “domain specific” structured text or other forms of writing
to complement markdown in a publishing workflow.

The use of Markdown can also reinforce traditional professional
separations and hierarchies where writers write, then hand off to a
designer who “designs” the eventual presentation. The workflow is
unidirectional and sequential as editorial & design work can’t be done
in parallel or give feedback to the initiating writing process. It
remains an urgent and exciting area of work to consider workflows and
tools that allow for parallel and cyclic workflows where the textual and
the visual can fully interoperate without a return to the problematics
of “WYSIWYG”. A strict separation, while beneficial in other ways, also
potentially ignores emerging online practices of writing where the loop
of writing, designing, and publishing drives new forms of writing,
design, and publication.

### The importance of standards

Finally, it remains urgent to enforce/encourage the translation of best
practices into open standards through engagement with standards bodies
like the W3C. The addition, for example, of the audio and video tags to
HTML5 has helped stimulate an explosion of tools and applications for
publishing audio and video online. The addition of firmer standards for
marking up academic references & footnotes would provide a target for
which various structured text and other formatting tools could then aim
and facilitate the kinds of interoperability of tools that markup
standards have long promised.
