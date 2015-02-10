---
title: Epub Trailer Generator – “Free Library for Every Soul” Hackaton – First Report
author: Silvio Lorusso
date: 2013-11-11
...

# Epub Trailer Generator – “Free Library for Every Soul” Hackaton – First Report {.entry-title .single-title itemprop="headline"}

By [Silvio
Lorusso](http://networkcultures.org/digitalpublishing/author/silviolorusso/ "Posts by Silvio Lorusso"),
November 11, 2013 at 1:02 pm.



![Unlike Us Reader Epub Trailer](imgs/trailer-Unlike-Us-Reader.gif)

![](imgs/dpt2013.jpg)

On the 2nd and 3rd of November, the INC subgroup ([Silvio
Lorusso](https://www.facebook.com/postdigitalpublishingarchive?fref=ts),
[Michael Murtaugh](http://automatist.org/kiss/), Kimmy Spreeuwenberg,
Margreet Riphagen) attended the hackathon [Free Libraries for Every
Soul](http://monnik.org/Free-Libraries-for-Every-Soul/solo), in Utrecht,
which was part of the Impakt festival. Here’s the description of the
project proposed by us:

> Situated in the “Digital Publishing Toolkit” project the subgroup
> ‘Book as Directory’ concerns itself with workflows for digital
> publications that move beyond putting a print PDF online. We want to
> explore the creative tension between the strict constraints and
> particularities of epub as an output format and the diversity of
> possible tools and practices that can be employed to produce them.
> Starting from specific materials from the Institute of Network
> Cultures (INC) including publications (in both word processor and page
> layout formats), web blogs, and video event recordings, we will be
> using the diversity of the participants knowledge and work practices
> to produce as many different workflows (and their resulting outcomes)
> as possible. In doing so, we will make use of a diverse toolbox of
> free software tools taken from different practices (graphic design,
> informatics, linguistics, text editing, blogging, library sciences,
> statistics, reverse engineering). The final outcome will be compiled
> into an epub cookbook demonstrating a tasty palette of possible
> digital publishing workflows.



Starting from the main goal of diversifying the array of digital
publishing workflows for epub, we worked on several concepts that
explored both the production of a publication in a digital format and
the management and manipulation of ready made e-books.

This post represents the first report on the concept developed during
the hackathon. More will follow!

(For a comprehensive overview on each project developed during the
hackaton, check [André Castro’s
report](http://pinknoi.so/post/5).)

## Epub Trailer Generator

During the hackaton we discussed the possible outputs that could derive
from well-structured content. Thinking beforehand of those outputs would
influence the structuring of the content.

In our discussion we didn’t limit the outputs and the sources to what is
generally considered a publication: we considered as well Flickr
streams, contact spreadsheets, etc.

We also realize that open format like Epub could be easily accessed and
harvested for content, in other ways than the mere linear reading. So we
started to think of ePub as an input/source that could be manipulated by
scripts.

In order to take the idea of Epub as input to the extreme, we needed a
very different output from an e-book. Therefore we chose the “book
trailer” relatively new genre, different from a theory publication both
as format and as attitude.

We developed a small [python
script](https://github.com/DigitalPublishingToolkit/Epub-Trailer/blob/master/epubtrailer.py)
that: 1. unzips the epub; 2. searches the metadata for informations such
as: title, authors, publisher, publication date; 3. gathers all the
pictures in the book; 4. get a font if it’s embedded in the ePub; 5.
creates an animated gif out of those contents.

The scripts employs the [PIL
library](http://www.pythonware.com/products/pil/) to handle the images
(resizing, creating text, etc.) and
[images2gif](https://pypi.python.org/pypi/images2gif) to convert all the
images to an animated gif.

**Usage**

    python epubtrailer.py file-name.epub

Here’s a couple of examples.



![“A Neoist Research Project ” Epub
Trailer](imgs/trailer-A-Neoist-Research-Project.gif)


![“To Save Everything, Click Here” Epub
Trailer](imgs/trailer-B00B3M3X2G-EBOK.gif)


