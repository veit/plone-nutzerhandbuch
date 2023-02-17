=============================
Aktivierung und Konfiguration
=============================

Aktivieren
----------

Nun können Sie im Zope Management Interface (ZMI) entweder eine neue Plone-Site mit dem Erweiterungsprofil *LinguaPlone* erstellen oder in einer bestehenden Plone-Site in *Konfiguration* → *Zusatzprodukte*.

Konfigurieren
-------------

Nun können Sie in Ihrer Plone-Site *Konfiguration* → *Spracheinstellungen* die Spracheinstellungen angeben:


Standardsprache der Website
  Die Standardsprache für den Inhalt und die Benutzerobrfläche der Website.
Verfügbare Sprachen
  Die möglichen Sprachen, in die die Inhalte übersetzt werden sollen.

Damit sich nun auch das Site-Root-Objekt mehrsprachig darstellen lässt, sollten Sie zunächst den View ``@@language-setup-folders`` aufrufen um für alle verfügbaren Sprachen eigene Ordner anlegen zu lassen. Geben Sie also z.B. ``http://mysite.org/@@language-setup-folders`` an, so sollten Sie folgende Statusmeldung erhalten::

 Setup of language root folders on Plone site 'mysite'
 Added 'en' folder: en
 INavigationRoot setup on folder 'en'
 Added 'de' folder: de
 INavigationRoot setup on folder 'de'
 Translations linked.
 Portal default page removed.
 Moved default page 'front-page' to folder 'de'.
 Root language switcher set up.
