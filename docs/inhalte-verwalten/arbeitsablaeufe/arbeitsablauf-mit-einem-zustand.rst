==============================
Arbeitsablauf mit einem Status
==============================

Ein Arbeitsablauf ohne Übergänge, alles ist sofort *veröffentlicht*.

.. graphviz::

    digraph "Single State Workflow" {
        published
            [shape=box,label="Veröffentlicht\n(veröffentlicht)",style="filled",fillcolor="#ffcc99"];
    }

Der eine Status ist:

#. Veröffentlicht

   Ein Arbeitsablauf, in dem der Status nicht geändert werden kann, sondern immer schon auf  *veröffentlicht* gesetzt ist.

   Der Unterschied zu keinem Arbeitsablauf ist der, dass Artikel mit diesem Arbeitsablauf auch von Portlets, Ansichten und Produkten die den Status *Veröffentlicht* erwarten, angezeigt werden.

.. image:: plone4-artikelstatus-veroeffentlicht.png
