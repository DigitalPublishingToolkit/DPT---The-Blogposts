---
title: First results and thoughts on using PhoneGap for e-publications
author: timoklok
date: 2013-11-15
...

# First results and thoughts on using PhoneGap for e-publications {.entry-title .single-title itemprop="headline"}

By [timoklok](http://networkcultures.org/digitalpublishing/author/timoklok/ "Posts by timoklok"),
November 15, 2013 at 5:52 pm.

For the SketchingBook project, we (Restruct, Mr.Sauli, Arjen De Jong)
decided to explore the possibilities of producing a publication in app
form through PhoneGap. These are the first results:



**Why & What PhoneGap**

> ” PhoneGap is a mobile development framework that enables software
> programmers to build applications for mobile devices using JavaScript,
> HTML5, and CSS3, instead of device-specific languages such as
> Objective-C or Java. The resulting applications are hybrid, meaning
> that they are neither truly native (because all layout rendering is
> done via web views instead of the platform’s native UI framework) nor
> purely web-based (because they are not just web apps, but are packaged
> as apps for distribution and have access to native device APIs). “

([wikipedia](http://en.wikipedia.org/wiki/PhoneGap))

**Why did we decide on PhoneGap:**

This decision was made based on requirements for the publication:

-   Offering a richer environment than the existing paper book: embedded
    video, smooth (swipe) interaction
-   We wanted to explore the possibilities of a modular purchase model,
    allowing for individual chapters to be bought (or added to the
    publication later on).
-   Some ‘smart’ components, for instance having the publication store
    which chapters have been read by the viewer.
-   Allow for a non-linear navigation, that would also store the path
    the viewer has taken through the chapters, so they could take a
    side-step into a different chapter but always be able to return to
    their starting point.
-   The publication relies heavily on full color image media, and less
    on text, there’s no need for reflowable pages. Tablets – rather the
    e-readers – are the obvious end-device for reading this publication.

In the scope of digital publication options, ranging from simple pdf’s
to full native apps, producing through PhoneGap seems a viable option
for this publication since:

-   It, in principle, allows the interaction listed in the requirements.
-   Is written in HTML/JS/CSS, so (within our team there’s) no need to
    learn new languages. The code is easy to share and adapt.
-   There’s no need for heavy interaction with hardware components such
    as camera, sensors etc (for which native code would be more
    suitable)
-   Producing a native app would probably be more expensive, less
    durable, with fewer reusable components.
-   It is (ideally) easy to produce a publication for different
    platforms.
-   For future publications, it seems easier to link such a HTML project
    to a database from which other publication forms are created (pdf’s,
    ePub, sites) then with a native app.

However, PhoneGap is also known to render slower in comparison to native
apps (because of the web view rendering), so test are needed to see how
far we can push the interaction.

**First results -\> PhoneGap Build**

After Adobe purchased PhoneGap, they have released the online [PhoneGap
Build](https://build.phonegap.com/) system. This allows user to upload a
zip file containing the HTML/JS/CSS files, and produces an app for iOS
and Android. This service for free for every user that only maintains a
single project, afterwards a subscription is required (but free for
unlimited open source projects).

To produce an iOS app (which is our first focus for this project), an
Apple developer account is always required (costing around 90e year).

The first results with this service were promising: after [enabling
hardware
acceleration](http://phonegap-tips.com/articles/force-hardware-acceleration-with-translate3d-sometimes.html)
for elements that move via CSS, and making sure video files were
[correctly
encoded](https://developer.apple.com/library/ios/technotes/tn2224/_index.html),
sliding to the next page appeared reasonably smooth (through buttons as
well as swipe gestures). Those different ‘pages’ are actually elements
on a single HTML document. Storing user data via
[localstorage](http://diveintohtml5.info/storage.html) also worked as
expected.

In anticipation of the final design & content, next step was to test the
possibilities of in app purchases for the different chapters:

**Progressing & moving to Xcode**

At this moment, the PhoneGap Build service doesn’t provide the plugins
needed to connect to the iOS store for in app purchases. Those plugins
do exists, but it means the ‘compiling’ of the app must be done locally,
using Apple development environment XCode, allowing the use of custom
plugins.

Switching from PhoneGap Build to Xcode was a painstaking experience,
since developing for the latest iOS version (7), requires besides all
the iOS SDK en PhoneGap libraries the latest Xcode version, which in
turn only runs on OSX Mavericks, so a complete system update was needed
before we could reach the same results as with PhoneGap Build.

After adding a dummy purchase option to the app (registering this on the
Apple Dev. centre) it was fairly simple to complete a purchase by using
[this](https://github.com/j3k0/PhoneGap-InAppPurchase-iOS/blob/master/README.md)
Javascript sample. This however was only possible after providing Apple
with all our bank and tax details, even for test purposes. Since the
purchase consists only of a payment and callback through the Apple
store, the action following the purchase is completely customisable. In
our case, we succeeded downloading a new file into the app from our
server. Because of Apple’s policy of checking all apps before releasing
them to the Apple store, such an action would probably mean this app
would be rejected. Alternatives are to have Apple host the downloadable
content for you, or packaging the complete content within the initial
app, and unlocking that content partly when purchased.

The latter option is the most simple, because there’s no need to
download a new series of files into the app and correctly linking them
to the existing content. Downside would be that all the content has to
be ready on the first launch of the app, and the total filesize would
increase dramatically. On the other hand, users would never have to
download new (large) packages (for instance if they are on a 3G
network). Also, we estimate a total size under 500MB for all content
which is not that large in comparison to other rich media
publications/apps.

More results will follow as soon as further decisions have been made
concerning content and design!
