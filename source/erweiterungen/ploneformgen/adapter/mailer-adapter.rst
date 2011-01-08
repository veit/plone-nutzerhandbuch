==============
Mailer-Adapter
==============

Adapter zum Versenden der Formulardaten als Mail.

Titel
  Titel des Mailer-Adapters.
Name des Empfängers
  Der vollständige Name des Empfängers der E-Mail.
E-Mail-Adresse des Empfängers
  Die E-Mail-Adresse des Empfängers der Formulardaten.

Adressierung
------------

Extrahieren des Empfängers
  Wählen Sie ein Formularfeld, aus dem die Empfängeradresse extrahiert werden soll. 
  
  Wird etwas anderes als *Keine* verwendet, überschreibt die Angabe diejenige aus *Empfänger-E-Mail-Adresse*.
  
  .. note::
  
     Seien Sie vorsichtig, Nutzern unkontrolliert Empfängeradressen eingeben zu lassen.

CC-Empfänger
  E-Mail-Adressen, die eine Kopie der Mail erhalten sollen.
BCC-Empfänger
  E-Mail-Adressen, die eine Kopie der Mail erhalten sollen ohne dass die anderen Empfänger davon erfahren.
Extrahieren der Rückantwortadresse
  Wählen Sie ein Formularfeld, aus dem die Rückantwortadresse extrahiert werden soll.
  
  .. note::
  
     Für dieses Feld sollte dann einer der Validatoren zur Überprüfung der E-Mail-Adressen verwendet werden.

Nachricht
---------

Betreff
  Betreffzeile der Nachricht. Diese wird verwendet, sofern kein Feld zum Extrahieren eines Betreffs angegeben wurde oder dieses leer ist.
Extrahieren des Betreffs
   Wählen Sie ein Formularfeld aus, aus dem der Betreff der Nachricht extrahiert werden soll. 
Vorangestellter Text
  Text, der den Formularangaben vorangestellt werden soll.
Angehängter Text
  Text, der den Formularangaben folgen soll.
Signatur
  Signatur am Fuß der Nachricht.
Zeige alle Felder
  Ist diese Angabe ausgewählt, werden alle eingegebenen Werte bis auf das Daten- und Beschreibungsfeld angezeigt. Die Angaben in *Zeige Antworten* werden dann ignoriert.
Zeige Antworten
  Diejenigen Felder, deren Werte auf der Danke-Seite dargestellt werden sollen.
Schließe leere Einträge ein
  Auch die Titel der Felder, für die keine Angaben gemacht wurden, werden angezeigt.

Vorlage
-------

Vorlage für den Haupttext der Mail
  Dies ist ein Zope-Page-Template, das für die Generierung des HTML-Haupttextes der Mail verwendet wird.
  
  Eine Anleitung zum Editieren von TAL (Template Attribute Language) finden Sie im `Plone-Entwicklerhandbuch`_.
  
.. _`Plone-Entwicklerhandbuch`: http://www.plone-entwicklerhandbuch.de/plone-entwicklerhandbuch/erscheinungsbild/zope-page-templates-zpt

Verschlüsselung
---------------

Schlüssel-Id
  Angabe der Schlüssel-Id oder E-Mail-Adresse, die zu Ihrem öffentlichen Schlüssel passt. Diese Angabe wird verwendet um den Haupttext Ihrer Nachrichten zu verschlüsseln.

  Bevor Sie Ihre Mails verschlüsseln, sollten Sie sicherstellen, dass der Haupttext der Nachrichten im plaintext-Format vorliegt.

