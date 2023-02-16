===========
Ersetzungen
===========

Inhalte ersetzen und Einfügen von Unicode-Zeichen, aktuellem Datum, Klassen und  Tags.

Inhalte ersetzen
----------------

::

 .. |reST| replace:: reStructuredText

 |reST| erlaubt, komplexe Sachverhalte einfach darzustellen.

wird so dargestellt:

.. |reST| replace:: reStructuredText

|reST| erlaubt, komplexe Sachverhalte einfach darzustellen.

Und::

 |rest| erlaubt, komplexe Sachverhalte einfach darzustellen.

 .. |rest| replace:: reStructuredText
 .. _|rest|: https://plone-nutzerhandbuch.de/restructured-text

wird so dargestellt:

|rest|_ erlaubt, komplexe Sachverhalte einfach darzustellen.

.. |rest| replace:: reStructuredText
.. _rest: https://plone-nutzerhandbuch.de/restructured-text

Unicode-Zeichenkodierungen
--------------------------

::

 |copy| Veit Schiele, 2009

 .. |copy| unicode:: 0xA9

wird so dargestellt:

|copy| Veit Schiele, 2009

..  |copy| unicode:: 0xA9

Datum
-----

::

 .. |date| date:: %d. %m. %Y
 .. |time| date:: %H:%M

 Das Dokument wurde zuletzt verändert am |date| um |time| Uhr.

wird zu:

.. |date| date:: %d. %m. %Y
.. |time| date:: %H:%M

Das Dokument wurde zuletzt verändert am |date| um |time| Uhr.

Klassen
-------

::

 .. class:: landscape

 +----------------+----------------+
 | Attribut       | Wert           |
 +----------------+----------------+

.. class:: landscape

wird zu::

 <table class="landscape docutils">
     <tr><td>Attribut</td>
         <td>Wert</td>
     </tr>
 </table>

Tags
----

::

 .. role:: custom(emphasis)

 :custom:`text`

ergibt::

 <p><em>text</em></p>

.. s.a. http://docutils.sourceforge.net/docs/ref/rst/directives.html#directives-for-substitution-definitions
