Tabellen
========

+--------------------------------------------+
| Tabellenkonstruktion                       |
| mit *reStructured Text*                    |
+==============+==============+==============+
| Spalte 1     | Spalte 2     | Spalte 3     |
+--------------+--------------+--------------+
| Spalte 1     | Zelle über mehrere Spalten  |
+--------------+--------------+--------------+
| Spalte 1     | Zelle über   | Zelle über   |
+--------------+ mehrere      | mehrere      |
| Spalte 1     | Zeilen       | Zeilen       |
+--------------+--------------+--------------+

Diese Tabelle ist in *reStructured Text* so erstellt worden::

 +--------------------------------------------+
 | Tabellenkonstruktion                       |
 | mit *reStructured Text*                    |
 +==============+==============+==============+
 | Spalte 1     | Spalte 2     | Spalte 3     |
 +--------------+--------------+--------------+
 | Spalte 1     | Zelle über mehrere Spalten  |
 +--------------+--------------+--------------+
 | Spalte 1     | Zelle über   | Zelle über   |
 +--------------+ mehrere      | mehrere      |
 | Spalte 1     | Zeilen       | Zeilen       |
 +--------------+--------------+--------------+

Die senkrechte Linie kann auf *Windows* mit ``strg-alt-<`` und auf Macs mit ``alt-7`` erstellt werden. Wenn Tabellen mit *reStructured Text* angelegt werden sollen, ist darauf zu achten, dass in den Formularfeldern die Courier oder eine andere nicht-proportionale-Schrift verwendet wird.

Es gibt jedoch noch eine einfachere Schreibweise::

 =====  =====  ======
    Inputs     Output
 ------------  ------
   A      B    A or B
 =====  =====  ======
 False  False  False
 True   False  True
 False  True   True
 True   True   True
 =====  =====  ======

