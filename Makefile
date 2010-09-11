
all: pdf epub

epub:
	bin/sphinx-build -b singlehtml -D html_theme=epub source build
	cd build; ebook-convert index.html plone-nutzerhandbuch.epub --use-auto-toc

pdf:
	bin/sphinx-build -b singlehtml source build
	cp styles/princexml.css build/_static/plone.css
	cd build; prince index.html plone-nutzerhandbuch.pdf
