
all: pdf epub

epub:
	bin/sphinx-build -b singlehtml -D html_theme=epub source build
	cd build; ebook-convert index.html plone-nutzerhandbuch.epub --use-auto-toc

pdf:
	bin/sphinx-build -b singlehtml source docs
	cd docs; pdfreactor -s pdfreactor.css -a links -a bookmarks -v debug index.html ../build/plone-nutzerhandbuch.pdf
