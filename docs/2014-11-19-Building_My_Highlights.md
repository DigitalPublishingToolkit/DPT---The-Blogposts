---
title: Building My Highlights
author: Marc de Bruijn
date: 2014-11-19
...

# Building My Highlights {.entry-title .single-title itemprop="headline"}

By [Marc de
Bruijn](http://networkcultures.org/digitalpublishing/author/marcdebruijn/ "Posts by Marc de Bruijn"),
November 19, 2014 at 3:28 pm.

[![highlights-01](imgs/highlights-01.png)]()

This is a short overview of the process of building a proof-of-concept
application. Requirements shifted during the development of the project
which, combined with a lot of uncertainty regarding the datasources to
be used, partly explains the technical exploratory process and the way
the final proof-of-concept was developed.

*My Highlights* was conceived as a mobile application allowing the user
to easily browse and filter a large collection of objects from
Highlights catalogue of the Stedelijk Museum. After the user selects
optional additional material (essay, interview, images, etc.) one is
able to generate an EPUB based on the selection, available for offline
use – for example on a smartphone while visiting the museum itself.

Apart from the technical development of the Highlights application, we
also designed the structure of the application and provided the basis of
the user interface in collaboration with Medamo. The application is
split into different sections, apart from the overview of a collection,
the application contains search, filters, guides and a section showing a
personal selection of content from the Highlights catalogue. All of the
sections are reached by selecting a series of four buttons contained in
a tabbar on the bottom of the screen. A common usage scenario involves
working from left to right in the tabbar, by first browsing the entirety
of the collection (the leftmost button), searching and filtering the
content (second and third button) and reviewing the selected choices in
the last section (available by selecting the button on the far right). A
basic interface design was developed based on the aforementioned
scenario and further developed and designed by Medamo.

In our day to day practice we mostly develop websites and site-specific
web-applications for use in exhibitions. Building native applications
for smartphones and tablets on multiple platforms (iOS, Android) is a
whole field entirely. There is the learning curve to consider for each
SDK, not to mention the difference in programming language (Objective-C
for iOS, Java for Android, etc.) and the breadth of devices to support.
Building an application using the Android SDK doesn’t guarantee it will
work on any given Android device and the same holds true to a lesser
extent when using iOS (though the device range is smaller). For
developers who work predominantly with web technologies this isn’t the
most straightforward method available, so at first we examined two
possible solutions; [*PhoneGap*](http://phonegap.com) and [*Sencha
Touch*](http://www.sencha.com/products/touch).

## PhoneGap

The promise of HTML5 web applications packaged as native apps is an
intriguing one, as it seemingly allows a web developer to ignore most of
the problems related to development using native SDKs. This is the
promise of *PhoneGap*, which gives a developer the tools to package an
HTML5 application and even – with some extra work – use some of the
native features of the targeted device (i.e. camera, compass, etc.) The
foundation of *PhoneGap* is [*Apache
Cordova*](http://cordova.apache.org) and it allows developers to package
HTML, JavaScript and CSS as native application binaries. In theory one
would create one application in HTML and use *PhoneGap* to generate all
the required application binaries based on that HTML master for the
platforms one wants to support. *Apache Cordova* also gives access to
device specific functions (camera, compass, accelerometer, etc.)
normally only available to applications built using the official SDKs.
Using *PhoneGap* a HTML application may interface with these services
through *Apache Cordova* in a unified way. As an example, the procedure
for accessing photo’s in the HTML context via *Apache Cordova* is
theoretically the same, whether the generated application binaries are
intended for distribution on an iPhone, Android or Windows phone or even
a Blackberry.*PhoneGap* in itself only offers the tools to create the
binaries, the actual application can be build using any client-side
application frameworks.

## Sencha Touch

*Sencha* offers a suite of tools, from a UI framework for building
mobile interfaces (*Sencha Touch*) to a JavaScript framework (*Ext JS*)
and an application (*Sencha Cmd*) which handles the packaging of the
code into native binaries. Due to the tight integration of the
individual components and the promise of speed rivaling that of native
applications Sencha appeared to be a viable solution at first sight. As
*Sencha Touch* is heavily integrated with *Ext JS* the learning curve is
quite high when unfamiliar with both frameworks. *Sencha* might have
been a viable option when developing a fully-fledged mobile application
to be deployed commercially, although many other competing options –
like *Ionic* – exist in that regard.

## jQuery Mobile

As the learning curve of *Sencha* proved to be a little too steep, we
turned to another HTML5 framework: [*jQuery
Mobile*](http://jquerymobile.com). As the name suggests the framework is
build on *jQuery* and therefore closely tied to the concepts used in
that particular library. *jQuery Mobile* mainly focuses on a consistent
UI experience on any platform (smartphone, tablet or desktop) and is
less (or not at all) concerned about speed or integration. Frameworks
like *Sencha* and [*Ionic*](http://ionicframework.com) try to mimic the
native UI widgets (lists, buttons, etc.) of each platform as close as
possible, while *jQuery Mobile* uses one style of widgets and aims at
rendering them as consistently as possible across multiple
platforms.*jQuery Mobile* is fairly easy and the integration with
*jQuery* certainly helps. However, for the *My Highlights* application a
custom design was created which didn’t really mesh with the default
widgets of the framework. Manipulating and overriding large portions the
framework’s CSS in order to support the design of the *My Highlights*
application, combined with the framework’s many quirks, conventions and
spotty documentation, made us abandon the framework after building a
portion of the application. *jQuery Mobile* offers a lot of options
which we didn’t necessarily need and the way some of the features have
been implemented were more of a hassle to support than actually speeding
up development.

## No specific framework

Ultimately we considered a more barebones scenario using only *jQuery*,
a library to handle URL routing ([*Flatiron
Director*](https://github.com/flatiron/director)) and a way to store
client-side data ([*jStorage*](https://github.com/andris9/jStorage)).
The application communicates with an external *WordPress* installation,
in lieu of a datasource like *Adlib*, in order to receive collection
data (via the newfangled [*WordPress JSON REST
API*](https://wordpress.org/plugins/json-rest-api/)) and generate an
EPUB based on the selections made in the *My Highlights* application.
This barebones setup, using only relatively small, individual JavaScript
libraries, allowed us to quickly develop a proof-of-concept application
which may be packaged as a *PhoneGap* binary or used as a web
application.

The code of the application and two WordPress plugins [are available on
GitHub](https://github.com/DigitalPublishingToolkit/my-highlights).



[![highlights-01](imgs/highlights-01.png)]()
[![highlights-03](imgs/highlights-03.png)]()
[![highlights-04](imgs/highlights-04.png)]()
[![highlights-05](imgs/highlights-05.png)]()
[![highlights-06](imgs/highlights-06.png)]()
[![highlights-07](imgs/highlights-07.png)]()
[![highlights-08](imgs/highlights-08.png)]()
[![highlights-09](imgs/highlights-09.png)]()
[![highlights-10](imgs/highlights-10.png)]()


