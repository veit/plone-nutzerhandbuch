
all: pdf epub

epub:
	bin/sphinx-build -b singlehtml source build

pdf:
	bin/sphinx-build -b singlehtml source build
	cd build; prince index.html plone-entwicklerhandbuch.pdf
