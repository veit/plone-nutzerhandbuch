=======================
Community-Arbeitsablauf
=======================

- Benutzer können Inhalte erzeugen, die sofort sichtbar sind.
- Inhalte sollten zur Redaktion eingereicht werden, damit sie z.B. in Termine und Nachrichten erscheinen.
- Auch während der Artikel der Redaktion zur Prüfung vorliegt, kann er von jedem gelesen werden.

.. graphviz::

    digraph "Community Workflow" {
        visible
            [shape=box,label="Öffentlicher Entwurf\n(sichtbar)",style="filled",fillcolor="#ffcc99"];
        pending
            [shape=box,label="Zur Redaktion eingereicht\n(wartend)",style="filled",fillcolor="#ffcc99"];
        private
            [shape=box,label="Privat\n(privat)",style="filled",fillcolor="#ffcc99"];
        published
            [shape=box,label="Veröffentlicht\n(veröffentlicht)",style="filled",fillcolor="#ffcc99"];
        private -> visible
            [label="Benuzter gibt Artikel als öffentlichen Entwurf frei.\n(zeigen)"];
        pending -> private
            [label="Benutzer setzt Artikel auf privat\n(verstecken)"];
        pending -> published
            [label="Redakteur veröffentlicht Artikel\n(veröffentlichen)"];
        published -> visible
            [label="Der Redakteur weist den Inhalt zur Überarbeitung zurück.\n(ablehnen),\nBenutzer zieht Veröffentlichungsgesuch zurück\n(zurückziehen)"];
        visible -> pending
            [label="Benutzer reicht Artikel zur Veröffentlichung ein.\n(einreichen)"];
        pending -> visible
            [label="Der Redakteur weist den Inhalt zur Überarbeitung zurück.\n(ablehnen),\nBenutzer zieht Veröffentlichungsgesuch zurück\n(zurückziehen)"];
        visible -> published
            [label="Redakteur veröffentlicht Artikel\n(veröffentlichen)"];
        visible -> private
            [label="Benutzer setzt Artikel auf privat\n(verstecken)"];
    }

Der Community-Arbeitsablauf hat folgende Stadien:

#. Öffentlicher Entwurf

   Ein neu erstellter Artikel hat den Status *Öffentlicher Entwurf* und ist damit nach dem Speichern sofort für alle sichtbar. 

   .. image:: plone4-community-arbeitsablauf-status-oeffentlicher-entwurf.png

   Folgende Übergänge gibt es in diesem Stadium:

   Privat schalten
    Falls Sie unter Ausschluss der Öffentlichkeit den Artikel bearbeiten wollen, kann der Artikel in den Status *Privat* gesetzt werden.

    .. image:: plone4-community-arbeitsablauf-status-oeffentlicher-entwurf-privat-schalten.png

   Zur Veröffentlichung einreichen
    Damit gelangt der Artikel in den Status *Zur Redaktion eingereicht*, in dem ein Redakteur prüfen kann, ob ein Artikel in den Status *Veröffentlicht* gesetzt werden und damit erst auf diversen Übersichtsseiten wie z.B. *Nachrichten* oder *Termine* erscheinen soll.

    .. image:: plone4-community-arbeitsablauf-status-oeffentlicher-entwurf-einreichen.png

#. Privat

   In diesem Stadium können nur Sie selbst und diejenigen, die die Inhalte verwalten den Artikel betrachten.

   .. image:: plone4-artikelstatus-privat.png

#. Zur Redaktion eingereicht

   Artikel im Stadium *Zur Redaktion eingereicht* werden Redakteuren in einer Revisionsliste vorgelegt.

   .. image:: plone4-artikelstatus-zur-redaktion-eingereicht.png

#. Veröffentlicht

   Der Artikel kann von allen betrachtet werden.

   .. image:: plone4-artikelstatus-veroeffentlicht.png

**Anmerkung:** Die Option *Erweitert…* wird in  :doc:`bedienelemente` beschrieben.

