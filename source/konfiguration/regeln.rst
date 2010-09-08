Regeln
======

Regeln lösen Aktionen aus, wenn ihre Bedingungen erfüllt sind. Nachdem Sie Regeln definiert haben, können Sie diese auf einen Ordner anwenden. 
Benutzen Sie hierzu die Ansicht *Regeln* des jeweiligen Ordners.

Global aktivieren
 Sollen die Regeln global eingeschaltet werden?

 Wenn dies nicht ausgewählt ist, wird nirgends auf der Website eine Regel angewendet.

Regel hinzufügen
----------------

- Titel
- Beschreibung
- Auslösendes Ereignis

  - Artikel hinzugefügt
  - Artikel geändert
  - Artikel entfernt
  - Status eines Artikels geändert

Eingeschaltet
 Ist diese Regel zur Zeit eingeschaltet
Keine weiteren Regeln ausführen
 Bestimmt, ob weitere Regeln nach dieser Regel ausgeführt werden.

Regel bearbeiten
----------------

Nach dem Hinzufügen können Sie die auch Bedingungen und Aktionen für diese Regel festlegen.

Bedingung hinzufügen
````````````````````
Ist eine der folgenden Bedingungen erfüllt, wird die Regel ausgeführt:

Artikeltyp
 Mit dieser Bedingung legen Sie fest, dass eine Aktion nur bei bestimmten Artikeltypen ausgeführt wird.
Dateiendung
 Mit dieser Bedingung können Sie festlegen, dass eine Aktion nur bei bestimmten Dateiendungen ausgeführt wird.
Stadien
 Mit dieser Bedingung legen Sie fest, dass eine Aktion nur bei Artikeln angewendet wird, die sich in einem bestimmten Status befinden.
Gruppe
 Mit dieser Bedingung legen Sie fest, dass eine Aktion nur ausgeführt wird, wenn der aktuelle Benutzer Mitglieder in einer bestimmten Gruppe ist.
Rolle
 Mit dieser Bedingung legen Sie fest, dass eine Aktion nur ausgeführt wird, wenn der Benutzer eine bestimmte Funktion hat.

Aktion hinzugügen
`````````````````

Protokoll hinzufügen
 Protokollieren der Aktion:

 - Name des Protokolls
 - Detailltiefe
 - Nachricht

   Eine Nachricht lässt sich mit folgenden Variablen erstellen:

   ``&e``
    Das Ereignis
   ``&c``
    Der Kontext

Nutzer benachrichtigen
 Mit einer Benachrichtigungsaktion zeigen Sie dem Benutzer eine Nachricht an. Diese kann einem der folgenden Nachrichtentypen zugeordnet werden:

 - Info
 - Warnung
 - Fehler

Kopieren
 Kopieren in einen anderen Ordner
Verschieben
 Verschieben in einen anderen Ordner
Löschen
 Löschen des Artikels
Statusänderung
 Ändert den Status des Artikels
E-Mail versenden
 Versenden einer E-Mail unter Angabe von Betreff, Absender, Empfänger und Nachrichtentext.

 Dabei können Sie für diese Felder folgende Variablen verwenden:

``${absolute_url}``
 URL des Artikels
``${user_email}``
 E-Mail-Adresse des Nutzers
``${user_fullname}``
 Name des Nutzers
``${user_id}``
 Id des Nutzers
``${contributors}``
 Contributors
``${created}``
  Date Created
``${creators}``
 Ersteller
``${description}``
 Beschreibung
``${effective}``
 Veröffentlichungsdatum
``${expires}``
 Ablaufdatum
``${format}``
 Format
``${identifier}``
 Identifier (URI)
``${keywords}``
 Betreff
``${language}``
 Sprache
``${modified}``
 Änderungsdatum
``${rights}``
 Veröffentlichungsrechte
``${subject}``
  Betreff
``${title}``
    Titel
``${type}``
 Artikeltyp
``${manager_emails}``
 E-Mails an Verwalter
``${member_emails}``
 E-Mail an Mitglieder
``${owner_emails}``
 E-Mail an Eigentümer
``${reviewer_emails}``
 E-Mail an Redakteure
``${change_authorid}``
 Geänderter Name des Autors 
``${change_comment}``
 Kommentar
``${change_title}``
 Geänderter Titel
``${change_type}``
 Geönderter Artikeltyp
``${review_state}``
 Geänderter Status
 
