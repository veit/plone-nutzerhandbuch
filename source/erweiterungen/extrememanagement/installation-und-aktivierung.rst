============================
Installation und Aktivierung
============================

Installation
------------

Um ``Products.eXtremeManagement`` zu installieren, wird in der ``buildout.cfg``-Datei folgendes eingetragen::

 [buildout]
 …
 eggs =
     …
     egenix-mx-base
     Products.eXtremeManagement
     xm.theme
 …
 
 [instance]
 …
 zcml =
     …
     xm.theme

Anschließend wird das Buildout-Skript aufgerufen und die Instanz gestartet::

 $ ./bin/buildout
 $ ./bin/instance start

Aktivierung
-----------

Nun können Sie im Zope Management Interface (ZMI) entweder eine neue Plone-Site mit den Erweiterungsprofilen *Extreme Management* und *eXtremeManagement theme* erstellen oder in einer bestehenden Plone-Site in *Konfiguration* → *Zusatzprodukte*.


