======
Blöcke
======

Literal Blocks
--------------

Ein Absatz, der lediglich aus zwei Doppelpunkten besteht, führt dazu, dass der nachfolgende, eingerückte Text in seiner Formatierung erhalten bleibt. Die zwei Doppelpunkte selbst werden nicht angezeigt.

Auch Leerzeichen, Zeilenumbrüche und alle Auszeichnungen (z.B. \*dies\* oder \\jenes) bleiben erhalten.

Sofern den zwei Doppelpunkten ein Leerzeichen vorausgeht, werden sie nicht, andernfalls lediglich ein Doppelpunkt dargestellt.

Line Blocks
-----------

Linienblöcke sind hilfreich für Adressen, Verse und ungestaltete Listen.

Jede neue Linie beginnt mit ``|``

Zeilenumbrüche und Einrückungen bleiben erhalten.

::

 | Veit Schiele
 | Mansteinstr. 7
 | D-10783 Berlin

| Veit Schiele
| Mansteinstr. 7
| D-10783 Berlin

Die senkrechte Linie kann auf *Windows* mit ``strg-alt-<`` und auf Macs mit ``alt-7`` erstellt werden.

Block Quotes
------------

::

 Block quotes sind
   eingerückte Absätze,
     die auch verschachtelt werden können.

Block quotes sind
  eingerückte Absätze,
    die auch verschachtelt werden können.

Doctest Blocks
--------------

Doctest blocks sind interaktive Python sessions. Sie beginnen mit ``>>>`` und enden mit einer Leerzeile.
