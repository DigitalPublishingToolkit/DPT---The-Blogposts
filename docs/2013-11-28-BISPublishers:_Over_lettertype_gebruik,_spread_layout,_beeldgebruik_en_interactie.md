---
title: BISPublishers: Over lettertype gebruik, spread layout, beeldgebruik en interactie
author: marcstumpel
date: 2013-11-28
...

# BISPublishers: Over lettertype gebruik, spread layout, beeldgebruik en interactie {.entry-title .single-title itemprop="headline"}

By [marcstumpel](http://networkcultures.org/digitalpublishing/author/marcstumpel/ "Posts by marcstumpel"),
November 28, 2013 at 4:29 pm.

De uitgeverij [BIS](http://www.bispublishers.nl/) vormt samen met het
webdesignbureau [Restruct](http://restruct.nl/), service designbureau
[Essense](http://essense.eu/) en webdeveloper [Mr
Sauli](http://mrsauli.nl/) de project subgroep BISpublishers.

Uitgeverij BIS is typisch een visuele uitgever, met een specialisatie in
het uitgeven van vakboeken voor creatieve professionals, academische
boeken, business boeken en boeken voor het algemeen publiek ( zoals
‘gift’ boeken). Engelstalige boeken in Amerika is voor hen de grootste
markt. Uitgeverij BIS is de E-book markt aan het verkennen, die zich
razendsnel ontwikkelt.



![BISpublishers subgroup, Photo: Martin
Risseeuw](imgs/11098483866_c6afec5f60_z.jpg)
BISpublishers subgroup, Photo: Martin Risseeuw



BISPublishers is begonnen met een kort onderzoek naar de wereld van
‘digital publishing’. Uit dit onderzoek zijn inzichten gewonnen die de
basis vormden voor de ideale formaat keuze, platform en device(s) met
betrekking tot twee digitale publicaties, waar zij momenteel aan werken.
De belangrijkste vragen ten grondslag van dit onderzoek: Hoe kunnen we
de e-reading experience verbeteren? Hoe we kunnen we ‘rich media’
content het beste verwerken? Hoe kunnen we interactieve publicaties
beschikbaar maken op verschillende devices tegen redelijke kosten? Welke
ontwerp tools gaan wij hiervoor inzetten? Welke devices willen wij ons
op richten?



De subgroep het heeft het digitale traject van auteur/publisher tot de
uiteindelijke lezer gevisualiseerd. Dit verloop is complex gebleken,
aangezien er veel trajecten mogelijk zijn en er constant nieuwe bij
komen. Door het in kaart brengen van verschillende eindgebruikers en
segmenten kwamen zij bij specifieke formaten terecht, zoals
[Epub](http://en.wikipedia.org/wiki/EPUB) en standalone apps.



![BISPublishers, Digital Landscap Journey](imgs/digitalpublishing.jpg)
BISPublishers, Digital Landscap Journey



De eerste case study, de publicatie -[Think Like a Lawyer, Don’t Act
Like One](http://thinklikealawyer.info/)- zit tussen een ‘business’ en
een’ gift’ boek in en behandelt 75 onderhandelingskwesties. Bij het
digitaal publiceren van dit boek was het uitgangspunt om een
vormgevingsgetrouwe e-book conversie te realiseren, waarbij het
lettertype gebruik, de spread-layout en het beeldgebruik zoveel zou
worden behouden. Developer Sauli Warmerhoven ([Mr.
Sauli](http://mrsauli.nl/)) bouwde een [EPUB3
generator](https://github.com/DigitalPublishingToolkit/epub_generator)
om de pagina opmaak voor dit boek te automatiseren.

Bij -Think Like a Lawyer, Don’t Act Like One- heeft de projectgroep
gekozen voor een eenduidige structuur, waardoor het een template-matig
boekje werd. Het kleine formaat (b5) was uitermate geschikt voor
conversie. Daarom is er gekozen voor het Epub formaat. Hoewel de Epub
generator nog verder kan worden ontwikkeld ([met de broncode beschikbaar
op Github](https://github.com/DigitalPublishingToolkit/epub_generator))
en de resultaten work-in-progress zijn, heeft de projectgroep aan de
hand van deze case al wel conclusies getrokken:

**1.** Als je een Epub ontwikkelt moet je onthouden dat hij zal worden
bekeken op e-readers. Je zal daarom rekening moeten houden met de
navigatie. Voor de ontwerper/publisher is het verstandig om de aanwezige
navigatie functionaliteit te gebruiken, in plaats van nieuwe
navigatiefuncties toe te voegen die mogelijk kan conflicteren met de
aanwezig functionaliteit.

**2.**
[Epub3](http://en.wikipedia.org/wiki/EPUB#Version_3.0_.28current_version.29)
en standaard formaten maken het mogelijk om meer controle uit te oefenen
op het ontwerp, maar het is niet geschikt voor grotere boeken.

**3.** De huidige Epub reader applicaties ondersteunen momenteel geen
interactieve elementen die zouden kunnen worden toegevoegd aan pagina’s
(zoals video’s of afbeeldingen-carrousels).

De tweede
publicatie -[Sketching](http://www.sketching.nl/bookDrawing.html)- is
een tekenleerboek voor (industrieel) ontwerpers, van de auteurs Koos
Eissen and Roselien Steur (TU Delft). Het boek, waarmee (industrieel)
ontwerpen kunnen leren schetsen, is in geprinte vorm 100.000 keer
verkocht en in 7 talen vertaald. Dit boek heeft BISpublishers omgezet
naar interactieve ervaring. Hierbij was de opdracht om een zeer visueel
e-learning boek te ontwikkelen waarbij verschillende tekentechnieken in
beeld worden gebracht. Daarnaast werden onder andere de interactie
mogelijkheden onderzocht zoals een sociale elementen, layered pagina
opmaak, navigatie en video.

Het doel was om deze productie non-lineair aan te pakken met een focus
op tablets en navigatie. Het boek werd opgedeeld in schets ‘exercises’
en ‘skills’. Door deze zijn verwerkt in het interactieontwerp kan je als
lezer verschillende stappen nemen, zoals makkelijk terugnavigeren naar
bepaalde oefeningen, of inspringen op basis van je eigen skills(et). Het
idee is dan ook om rekening te houden met verschillende typen lezers en
ontwerpers met verschillende of specifieke skills.

BISpublishers heeft voor deze publicatie in applicatie vorm niet gekozen
voor het Epub formaat, maar voor een gratis open source web framework:
[Phonegap](http://phonegap.com/). Hiermee konden zij het boek in website
vorm omzetten, ofwel verpakken, in applicatie formaat. Dit werd mede
mogelijk gemaakt door [Adobe PhoneGapp
Build](https://build.phonegap.com/).

De resultaten van de eerste experimenten met Phonegap voor Sketching
zijn veelbelovend. Er kwam een goedwerkende applicatie uitgerold, die op
diverse manieren te presenteren is, in verschillende segmenten. De app
werd daarnaast automatisch gekoppeld aan de iOS store. BISPublisher liep
bij het testen nog wel tegen wat ‘performance issues’ aan, zoals de
reactietijd van de app bij ingewikkelde interacties, maar bij de
Sketching publicatie zijn zij nog niet tegen limieten van PhoneGap
aangelopen. Zij hoefden relatief weinig aan te passen, om een native app
te ontwikkelen voor meerdere platformen. Hoewel je als uitgever zodanig
bent aangewezen op Adobe, is het een voordeel met HTML en CSS heel veel
kan doen. Dit zijn bekende programmeertalen, dus ontwikkelaars kunnen
daar snel mee aan de haal. Native code schrijven zou veel meer tijd in
beslag nemen. Bovendien kan je als uitgever op deze wijze makkelijk en
met minder kosten een boek distribueren, mocht dit wenselijk zijn. Naast
HTML en CSS blijft de koppeling met andere formaten (zoals XML of
[MultiMarkDown](http://fletcherpenney.net/multimarkdown/)) heel goed
mogelijk.

BISPublishers is van plan om PhoneGap verder testen en uit te zoeken of
zij -Sketching- volledig met PhoneGap gaan publiceren. Deze aanpak zorgt
er in ieder geval voor dat zij zich iets minder hoeven te focussen op de
technische ontwikkeling en de conversie tussen verschillende formaten,
waardoor er meer tijd en aandacht kan worden besteed aan de content.

The original presentation file (PDF) can be found
[here](http://networkcultures.org/digitalpublishing/wp-content/uploads/sites/26/2013/11/04_BIS-Publisherssmallpdf.com_.pdf)**Watch
the full presentation below**

![Video: http://vimeo.com/80883773](imgs/456897264_640.jpg)

[Showcase BISPublishers – Over lettertype gebruik, spread layout,
beeldgebruik en interactie](http://vimeo.com/80883773) from [network
cultures](http://vimeo.com/networkcultures) on
[Vimeo](https://vimeo.com).
