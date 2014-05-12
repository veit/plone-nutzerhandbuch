======================================
Installation des Plone-Nutzerhandbuchs
======================================

#. Auschecken des Projekts
   ::
    $ git clone https://github.com/veit/plone-nutzerhandbuch.git
#. Wechseln in das Verzeichnis
   ::
    $ cd plone-nutzerhandbuch
#. Installation des Sphinx Documentation Generator
   ::
    $ python2.7 bootstrap.py
    $ ./bin/buildout
#. Erstellen der HTML-Dateien in ``plone-nutzerhandbuch/docs/html/``
   ::
    $ cd docs/
    $ make html

.. _`Sphinx Documentation Generator`: http://sphinx.pocoo.org/

Falls Sie die Sourcen für Ihre Zwecke anpassen möchten, beachten Sie bitte, dass Sphinx ein `erweitertes Markup`_ für `ReStructuredText`_ bereitstellt.

.. _`erweitertes Markup`: http://sphinx.pocoo.org/markup/ 
.. _`ReStructuredText`: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html

In `collective.developermanual`_ steht auch ein Skript bereit, das mit `collective.transmogrify`_ die generierten HTML-Seiten von Sphinx einfach in eine Plone-Site integriert.

.. _`collective.developermanual`: https://svn.plone.org/svn/collective/collective.developermanual/trunk/
.. _`collective.transmogrify`: http://pypi.python.org/pypi/collective.transmogrifier/

Beteiligen Sie sich an der Dokumentation
========================================

Gerne richten wir für Sie auch einen eigenen Zweig auf unserem Repository ein, sodass Sie das Nutzerhandbuch für Ihre Plone-Site anpassen können und zugleich einfach Änderungen aus dem Hauptzweig des Entwicklerhandbuchs übernehmen können. Schreiben Sie uns hierzu einfach eine E-Mail an plone-nutzerhandbuch@veit-schiele.de

.. _`plone-nutzerhandbuch@veit-schiele.de`: mailto:plone-nutzerhandbuch@veit-schiele.de

Dokumentenformat
================

Hier einige Regeln, die bei der Dokumentation beachtet werden sollten:

Seitenstruktur
--------------

Die Hauptüberschrift, die auch im Inhaltsverzeichnis erscheint, sollte so geschrieben werden::

    ======================================
    Installation des Plone-Nutzerhandbuchs
    ======================================

Kapitelstruktur
===============

Jedes Kapitel oder jeder Ordner muss eine ``index.txt``-Datei mit folgenden Abschnitten enthalten:

* Überschrift des Abschnitts: Dieser wird im Inhaltsverzeichnis angezeigt.
* Sphinx ``toctree``-Anweisung wobei jede Datei in diesem Ordner verlinkt sein sollte.

Hervorhebungen
--------------

Mit `Pygments <http://pygments.org/>`_ lassen sich Hervorhebungen in Sphinx angeben.

Auch verschiedenartige Hervorhebungen lassen sich realisieren:

- für Python-Skripte::

    .. code-block:: python
        
        if "foo" == "bar":
            pass

- Für XML::

    .. code-block:: xml
    
        <?xml version="1.0" encoding="UTF-8"?>
        <rules
            xmlns="http://namespaces.plone.org/xdv"
            xmlns:css="http://namespaces.plone.org/xdv+css">
        ...
        </rules>

- Für Angaben in der Konsole::
        
    .. code-block:: console
    
        $ sh myscript.sh
        
- Soll ein gesamtes Dokument hervorgehoben werden, kann dies z.B. so geschehen::

    ..highlight\:\: console
        
        $ ./bin/instance start
                         

RestructuredText-Markierungen
-----------------------------

- Kursiv::

    *Italic*

- Halbfett::

    **Halbfett**

- Hervorhebung von Code innerhalb einer Zeile::

    ``code_hervorhebung``

- Externe Links::

    `Externer Link <http://www.plone-nutzerhandbuch.de>`_

- Interner Link::

    :doc:`Interner Link </erweiterungen/poi/aufgabenverwaltung-erstellen.txt>`

- Aufzählungsliste::

    * Erster Punkt
    * Zweiter Punkt

Informationsboxen
-----------------

Informationsboxen lassen sich in Sphinx mit den Anweisungen ``warning`` und  ``note`` angeben.

Warnungen
`````````

.. warning:: 
 
    Diese Box enthält eine Warnung!

Warnungen wie diese können so angegeben werden::

    .. warning:: 
 
        Diese Box enthält eine Warnung!

Hinweise
````````

.. note::

    TODO: Diese Box enthält einen Hinweis!

::

    .. note::

        TODO: Diese Box enthält einen Hinweis! 

Tipps
`````

.. tip::
    Diese Box enthält einen Tipp!

::

    .. tip::
        Diese Box enthält einen Tipp!


