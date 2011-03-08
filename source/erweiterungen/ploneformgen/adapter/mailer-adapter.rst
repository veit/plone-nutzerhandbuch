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
  
  .. tip::
  
     Seien Sie vorsichtig, Nutzern unkontrolliert Empfängeradressen eingeben zu lassen.

CC-Empfänger
  E-Mail-Adressen, die eine Kopie der Mail erhalten sollen.
BCC-Empfänger
  E-Mail-Adressen, die eine Kopie der Mail erhalten sollen ohne dass die anderen Empfänger davon erfahren.
Extrahieren der Rückantwortadresse
  Wählen Sie ein Formularfeld, aus dem die Rückantwortadresse extrahiert werden soll.
  
  .. tip::
  
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

  .. tip::

      Hier ist ein Beispiel, wie der Wert eines Feldes, in diesem Fall mit der ID ``name`` in die Vorlage eingefügt werden kann::

        <tal:block tal:content="python:request.form.get('name', 'Plonista')"/>

      ``name`` ist die ID des Feldes, in den der Name desjenigen eingetragen werden soll, der das Formular ausfüllt und ``Plonista`` ist der Standardwert, der genommen wird sofern das Feld ``name`` leer ist.

Mail-Body-Typ
  Mime-Typ des Textkörpers der Mail. 
HTTP-Headers
  Die Angaben in den HTML-Headers, die in die Nachricht eingefügt werden.

  X-Forwarded-For
    Die IP-Adresse desjenigen, der auf das Formular über einen Proxy-Server zugreift.
  Remote Address
    Die IP-Adresse des Servers, über den auf das Formular zugegriffen wird.
  Pfad-Information
    Pfad zum Formular
  User Agent
    Der Webbrowser, mit dem das Formular ausgefüllt wurde.
  HTTP-Refferer
    Internetadresse, von der der Nutzer auf das Formular gekommen ist.

Zusätzliche Headers-Angaben
  Hier können zusätzliche RFC822-kompatible E-Mail-Headers-Angaben gemacht werden.

Verschlüsselung
---------------

Schlüssel-ID
  Angabe der Schlüssel-ID oder E-Mail-Adresse, die zu Ihrem öffentlichen Schlüssel passt. Diese Angabe wird verwendet um den Haupttext Ihrer Nachrichten zu verschlüsseln.

  Bevor Sie Ihre Mails verschlüsseln, sollten Sie sicherstellen, dass der Haupttext der Nachrichten im plaintext-Format vorliegt.

Überschreiben
-------------

Falls die an anderer Stelle gemachten Angaben erhalten bleiben sollen, lassen Sie diese Felder bitte leer.
  
  .. note::

      Fehler im TALES-Ausdruck in einem dieser Felder führen zu einem Fehler bei der Anzeige des Formulars.

Betreff
  Ein TALES-Ausdruck, der an anderer Stelle gemachte Angaben zur Betreffzeile überschreibt.

  .. tip::

       Wollen Sie die Betreffzeile z.B. zusammensetzen aus einer statischen Anrede und dem Wert in einem Feld, so können Sie z.B. den folgenden TALES-Ausdruck verwenden::

         python:'Vielen Dank' + request.get('name', 'supporter')

       Dabei ist ``name`` die ID eines Feldes, in die der Name desjenigen eingetragen werden soll, der das Formular ausgefüllt hat und ``supporter`` der Standardwert, der eingetragen wird sofern kein Eintrag in ``name`` erfolgte. 
  
Absender
  Ein TALES-Ausdruck, der an anderer Stelle gemachte Angaben zum Absender überschreibt.

  Üblicherweise verwendet PloneFormGen die E-Mail-Adresse, die für die gesamte Website angegeben ist, als Absenderadresse. Wollen Sie für ein Formular eine andere Absenderadress verwendent, können Sie dies hier angeben, z.B.::

    string:myform@veit-schiele.de

  .. note::

     Sie können mehrere Mailer-Adapter in einem Formular verwenden sodass für jeden Mailer-Adapter eine andere Absenderadresse angegeben werden kann.

Empfänger
  Ein TALES-Ausdruck, der an anderer Stelle gemachte Angaben zum Empfänger überschreibt.

  .. tip::

     Um demjenigen, der das Formular ausgefüllt hat, eine Mail mit seinen Formulardaten zukommen zu lassen, können Sie hier z.B. folgendes eingeben::

       request/form/replyto

  .. note::

     Sie können mehrere Mailer-Adapter in einem Formular verwenden sodass ein Mailer-Adapter eine Mail an denjenigen sendet, der das Formular ausgefüllt hat **und** ein anderer Adapter die Formulardaten an Sie selbst schickt.

BCC
  Ein TALES-Ausdruck, der an anderer Stelle gemachte Angaben zu den Empfängern von Blindkopien überschreibt.
Bedingung
  Ein TALES-Ausdruck für die Bedingung, unter der eine Mail versendet wird.

