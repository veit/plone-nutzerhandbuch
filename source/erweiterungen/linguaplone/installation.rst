=========================
Installation mit Buildout
=========================

Um ``Products.LinguaPlone`` zu installieren, wird in der ``buildout.cfg``-Datei folgendes eingetragen::

 [buildout]
 …
 eggs =
     …
     Products.LinguaPlone
 …

Anschließend wird das Buildout-Skript aufgerufen und die Instanz gestartet::

 $ ./bin/buildout
 $ ./bin/instance start

