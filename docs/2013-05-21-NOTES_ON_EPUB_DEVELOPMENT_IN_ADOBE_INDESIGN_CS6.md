---
title: NOTES ON EPUB DEVELOPMENT IN ADOBE INDESIGN CS6
author: Silvio Lorusso
date: 2013-05-21
...

# Notes on EPUB Development in Adobe inDesign CS6 {.entry-title .single-title itemprop="headline"}

By [Silvio
Lorusso](http://networkcultures.org/digitalpublishing/author/silviolorusso/ "Posts by Silvio Lorusso"),
May 21, 2013 at 9:16 am.



Version: 0.1 – May 11th, 2013



### Abstract

These notes focus on the ways an InDesign CS6 file should be arranged in
order to be appropriately exported as ePub. Further insights are
provided in order to improve quality of the exported ePub in terms of
file size, metadata, layout.

### Required Knowledge

-   Adobe InDesign CS6
-   Basic HTML and CSS



## [1: Premises

### [1.1: Legend

-   Software Command
-   Shortcut
-   Code Snippet

### [1.2: Wait, weren’t we supposed to use open source tools?

We all love opes source, but in some cases a pragmatic approach it’s
needed: a perspective that takes into account the actual workflow
without denying it beforehand. Not every designer would be happy to give
up the softwares used for the last five years for the sake of open
source.

Developing an EPUB through InDesign could be considered a transitional
process, in doing so the designer will anyway acquire a know-how that
could be invested in open source tools and procedures.

### [1.3: So you’re saying that obtaining EPUB from Indesign is not necessarily the best practice…

Exactly, it really depends on the context. This procedure could be
useful whether:

-   you, or your collaborators, don’t have any HTML or CSS knowledge
    (but in this case you won’t be able to go through the whole tutorial
    and this will heavily impact the quality of your final ePub, check
    [1.4](#1-4));
-   you have an articulated publication already set as an InDesign file;
-   you want to convert your backlist to ePub and the books are archived
    as InDesign packages.

### [1.4: Is Indesign enough to develop a high quality ePub?](#toc-1-4) {#1-4}

No, it’s not enough. There are strong limitations for ePub development
within InDesign, this is because its primary function is to set files
for print.

Therefore if you want a high quality ePub you need to tweak the code
produced by the software, in order to do so you will need HTML and CSS
skills.

### [1.5: May I use the same structure of the InDesign file for both print and ePub?](#toc-1-5) {#1-5}

Rarely the InDesign file ready for print will work fine to be exported
“as is” to ePub. But in case you want to produce an ePub version of the
printed ducument, setting the file as follows will save you a lot of
work. In this sense this tutorial proposes an ePub-first approach.

### [1.6: Resources](#toc-1-6) {#1-6}

-   “InDesign CS6 to EPUB, Kindle, and iPad” course by Anne-Marie
    Concepcion on
    [Lynda.com](http://www.lynda.com/EPUB-tutorials/InDesign-CS6-EPUB-Kindle-iPad/98834-2.html);
-   [*La pratica
    dell’ePub*](http://www.apogeonline.com/libri/9788850314126/scheda)
    (*The ePub Practice*) by Ivan Rachieli, 2011;
-   [Open Packaging Format (OPF) 2.0.1 v1.0.1 Recommended
    Specification](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm).

### [1.7: Softwares](#toc-1-7) {#1-7}

-   [Adobe InDesign
    CS6](https://creative.adobe.com/apps?trial=IDSN&promoid=JZXRC)
-   [EpubCheck](https://code.google.com/p/epubcheck/)
-   [EPUB zip/unzip
    apps](http://www.mobileread.com/forums/showpost.php?p=1181614&postcount=18)
-   [Calibre](http://calibre-ebook.com/)
-   [Adobe Digital
    Editions](http://www.adobe.com/it/products/digital-editions.html)

### [1.8: Attachments](#toc-1-8) {#1-8}

-   [InDesign package with example
    content](http://networkcultures.org/digitalpublishing/wp-content/uploads/sites/26/2013/05/package.zip)
-   [CSS file to be included when exporting the ePub via
    InDesign](http://networkcultures.org/digitalpublishing/wp-content/uploads/sites/26/2013/05/unlike-us-reader.css),
    check [9.4](#9-4)
-   [ePub
    example](http://networkcultures.org/digitalpublishing/wp-content/uploads/sites/26/2014/10/unlike-us-reader.epub)

## [2: General](#toc-2) {#2}

### [2.1: No Local Overrides!](#toc-2-1) {#2-1}

This simply means that you should set everything in your document either
as a Paragraph Style or a Charachter Style. When you have set one of those and
change a setting locally a plus sign (+) appears next to the name of the
syle. You should avoid this because it would heavily affect the
cleanness of the ePub code.

[More
info](http://help.adobe.com/en_US/indesign/cs/using/WS9D351498-DAAC-4be1-B4B8-2B6C72FF6CEDa.html)



![](imgs/1.png)
The Paragraph Styles panel



### 2.2: Use Master Pages

Keep all the repeating elements such as title, page number, article
title in Master pages. In this way they won’t be
rendered in the ePub.

[More
info](http://help.adobe.com/en_US/indesign/cs/using/WSa285fff53dea4f8617383751001ea8cb3f-7105a.html)



![](imgs/2.png)
Example of master page



### [2.3: Paragraph Means Paragraph](#toc-2-3) {#2-3}

Don’t use paragraph breaks to space elements, use instead the bounding
box itself.



![](imgs/3.png)
Wrong use of paragraphs





![](imgs/4.png)
Correct use of paragraphs



### [2.4: Paragraph Really Means Paragraph](#toc-2-4) {#2-4}

Use the Space After feature in the Paragraph Style instead of a double paragraph break,
except in the case of colophon and exceptional layouts.



![](imgs/5.png)
Paragraphs spaced via Space After



### [2.5: Paragraph = Paragraph](#toc-2-5) {#2-5}

Use soft returns (Shift+Return) instead of
paragraph breaks (Return) when you work on the
visual appearance of text. A paragraph break could cause problems in a
reflowable context, while the soft returns could be automatically
stripped out when exporting.

[More
info](http://help.adobe.com/en_US/indesign/cs/using/WSa285fff53dea4f8617383751001ea8cb3f-6f77a.html)



![](imgs/6.png)
Soft returns used to break the title for visual purposes.



### [2.6: ALL CAPS hide Actual Caps](#toc-2-6) {#2-6}

Even if you have an ALL CAPS setting remember to use Capitals when you
write the text: it may happen that in the ePub version the setting is
ignored, the result would be for instance a lowercase title.

### [2.7: Letters Aren’t Meant to be Stretched](#toc-2-7) {#2-7}

Do not use Vertical Scale to adjust the
paragraphs (for instance when you have a single word going to the next
line), use instead the Justification settings in
the Paragraph Style.



![](imgs/7.png)
Vertical Scale setting





![](imgs/8.png)
Justification settings in the Paragraph Style



### [2.8: Fonts](#toc-2-8) {#2-8}

Embed a font only if you consider it necessary. On some devices only the
headings’ fonts will be preserved. Also, only the fonts licensed for
“e-use will” be actually embedded by InDesign, therefore if you want to
embed a font make sure you own the license. An
[OpenType](http://en.wikipedia.org/wiki/OpenType) font is preferrable.

In order to embed fonts just check Include Embeddable
Fonts from the EPUB Export Options (Cmd+E).



![](imgs/9.png)
Include Embeddable Fonts checked in the EPUB Export Options



### [2.9: Export Early, Export Often](#toc-2-9) {#2-9}

You can find the export option from File \>
Export (or Cmd+E). Of course you need to
choose EPUB as the resulting format. A detail explanation of all the
options available can be found at [9.1](#9-1).

### [2.10: How do I open an EPUB file?](#toc-2-10) {#2-10}

There are several softwares and online applications available. Among the
most used there are [Calibre](http://calibre-ebook.com/) and [Adobe
Digital
Editions](http://www.adobe.com/it/products/digital-editions.html).

## [3: Cover and Images](#toc-3) {#3}

### [3.1: Formats and Resolution](#toc-3-1) {#3-1}

As we will see afterwards (see [9.3](#9-3)), from InDesign is it
possible to export images in 3 formats:

-   JPEG
-   GIF
-   PNG

JPEG could be used in any case, except for images with transparent
background (such as logos). In this case PNG is preferable.

150ppi is generally considered to be a good compromise in terms of
resolution and file size. File size is important cause it directly
affects loading time on limited computing capacity such as mobiles and
e-readers.

### [3.2: Colour Over Greyscale](#toc-3-2) {#3-2}

Consider that your book could be seen on a E Ink device as well as on a
tablet, therefore it makes sense to include your images in colours. On
an e-reader they will automatically set as greyscale.

### [3.3: Two Covers?](#toc-3-3) {#3-3}

In InDesign there are 2 choices for including the cover in the EPUB Export Options(Cmd+E):

1.  Include the cover of your book in the InDesign file as the first
    page. Consider that in this way, it will be exported as both as
    cover and first page of the book.
2.  Choose an image from your computer.



![](imgs/10.png)
Cover settings in the EPUB
Export Options



### [3.4: Optimal Cover Size](#toc-3-4) {#3-4}

There is no clear answer, but it is suggested to keep the size less than
1000px in width and height.

[More
info](http://blog.threepress.org/2009/11/20/best-practices-in-epub-cover-images/)

### [3.5: Groups for Complex Layout](#toc-3-5) {#3-5}

Group elements and rasterize if you want to preserve complex text
layouts. Consider that this will be rendered as image, so it’s better to
have a text version of the same content as well.

1.  Select and group elements (Cmd+G);
2.  While selected go to Object \> Object Export
    Options;
3.  Click on EPUB and HTML, then check Custom Rasterization;
4.  Choose PNG if you want a transparent background;
5.  If you want to have it as a fullpage image check Insert Page Break and select Before and After Image;
6.  Add a description of the picture as an Alt
    Text, in this way if the image is not shown people will still
    be able to know what it is about.



![](imgs/11.png)
Group for complex text layout





![](imgs/12.png)
Group for images that are connected





![](imgs/13.png)
Object Export Options, , Custom
Rasterization checked



### [3.6: Images as Part of the Text](#toc-3-6) {#3-6}

Images need to be inserted in the flow of text in order to be shown at
the right place. Otherwise they will be shown after the whole text.
There are 2 ways to insert the images:

1.  Click on the small blue square on the top right and drag it to the
    point the picture belong in the text;
2.  Cut the image and paste it while you’re inside the textbox, do the
    same with the caption.

With the first method there are some known problems: both the picture
and the caption will be included in a bounding box (\). In order to fix this you will need to work
on the HTML and CSS.



![](imgs/14.png)
First method: image linked to the text



### [3.7: Manage the Layout of the Image](#toc-3-7) {#3-7}

Go to Object \> Object Export Options to manage
the layout of the image.

[More
info](http://help.adobe.com/en_US/indesign/cs/using/WSa285fff53dea4f8617383751001ea8cb3f-6f2fa.html#WS8c5bc4f64c7a4a3d-7cbbfcee12dbd4ad69f-8000)

### [3.8: Alt Text for Every Picture](#toc-3-8) {#3-8}

As said in [3.6](#3-6), it’s important to have an Alt Text for every
image included in the document.



![](imgs/15.png)
Alt Text box in Object Export
Options.



## [4: Organizing the File for ePub Export](#toc-4) {#4}

### [4.1: The Articles Panel](#toc-4-1) {#4-1}

Use the Articles Panel (Window \> Articles) to
manage the contents and the order of your publication. Add content to
your articles by drag and drop content into it. When export to ePub
(Cmd+E) set Content
Order as Same as Articles Panel to make
your changes effective.

When you add a text box to an article, the whole text will be rendered
in the ePub even if it’s oversetting in the InDesign document.

[More
info](http://help.adobe.com/en_US/indesign/cs/using/WS8c5bc4f64c7a4a3d78b7a8b312dbccaf5b2-8000.html)



![](imgs/16.png)
Window \> Articles.





![](imgs/17.png)
The Articles Panel.





![](imgs/18.png)
Same as Articles Panel as Content Order in the EPUB Export
Options.



### [4.2: No Tags, Text Repetitions, Etc.](#toc-4-2) {#4-2}

Don’t include in neither in the Articles panel
nor in the flow of text unnecessary elements such as tags or repeated
text.



![](imgs/19.png)
A list of tags, not to be included in the articles.



### [4.3: Split the Document](#toc-4-3) {#4-3}

Splitting the document (in different XHTML files) is important because
having a too big document would mean a quite big load for a device in
order to quickly navigate it, for instance when one wants to check a
footnote and then go back to the text.

In order to split the document, check the Split
Document option in the Export Tagging
options for each paragraph style you want to break the document, such as
the title of the TOC (Table of Contents), or the titles of articles.

Then you will need to select Split Document based on Based on Paragraph Style Export Tags from the Export(Cmd+E) panel.



![](imgs/20.png)
Split Document checked in the Paragraph Style Options





![](imgs/21.png)
Split Document based on Based
on Paragraph Style Export Tags from the Export(Cmd+E) panel.



## [5: General TOC and Inner TOC](#toc-5) {#5}

### [5.1: The General TOC](#toc-5-1) {#5-1}

Any ePub document has a general TOC (Table of Contents) that isn’t
included in the actual pages of the document. Even if you don’t do
anything, it will be automatically created and it will include a single
voice which is the whole document.

### [5.2: Modify the General TOC](#toc-5-2) {#5-2}

In order to create a general TOC for the ePub go to Layout \> Table of Content:

1.  Include the paragraph style that you want to use as title of the TOC
    element;
2.  You can add other styles to create a hierarchic TOC;
3.  Save the style;
4.  When you export the ePub choose the style you created as TOC Style.

[More
Info](http://help.adobe.com/en_US/indesign/cs/using/WS49FB9AF6-38AB-42fb-B056-8DACE18DDF63a.html)



![](imgs/22.png)
TOC based on article-title as Paragraph Style.





![](imgs/23.png)
TOC Style selection in the EPUB
Export Options.



### [5.3: The Inner TOC](#toc-5-3) {#5-3}

Even if it’s not mandatory, it could be useful for readers to have an
inner TOC, it could be different from the general one: other contents
could be added and in a more articulate way.

If there is already one, the TOC prepared for the printed version can be
preserved. In this case it’s needed to add an internal hyperlink for
each voice (see [7.2](#7-2)).

### [5.4: No Page Numbers!](#toc-5-4) {#5-4}

Remember not to include any reference to page numbers in the Inner TOC.
You could for instance not include them in the Articles panel (check [4.1](#4-1)).

## [6: Lists and Tables](6) {#6}

### [6.1: Lists](#toc-6-1) {#6-1}

For each list create a paragraph style from Window \>
Styles \> Paragraph Styles. The options specifically referred to
lists are the one under Bullets and Numberings.

[More
info](http://help.adobe.com/en_US/indesign/cs/using/WSa285fff53dea4f8617383751001ea8cb3f-6da6a.html)



![](imgs/24.png)
Bullets and Numberings panel in the Paragraph Style Options



### [6.2: Tables](#toc-6-2) {#6-2}

For each table create a table style from Window \>
Styles \> Table Styles. If you have a table with a complex layout
is better to rasterize it (see [3.6](#3-6)).

[More
info](http://help.adobe.com/en_US/indesign/cs/using/WSa285fff53dea4f8617383751001ea8cb3f-6ff5a.html)



![](imgs/25.png)



## [7: External and Internal Hyperlinks](#toc-7) {#7}

### [7.1: External Hyperlinks](#toc-7-1) {#7-1}

Add external hyperlinks via Windows \> Interactive \>
Hyperlinks. You can search them looking for “www”, “http”, etc.
You can also attribute a specific Character
Style to links.

The task can be done automatically using the option Convert URLs to Hyperlinks findable clicking on the
right top triangle. Usually this method doesn’t work perfectly because
the ”http://” is not automatically added.



![](imgs/26.png)
Hyperlinks panel



### [7.2: Internal Hyperlinks](#toc-7-2) {#7-2}

Add internal hyperlinks to the inner TOC and to the whole document via
Windows \> Interactive \> Hyperlinks. In oder to
do so you need to select the text you want your link to go to and select
New Hyperlink Destination. Give it a name and
save it.

After that you need to go to the text that links to the previous text
and to Create a New Hyperlink. It should link to
Text Anchor, in particular the one you just
created.



![](imgs/27.png)
Adding a New Hyperlink Destination





![](imgs/28.png)
Linking to Text Anchor



## [8: Cleaning the file and Adding Main Metadata](#toc-8) {#8}

### [8.1: No Unused Styles](#toc-8-1) {#8-1}

Delete all the unused styles. You can look for them via Edit \> Find/Change. There you need to look for a
specific style from Find Format.

[More
info](http://help.adobe.com/en_US/indesign/cs/using/WSFB3603CC-8D84-48d8-9F77-F3E0644CB0B6a.html)



![](imgs/29.png)
Find/Change panel



### [8.2: No Local Overrides](#toc-8-2) {#8-2}

As said before (see [2.1](#2-1)) it’s preferable not to have local
overrides, in order to keep the ePub clean. Find and remove any local
overrides, indicated by the plus sign(+) next to the style. You can use
the [Show Text Overrides
plugin](http://in-tools.com/article/scripts-blog/showing-text-formatting-overrides/)
to highlight them.

### [8.3: No Spaces in Filenames](#toc-8-3) {#8-3}

Make sure that all linked files (and the InDesign file itself) don’t
have spaces nor special characters in their names.

### [8.4: No Useless nor Print-oriented Characters](#toc-8-4) {#8-4}

Make sure there are no double spaces and all the typical formatting
errors. Check misspells and useless characters (this should be already
done for the printed version).

### [8.5: No References to the Printed Edition](#toc-8-5) {#8-5}

Make sure there are no references to the printed edition such as
“printed in…”, etc. Also make sure there are no references to inner
pages (such as “p. 23”), in notes as well. Lastly, make sure that there
are no repetitions of the the title in pages such as frontispiece, etc.

### [8.6: Add links and e-version specific elements to colophon.](#toc-8-6) {#8-6}

You’ll probably mention the publishing house, so add a link to its
website. Remember to use an ISBN specific for the ePub. Remember also to
add the rights for your publication.



![](imgs/30.png)
Creative Commons as the rights in the text of the publication



### [8.7: InDesign Errors and Layout Problems](#toc-8-7) {#8-7}

InDesign automatically detect errors in the document (such as missing
fonts). You can find the alert on the bottom left of the software’s
window. Make sure there are no problems with pictures and with the
layout in general (missing fonts, broken paragraphs, etc).

[More
info](http://help.adobe.com/en_US/indesign/cs/using/WSa285fff53dea4f8617383751001ea8cb3f-7060a.html)



![](imgs/31.png)
The Preflight panel showing there are no errors



### [8.8: Check Both Internal and External Hyperlinks](#toc-8-8) {#8-8}

As above. Make sure that internal links are bidirectional. If you added
them automatically, consider that you’ll probably get external links
where you don’t want them.

### [8.9: Assign HTML Tags](#toc-8-9) {#8-9}

By default InDesign will export each paragraph style as a \ (paragraph in HTML) and characters as \. HTML allows to tag elements in a more
specific way, hierarchically defining headlines for instance (\<h1\>, \<h2\>, etc.).

You can set what tag you want to use and what class from the Export Tagging panel from Paragraph
Style Options. It is also useful to merge style that are similar
under a single class.

Remember to do so for bold (\),
italic (\) and superscript (\).



![](imgs/32.png)
Export Tagging options in Paragraph Style Options



### [8.10: Metadata](#toc-8-10) {#8-10}

Add the basic metadata (data about other data) from File \> File Info, other ones will be implemented
directly in the ePub code (see [10.4.1](#10-4-1)).

-   Title;
-   Author(s);
-   Description;
-   Keywords;
-   Rights.



![](imgs/33.png)
File Info options.



## [9: Export](#toc-9) {#9}

### [9.1: Export Options](#toc-9-1) {#9-1}

You can export from File \> Export (Cmd+E).

[More
info](http://helpx.adobe.com/indesign/using/export-content-epub-cs6.html)

### [9.2: General Panel](#toc-9-2) {#9-2}

1.  Even though the official current version for EPUB is 3.0, the *de
    facto* is 2.0.1 as it’s widely supported.
2.  As said before (see [2.4](#2-4)) there are two possibilities for the
    cover.
3.  Choose the style you created before (see [5.2](#5-2)) as TOC Style.
4.  You can add margins to your page even though most e-readers will
    overwrite this setting.
5.  Choose Same as Articles Panel as Content Order.
6.  The default for footnotes is at the end of the story. If you prefer
    you can add footnotes after paragraph.
7.  Check Remove Forced Line Breaks to remove
    those breaks used for print layout.
8.  Finally you can map bullet and numbers respectively to unordered and
    ordered lists.



![](imgs/34.png)
General options in EPUB Export
Options



### [9.3: Image Panel](#toc-9-3) {#9-3}

1.  Check Preserve Appearance from Layout if you
    want to keep the way images are cropped, etc.
2.  Choose Relative to Page as Image Size if you want a value expressed in
    percentage (e.g. 40% of the page width);
3.  Choose Image Alignment and Spacing;
4.  You can insert a page break before, after or both before and after
    you images;
5.  Choose JPEG as Image Conversion’s format;
6.  Choose the Image Quality and the Format Method for your images;
7.  If you check Ignore Object Export Settings
    the settings for specific images will be overwritten.



![](imgs/35.png)
Image options in EPUB Export
Options



### [9.4: Advanced Panel](#toc-9-4) {#9-4}

1.  You can choose to Include Document Metadata;
2.  Also you can add the Publisher and a Unique ID that could be the ISBN;
3.  Check Include Style Definitions if you want
    InDesign to generate a CSS for you;
4.  You shouldn’t have any local override, so you don’t need to check
    Preserve Local Overrides;
5.  Include Embeddable Fonts only if you need
    them;
6.  You can add Additional CSS, such as the one
    attached to this tutorial, this could be useful if you have a whole
    series with the same style.



![](imgs/36.png)
Advanced options in EPUB Export
Options



### [9.5: Validate your EPUB](#toc-9-5) {#9-5}

In order to validate you EPUB you need EpubCheck. You can use either the
[online
validator](http://www.google.com/url?q=http%3A%2F%2Fvalidator.idpf.org%2F&sa=D&sntz=1&usg=AFQjCNGFdp5mf_sMg3HV2Fr2hy9eM2YbcA)
or the [desktop app](https://code.google.com/p/epubcheck/). Correct the
errors if there are.

## [10: Fix HTML and CSS](#toc-10) {#10}

An ePub file is basically a ZIP file containing, beside other structure
files, all the contents in XHTML documents and the style in one or more
CSS files. You can make changes to those files using any Text Editor. Of
course you can use editors with syntax highlight such as
[gedit](http://projects.gnome.org/gedit/) or
[Coda](http://panic.com/coda/).

### [10.1: Access the ePub](#toc-10-1) {#10-1}

In order to access the inner files of your ePub you need to unzip it. To
do so you can use this [ePub unzip
app](http://www.mobileread.com/forums/showpost.php?p=1181614&postcount=18).
From the same link you can download the ePub zip app that you will need
to compact your ePub again after you made your changes.

### [10.2: Cover](#toc-10-2) {#10-2}

Keith Falgren
[suggests](http://blog.threepress.org/2009/11/20/best-practices-in-epub-cover-images/)
the following solution as the best practice for the cover. The following
code should be included in a specific XHTML file.

``` {.code}
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        Cover
        
            body, div, dl, dt, dd, ul, ol, li, h1, h2, h3, h4, h5, h6, p, pre, code, blockquote {
                margin: 0;
                padding: 0;
                border-width: 0;
            }
            p#cover {
                margin: 0;
                padding: 0;
                text-align: center;
            }
            img#cover-image {
                height: 100%;
                max-width: 100%;
            }
        
    </head>
    <body>
        
            
        
</html>
            
```

### [10.3: CSS and XHTML](#toc-10-3) {#10-3}

#### [10.3.1: Padding or Margin?](#toc-10-3-1) {#10-3-1}

There are two possibilities to space elements vertically:

1.  using margin (margin-bottom: 3em;);
2.  using padding (padding-bottom: 3em;);

Apparently they act the same, but actually padding is suggested because
it works better when near to the bottom of the page.

#### [10.3.2: Delete Defaults](#toc-10-3-2) {#10-3-2}

InDesign will automatically add CSS settings that are not rendered
because they are defaults. Examples are:

-   margin: 0;
-   padding: 0;
-   font-style: normal;

#### [10.3.3: Delete Font Colour if not necessary](#toc-10-3-3) {#10-3-3}

InDesign will automatically add a colour for the text in the CSS. In
several cases this attribute is useless therefore it can be deleted.

#### [10.3.4: Delete Redundant Classes](#toc-10-3-4) {#10-3-4}

Such tags as superscripts or italics (\,
\) automatically get a class from
InDesign:

-   \
-   \

The class can be deleted as long it’s not there to differentiate tags.

#### [10.3.5: Use Page Breaks](#toc-10-3-5) {#10-3-5}

Page breaks are useful to break a page before or after a certain
element. It’s also possible to avoid that automatic page breaks happen
within some elements bound together. The CSS attributes are:

-   page-break-before: always;
-   page-break-after: before;
-   page-break-inside: avoid;

[More info](http://www.w3schools.com/cssref/pr_print_pageba.asp)

#### [10.3.6: Images with Captions](#toc-10-3-6) {#10-3-6}

It’s useful to bind together images with their captions. In order to do
so set the images as follows in the XHTML files.

``` {.code}

    
    Caption
            
```

#### [10.3.7: No “char-style-override” class](#toc-10-3-7) {#10-3-7}

Often InDesign adds a char-style-override
class to certain tags. Make sure the class doesn’t add anything and
delete it both from the XHTML than CSS files.

### [10.4: The OPF file](#toc-10-4) {#10-4}

The OPF file is basically divided in 4 parts:

-   metadata;
-   manifest;
-   spine;
-   guide.

[More info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#TOC2.0)

#### [10.4.1: Metadata](#toc-10-4-1) {#10-4-1}

Metadata are data about other data. They are used to provide information
about the publication as a whole.

[More info](http://en.wikipedia.org/wiki/Metadata)

##### [10.4.1.1: Namespaces](10-4-1-1) {#10-4-1-1}

InDesign will automatically set the XML namespace to the following:

``` {.code}
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
            
```

Add the following to have the possibility to add futher info in the
metadata:

``` {.code}
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
            
```

##### [10.4.1.2: Title](10-4-1-2) {#10-4-1-2}

The title should be already included in the following form:

``` {.code}
Unlike Us Reader
            
```

[More
info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2.1)

##### [10.4.1.3: Authors and Roles](10-4-1-3) {#10-4-1-3}

Author set in InDesign should be already there. More than one authors
could be added and through the opf:role
attribute their role could be specified.

``` {.code}
Geert Lovink
Miriam Rasch
Solon Barocas
Caroline Bassett
[...]
            
```

[More
info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2.2)

##### [10.4.1.4: Publisher](10-4-1-4) {#10-4-1-4}

The publisher should be already included in the following form:

``` {.code}
Institute of Network Cultures
            
```

[More
info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2.5)

##### [10.4.1.5: Subjects](10-4-1-5) {#10-4-1-5}

Subjects can be added in form of keywords.

``` {.code}
social, media, monopolies, alternatives, internet, web, online, digital, Facebook, twitter, Mark Zuckerberg, unlike us, critique, theory, art, practice, economy, political, philosophy, social sciences, essays, network, privacy, database, web 2.0, individuation, collective, Lorea, Foursquare, design, program, code, graph, business, intervention, resistance, occupy, protest, Diaspora, hackers, hacking, federation, Distribution, centralization, decentralization, architecture
            
```

[More
info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2.3)

##### [10.4.1.6: Description](10-4-1-6) {#10-4-1-6}

A short description of the content could be added.

``` {.code}
The Unlike Us Reader offers a critical examination of social media, bringing together theoretical essays, personal discussions, and artistic manifestos. How can we understand the social media we use everyday, or consciously choose not to use? We know very well that monopolies control social media, but what are the alternatives? While Facebook continues to increase its user population and combines loose privacy restrictions with control over data, many researchers, programmers, and activists turn towards designing a decentralized future. Through understanding the big networks from within, be it by philosophy or art, new perspectives emerge.
            
```

[More
info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2.3)

##### [10.4.1.7: Date](10-4-1-7) {#10-4-1-7}

A date relative to the publication could be added in the following form;
month and day are not mandatory.

``` {.code}
2013-02
            
```

[More
info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2.10)

##### [10.4.1.8: Language](10-4-1-8) {#10-4-1-8}

The language of the publication could be added in the following form:

``` {.code}
en-GB
            
```

##### [10.4.1.9: Rights](10-4-1-9) {#10-4-1-9}

Rights of the publication could be added in the following form:

``` {.code}
This publication is licensed under Creative Commons Attribution, NonCommercial, ShareAlike 3.0 Unported (CC BY-NC-SA 3.0).
            
```

##### [10.4.1.10: Identifier](10-4-1-10) {#10-4-1-10}

At least one unique identifier must be included. This could be the ISBN
number.

``` {.code}
978-90-818575-5-0
            
```

[More
info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2.10)

##### [10.4.1.11: Other Metadata](10-4-1-11) {#10-4-1-11}

It is possible to add other metadata.

[More info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#TOC2.2)

#### [10.4.2: Spine](#toc-10-4-2) {#10-4-2}

The spine defines the linear order of the publication. The linear attribute is useful for items that are part
of the publication but are not actual content (such as cover, colophon,
etc.)

``` {.code}

    
    
    
    [...]

            
```

[More
info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4)

#### [10.4.3: Guide (optional)](#toc-10-4-3) {#10-4-3}

The guide element identifies fundamental structural components of the
publication such as cover, list of illustrations, etc.

[More
info](http://www.idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.6)

### [10.5: The General Table of Contents: the NCX file](#toc-10-5) {#10-5}

The NCX file structures the TOC that will be automatically displayed by
the reading software. InDesign doesn’t allow complex structures,
therefore if you need a nested TOC you’ll need to organize it in the
following way.

``` {.code}

        
                Theory of Social Media
            
            
                
                    
                        The Most Precious Good in the Era of Social Technologies
                    
                    
                

            
```

ID’s should not be repeated more than once and the playOrder attribute should be consistent with the
actual order of the XHTML files.
