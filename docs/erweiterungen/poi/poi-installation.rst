=============================
Poi-Installation mit Buildout
=============================

Um das von uns erweiterte ``Products.Poi`` zu installieren, wird in der ``buildout.cfg``-Datei folgendes eingetragen::

 [buildout]
 parts =
     …
     productcheckouts
     instance
 …
 eggs =
     …
     Products.Poi
 develop =
     …
     src/Products.Poi
 …
 [productcheckouts]
 recipe = infrae.subversion
 urls = http://svn.plone.org/svn/collective/Products.Poi/branches/timemanagement Products.Poi
 location = src
 as_eggs = true

Anschließend wird das Buildout-Skript aufgerufen und die Instanz gestartet::

 $ ./bin/buildout
 $ ./bin/instance start

Nun können Sie im Zope Management Interface (ZMI) entweder eine neue Plone-Site mit dem Erweiterungsprofil *Poi* erstellen oder in einer bestehenden Plone-Site in Konfiguration → Zusatzprodukte.
