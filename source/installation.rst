Installation des Plone-Nutzerhandbuchs
======================================

#. Auschecken des Buildout-Projekts
   ::
    $ svn co https://dev.veit-schiele.de/svn/plone-nutzerhandbuch/trunk/ plone-nutzerhandbuch
#. Wechseln in das Verzeichnis
   ::
    $ cd plone-nutzerhandbuch
#. Installation des `Sphinx Documentation Generator`_
   ::
    $ python2.6 bootstrap
    $ ./bin/buildout
#. Erstellen der HTML-Dokumentation
   ::
    $ cd docs/
    $ make html

Beteiligen Sie sich an der Dokumentation
========================================

Gerne richten wir für Sie auch einen eigenen Zweig auf unserem Repository ein, sodass Sie das Entwicklerhandbuch für Ihre Plone-Site anpassen können und zugleich einfach Änderungen aus dem Hauptzweig des Entwicklerhandbuchs übernehmen können. Schreiben Sie uns hierzu einfach eine E-Mail an `plone-nutzerhandbuch@veit-schiele.de`_

.. _`Sphinx Documentation Generator`: http://sphinx.pocoo.org/
.. _`plone-nutzerhandbuch@veit-schiele.de`: mailto:plone-nutzerhandbuch@veit-schiele.de

