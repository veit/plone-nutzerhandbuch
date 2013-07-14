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


