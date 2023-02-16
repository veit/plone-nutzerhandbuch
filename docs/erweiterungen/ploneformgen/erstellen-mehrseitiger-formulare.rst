================================
Erstellen mehrseitiger Formulare
================================

Mehrseitige Formulare lassen sich als Abfolge von Formularordnern mit PloneFormGen abbilden.

Hierzu sind die folgenden Schritte notwendig:

#. Erstellen Sie eine Reihe von :doc:`formularordner`.
#. Löschen Sie in allen bis auf den letzten Formularordner alle :doc:`adapter/index`.
#. Erstellen Sie stattdessen in diesen :doc:`formularordner` im :doc:`ueberschreiben` eine eigene Aktion im Erfolgsfall mit folgendem TALES-Ausdruck::

    traverse_to:string:id-des-naechsten-formularordners

#. Ersetzen Sie in all diesen Formularordnern die *Absenden*-Taste durch *Weiter*.
#. Erstellen Sie in jedem dieser Ordner versteckte Felder, die alle Felder der vorherigen Formulare enthalten.

   .. note::

    Nicht für alle Feldtypen kann angegeben werden, dass sie versteckt werden sollen. Verwenden Sie daher eines der folgenden Felder um die Formularinhalte aufzunehmen:

    - :doc:`textfelder/string-field`
    - :doc:`textfelder/lines-field`
    - :doc:`textfelder/text-field`

#. Aktivieren Sie im letzten Formularordner den gewünschten Aktionsadapter.
