Installation des Plone-Nutzerhandbuchs
======================================

Sie können das Plone-Nutzerhandbuch als `Buildout`_-Projekt mit dem `Sphinx Documentation Generator`_ und den Sourcen anonym aus unserem SVN-Repository auschecken:

.. _`Buildout`: http://pypi.python.org/pypi/zc.buildout
.. _`Sphinx Documentation Generator`: http://sphinx.pocoo.org/

#. Auschecken des Projekts
   ::
    $ svn co https://dev.veit-schiele.de/svn/plone-nutzerhandbuch/trunk/ plone-nutzerhandbuch
#. Wechseln in das Verzeichnis
   ::
    $ cd plone-nutzerhandbuch
#. Installation des Sphinx Documentation Generator
   ::
    $ python2.6 bootstrap
    $ ./bin/buildout
#. Erstellen der HTML-Dateien in ``plone-nutzerhandbuch/docs/html/``
   ::
    $ cd docs/
    $ make html

.. _`Sphinx Documentation Generator`: http://sphinx.pocoo.org/

Falls Sie die Sourcen für Ihre Zwecke anpassen möchten, beachten Sie bitte, dass Sphinx ein `erweitertes Markup`_ für `ReStructuredText`_ bereitstellt.

.. _`erweitertes Markup`: http://sphinx.pocoo.org/markup/ 
.. _`ReStructuredText`: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html

Beteiligen Sie sich an der Dokumentation
========================================

Gerne richten wir für Sie auch einen eigenen Zweig auf unserem Repository ein, sodass Sie das Nutzerhandbuch für Ihre Plone-Site anpassen können und zugleich einfach Änderungen aus dem Hauptzweig des Entwicklerhandbuchs übernehmen können. Schreiben Sie uns hierzu einfach eine E-Mail an plone-nutzerhandbuch@veit-schiele.de

.. _`plone-nutzerhandbuch@veit-schiele.de`: mailto:plone-nutzerhandbuch@veit-schiele.de

