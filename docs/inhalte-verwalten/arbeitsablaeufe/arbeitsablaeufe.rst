==============
Arbeitsabläufe
==============

Ein Arbeitsablauf besteht in Plone aus einer bestimmten Anzahl von Stadien, in denen sich ein Artikel befinden kann und einer Reihe von Übergängen zwischen diesen Stadien. Diese Stadien werden im Status-Menü farblich markiert, für den *Community-Arbeitsablauf* sind die Farben für die verschiedenen Stadien:

+--------+------------------------------+
| Farbe  | Status                       |
+--------+------------------------------+
| rot    | privat                       |
+--------+------------------------------+
| grün   | öffentlicher Entwurf         |
+--------+------------------------------+
| orange | zur Redaktion eingereicht    |
+--------+------------------------------+
| blau   | veröffentlicht               |
+--------+------------------------------+


Übergang
--------

Übergänge zwischen den verschiedenen Stadien sind an bestimmte Rechte geknüpft. So wird z.B. im Stadium *veröffentlicht* das ``Review``-Recht benötigt um einen Artikel zurückweisen zu können, wohingegen diejenigen, die die Rolle zum Hinzufügen von Artikeln haben, ihre Artikel mit dem Recht »Zur Veröffentlichung« zurückziehen können.

Rechte
------

Meist werden folgende Rechte in den Workflows geändert:

- Zugang zu Informationen.
- Zugang zur Hauptansicht eines Artikels.
- Berechtigung, die Verzeichnisübersicht zu sehen.
- Editiermöglichkeit für die Inhalte.
- Operationen zum Verwalten der Inhalte.
- Rechte zum Hinzufügen von Artikeln.

  Darüberhinaus haben viele Artikeltypen ihre eigenen Berechtigungen zum Hinzufügen, von Inhalten, so dass dann beide Berechtigungen benötigt werden.
