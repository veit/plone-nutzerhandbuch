=============
uwosh.pfg.d2c
=============

`uwosh.pfg.d2c <https://pypi.python.org/pypi/uwosh.pfg.d2c>`_ erlaubt die
Erstellung von Artikeltypen aus einem PloneFormGen-Formular. Dabei fügt das
Produkt im *hinzufügen*-Menü einen neuen Eintrag hinzu: *Save Data to Content
Adapter*. Ist dieser Adapter aktiviert, wird aus dem Formular beim Abschicken
ein neuer Artikel mit den Formularinhalten angelegt.

Zuvor sollten jedoch auf der Site folgende Änderungen vorgenommen worden sein:

#. Zunächst erstellen sie als *Manager* einen neuen Artikeltyp:

   #. Wechseln sie hierzu im ZMI in das *Types Tool*.
   #. Kopieren Sie den Artikeltyp ``FormSaveData2ContentEntry``.
   #. Anschließend sollten Sie den Artikeltyp mit *Rename* umbenennen.
   #. Konfigurieren Sie die Felder ihres neuen Artikeltyps:

      #. Klicken Sie auf den Titel des Artikeltyps
      #. Spezifizieren Sie die Beschreibung ihres Artikeltyps
      #. Soll ihr Artikeltyp sich ähnlich verhalten wie ein Plone-Dokument, so
         geben Sie für die folgenden drei Felder den Wert ``document_view`` an:

         * Initial view name
         * Default view method
         * Available view methods

   #. Falls ihr Artikeltyp auch ohne PloneFormGen-Formular erstellt werden soll,
      aktivieren Sie die Checkbox für *Implicitly Addable*.

#. Anschließend können sie in ihrem PloneFormGen-Formular einen neuen *Save Data
   to Content Adapter* hinzufügen:

   Assign Workflow Here
    Hier können sie einen neuen Workflow hinzufügen.

    Der Standardwert ist *Default*, womit der Standard-Workflow hinzugefügt
    wird.

   Title
    Der initiale Titel beim Erstellen des Artikeltyps.

   Avoid security checks
    Ist die Checkbox aktiviert, wird nicht überprüft ob der Nutzer die
    Berechtigungen zum Erstellen des Artikeltyps hat.

    Ist die Checkbox nicht aktiviert, werden nicht-angemeldete Nutzer keine
    neuen Artikel anlegen können.

   Title Field
    Erlaubt die Auswahl, ob als Titel der Artikel der Titel des Artikeltyps oder
    Text verwendet werden soll.

    .. note::
       Ändern sie diese Angaben zu einem späteren Zeitpunkt, müssen die bereits
       früher angelegten Artikel neu indiziert werden.

   Saved entry content type
    Angabe des Artikeltyps, der zum Speichern der Formularinhalte verwendet
    werden soll.
   Nice Ids
    Generiert lesbare IDs aus dem Eintrag im Title-Feld.
