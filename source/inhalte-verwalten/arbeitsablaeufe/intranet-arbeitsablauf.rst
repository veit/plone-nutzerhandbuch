Intranet-Arbeitsablauf
======================

- Beim Intranet-Arbeitsablauf können Artikel nur für angemeldete Nutzer sichtbar sein.
- Die möglichen Zustände sind: *Interner Entwurf*, *Zur Redaktion eingereicht*, *Intern veröffentlicht*, *Extern veröffentlicht* und *Privat*. 

|Intranet-Arbeitsablauf|

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

.. |Intranet-Arbeitsablauf| image:: intranet-workflow.gif/image_preview
.. image:: ina02.png

