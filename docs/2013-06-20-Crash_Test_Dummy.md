---
title: Crash Test Dummy
author: Marc de Bruijn
date: 2013-06-20
...

# Crash Test Dummy {.entry-title .single-title itemprop="headline"}

By [Marc de
Bruijn](http://networkcultures.org/digitalpublishing/author/marcdebruijn/ "Posts by Marc de Bruijn"),
June 20, 2013 at 11:18 am.

In order to test the capabilities of the various EPUB readers we created
a dummy EPUB containing a couple of features often requested by
designers and publishers. While EPUB 3 is a modern standard with a lot
of possibilities, the utilisation of a relatively simple design and the
inclusion of rich media is seriously hampered by the limitations of the
EPUB readers. Most readers place restrictions on style and content,
often showing a mangled version of the original or something wholly
different. As such there is no uniform way in which EPUB is interpreted
by readers and the situation is more or less comparable to developing
websites a few years ago, and having to support older iterations of
Internet Explorer (notably version 6) by resorting to ugly hacks (the
lack alpha transparency in PNG images
((<http://support.microsoft.com/kb/294714>, more wonderful quirks here:
<http://www.positioniseverything.net/explorer.html>)) comes to mind, for
example) or opting out of certain technical innovations. The situation
regarding EPUB interpretation is more or less the same – viz. faulty
support of the standard by major EPUB readers. ((See:
<http://www.bisg.org/docs/BISG_EPUB3PlatformGrid.xls> for a detailed
comparison.)) The landscape is even more fragmented, however, there are
a great many EPUB readers for various platforms out there compared to
the relatively small amount of browsers (courtesy of three major players
((Internet Explorer (Microsoft), Firefox (Mozilla) and Safari
(Apple).))) a developer had to support.

 

## About the Dummy EPUB

We started out rather traditionally by creating an initial design in
Adobe Illustrator, containing various ideas partly based on the wishlist
of one of the publishers we work for (Valiz).

The ideas consist of the following:

1.  The content is divided into two sections, a normal text section and
    a black one containing related content (images, notes, other media,
    etc.) The user may slide the black section into view by
    tapping/clicking on an image or footnote. From a technical
    standpoint this requires some JavaScript animation and CSS styling.
    For convenience sake this point will be referred to in our test
    results and tables simply as *“JavaScript”*.
2.  The text section has a left margin containing notes, images and
    quotes from related publications. For this to work a reader has to
    support more complex CSS styles, as opposed to styling or colouring
    text – appears in test results and tables as *“Complex Styles”*;
3.  Multiple custom typefaces (test results and tables: *“Fonts”*);
4.  Coloured text elements and blocks, text styles (*“Basic Styles”*);
5.  The inclusion of video and audio;



![](imgs/05.jpg)
The top section of the original, static design in Adobe Illustrator.



The static Illustrator design was then converted into an HTML page
adhering to the EPUB 3 standard. After some initial tests in various
EPUB readers and finding that support for JavaScript isn’t widespread
for example, we decided to simplify the design by eliminating the two
section layout – we aim to implement a variation of this concept at a
later date, however. The JavaScript in the dummy EPUB consists of two
simple scripts, one animating images and another toggling the stack
order of an element.

Some additional images of the design [can be found
here](https://plus.google.com/photos/113897703800209573412/albums/5891201595830168561?authkey=CKj5zZvJ7dvElQE).

The EPUB we prepared contains custom fonts,
[Neuton](http://www.google.com/fonts/specimen/Neuton) and
[Lato](http://www.google.com/fonts/specimen/Lato), both released under
the SIL Open Font License (OFL), offering multiple weights and styles
and suitable for use with the CSS3 @font-face rule. Also contained
within the EPUB are sound and video samples MP3/OGG and MP4/WebM
((Consistent video playback might be helped by including the OGG/Vorbis
video format.)) format respectively. CSS styling is applied to the whole
document, ranging from simple styling (headers, coloured blocks, bolds
and italics, etc.) to more complex positioning of images and notes in
the margin.



![](imgs/Chrome01.png)
The HTML portion of the EPUB as rendered by Google Chrome.



Lastly, the document contains endnotes as per the IDPF [accessibility
guidelines](http://www.idpf.org/accessibility/guidelines/content/xhtml/notes.php)
regarding notes. Footnotes are also mentioned in these guidelines, but
as most EPUB readers forgo with displaying the traditional page
structure the inclusion of footnotes might not be a very viable
strategy. Unfortunately endnotes do not seem to work correctly in the
EPUB we prepared, we’re not certain if this is due to a syntactical
error on our part or lack of support by EPUB readers – this is something
we intend to investigate further in the future.

We tested our dummy EPUB on several platforms (desktop, tablet and
smartphone), making sure to include the major EPUB readers of the
respective platforms. A complete collection of application screenshots
[can be found on
Google+](https://plus.google.com/photos/113897703800209573412/albums/5890421128762040017?authkey=CP_w1-Hlg4ufyAE).

The EPUB itself [is hosted
here](https://docs.google.com/file/d/0B1ynUAxdZ4oUMnAzRTU1UDNIaTg/edit?usp=sharing).
Below is a screenshot of Google Chrome showing what the first part of
the EPUB should look like.

 

## On the desktop (Mac)

The desktop/notebook is probably not the most popular platform to peruse
ebooks, as it doesn’t have the portability of a tablet or smartphone.
There exist some applications for this platform, notably Kindle. iBooks
[is also being ported](http://www.apple.com/osx/preview/#ibooks) to the
bigger screen.

### Kindle

*Developer:* Amazon*Version:* 1.10.3*Website:*
<http://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000464931>



![](imgs/Amazon02.png)
Kindle for Mac



Kindle of course doesn’t support EPUB, so the document has to be
converted to an AZW3 file – this process is rather trivial and can be
done by Calibre. ((Calibre seems to strip audio and video, for some
reason. So another method of conversion (with KindleGen, for example)
might be worth investigating.)) Support for anything more than images is
seriously lacking. No styling (CSS is simply not parsed), video and
audio do not work and fonts are overridden. This all wouldn’t be a
problem if Kindle wasn’t one of the biggest ebook platforms in the
world.

### Calibre

*Developer:* Kovid Goyal*Version:* 0.9.35*Website:*
<http://calibre-ebook.com>



![](imgs/Calibre01.png)
Calibre



The cross platform solution for Linux, Mac and Windows. Due to its open
source nature it characteristically supports an impressive range of
features and functionality – managing an ebook library and exporting to
different ebook formats is also possible with Calibre. The EPUB viewer
is rather slow, it takes several seconds to load an EPUB, and has CSS
isn’t fully supported it seems, bolder or lighter variations of the font
are not displayed, for example.

### Adobe Digital Editions

*Developer:* Adobe*Version:* 2.0.6*Website:*
<http://www.adobe.com/products/digital-editions.html>



![](imgs/Adobe-Digital-Editions02.png)
Adobe Digital Editions



Adobe Digital Editions is comparable with Kindle regarding the lack
support for various EPUB features. The application accepts EPUB, but
strips it of anything except images.

### Kitabu

*Developer:* Sixty Four*Version:* 1.0.7*Website:*
<https://www.facebook.com/pages/Kitabu/242717922467492>



![](imgs/Kitabu02.png)
Kitabu



A very simple, free EPUB reader. Fonts and most styling are overridden
and the application insists on dividing the content into columns. This
may be disabled by the user, though the application still retains the
concept of pagination at all times, this differs from other readers like
Ehon or Kindle.

### Ehon

*Developer:* Pierre Oleo*Version:* 1.0.1*Website:* <http://ehonapp.com>



![](imgs/Ehon02.png)
Ehon



This application is relatively unknown and isn’t actively developed, it
seems. Probably some version of WebKit is used for rendering the ePub,
hence the full support for all the features of the publication.

### Azardi

*Developer:* Infogrid Pacific*Version:* 20.0*Website:*
<http://azardi.infogridpacific.com>



![](imgs/Azardi02.png)
Azardi



Despite the very awkward interface, Azardi renders the EPUB reasonably
well. No support for custom fonts and the structure is slightly mangled
due to the application’s insistence on displaying facing pages.
JavaScript support is present and audio and video work.

 

## On tablets and smartphones

Most of the applications mentioned below are available for both tablets
and smartphones. The differences between EPUB display on tablets and
smartphones are rather trivial. Of course the screen sizes of
smartphones are significantly smaller, but in terms of technical
possibilities (or lack thereof) both platforms are the same.

### iBooks

*Developer:* Apple*Version:* 3.1*Website:*
<https://itunes.apple.com/us/app/id364709193>*Environment:* iOS



![](imgs/iBooks02.png)
iBooks



The EPUB support of iBooks is a pleasant surprise. Custom fonts work as
does the CSS styling and JavaScript. Unfortunately everything in the
application is wrapped in the skeuomorphic GUI which clashes rather
violently on a visual level. The amount of space devoted to the actual
content is relatively small as the book margins are defined by the
application, not the EPUB.

### Kindle

*Developer:* AMZN Mobile*Version:* 3.8*Website:*
<http://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000301301>*Environment:*
iOS, Android



![](imgs/KindleiOS02.png)
Kindle on iOS



The experience is roughly comparable to the desktop version of the
application. Content is divided into two columns here, no styling or
custom fonts. Audio and video were stripped during the conversion by
Calibre.

### Bluefire Reader

*Developer:* Bluefire Productions*Version:* 1.9.7*Website:*
<http://www.bluefirereader.com>*Environment:* iOS



![](imgs/Bluefire-Reader02.png)
Bluefire Reader



Bluefire renders the EPUB as expected from most tablet readers, no
styling or media.

### Readmill

*Developer:* Readmill Network*Version:* 3.2*Website:*
<https://readmill.com>*Environment:* iOS



![](imgs/Readmill02.png)
Readmill



This application doesn’t allow to load EPUB files directly and instead
requires the user to upload files (PDF or EPUB) to their personal
library which can then be synced across other devices. Readmill’s
website proudly touts a focus on design and typography, which in
practice means that any CSS styling in an EPUB is ignored and the
Readmill ebook styles are applied to the entirety of the document.

### Kobo Books

*Developer:* Kobo*Version:* 5.12*Website:*
<http://www.kobo.com/apps>*Environment:* iOS, Android



![](imgs/Kobo02.png)
Kobo Books



It’s telling that Kobo Books is a pleasant surprise, although it mangles
several aspects of the design and doesn’t display the custom typography,
it’s because the other readers are just really bad at interpreting
anything more than simple text and displaying imagery.

### Lektz

*Developer:* AEL Data Services*Version:* 3.1*Website:*
<http://lektz.com>*Environment:* iOS, Android



![](imgs/Lektz02.png)
Lektz



This reader is one of the applications to (at least partly) implement
the Readium SDK. Readium is a non profit organisations backed by the
IDPF and several partners aiming to develop a cross-platform SDK for
developers. In practice this means Readium provides the interpreter for
EPUBs on various platforms, including the web. Partners include Sony,
Kobo and three large French publishing houses (Gallimard, La Martinière
and Flammarion). Support of large commercial parties is vital for the
emergence of Readium as a standard SDK for EPUB readers, so the initial
roster of backers is a good start. Lektz supports all features of the
dummy EPUB, except for audio and video.

### Aldiko Book Reader

![](imgs/Aldiko02.png)

*Developer:* Aldiko*Version:* 2.2.3*Website:*
<http://www.aldiko.com>*Environment:* Android

Barebones presentation of text and images. No video, audio or any
styling.

 

### ePub Reader

![](imgs/ePub-Reader02.png)

*Developer:* Graphilos Studio*Version:* 1.5.3*Website:*
<http://www.graphilos.com>*Environment:* Android

The “best” of the Android applications in terms of CSS styling. However,
all the pages seem to exceed the available screen size.

 

### Mantano Reader Lite

![](imgs/Mantano02.png)

*Developer:* Mantano SAS*Version:* 1.2.9*Website:*
<http://www.mantano.com>*Environment:* Android

Presentation quite similar to Aldiko: just text and images, no video,
audio or styling (except font sizes).

 

### Moon+ Reader

![](imgs/Moon02.png)

*Developer:* Moon+*Version:* 1.9.7.0*Website:*
<http://www.moondownload.com>*Environment:* Android

Moon+ applies its own styling to the background of the publication and
ignores any CSS styling (except for texts that are defined as bold or
italic). No support for video or audio.

 

### Universal Book Reader

![](imgs/UBReader02.png)

*Developer:* Mobile Systems*Version:* 2.1.260*Website:*
<http://www.ubreader.com>*Environment:* Android

No CSS styling (font sizes excepted) or custom fonts. No support for
video or audio.

 

## Summary

Below are three tables to compare the tested featured across platforms.
The lack of support for the more advanced features of EPUB 3 on tablets
and smartphones is worrying, in our opinion. The lack of any real
support hampers the production of media rich publications and any
efforts regarding (visual) design. At the moment, any innovations,
technical or otherwise, will only be usable or visible in a very small
subset of applications which aren’t widely used nor connected to viable
commercial outlets (Amazon Bookstore, Apple App Store, etc.)

### Desktop

[table id=1 /]

### Tablet & Smartphone

#### iOS

[table id=2 /]

#### Android

[table id=3 /]

## So… What now?

After surveying the field of current EPUB readers we may conclude that
the impossibilities surpass the possibilities when it comes to the EPUB
3 standard at the moment. The efforts of the Readium foundation are a
good sign for the future, especially because the foundation is backed by
commercial vendors and publishers. Apple’s iBooks might even become a
rather good EPUB reader, but only if the GUI is significantly less in
the way of the content in coming iterations of the application –
hopefully the release iOS 7 will introduce those changes. Amazon’s
Kindle is a bigger problem, as they insist on using their own file
format (KF8/AZW) and the lack of support in our tests on both iPad and
desktop. The AZW format merits further investigation though, as KF8/AZW
is commonly referred to as a wrapper format of EPUB 3, so some of the
features (fonts, basic styles, video, audio, etc.) should be supported.
We intend to prepare some further tests regarding the conversion of EPUB
3 to KF8/AZW and interpretation of the resulting files in various
versions of Kindle.

In relation to the Digital Publishing Toolkit project we’ve decided,
together with Valiz Publishers, to produce two EPUBs based on a printed
entry from Valiz’ “Context Without Walls” series.

The first version is a “conventional” EPUB, utilising only the features
supported by the broadest range of readers. This version will be
distributed through the common commercial channels (Amazon Bookstore,
App Store Books, etc.)

The second version is the “EPUB of the future”, which can only be
perused in conjunction with readers that fully implement the EPUB 3
standard. As such readers are scarce and relatively unpopular compared
to the applications provided by larger commercial parties (Apple,
Amazon, Sony, etc.), we also aim to use one of the libraries offered by
Readium – probably Readium.js – to present the EPUB to a larger
audience.
