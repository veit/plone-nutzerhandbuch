======================================
PloneFormGen-Installation mit Buildout
======================================

Installation
------------

Um ``Products.PloneFormGen`` zu installieren, wird in der ``buildout.cfg``-Datei folgendes eingetragen::

 [buildout]
 …
 eggs =
     …
     Products.PloneFormGen
 …

Anschließend wird das Buildout-Skript aufgerufen und die Instanz gestartet::

 $ ./bin/buildout
 $ ./bin/instance start

