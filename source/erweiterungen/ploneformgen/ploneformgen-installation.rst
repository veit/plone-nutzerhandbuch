======================================
PloneFormGen-Installation mit Buildout
======================================

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

Nun können Sie im Zope Management Interface (ZMI) entweder eine neue Plone-Site mit dem Erweiterungsprofil *PloneFormGen* erstellen oder in einer bestehenden Plone-Site in Konfiguration → Zusatzprodukte.
 
