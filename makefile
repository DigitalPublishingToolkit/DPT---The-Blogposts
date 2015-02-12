# Makefile for blog posts
#allmarkdown=$(shell ls docs/*.md)
#$(filter-out docs/book.md, $(wildcard docs/*.md))


book.md:
	./scripts/assemble_book_md.sh 


book.epub: docs/book.md epub/metadata.xml epub/styles.epub.css epub/cover.png
	cd docs && pandoc \
		--from markdown \
		--to epub3 \
		--self-contained \
		--epub-chapter-level=1 \
		--epub-stylesheet=../epub/styles.epub.css \
		--epub-cover-image=../epub/cover.jpg \
		--epub-metadata=../epub/metadata.xml \
		--epub-embed-font=../lib/UbuntuMono-B.ttf \
		--epub-embed-font=../lib/OpenSans-Bold.ttf \
		--epub-embed-font=../lib/OpenSans-BoldItalic.ttf \
		--epub-embed-font=../lib/OpenSans-Italic.ttf \
		--epub-embed-font=../lib/OpenSans-Light.ttf \
		--epub-embed-font=../lib/OpenSans-LightItalic.ttf \
		--default-image-extension png \
		--toc-depth=1 \
		-o ../book.epub \
		book.md


# for i in `ls -r docs/*.md`;  do ./scripts/md_stripmetada.py $i >> book.md; done; mv book.md docs/;
