---
title: Converting a Docx directly to EPUB using Calibre
author: Silvio Lorusso
date: 2014-03-28
...

# Converting a Docx directly to EPUB using Calibre {.entry-title .single-title itemprop="headline"}

By [Silvio
Lorusso](http://networkcultures.org/digitalpublishing/author/silviolorusso/ "Posts by Silvio Lorusso"),
March 28, 2014 at 4:53 pm.

Recently the software Calibre added Docx to its converter as a possible
input format. Thus it’s allowed to convert directly from Docx to Epub.
The procedure is quite simple. We’ll use the[test Docx
document](http://calibre-ebook.com/downloads/demos/demo.docx) provided
by the Calibre team.

![](imgs/WO27sNlmw2vvZPxxx8Kgu_4tBsBu6hw7hi760my0Oky50IAOo8OwxbUpp7jhf77rc5U5NxhPe4sBqqhdjHYMX2LCOm1xxvUVnZUuH3EECIlbJkO-IU8VKSs4JWDCew)

Add the docx file by drag-and-dropping it into calibre. In this way
it’ll be added to your library.

Click on Convert Books in the top
bar.![](imgs/naBmT80H2RBHdTTl7hITimGg6-U_go616rWAxH_5EKiacM4ljD3r7dC63RitpYjRTggs8_Ych7fDOvYLQQJHF7qYOHxFnhtXM9iG5Io1K85OxbJHdfQFcqxN3qIOIQ)

Select “DOCX” as input format and “EPUB” as output, add metadata and
click OK.

![](imgs/MHE6obYW4_0zKncQKDUzeSlTDfrrGeNyBmJpkp2hRROy1roWQRz8zc1htIZqKpzLUqmm0MQwtCQ7ubPuOMPdNmoIWQf-ihDLCugefc-AzymvTH1ljFdNi0t4KpcgVA)

You should now be able to see EPUB on the right. Click on it to open the
epub with the Calibre viewer, right click on it to see the option to
save the file to your disk.

Now let’s have a look to the output
Epub.![](imgs/d8qMJp8dqkv37b3yd-hBN5EtNUOEHZpeQN5HRpD2Y-D6X3vOysWmaTsTSTtyd7c0GOPxFUSZRdbK7fziFUGOKHyfjBN5M1y0-jmZGfo9C8CdJ5Y07IrrQbX571KkqA)

Calibre added a default cover (with generated author and title) because
we didn’t specified any.

![](imgs/rr9W7BlgZAEscQL76OKFFnJyTiz7GStpU-oKjAS95lUaPig6fEFjMYl7gsOiwQGFpCdc4MbnJC-rShxt0K-CAXy7_mgjSDhca4sz2Y1GT4-XesWnNbdJAqPlPeROMQ)

Besides some minor glitches, all the features of the Docx document are
preserved.

Let’s have a look now into the Epub. To do so we need to unzip it. We
can either change the extension to “.zip” or use the[Epub
UnZip](http://www.mobileread.com/forums/showthread.php?t=55681&page=2)
tool.

The nice thing is that the conversion keeps (or create) a table of
contents, splitting the document in several HTML files. From the
document itself:

> There are two approaches that calibre takes when generating a Table of
> Contents. The first is if the Word document has a Table of Contents
> itself. Provided that the Table of Contents uses hyperlinks, calibre
> will automatically use it […] If no Table of Contents is found in the
> document, then a table of contents is automatically generated from the
> headings in the document. A heading is identified as something that
> has the Heading 1 or Heading 2, etc. style applied to it. These
> headings are turned into a Table of Contents with Heading 1 being the
> topmost level, Heading 2 the second level and so on.

![](imgs/S2TIqcR7eBirL26bcW2SwzhnUJ3ewKyKIF6aqSP8EFzPHdkm804viATqHDm7vvkaKj88VEU6PWRyGWt39SjKvg2QSBodMxPqJ1ZWGwO3rW_Xk53owv5WJ1M4sqBJ2w)

This means that by merging several Docx in a single one, it is possible
to obtain an Epub containing multiple chapters, therefore an entire
book.

![](imgs/6aHG-UWIlwHNlXEhIda4IGkXW7xUfXrKjU5PHklmzXfagbT3usquVm7m2k6fJ6uTwEu5q4cgsa7OsIKovuH0GkmAAmnX8PJQQvAakzokORnR_P6X7k3bh2K1S6OXVg)

The Epub obtained passes validation and it wouldn’t be too intensive to
clean its code, especially if not many styles are expressed.

![](imgs/rbOTbqoWmaf0_YyWqcoCGkj3FmY_tgsz2jTXGlMHAtiLhf9udP26uGeGW3_w4Y8ZT_d5rairVgWA2gujRER0_G3hRfbUJxSbfLoaxLY6dE1g10wTqOwGyFEIuYuBow)Metadata
should be added or modified in the content.opf file.
