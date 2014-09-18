
all: pdf epub

epub:
	bin/sphinx-build -b singlehtml -D html_theme=epub source build
	cd build; ebook-convert index.html plone-nutzerhandbuch.epub --use-auto-toc

pdf:
	bin/sphinx-build -c source/conf-pdf -b singlehtml source docs
	bin/py scripts/pdfreactor_fix.py docs/index.html
	cd docs; pdfreactor -A "Veit Schiele" -F pdfa3 --javascript -s pdfreactor.css -a links -a bookmarks -v info index.html.out ../build/plone-nutzerhandbuch.pdf
