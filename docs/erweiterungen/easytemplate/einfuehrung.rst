==========
Einführung
==========

Anwendungsfälle
---------------

- Verwenden von ungefiltertem HTML (``<script>`` u.a.).
- Hinzufügen dynamischher Listen und Tabellen auf Seiten.
- Hinzufügen dynamischer E-Mail-Texte, Betreffzeilen und Empfänger in Aktionen von Regeln.
- Unterschiedliche Texte für angemeldete und nicht-angemeldete Nutzer anzeigen.
- Erstellen einfacher Text-Portlets mit dynamischen Inhalten.

Beispiel
--------

Um zum Beispiel eine Liste aller Elemente im Ordner Effektive Bedienung zu erhalten, können Sie im Haupttext eines Templated Documents folgendes eingeben::

 {{ list_folder("news").decode("utf-8") }}
