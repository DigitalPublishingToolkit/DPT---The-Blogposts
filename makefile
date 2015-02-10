# Generic Makefile
#allmarkdown=$(shell ls docs/*.md)
#$(filter-out docs/book.md, $(wildcard docs/*.md))


x: 
	ls docs/*.md 



book.epub: docs/book.md epub/metadata.xml epub/styles.epub.css epub/cover.png
	cd docs && pandoc \
		--from markdown \
		--to epub3 \
		--self-contained \
		--epub-chapter-level=1 \
		--epub-stylesheet=../epub/styles.epub.css \
		--epub-cover-image=../epub/cover.png \
		--epub-metadata=../epub/metadata.xml \
		--epub-embed-font=../lib/UbuntuMono-B.ttf \
		--default-image-extension png \
		--toc-depth=1 \
		-o ../book.epub \
		book.md


# for i in `ls -r docs/*.md`;  do ./scripts/md_stripmetada.py $i >> book.md; done; mv book.md docs/;
