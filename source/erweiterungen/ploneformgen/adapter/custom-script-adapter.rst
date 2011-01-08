==============
Skript-Adapter
==============

Ein Python-Skript für die Formulardaten

Titel
  Titel des Skript-Adapters
Proxy-Rolle
  Rolle, als die dieses Skript ausgeführt werden soll.
  
  - Keine Proxy-Rolle
  - Verwalten

Skript
  Hier kann das Skript eingefügt werden.

  Folgende parameter sind möglich:

  ``fields``
    HTTP-Request-Formularfelder als Schlüssel-Wert-Paare.
  ``request``
    Der aktuelle HTTP-Request.
  ``ploneformgen``
    Das PloneFormGen-Objekt.

    Rückgabewerte werden nur verarbeitet wenn ein Dictionary mit Inhalten zurückgegeben wird. 

    Andernfalls wird die Ausführung des Skripts gestoppt und der Nutzer zum Formular zurückgeführt. Fehlermeldungen können in der Form ``{'field_id':'Error message'}`` angegeben werden.

