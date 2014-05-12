================================================
Stadien und Übergänge der Poi-Aufgabenverwaltung
================================================

.. graphviz::

    digraph "poi_tracker_workflow" {
        restricted
            [shape=box,label="Only members can submit\n(restricted)",style="filled",fillcolor="#ffcc99"];
        protected
            [shape=box,label="Protected against anonymous views\n(protected)",style="filled",fillcolor="#ffcc99"];
        open
            [shape=box,label="Offen für neue Problemstellungen.\n(offen)",style="filled",fillcolor="#ffcc99"];
        closed
            [shape=box,label="Keine neuen Problemstellungen einzugeben.\n(closed)",style="filled",fillcolor="#ffcc99"];
        protected -> restricted
            [label="Restrict tracker\n(restrict)"];
        protected -> open
            [label="Öffne Tracker\n(offen)"];
        restricted -> closed
            [label="Schließen des Trackers\n(close)"];
        open -> closed
            [label="Schließen des Trackers\n(close)"];
        restricted -> open
            [label="Öffne Tracker\n(offen)"];
        protected -> closed
            [label="Schließen des Trackers\n(close)"];
        closed -> open
            [label="Öffne Tracker\n(offen)"];
        restricted -> protected
            [label="Protected tracker against anonymous views\n(protect)"];
    }

Durch diese Stadien lässt sich festlegen, wer Aufgaben sehen, bearbeiten oder erstellen darf. Im Einzelnen:

Offen für neue Problemstellungen (open)
 Auch nicht-angemeldete Nutzer können die Aufgaben sehen.
Only members can submit (restricted)
 Nicht-angemeldete Nutzer können die Aufgaben und Antworten sehen, jedoch nur angemeldete Nutzer können Problemstellungen hinzufügen.
Protected against anonymous views (protected)
 Nutzer der Rolle *Readers* können  lesen, *Editors* bearbeiten und *Contributors* hinzufügen wobei nicht-angemeldete Nutzer nichts zu sehen bekommen.
Keine neuen Problemstellungen einzugeben (closed)
 Es können keine neuen Problemstellungen mehr eingegeben werden.
 
