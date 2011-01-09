====================
Datums- und Zeitfeld
====================

Feld für die Angabe von Datum und Zeit

Label
  Titel des Feldes
Hilfetext
  Hier kann ein Hilfetext für die Eingabe in dieses Feld angegeben werden.
Erforderlich
  Es muss ein Wert für dieses Feld angegeben werden.
Standardwert
  Der Wert, der beim ersten Aufruf des Formulars eingetragen sein soll.
Anzeigen der Zeitauswahl 
  Soll eine bestimmte Zeit eingegeben werden können?
Erstes Jahr
  Das erste Jahr, das eingetragen werden kann.
Letztes Jahr
  Das letzte Jahr, das eingetragen werden kann.
Zukünftige Jahre
  Wieviele Jahre, die in der Zukunft liegen, sollen angezeigt werden.

.. note::

    Die für die Darstellung von Datum und Uhrheit  benötigten Javascript- und CSS-Dateien werden häufig nicht für nicht-angemeldete Nutzer geladen. Falls dieses Feld also für anonyme Nutzer angezeigt werden soll, muss der Verwalter der Website im *Portal CSS Tool* und im *Portal Javascripts Tool* den folgenden TAL-Ausdruck für diese Dateien entfernen::

      not: portal/portal_membership/isAnonymousUser

