========================
Dynamische Standardwerte
========================

.. admonition :: Beschreibung

    PloneFormGen erlaubt die Berechnung von Standardwerten aus TALES- oder
    Python-Ausrücken im *Überschreiben*-Reiter eines jeden Feldes. Damit ist es
    z.B. möglich, automatisch die E-Mail-Adresse des jeweiligen Nutzers in das
    Formularfeld einzusetzen.

Die *Template Attribute Language Expression Syntax (TALES)* ist eine einfache
Notation für Werte über einen Pfad, eine Zeichenkette oder einen Python-
Ausdruck. In dieser Anleitung werden wir jedoch keine Einführung in TALES geben.
Diese finden Sie in unserem Plone-Entwicklerhandbuch: `TALES <http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/anhang/glossar/tales>`_.
 
Kontextvariablen
================

Sie können die folgenden TALES-Kontextvariablen verwenden:

``here``
    Das aktuelle Objekt.

    ``here/memberEmail``
        gibt die E-Mail-Adresse des aktuellen Nutzers aus.

``folder``
    Der aktuelle Formularordner.

    ``folder/getEmail``
        gibt Ihnen z.B. die E-Mail-Adresse des Formularordners zurück.

``folder_url``
    Die URL des Formularordners
``portal``
    Die Plone-Site
``portal_url``
    Die URL der Plone-Site.
``request``
    Das ``REQUEST``-Objekt.
``member``
    Die Daten des angemeldeten Nutzers.

    ``member/id``
        gibt die ID des angemeldeten Nutzers aus.

``nothing``
    Entspricht ``none`` in Python.

``member/id | nothing``
    gibt ebenfalls die ID des angemeldeten Nutzers aus, vermeidet jedoch eine
    Fehlermeldung bei der Nutzung des Formulars durch nicht-angemeldete Nutzer.

``modules``
    Der Module-Importer.

Python-Ausrücke
===============

Hierzu wird ``python:`` vorangestellt, also z.B.

``python: DateTime()``
    gibt das aktuelle Datum aus::

        2013/07/13 13:50:31.559413 GMT+2

Aufruf eines Python-Skript
==========================

Für Komplexere Berechnungen sind TALES-Ausdrücke jedoch kaum geeignet. Hier
empfiehlt sich, ein Python-Skript im Formularodner zu erstellen und dieses
anschließend mit TALES aufzurufen. Wenn daas Python-Skript die ID ``getGroup``
hat, ist der zugehörige TALES-Ausdruck ``folder/getGroup``.

Das Python-Skript selbst kann dann z.B. folgendermaßen aussehen::

    request = container.REQUEST
    request.form.setdefault('group', 'calculated group')

Selbstverständlich kann in diesem Python-Skript auch eine externe Methode
aufgerufen werden. Im folgenden ein einfaches Beispiel:

#. Zunächst erstellen wir das Python-Skript::

    request = container.REQUEST
    RESPONSE =  request.RESPONSE

    # Call external method to get existing groups
    context.getGroups(context, request.form.keys(), request.form.values())

#. Nun kann die externe Methode in Ihrem Produkt erstellt werden::

    def getGroups(self)
        """Yor external method"""
        …

#. Schließlich wird das Python-Skript als TALES-Ausdruck in *Überschreiben*
   eingetragen. 
