---
title: Making the VolkskrantBuilding.epub
author: Andre Castro
date: 2014-11-23
...

# Making the VolkskrantBuilding.epub {.entry-title .single-title itemprop="headline"}

By [Andre
Castro](http://networkcultures.org/digitalpublishing/author/andre/ "Posts by Andre Castro"),
November 23, 2014 at 3:02 pm.

![caption](imgs/stream1.jpg)

![caption](imgs/cook_TVB_sml.jpg)

![caption](imgs/trailer-TheVolkskrantBuilding.gif)

Last week [The Institute of Network
Cultures](http://networkcultures.org/) and [Amsterdam Creative
Industries Network](http://amsterdamcreativeindustries.com/) launched
the publication [The Volkskrant Building: Manufacturing Difference in
Amsterdam’s Creative
City](http://networkcultures.org/blog/publication/the-volkskrant-building-manufacturing-difference-in-amsterdams-creative-city-boukje-cnossen-and-sebastian-olma/)
(TVB) by Boukje Cnossen and Sebastian Olma. I use this post to share the
process that led to the production of its EPUB edition.

From the onset it was clear that TVB had to go from manuscript to its
two output format – EPUB and paper – in little more than one week. We
were starting from good position: the manuscript, a .docx file, was in
its final form and had been carefully edited, with all of its text
formatting accomplished through styles, as described by Miriam Rasch in
the [Style Guide for Hybrid Publishing
blog-post](http://networkcultures.org/digitalpublishing/2014/10/21/style-guide-for-hybrid-publishing/).
This consistency of the manuscript allows for the necessary format
conversions to be performed with ease and little obstructions. Despite
this advantage, the short time span available for the production of TVB
remained a challenge. While [UNDOG](http://www.undog.nl/) design studio
worked on the identity of the book, I developed the EPUB. This meant I
had to follow the studio’s lead, wait for its work to be completed, and
only then could I apply the same identity to the EPUB edition. The
adoption of such dynamic, in hybrid workflows, is highly questionable,
given its inefficiency and imposition of top-down dynamic instead of a
more collaborative and egalitarian approach between all of those
involved in the production of a book, but that is in itself subject for
another blog post.

In my usual method for creating EPUBs I use:

-   [Markdown](http://daringfireball.net/projects/markdown/syntax)
    source-files: a plain-text markup language, used to do most of the
    work on the book’s text; It can perhaps be best described as a
    preparatory document for the generation of the EPUB, where all
    content, text-formatting and structure of the EPUB are already
    present, under a simpler form.
-   [Pandoc](http://johnmacfarlane.net/pandoc/): the conversion
    software, that translates between different markup languages. In
    this case I used Pandoc to convert the manuscript from .docx to
    Markdown and from Markdown to EPUB3;
-   [Git](http://git-scm.com/): the versioning system which tracks the
    history of changes the sources files undergo during the production
    of the EPUB.

For the production of the TVB ebook, in addition to these tools I chose
to use a Makefile, in a similar way as described by Michael Murtaugh in
the [Make Book blog
post](http://networkcultures.org/digitalpublishing/2014/10/01/make-book/).
The Makefile became center of operations that compiled all the source
files and addressed them to Pandoc, to be converted into an EPUB.

The Makefile used in the production of TVB EPUB:

    VolkskrantBuilding.epub: 
        cd docs && pandoc \
        --from markdown \
        --to epub3 \
        --self-contained \
        --epub-chapter-level=1 \
        --toc-depth=2 \
        --epub-cover-image=media/cover.png \
        --epub-metadata=metadata.xml \
        --epub-stylesheet=styles.epub.css \
        --epub-embed-font=VAGRoundedStd-Black.otf \
        --epub-embed-font=VAGRoundedStd-Bold.otf \
        --epub-embed-font=VAGRoundedStd-Light.otf \
        --epub-embed-font=VAGRoundedStd-Thin.otf \
        --default-image-extension png \
        -o VolkskrantBuilding.epub \
        VK.md

This approach centered on a Makefile allowed me to narrow my focus to
the source files and the Makefile. As a result it sped-up and simplified
the development process. The source files – the Markdown text files,
images, metadata, CSS styles – became the ingredients necessary to cook
this EPUB dish and the recipe, where the Makefile was the
recipe.`make VolkskrantBuilding.epub`. Once the `make` command was
executed I’d evaluate the result. If I happened to dislike the dish I
just created, I would very simply adjust the ingredients or the recipe.
I iterates through this circle, fine-tuning ingredients and recipe,
cooking, and tasting, until I got to a satisfactory EPUB.

The described approach contrasts with my default method for producing
EPUBs. Usually I create a rough EPUB with Pandoc, unzip it and start
working on its constituent files – editing the metadata inside
content.opf, the stylesheet, or the content .xhtml files. When all
editing is done I zip the files back into an EPUB and look at the
result. I repeat the whole process few more times until I am happy with
the outcome. If I carry on with the culinary analogies I’d say that this
approach would be like cooking an already cooked dish. The EPUB is in
front of me, and what I do is separate its different parts, change them
individually, and then put them back together in a slightly different
dish. Although it works, this approach is somehow unfocused, slow, and
forces me to work with HTML files. Although HTML is a powerful, and yet
simple markup language, its unrendered source is unpleasant to either
read or edit. Edit large sections of text wrapped by countless HTML tags
instinctively feels like a recipe for disaster.

With the Makefile approach I am spared from working with HTML. Instead I
deal mostly with Markdown source files, which contrarily to HTML are
easy to read and edit and can be quickly compiled into an EPUB. The
feedback loop between a change and its effect on the EPUB become much
shorter and direct. Even in cases of more expressive sections, which
fall outside the scope of Markdown, such as the red quotations blocks
that permeate TVB, can be handled within Markdown, by adding HTML
snippets, which will easily do the job.

The big downside of this approach is that it leaves one at the mercy of
the conversion software used. Although Pandoc is an incredibly powerful
piece of software, it is not perfect, as I am afraid no piece of
software is. Pandoc conversions, are sometimes, specially in very small
details, not exactly what one wishes. An example of this is the way
Pandoc handles footnote references in EPUB3 conversions. The conversion
presents superscript footnote reference numbers by wrapping the numbers
in HTML superscript tags ``, as in:

    squatters movement.2` tags are a simple means to
format text as superscript. Yet it goes against the [accessibility
guidelines](http://www.idpf.org/accessibility/guidelines/content/xhtml/notes.php)
from the International Digital Publishing Forum, which state “Do not use
the sup element to superscript note references, as it is redundant
presentational tagging. The CSS vertical-align property can be set to
superscript the a elements.” Furthermore, they compromise the
responsiveness of footnote references in the iPad’s iBooks reader. All
in all, it is understandable that such issue arises. EPUB3 specs are
still in development and Pandoc is an open-source project of small
dimensions, which probably has more pressing issues to tackle than to
make footnotes respond well on the iPad. Yet, one can do something about
it. The most obvious fix is to remove all the sup tags from the EPUB
once it is created (via a script). The other solutions are directly
related to the fact that Pandoc is Free/Open-Source software, licensed
under the [GNU General Public License version
2](http://www.gnu.org/licenses/gpl-2.0.html). The license clearly states
that “You may modify your copy or copies of the Program or any portion
of it”, which means that anyone has the permission to modify Pandoc
source-code, and alter the way footnote references are encoded in EPUB3
conversions. Other possibility is to visit the [central
repository](http://github.com/jgm/pandoc) where the development of
Pandoc takes place and address this problem by [opening an
issue](http://github.com/jgm/pandoc/issues), which will be read
considered by Pandoc’s developers.

In a nutshell Makefiles are useful and simple ways to optimize the
development of an EPUB into recipes that can simplify the development of
an EPUB and make the most out of the combination of small, simple and
yet powerful pieces of software. However this approach isn’t perfect. It
isn’t a one-size-fits-all recipe that can be applied to the production
each and every EPUB, as it produces default behaviors and nearly
invisible artifacts that in some contexts can become disruptive.
Consequently the employment of other approaches and experimentation
remains essential to the innovation and diversification of ebooks.
