---
title: On the publication of Think Like a Lawyer, Don’t Act Like One
author: sauli
date: 2013-10-16
...

# On the publication of Think Like a Lawyer, Don’t Act Like One {.entry-title .single-title itemprop="headline"}

By [sauli](http://networkcultures.org/digitalpublishing/author/sauli-2/ "Posts by sauli"),
October 16, 2013 at 11:19 am.

Our subgroup, consisting of BIS publishers, Essense, and Sauli
Warmenhoven set out to create a ePub version of the BIS publication of
*Think Like a Lawyer, Don’t Act Like One*. This publication has a
relatively straightforward layout, with its 75 lessons generally being
displayed in similar fashion, namely the text of a lesson on one page,
and on the facing page a full-bleed image.

![page from Think Like a Lawyer, Don't Act Like
One](imgs/2013-10-16-11.15.23.png) ![page from Think Like a Lawyer,
Don't Act Like One](imgs/2013-10-16-11.15.29.png)

We felt that this publication was an excellent opportunity to try our
hand at a fixed layout epub. Though fixed layout support is in its
infancy, as there is no common support for it, fixed layouts are
possible on modern tablets, such as the iPad and recent kindles, we
thought it would be worthwile to be ambitious in this regard. In the end
the choice was made to create a second version with a simpler layout, to
facilitate the reading of the publication on older devices.

In order to generate the 160 or so pages of the publication, we
developed a simple tool that acted as a CMS of sorts. The tool allows
for the creation of page spreads, and the entering of associated texts
and background-images. When all content is entered, an epub is generated
on the basis of predetermined templates. This generated file then has to
be checked for errors, and was in this case disassembled so that the
page spreads that do not follow standard layout could be done by hand.
All in all even with the use of the tool it still turned out to be a
significant workload, that could, in the future, only in part be
lightened by a more efficient workflow.

[link to the code on
github](https://github.com/DigitalPublishingToolkit/epub_generator)
