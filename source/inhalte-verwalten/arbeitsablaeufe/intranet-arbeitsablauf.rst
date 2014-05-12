======================
Intranet-Arbeitsablauf
======================

- Beim Intranet-Arbeitsablauf können Artikel nur für angemeldete Nutzer sichtbar sein.
- Die möglichen Zustände sind: *Interner Entwurf*, *Zur Redaktion eingereicht*, *Intern veröffentlicht*, *Extern veröffentlicht* und *Privat*. 

.. graphviz::

    digraph "Intranet/Extranet Workflow" {
        internally_published
            [shape=box,label="Intern veröffentlicht\n(internally_published)",style="filled",fillcolor="#ffcc99"];
        internal
            [shape=box,label="Interner Entwurf\n(internal)",style="filled",fillcolor="#ffcc99"];
        pending
            [shape=box,label="Zur Redaktion eingereicht\n(wartend)",style="filled",fillcolor="#ffcc99"];
        private
            [shape=box,label="Privat\n(privat)",style="filled",fillcolor="#ffcc99"];
        external
            [shape=box,label="Extern sichtbar\n(external)",style="filled",fillcolor="#ffcc99"];
        pending -> external
            [label="Der Redakteur macht den Inhalt extern zugänglich.\n(publish_externally)"];
        private -> internal
            [label="Benuzter gibt Artikel als internen Entwurf frei.\n(show_internally)"];
        internally_published -> internal
            [label="Zurückweisen\n(ablehnen),\nBenutzer zieht Veröffentlichungsgesuch zurück\n(zurückziehen)"];
        internal -> private
            [label="Benutzer setzt Artikel auf privat\n(verstecken)"];
        internal -> internally_published
            [label="Der Redakteur macht den Inhalt intern zugänglich.\n(publish_internally)"];
        pending -> internal
            [label="Zurückweisen\n(ablehnen),\nBenutzer zieht Veröffentlichungsgesuch zurück\n(zurückziehen)"];
        internally_published -> external
            [label="Der Redakteur macht den Inhalt extern zugänglich.\n(publish_externally)"];
        pending -> internally_published
            [label="Der Redakteur macht den Inhalt intern zugänglich.\n(publish_internally)"];
        internal -> pending
            [label="Zur Veröffentlichung einreichen\n(einreichen)"];
        external -> internal
            [label="Benutzer zieht Veröffentlichungsgesuch zurück\n(zurückziehen)"];
    }

Der Intranet-Arbeitsablauf enthält folgende Stadien:

#. interner Entwurf

   Ein neu erstellter Artikel hat den Status *interner Entwurf*. Damit ist er für jeden angemeldeten Nutzer sichtbar.

   .. image:: plone4-intranet-arbeitsablauf-status-interner-entwurf.png

   Folgende Übergänge gibt es in diesem Stadium:

   Privat schalten
    Falls Sie unter Ausschluss der Öffentlichkeit den Artikel bearbeiten wollen, kann der Artikel in den Status *Privat* gesetzt werden.

    .. image:: plone4-intranet-arbeitsablauf-status-interner-entwurf-privat-schalten.png

   Zur Veröffentlichung einreichen
    Damit gelangt der Artikel in den Status *Zur Redaktion eingereicht*, in dem ein Redakteur prüfen kann, ob ein Artikel in den Status *Intern veröffentlicht* gesetzt werden soll.

    .. image:: plone4-intranet-arbeitsablauf-status-interner-entwurf-einreichen.png

#. Privat

   In diesem Stadium können nur Sie selbst und diejenigen, die die Inhalte verwalten den Artikel betrachten.

   .. image:: plone4-artikelstatus-privat.png 

#. Zur Redaktion eingereicht

   Artikel im Stadium *Zur Redaktion eingereicht* werden Redakteuren in einer Revisionsliste vorgelegt.

   .. image:: plone4-arbeitsablauf-zur-redaktion-eingereicht.png

   Der Redaktion stehen folgende Übergänge zur Verfügung:

   Extern veröffentlichen
    Anschließend kann der Artikel von allen betrachtet werden.
   Intern veröffentlichen
    Der Artikel steht intern, d.h. allen angemeldeten Nutzern zur Verfügung.
   Zurückweisen
    Nach dem Zurückweisen wird der Artikel wieder in den Status *Interner Entwurf* gesetzt.

   .. image:: plone4-intranet-arbeitsablauf-status-interner-entwurf-redaktionssicht-intern-veroeffentlichen.png

#. Intern veröffentlicht

   Im Status *Intern veröffentlicht* können alle angemeldeten Nutzer das Dokument sehen. Folgende Übergänge stehen in diesem Stadium zur Verfügung:

   Extern veröffentlichen
    Anschließend kann der Artikel von allen betrachtet werden.
   Zurückweisen 
    Nach dem Zurückweisen wird der Artikel wieder in den Status *Interner Entwurf* gesetzt.

   .. image:: plone4-artikelstatus-2zur-redaktion-eingereicht-zurueckweisen-redaktionssicht.png

#. Extern sichtbar

   Der Artikel kann von allen betrachtet werden. 

   .. image:: plone4-intranet-arbeitsablauf-status-extern-sichtbar.png

