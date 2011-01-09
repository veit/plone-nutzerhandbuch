======================================
PloneFormGen-Installation mit Buildout
======================================

Installation
------------

Um ``Products.PloneFormGen`` zu installieren, wird in der ``buildout.cfg``-Datei folgendes eingetragen::

 [buildout]
 …
 eggs =
     …
     Products.PloneFormGen
 …

Anschließend wird das Buildout-Skript aufgerufen und die Instanz gestartet::

 $ ./bin/buildout
 $ ./bin/instance start

Aktivieren
----------

Nun können Sie im Zope Management Interface (ZMI) entweder eine neue Plone-Site mit dem Erweiterungsprofil *PloneFormGen* erstellen oder in einer bestehenden Plone-Site in *Konfiguration* → *Zusatzprodukte*.

Konfigurieren
-------------

Schließlich können Sie in Ihrer Plone-Site *Konfiguration* → *PloneFormGen-Berechtigungen* die Funktionalitäten von PloneFormGen für bestimmte Rollen anzeigen oder verstecken:

Add Form Folders/Fields
  
Add Mailers
  Wer darf Mail-Adapter hinzufügen?

  Üblicherweise sind dies Beitragende, Verwalter und Eigentümer.

Add Data Savers
  Wer darf Datenspeicheradapter hinzufügen?

  Üblicherweise sind dies Verwalter und Eigentümer.

Add Custom Scripts
  Wer darf Skript-Adapter hinzufügen?

  Üblicherweise sind dies Verwalter.

Edit TALES Fields
  Wer darf Felder hinzufügen, in denen die *Template Attribute Language Expression Syntax (TALES)* verwendet wird:
  
  - Im Formularordner
  
    - Eigene Aktion im Erfolgsfall
    - Skript beim Laden des Formulars
    - Skript nach der Validierung
    - Header-Angaben

  - Im Mailer-Adapter

    - Vorlage für den Haupttext der Mail

  - In Formularfeldern

    - Eigener Validator
    - Optionen des Vokabulars
    - Standardausdruck

  Üblicherweise sind dies Verwalter.

Edit Python Fields
  Wer darf Felder hinzufügen, in denen Python-Skripte verwendet werden?

  Üblicherweise sind dies Verwalter.

Edit Advanced Fields
  Wer darf die folgenden Felder des Mail-Adapters bearbeiten:

  - Im Formularordner

    - Angabe des Aktionsadapters

  - Im Mailer-Adapter

    - Extrahieren des Empfängers
    - Extrahieren der Rückantwortadresse
    - Extrahieren der Betreffzeile
    - Typ des Mail-Body festlegen
    - Konfigurieren der HTTP-Headers
    - Konfigurieren zusätzlicher Header-Angaben

  - In Formularfeldern

    - Versteckt (Diese Option ist üblicherweise nicht sinnvoll, wenn nicht zugleich dynamische Feldinhalte generiert werden können.)

  Üblicherweise sind dies Verwalter.

Edit Mail Addresses
  Wer dard die E-Mail-Adressen bearbeiten?

  Üblicherweise sind dies Verwalter und Eigentümer.

Edit Encryption Specs
  Wer darf die Verschlüsselungsangaben bearbeiten?

  Üblicherweise sind dies Verwalter.

Download Saved Input
  Wer darf die Formulardaten herunterladen?

  Üblicherweise sind dies Verwalter und Eigentümer.

Die hier vorgenommenen Einstellungen gelten für die gesamte Website. Sollen für bestimmte Formulare auf der Website andere Berechtigungen gelten, so können diese Berchtigungen auch im *Zope Management Interface (ZMI)* eines Formularordners im *Security-*Reiter angegeben werden. 

