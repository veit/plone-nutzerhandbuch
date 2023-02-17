===================================
Migration des Plone-Nutzerhandbuchs
===================================

Das Plone-Nutzerhandbuch enthält eine Buildout-Konfigurationsdatei, mit der sich die Inhalte des Plone-Nutzerhandbuchs in eine Plone-Site überführen lassen. Dabei wird eine Pipeline für ``collective.transmogrifier`` definiert, die die Inhalte als *Reference Manual* des `Plone Help Center`_ erstellt.

.. _`Plone Help Center`: http://plone.org/products/plonehelpcenter

Voraussetzungen
===============

- `Git`_

  .. _`Git`: http://git-scm.com/

  Linux
  ::
   $ sudo apt-get install git-core
  Mac
  ::
   $ sudo port install git-core

- Erstellen der Dokumentation

  Dies ist in :doc:`installation` beschrieben.

Migration
=========

#. Installation der Migrationsskripte
   ::
    $ ./bin/buildout -c migration.cfg

   Dies erzeugt das Skript ``bin/migration``.

#. Aufrufen des Skripts mit::

    $ ./bin/migration --ploneupload:target=http://admin:secret@localhost:8080/Plone/documentation/manual/plone-nutzerhandbuch

   .. note::

    In userem Fall wird das Plone-Nutzerhandbuch in eine lokale Plone-Site mit der ID `Plone` importiert wobei das Plone Help Center die ID ``documentation`` und das *reference Manual* die ID ``plone-nutzerhandbuch`` hat. Falls Sie die Dokumentation in eine andere Plone-Site mit anderen *HTTP Basic Auth*-Credentials importieren möchten, können Sie diese Zeile selbstverständlich entsprechend abändern.

   Folgende Schritte werden während der Migration ausgeführt:

   - Aus der Sphinx-Dokumentation werden Titel, Beschreibung und Haupttext von jeder Seite extrahiert.
   - Anschließend werden die Inhalte für das Plone Help Center mit XML-RPC erzeugt.
   - Veröffentlichen der Artikel sofern notwendig und Verstecken des Ordners, der die Bilder enthält in der Navigation.

   .. note::

    Das Skript zum Hochladen der Dateien überschreibt momentan noch nicht bereits vorhandene Artikel. Falls Seiten umbenannt oder verschoben wurden, sollte zunächst die gesamte Dokumentation gelöscht werden bevor die Dateien erneut hochgeladen werden.

Gestaltung
==========

Eine exemplarische CSS-Datei unter ``styles/sphinx.css``. Diese Datei können Sie ggf. für Ihre Plone-Site übernehmen um die folgenden Elemente zu gestalten:

- Die Standard-Sphinx-Gestaltung für Notizen, Warnungen etc.
- Die Pygments-Gestaltung für Syntax-Hervorhebungen.
