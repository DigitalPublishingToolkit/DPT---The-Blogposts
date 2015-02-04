---
title: make book
author: Michael Murtaugh
date: 2014-10-1
...

# make book {.entry-title .single-title itemprop="headline"}

By [Michael
Murtaugh](http://networkcultures.org/digitalpublishing/author/michaelmurtaugh/ "Posts by Michael Murtaugh"),
October 1, 2014 at 1:30 pm.

![caption](imgs/SotQreader-trailer.gif)

*Make* is a popular free software tool that helps programmers compile
their code into programs. Increasingly the tool is finding new uses in
publishing workflows to compile prose text into electronic formats like
epub and PDF. The INC subgroup has been using *make* in their hybrid
workflow to produce multiple formats of the [Society of Query
reader](http://networkcultures.org/blog/publication/society-of-the-query-reader-reflections-on-web-search/).
While not a “killer app” with a pretty graphical interface, *make*
represents a distillation of practice that suggests future tools for
creating flexible, editable workflows where tweaks and workarounds are
the norm.

**make software**

*Make* is the name of a software program close to the heart of the Free
software movement. When programmer Richard Stallman founded the GNU
(Gnu’s Not Unix) project in the 1980s it was in part an effort to
reclaim the fruits of his own labour, and this meant rebuilding the
essential tools that turn what he writes (computer code) into something
usable (a computer program). According to the [GNU
website](http://www.gnu.org/software/make/):

> GNU Make is a tool which controls the generation of executables and
> other non-source files of a program from the program’s source files.

Free software is distributed as a collection of *source* files, text
files of computer code, that typically need to be *compiled* into
something usable (executable) in a particular situation. In Free
software, heterogeneous beast that it is, there is typically *no single
way* to make such a translation happen. And that’s a good thing. Free
software is designed to work in a variety of situations of use both
technically and socially determined. A software may need to run on
different computer hardware or operating systems, and programs often are
structured in a modular fashion to allow a user to pick and choose which
components she or he needs. As a result, this translation, typically
called the *build* process, can be in programmers parlance,
*non-trivial*.

For this reason, free software has historically been distributed with
additional programs, known as a make or build scripts, that make it
easier for someone to actually use it. After generations, this practice
was itself codified in a piece of software, *make*, a distillation of
the common patterns employed in the writing of these scripts. Using
*make*, the programmer writes a *makefile* that concisely describes the
steps necessary for each piece of the process (known as rules) and how
the pieces fit together (known as dependencies). In this process outputs
are named, known as *targets*. *Make* inherently supports multiple
targets allowing a software to be built in a number of ways to produce
different outputs. Once the *makefile* is written, a user just specifies
a target and *make* performs all the steps necessary, in the right
order, to produce the result. When source files are edited, make is
clever about only performing the steps necessary given what has changed.

## make epub; make webpages; make trailer

Crucially *make* does not itself do anything particular to the
compilation of code — the details are left to the specifics of each
rule. In this way more like a manager that delegates the “actual” work
of *making* to others. As the phrase *other non-source files*, obliquely
suggests *make* can in fact be used to produce more than just computer
programs. Increasingly, coders have been realizing the value of using
make outside of the context of code and started applying it to *regular*
texts. In a [recent presentation at a Linux users
event](https://www.socallinuxexpo.org/scale12x/presentations/git-and-make-not-just-code),
programmer Don Marti described *make* as an “executable notebook” to
create e-books in the epub format in a workflow based on *make* along
with other tools such as [git](http://git-scm.com/),
[markdown](http://daringfireball.net/projects/markdown/), and
[pandoc](http://johnmacfarlane.net/pandoc/). In his talk he describes
strategies for elegantly incorporating source files in DOCX (Word)
format, and managing distributed writing among a team, all without a
central server or “CMS”-centric paradigm.

The tools described in Marti’s presentation strongly echo the tools we
have been experimenting with in the INC subgroup. We have been using
*make* to produce electronic publications of the Society of the Query
reader. In our case a makefile is used to produce a variety of outputs
from the same markdown sources:
[epub](https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader/blob/master/build/SotQreader.epub),
web pages, [a GIF-format book
trailer](https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader/blob/master/build/SotQreader-trailer.gif),
and a (preview)
[PDF](https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader/blob/master/build/SotQreader.pdf).
In addition, we have been [investigating how to bridge to a designer
producing a layout in a program like
InDesign](http://networkcultures.org/digitalpublishing/2014/05/import-html-into-indesign-via-xml/).
The [latest version of the
makefile](https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader/blob/master/makefile)
is posted on the [project’s online code
repository](https://github.com/DigitalPublishingToolkit/Society-of-the-Query-Reader).

Beyond just supporting multiple outputs from the same sources, what’s
really significant about using a *make* in a publishing workflow is that
it makes the various steps of a workflow explicit, including various
“workarounds” and patches. By concisely describing all the steps for a
particular production, the *makefile* becomes a legible and crucially
*editable* snapshot of the workflow. Makefiles provide a flexibility and
re-editability that means that as the needs of a project change and as
tools and formats develop, the workflow remains adaptable. Of course,
there are many problems with makefiles: the format, though concise, is
technically challenging and often obscure. Also, *make* is typically
used from the command line, a way of working that is alien and
intimidating to many non-programmers. Still, the solutions that *make*
offers to a host of non-trivial problems is at the very least suggestive
of the kinds of features future tools for hybrid publishing would
ideally provide.

**Links**

-   [Nathan Willis’ post on LWN](http://lwn.net/Articles/589196/), where
    I originally read out about Marti’s presentation
-   [Don Marti presentation at
    SCALE](https://www.socallinuxexpo.org/scale12x/presentations/git-and-make-not-just-code)
-   [Don Marti slides](http://zgp.org/static/scale12x/)
-   [GNU Make](http://www.gnu.org/software/make/) the official project
    homepage
