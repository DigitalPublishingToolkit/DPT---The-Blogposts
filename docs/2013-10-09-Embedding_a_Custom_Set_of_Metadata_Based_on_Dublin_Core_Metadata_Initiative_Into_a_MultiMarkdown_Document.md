---
title: Embedding a Custom Set of Metadata Based on Dublin Core Metadata Initiative Into a MultiMarkdown Document
author: Silvio Lorusso
date: 2013-10-09
...

# Embedding a Custom Set of Metadata Based on Dublin Core Metadata Initiative Into a MultiMarkdown Document {.entry-title .single-title itemprop="headline"}

By [Silvio
Lorusso](http://networkcultures.org/digitalpublishing/author/silviolorusso/ "Posts by Silvio Lorusso"),
October 9, 2013 at 3:57 pm.

(updated on the 21st of October)

— INC subgroup

In this post I’ll treat the issues that emerge from the proposal of
embedding a custom set of metadata, based on the Dublin Core standard,
within a MultiMarkdown document.

The metadata set here employed is an extremely simplified version of
what it is needed in our research project, but it gives anyway several
insights that are useful in the definition of a more complex set.

The work is divided in 2 phases:

1.  the set of metadata is defined into a Dublin Core Application
    Profile (DCAP);
2.  the ways to insert the DCAP within a MultiMarkdown document are
    discussed.



## What Metadata?

1.  Metadata tied to workflow and production. Those allow to structure a
    text in such a way that, with the help of a style sheet, different
    kinds of output technologies (and formats) can be used.
2.  Metadata as the translation table between the tags under **1.** and
    the output appearance. E.g. `This is a Title` has a
    related list in which it is stipulated that on paper words in the
    field title are printed Bold face in Green. In the same list it is
    stipulated that on a B&W e-reader it is only Bold.
3.  Metadata for keywords and classifications. Here a word or small
    noun-phrase is tagged with a tag that is coupled to a glossary
    orontology in which the meaning of the term is given. E.g.
    `<glossA23>Spinach</glossA23>` means the word spinach according to
    glossary A (vegetables) is defined in field 23.
4.  Metadata that deal with navigation e.g. anchors in an hypertext
    environment.

## Why Embedding Metadata into MMD?

Embedding Metadata directly into MMD means that:

1.  the context of a document is bound to its content, so even if the
    document is considered in itself it still tells its context (author,
    date, etc.);
2.  the one who inserts the metadata only needs to know the MMD syntax
    so that she can use her preferred software to compile a document;
3.  the one who inserts the metadata could use –but is not bound to– any
    interface with custom forms.

An index of all the documents is then created according to a “media
player” model (already used for e-books like in tools like
[Calibre](http://calibre-ebook.com/)). The metadata of each document are
directly extracted and updated each time a document is modified.

## A Simplified Version of the Metadata Set Mapped to Dublin Core

Following the Dublin Core’s
[MyBookCase](http://dublincore.org/documents/profile-guidelines/)
example we define a simplified version of our metadata set by creating a
Dublin Core Application Profile (DCAP).

### Functional Requirements

First we list the functional requirements for our DCAP:

-   Retrieve articles through a title or an author search;
-   Sort retrieved items by publication date;
-   Sort retrieved items by editing date;
-   Provide the author’s name and affiliation for contact purposes.
-   Sort different typologies of articles, such as blogposts or essays;
-   Arrange the articles according to the project they belong to;
-   Retrieve a certain part of an article, such as the abstract;
-   Retrieve specific information within the text, such as names of
    people or organizations that are mentioned into it.

### Domain Model

Then we develop a [domain
model](http://dublincore.org/documents/profile-guidelines/#sect-4):

The domain model for IncPubBeta has 3 *things*: **Projects**,
**Articles** and **Persons** (the authors of the articles). The domain
model therefore consists of:

An **Article** that belongs to a **Project** and is authored by a
**Person**.

![Domain Model](imgs/Screen-Shot-2013-09-30-at-3.18.13-PM.png)

Now we select or define metadata:

An **Article**:

-   may have a **Title**;
-   may have a **Publication Date**;
-   may have an **Edited Date**;
-   may have a **Type** (blogpost or essay);
-   may have an **Abstract**;
-   may have one or more **Agents** mentioned (such as people or
    organizations);
-   may have a **Parent** project;
-   may have one or more **Authors**.

A **Parent** is a **Project** that has:

-   a **Title**;

An **Author** is a **Person** that has:

-   a **Name**;
-   an **Affiliation**.

### Metadata Evaluation

At this stage we evaluate the possibilty to use terms from existing
vocabularies in our DCPA:

#### Article

For the **Title** we can use
[dcterms:title](http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=elements#title),
simply defined as “A name given to the resource”. It takes a free text
as value.

**Publication Date** is mapped to
[dcterms:date](http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=terms#date),
formatted according to the [W3C Date and Time Formats
Specification](http://www.w3.org/TR/NOTE-datetime).

**Edited Date** is mapped to
[dcterms:modified](http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=terms#modified),
formatted according to the [W3C Date and Time Formats
Specification](http://www.w3.org/TR/NOTE-datetime).

**Type** is mapped to
[dcterms:type](http://purl.org/dc/elements/1.1/type), defined as “the
nature or genre of the resource”. It uses a domain specific vocabulary
limited in our case to the following values:

-   Essay;
-   Blogpost.

**Abstract** is mapped to
[dcterms:abstract](http://dublincore.org/documents/dcmi-terms/#terms-abstract)
and it is defined as ”a summary of the resource”.

**Agent** is mapped to
[foaf:agent](http://xmlns.com/foaf/spec/#term_Agent) and it is defined
as ”an agent (eg. person, group, software or physical artifact)”.

**Parent** is mapped to
[dcterms:isPartOf](http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=terms#isPartOf),
defined as “a related resource in which the described resource is
physically or logically included”. It is used with a non-literal value
in order to be described with multiple components.

**Author** is mapped to [dcterms:creators][dcdatesub], defined as “an
entity primarily responsible for making the resource“. It is used with a
non-literal value in order to be described with multiple components.

#### Parent as Project

**Title** is mapped to
[dcterms:title](http://dublincore.org/documents/2012/06/14/dcmi-terms/?v=elements#title)
and it takes a free text as value.

#### Author as Person:

**Name** is mapped to
[foaf:name](http://xmlns.com/foaf/spec/#term_name) (part of the FOAF
vocabulary), defined as “a name for some thing”.

**Affiliation** is mapped to
[foaf:workplaceHomepage](http://xmlns.com/foaf/spec/#term_workplaceHomepage)(part
of the FOAF vocabulary), defined as “a workplace homepage of some
person; the homepage of an organization they work for”. It takes the URL
of the workplace as value.

## Summary

Two vocabularies are used in our DCAP:

-   [DCMI Metadata Terms](http://dublincore.org/documents/dcmi-terms/);
-   [FOAF Vocabulary](http://xmlns.com/foaf/spec/).

## Description Set Profile

We design our Metadata Record, called *IncPubBeta*, with a Description
Set Profile (DSP) which is technology-agnostic.

    DescriptionSet: IncPubBeta
        Description template: Article
        minimum = 1; maximum = unlimited
            Statement template: title
            minimum = 1; maximum = 1
                Property: http://purl.org/dc/terms/title
                Type of Value = "literal"
            Statement template: dateCreated
            minimum = 1; maximum = 1
                Property: http://purl.org/dc/terms/created
                Type of Value = "literal"
                Syntax Encoding Scheme URI = http://purl.org/dc/terms/W3CDTF
            Statement template: dateModified
            minimum = 1; maximum = 1
                Property: http://purl.org/dc/terms/modified
                Type of Value = "literal"
                Syntax Encoding Scheme URI = http://purl.org/dc/terms/W3CDTF
            Statement template: type
            minimum = 1; maximum = 1
                Property: http://purl.org/dc/terms/type
                Type of Value = "literal"
                takes list = yes
            Statement template: abstract
            minimum = 1; maximum = 1
                Property: http://purl.org/dc/terms/abstract
                Type of Value = "literal"
            Statement template: agent
            minimum = 0; maximum = unlimited
                Property: http://xmlns.com/foaf/0.1/agent
                Type of Value = "literal"
            Statement template: parent
            minimum = 0; maximum = unlimited 
                Property: http://purl.org/dc/terms/isPartOf
                Type of Value = "non-literal"
                defined as = project 
            Statement template: author
            minimum = 0; maximum = unlimited 
                Property: http://purl.org/dc/terms/creator
                Type of Value = "non-literal"
                defined as = person

        Description template: Project id=project
        minimum = 1; maximum = unlimited
            Statement template: title
            minimum = 1; maximum = 1
                Property: http://purl.org/dc/terms/title
                Type of Value = "literal"

        Description template: Person id=person
        minimum = 1; maximum = unlimited
            Statement template: name
                Property: http://xmlns.com/foaf/0.1/name
                minimum = 1; maximum = 1 
                Type of Value = "literal"
            Statement template: affiliation
                Property: http://xmlns.com/foaf/0.1/name
                minimum = 1; maximum = 1 
                Type of Value = “non-literal"
                value URI = mandatory

## Support for Metadata in MultiMarkdown

MultiMarkdown
[features](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#metadata)
the possibility to insert metadata at the beginning of the document in
the following way:

    Title: This is the title  
    Author: John Doe
    Affiliation: MIT

## Comparison Between our DCAP and MultiMarkdown Default Metadata

In the comparison between our DCAP and MultiMarkdown default metadata
set we will particularly consider two aspects:

-   legibility, which is a key issue in Markdown language;
-   adherence to a shared standard for defining metadata.

### Article’s Title

**Title** could be seamlessly mapped to
[Title](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#title)
metadata, present in MultiMarkdown and defined as follows.

> Used to provide the official title of a document. This is set as the
> string within the `<head>` section of an HTML document, and
> is also used by other export formats.

    Title: This is my title

### Publication Date

**Publication Date** could be seamlessly mapped to
[Date](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#date)
metadata, present in MultiMarkdown and defined as follows.

> Provide a date for the document.

Even though MMD doesn’t provide any particular way to fomat dates, it is
preferable to adhere to [W3C Dates and Times
Formats](http://www.w3.org/TR/NOTE-datetime).

    Date: 2012-10-08

### Edited Date

There is no metadata similar to **Edited Date** in MMD. So I propose
*Modified* metadata to stick with the DC syntax.

    Modified: 2013-10-08

### Type

There is no metadata similar to **Type** in MMD. So we propose *Type*
metadata to stick with the DC syntax. It allows for a custom vocabulary.

    Type: Blogpost

### Parent Project’s Title

There is no metadata similar to **Parent** in MMD. So I propose
*Project* to give an immediate idea of what this metadata is about.

    Project: My project’s Title

### Author’s Name

The **Name** of an **Author** could be seamlessly mapped to
[Author](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#author)
metadata, present in MultiMarkdown and defined as follows.

> Self-explanatory. I strip this out to provide an author string to
> LaTeX documents. Also used as the sender for letterhead and envelope
> templates.

    Author: John Doe

### Author’s Affiliation

The **Affiliation** of an **Author** could be seamlessly mapped to
[Affiliation](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide#affiliation)
metadata, present in MultiMarkdown and defined as follows.

> Use this to include an organization that the author is affiliated
> with, e.g. a university, company, or organization.

In our case we will limit the values to URLs.

    Affiliation: http://www.international.hva.nl/

This is off course problematic in case the workplace homepage moves to
another address.

The **Affiliation** is dependent to a specific **Author**, so ways to
express this dependency are needed., specifically in case of multiple
authors.

#### Affiliation Consequent to Name

A possibility could be to insert **Affiliation** consequently to
**Author**, like in the following example.

    Author: John Doe
    Affiliation: http://www.international.hva.nl/
    Author: Mario Rossi
    Affiliation: http://www.unimi.it/

### Abstract

In order to identify the **Abstract** within a MMD document, it is
necessary to implement some extra syntax. Following there are some
references and possibilities listed.

#### LaTEX

In
[LaTEX](http://en.wikibooks.org/wiki/LaTeX/Document_Structure#Abstract)
an Abstract is identified in the following way.

    begin{abstract}
    Your abstract goes here...
    ...
    end{abstract}

This could be simplified for MMD in the following way.

    abstract
    Your abstract goes here...

In this case a blank line would represent the end of the abstract. The
advantage of this solution would be that the abstract is not written
more than once. The solution is not MMD compatible.

#### Pandoc’s Markdown

The software Pandoc has an extended Markdown
[syntax](http://en.wikipedia.org/wiki/YAML) that includes the
possibility to insert an abstract within a
[YAML](http://en.wikipedia.org/wiki/YAML) object in the following way:

    ---
    abstract: |
      This is the abstract.

      It consists of two paragraphs.
    ...
    ---

    #{abstract}

The syntax is conflicting with MMD because `---` is used to draw an
horizontal line.

#### HTML5

Another possibility could be to insert the abstract within a `section`
tag.

    
         This is the abstract.

         It consists of two paragraphs.
    

The solution doesn’t conflict with MMD and allows to write the abstract
only once. The main drawback is on the readability of the text.

### Agent

As for the abstract, a way to tag **Agents** (such as people,
organizations, institutions) within the document is desirable. Following
there are some references and possibilities listed.

#### LaTEX

LaTEX uses the following way to define nouns.

    noun{Jack} and noun{Joe Bloggs} went up the hill.

A simple way to do this in MMD could be the following.

    [Jack]{agent} and [Joe Bloggs]{agent} went up the hill.

And in the case of having a link to tag as agent, one could do like
this:

    [Jack](http://jack.com){agent} went up the hill.

The solution, similar to [Markdown Extra’s Special
Attributes](http://michelf.ca/projects/php-markdown/extra/#spe-attr), is
only a proposal and it doesn’t work in MMD.

#### Semantic MediaWiki

In [Semantic
MediaWiki](http://semantic-mediawiki.org/wiki/Semantic_MediaWiki), an
extension to MediaWiki, it is possible to tag links and normal text in
the following ways.

This article has the following agent: `[[Agent::John Doe]]`.

This article has the following agent: `[[Has Agent::John Doe]]`.

A possible solution in MMD would be to keep the syntax as is, even
though the result is less legible.

#### HTML5

Another possibility could be to insert the agent within a `span` tag.

    This is an agent: Bruno Latour.

The solution doesn’t conflict with MMD. The main drawback is again the
readability of the text.

## Example of the Whole Set within MMD

Here’s an example of the whole set of metadata as proposed above. In the
case of **Abstract** and **Agent**, the HTML5 solutions are employed.

    Title: This is my title  
    Date: 2012-10-08
    Modified: 2013-10-08  
    Type: Blogpost  
    Project: My project’s Title
    Author: John Doe
    Affiliation: http://www.international.hva.nl/
    Author: Mario Rossi
    Affiliation: http://www.unimi.it/

    
        This is the abstract.

        It consists of two paragraphs.
    

    # “This is my title”
    ## Part of *My project’s Title*

    This is an agent: Bruno Latour.

## Conclusions

Even though the proposed scenario that employs HTML5 is fully functional
within MMD, some issue regarding the legibility of code (main concern
while using MMD) do arise. In order to extract the metadata correctly, a
preprocessor is anyway needed. A possibility not treated in the post is
to include DC metadata directly as HTML header. This solution was
consciously avoided because it totally breaks the legibility.

## Resources

-   [Guidelines for Dublin Core Application
    Profiles](http://dublincore.org/documents/profile-guidelines/);
-   [Dublin Core User
    Guide](http://wiki.dublincore.org/index.php/User_Guide);
-   [MultiMarkdown Syntax
    Guide](https://github.com/fletcher/MultiMarkdown/wiki/MultiMarkdown-Syntax-Guide);
-   [Sematic Tagging in
    Markdown](http://stackoverflow.com/questions/8783641/semantic-tagging-in-markdown);
-   [Additional Markdown We Need in Scholarly
    Texts](http://blogs.plos.org/mfenner/2012/12/18/additional-markdown-we-need-in-scholarly-texts/)
    by Martin Fenner;
-   [Fountain](http://fountain.io/syntax), a plain text markup language
    for screenwriting based on Markdown;
-   [Introduction to Semantic
    MediaWiki](http://semantic-mediawiki.org/wiki/Help:Introduction_to_Semantic_MediaWiki).
