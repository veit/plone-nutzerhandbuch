=========================
Feld mit visuellem Editor
=========================

Feld, für dessen Eingabe ein `visueller Editor`_ verwendet werden kann.

.. _`visueller Editor`: ../../../visueller-editor-tinymce

Label
  Titel des Feldes
Hilfetext
  Hier kann ein Hilfetext für die Eingabe in dieses Feld angegeben werden.
Erforderlich
  Es muss ein Wert für dieses Feld angegeben werden.
Versteckt
  Das Feld wird nicht angezeigt.
Standardwert
  Der Wert, der beim ersten Aufruf des Formulars eingetragen sein soll.
Anzahl der Zeilen
  Die maximale Anzahl der Zeilen, die im Formular angezeigt werden sollen.
Maximale Länge
  Die maximale Anzahl von Zeichen, die ein Nutzer eingeben kann.

.. note::

    Die für den visuellen Editor benötigten Javascript- und CSS-Dateien werden häufig nicht für nicht-angemeldete Nutzer geladen. Falls dieses Feld also für anonyme Nutzer angezeigt werden soll, muss der Verwalter der Website im *Portal CSS Tool* und im *Portal Javascripts Tool* den folgenden TAL-Ausdruck für diese Dateien entfernen::

      not: portal/portal_membership/isAnonymousUser
