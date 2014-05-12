======================================
Stadien und Übergänge der Poi-Aufgaben
======================================

Folgende Stadien und Übergänge sind für eine Aufgabe möglich:

.. graphviz::

    digraph "poi_issue_workflow" {
    resolved [shape=box,label="Gelöst\n(resolved)",style="filled",fillcolor="#ffcc99"];
    inprogress [shape=box,label="In Arbeit\n(in-progress)",style="filled",fillcolor="#ffcc99"];
    rejected [shape=box,label="Zurückgewiesen\n(rejected)",style="filled",fillcolor="#ffcc99"];
    closed [shape=box,label="Getestet und bestätigt geschlossen\n(closed)",style="filled",fillcolor="#ffcc99"];
    new [shape=box,label="Bei der Erstellung\n(new)",style="filled",fillcolor="#ffcc99"];
    postponed [shape=box,label="Verschoben\n(postponed)",style="filled",fillcolor="#ffcc99"];
    open [shape=box,label="Bestätigt\n(offen)",style="filled",fillcolor="#ffcc99"];
    unconfirmed [shape=box,label="Unbestätigt\n(unconfirmed)",style="filled",fillcolor="#ffcc99"];
    unconfirmed -> open [label="Offen\n(accept-unconfirmed)"];
    resolved -> closed [label="Bestätige Lösung\n(confirm-resolved)"];
    new -> unconfirmed [label="Verschicke Problemstellung beim Speichern\n(post)"];
    rejected -> open [label="Offen\n(open-rejected)"];
    unconfirmed -> resolved [label="Resolve immediately\n(resolve-unconfirmed)"];
    unconfirmed -> rejected [label="Ablehnen\n(reject-unconfirmed)"];
    inprogress -> resolved [label="Lösen\n(resolve-in-progress)"];
    open -> inprogress [label="Arbeit beginnen\n(begin-open)"];
    unconfirmed -> postponed [label="Verschieben\n(postpone-unconfirmed)"];
    open -> rejected [label="Ablehnen\n(reject-open)"];
    open -> postponed [label="Zurückstellen\n(hold-open)"];
    open -> resolved [label="Lösen\n(resolve-open)"];
    postponed -> inprogress [label="Arbeit beginnen\n(re-start)"];
    closed -> open [label="Erneut Öffnen\n(open-closed)"];
    inprogress -> postponed [label="Verschieben\n(postpone)"];
    postponed -> open [label="Erneut Öffnen\n(open-postponed)"];
    resolved -> open [label="Erneut Öffnen\n(open-resolved)"];
    }

Bei der Erstellung 

 - Verschicke Problemstellung beim Speichern

Unbestätigt

 - Ablehnen
 - Offen
 - Sofort gelöst
 - Verschieben

Bestätigt

 - Gelöst
 - Ablehnen
 - Zurückstellen

Arbeit beginnen

 - Verschieben
 - Gelöst

Gelöst

 - Lösung bestätigt
 - Erneut öffnen

Getestet und bestätigt geschlossen

 - Erneut öffnen

Verschoben

 - Erneut öffnen

Zurückgewiesen

 - Öffnen

