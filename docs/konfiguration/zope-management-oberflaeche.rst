Zope-Management-Oberfläche
==========================

Auf der Zope-Management-Oberfläche werden Ihnen folgende Werkzeuge zur Verfügung gestellt:

.. glossary::

    Mail Host ``MailHost``
     Einstellung für den verschickenden Mailserver
    RAM Cache Manager
     Der *RAM Cache Manager* erlaubt das Speichern von Ergebnissen aufwändiger Aufrufe wie die von Python-Skripten und externen Methoden im Arbeitsspeicher. Da er jedoch keine HTTP-Header speichert, wird das Caching ganzer HTML-Seiten nicht empfohlen.
    Resource Registry Cache
     Cache für Dateien der *Resource-Registries*.
    Pluggable Auth Service ``acl_users``
     Speicher für Nutzer, Gruppen und Authentifizierungseinstellungen.
    Archetype Tool
     Archetypes-spezifische Einstellungen. Hier können Sie gegebenenfalls das Schema von Artikeln aktualisieren.
    Caching Policy Manager
     Hier können Sie gegebenenfalls Caching-Regeln festlegen.
    Content Type Registry
     Hier können Dateiendungen bestimmten Artikeltypen zugeordnet werden.
    Site Error Log
     Hier wird Ihnen eine Liste der Fehler angezeigt, die zuletzt in der Site auftraten. Dabei können Sie angeben, wieviele Fehler Ihnen angezeigt werden sollen und ob die Fehler in Zope’s event-log-Datei geschrieben werden sollen. Dieselben Angaben finden Sie auch bereits in :doc:`fehler`.
    Plone Utility Tool ``plone_utils``
     Es stellt verschiedene Hilfsmethoden zur Verfügung.
    Plone Action Icons Tool
     Verknüpft Aktionen mit Icons.
    Plone Actions Tool
     Hier werden die Aktionen der folgenden Kategorien verwaltet:

     - ``document_actions``
     - ``site_actions``
     - ``folder_buttons``
     - ``object``
     - ``object_buttons``
     - ``portal_tabs``
     - ``user``

    CMFEditions Portal Archivist Tool
     Erlaubt die Versionierung in Plone.
    ATCT Tool
     Das Archetypes Content Types Tool bietet folgende Funktionen:

     - Skalieren von Bildern
     - Eigenschaften der Album-Ansicht etc.

    Plone Calendar Tool
     Hier lassen sich folgende Angaben zur Kalenderansicht in Plone machen:

     - Artikeltypen, die im Kalender angezeigt werden sollen. Beachten Sie dabei bitte, dass alle Artikeltypen die Attribute ``start`` und ``end`` besitzen müssen, die sog. DateTime-Objekte aus dem Katalog zurückgeben.
     - Stadien des Arbeitsablaufs, die im Kalender gezeigt werden sollen.
     - Soll der angezeigte Monat das Kalenders über die Sitzungen eines Nutzers erhalten bleiben?
     - Erster Tag der Woche

    Plone Catalog Tool
     Indices aller Inhalte der Plone-Site
    Plone Control Panel Tool
     Aktionen in der Plone-Konfiguration
    Stylesheets Registry
     Registrierung von CSS-Dateien
    CMF Diff Tool
     Einstellungen zum Vergleich verschiedener Versionen eines Atikels.
    Plone Discussion Tool
     Gewährleistet, dass Antworten auf Diskussionsbeiträge als sog. ``talkback``-Unterobjekt  gespeichert werden.
    Plone Factory Tool
     Gewährleistet, dass ein neu erstelltes Objekt bis zum Speichern nur temporär vorgehalten wird und so Artefakte vermieden werden.
    Form Controller Tool
     Hier werden Validatoren und Aktionen für Formulare bereitgestellt.
    PlonePAS GroupData Tool
     Verwaltet Eigenschaften von Gruppen
    PlonePAS Groups Tool
     Verwaltet Funktionen für Gruppen
    CMFEditions Portal ZVC based Histories Storage Tool
     Stellt eine Ansicht existierender und gelöschter Arbeitskopien bereit.
    Portal Interface Tool
     Listet die angebotenen und verfügbaren Interfaces für die Objekte auf.
    JavaScripts Registry
     Registrierung von JavaScript-Dateien
    KSS Registry
     Registrierung von Kinetic-Stylesheet-Dateien
    Plone Language Tool
     Erlaubt folgende Spracheinstellungen:

     - Standardsprache
     - Auf der Plone-Site verfügbare Sprachen
     - Kombinierte Sprachangaben, z.B. ``de-at``
     - Einstellungen zum Aushandeln der ausgelieferten Sprache
     - Einstellungen für mehrsprachige Inhalte

    PlonePAS MemberData Tool
     Verwaltet die Eigenschaften von Mitgliedern
    PlonePAS Membership Tool
     Verwaltet die Richtlinien für Mitglieder:

     - Erstellen von Nutzerverzeichnissen.
     - Artikeltyp, in dem die Nutzerverzeichnisse angelegt werden sollen.
     - ID des Ordners, in dem die Nutzerverzeichnisse angelegt werden sollen.

    Plone Metadata Tool
     Verwaltet Metadaten wie Stichworte, Ort, Sprache, Autor, Urheberrechte etc.
    Plone Migration Tool
     Hier können Sie Ihre Plone-Site migrieren falls die verwendete Plone-Version aktualisiert wurde. Darüberhinaus werden Ihnen hier die Versionen von Python, Zope und Plone angezeigt.

     Hinweise zur Aktualisierung Ihrer Plone-Site finden Sie im Plone-Entwicklerhandbuch im Kapitel `Migrationen`_.

    .. _`Migrationen`:

    Version Data Modifier Registry ``portal_modifier``
     Hier können Methoden für die Verwaltung von verschiedenen Versionen registriert werden, z.B. zum Beibehalten der UID, des Status, der Referenzen etc.
    Password Reset Tool
     Erlaubt das sichere Zurücksetzen von Nutzerpasswörtern. Hier kann ebenfalls angegeben werden, in welchem Zeitraum das Passwort zurückgesetzt werden muss und ob der Name des Nutzers angegeben werden muss. Darüberhinaus wird Ihnen angezeigt, wieviele Anfragen zum Zurücksetzen des Passworts offen sind.
    Plone Properties Tool
     Verwaltet allgemeine Eigenschaften der Website:

     ``site_properties``
      Eigenschaften, die für die gesamte Plone-Site gelten.
     ``navtree_properties``
      Eigenschaften für das Erstellen der Navigation und Sitemap.
     ``imaging_properties``
      Angabe der maximalen Höhe und Breite von Bildern.

    CMFEditions Purge Policy Keeping Only the n last Versions ``portal_purgepolicy``
     Maximale Anzahl von Versionen, die gespeichert werden sollen.

     Der Standardwert ``-1`` steht für unbeschränkte Anzahl von Versionen.

    Plone QuickInstaller Tool
     Erlaubt Ihnen die Verwendung von Zusatzprodukten in Ihrer Site. Darüberhinaus können Sie auch bereits installierte Produkte deinstallieren oder aktualisieren. Schließlich wird Ihnen noch für jedes Produkt das Installationsprotokoll angezeigt.
    Reference Factory Registry
     Verwaltet Methoden für verschiedene Arten von Referenzen.
    Plone Registration Tool
     Erlaubt die Registrierung von neuen Nutzern der Plone-Site. Hier kann ein regulärer Ausdruck für die ID der Mitglieder angegeben werden. Der Standardwert ist ``^\w[\w\.\-@]+\w$``.
    CMFEditions Standard Copy Modify Merge Repository ``portal_repository``
     Repository zum Verwalten von Versionen
    Generic Setup Tool ``portal_setup``
     Verwaltet Zusatzprodukte und Konfigurationen:

     - Importieren von Profilen oder sog. *Snapshots*
     - Export von Profilen
     - Aktualisierung von Profilen
     - Erstellen von Snapshots der aktuellen Konfiguration der Plone-Site
     - Profile vergleichen
     - Löschen doppelt registrierter Profile

    Plone Skins Tool ``portal_skins``
     Kontrolliert das Verhalten des Skins, die Reihenfolge in der die Layer durchsucht werden etc.
    Plone Syndication Tool ``portal_syndication``
     Erstellt RSS-Feeds. Zudem können Sie die Standardwerte für RSS-Feeds dieser Seite festlegen.
    TinyMCE ``portal_tinymce``
     Hilfsmethoden für den visuellen Editor TinyMCE.
    Portal Transforms ``portal_transforms``
     Steuert die Konvertierung der Daten zwischen verschiedenen MIME-Types.
    Plone Types Tool ``portal_types``
     Kontrolliert die auf der Plone-Site verfügbaren Artikeltypen.
    Unique Id Annotation Tool ``portal_uidannotation``
     Stellt Methoden zur Verwaltung von sog. *unique id annotations* bereit.
    Unique Id Generator Tool ``portal_uidgenerator``
     Generiert einmalige IDs.
    Unique Id Handler Tool ``portal_uidhandler``
     Bietet Unterstützung für den Zugriff auf UIDs eines Objekts.
    ``portal_historyidhandler``
     Erlaubt die Anfrage am ``portal_uid_handler``-Tool
    Plone Undo Tool ``portal_undo``
      Definiert Aktionen und Funktionen zum Zurücknehmen von Transaktionen.
    Plone URL Tool ``portal_url``
     Mechanismus zum Finden des Root-Objekts einer CMFSite und zum Berechnen des Pfads zu Objekten relativ zu diesem Root-Objekt.

     **Achtung:** Das Speichern von Aktionen in diesem Tool wird nicht mehr unterstützt. Stattdessen sollte das Plone Actions Tool verwendet werden.

    Plone View Customizations ``portal_view_customizations``
     Hier können View-Templates registriert und angepasst werden.
    Plone Workflow Tool ``portal_workflow``
     Enthält die Definitionen der Arbeitsabläufe der Plone-Site
    Reference Catalog ``reference_catalog``
     Katalog der Referenzen mit den Indices UID, relationship, sourceUID, targetId und targetUID.
    Portal Translation Service Tool ``translation_service``
     Hilfsmethoden zum Zugang zur *Message Factory*.
    UID-Catalog ``uid_catalog``
     Katalog mit den Indices Title, Type, UID, id und portal_type.
