Listen
======

*reStructured Text* ermöglicht mehrere Listentypen:

- Auflistungen;
- nummerierte Listen;
- Definitionslisten;
- Feldlisten;
- Optionslisten

wie auch deren Verschachtelung.

Auflistungen
------------

Für die Erstellung einer Auflistung wird vor dem Text entweder ``-``, ``*`` oder ``+`` gefolgt von einem Leerzeichen eingegeben::

 - Auflistungen;
 - nummerierte Listen;
 - Definitionslisten;
 - Feldlisten;
 - Optionslisten

Vor dem ersten und nach dem letzten Listeneintrag muss eine Leerzeile eingefügt werden. 

Nummerierte Listen
------------------

#. Auflistungen;

#. nummerierte Listen;

#. Definitionslisten

hingegen setzen ein Zeichen mit einem anschließenden Punkt voraus z.B. ``#.``::

 #. Auflistungen;

 #. nummerierte Listen;

 #.  Definitionslisten

Definitionslisten
-----------------

Während der zu definierende Begriff als einzeilige Phrase geschreiben wird kann die Definition über mehrere Absätze gehen, z.B.::

 Begriff
  Definition

Dabei darf zwischen Begriff und Definition keine Leerzeile stehen.

Feldlisten
----------

Feldlisten können zur Darstellung von Datensätzen, zur Weiterverarbeitung in Datenbanken oder einfach als zweispaltige Tabelle verwendet werden. Aus::

 :Autor:  Veit Schiele
 :Beteiligte: Sönke Löffler-von Gierke
 :Rechte: (Scheme=URL) http://www.plone-nutzerhandbuch.de/plone-nutzerhandbuch/structured-text/anhang/copyright/ 

wird 

:Autor:  Veit Schiele
:Beteiligte: Sönke Löffler-von Gierke
:Rechte: (Scheme=URL) http://www.plone-nutzerhandbuch.de/plone-nutzerhandbuch/structured-text/anhang/copyright/ 

Optionslisten
-------------

::

 -a            Option "a"
 -b args       Optionen können Argumente 
               und lange Beschreibungen haben
 /V            Auch Sonderzeichen in Optionen sind möglich

-a            Option "a"
-b args       Optionen können Argumente 
              und lange Beschreibungen haben
/V            Auch Sonderzeichen in Optionen sind möglich

