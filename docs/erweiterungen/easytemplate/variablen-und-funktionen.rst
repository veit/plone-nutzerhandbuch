========================
Variablen und Funktionen
========================

Im folgenden werden die verfügbaren Variablen und Funktionen beschrieben.Beachten Sie bitte, dass die Tags als Funktionen beschreibt und zum Rendern der Tags ggf. ``()`` hinzugefügt werden muss.

Für das *Templated Document* stehen folgende Variablen von Plone zur Verfügung:

``portal``
 Die Plone Site, z.B.::

  {{ portal.Title().decode("utf-8") }}

``context``
 Der Kontext des Templated Documents, z.B.::

  {{ context.Title().decode("utf-8") }}
  {{ context.absolute_url().decode("utf-8") }}

``portal_url``
 Die URL der Plone-Site, z.B.::

  <a href="{{ portal_url() }}">Home</a>

``object_url``
 Die URL des Objekts.
``user``
 Der aktuelle Nutzer
``request``
 Gibt Objekte der Site entsprechend der Anfrage zurück, z.B.::

  {{ query({"portal_type":"News Item","sort_on":"Date","sort_order":"reverse"}) }}

``portal_state``
 Informationen über den aktuellen Status der Site wie z.B.

 - Ist der Nutzer angemeldet?
 - Welches ist die navigation_root?
 - Titel des Portals
 - Aktive Sprache?

Da Jinja die Strings als ASCII oder Unicode erwartet, müssen Sie in allen Ausgaben, die Umlaute o.ä. enthalten können, diese nach UTF-8 dekodieren.

Darüberhinaus können z.B. auch *Viewlets* und *Provider* angezeigt werden::

 {{ viewlet("portal.logo") }}
 {{ provider("plone.rightcolumn") }}
