Rollen
======

Auf der Website können Benutzer unterschiedliche Rollen annehmen, die mit unterschiedlichen Rechten verbunden sind. 

Dabei wird üblicherweise unterschieden zwischen den Rollen zum Hinzufügen, Bearbeiten, Ansehen und Veröffentlichen. Jeder an der Website angemeldete Benutzer erhält automatisch bestimmte Rollen zugewiesen, die lediglich vom Administrator geändert werden können. Solche Rollen können jedoch nicht nur einzelnen Benutzern sondern auch bestimmten Gruppen zugewiesen werden.

Jede Plone-Website kommt mit den folgenden Rollen:

.. glossary::

   Mitglied
    Jeder angemeldete Nutzer der Website erhält automatisch die Rolle als Mitglied. Dabei kann ein Mitglied z.B. in seinem Verzeichnis Artikel erstellen und bearbeiten.
   Eigentümer
    Sie sind für jeden Artikel, den Sie hinzufügen, der Eigentümer. Mit dieser Rolle erhalten Sie auch die Rechte zum Bearbeiten und Löschen.
   Beteiligter
    Ein Eigentümer kann das Recht zum Hinzufügen auf jemand anders übertragen indem er ihm die Rollte *Beteiligter* zuweist. Dies geschieht im *Zugriff*-Reiter unter der Option *Kann hinzufügen*.
   Editor
    Mit dieser Rolle weist ein Eigentümer jemand anders die Rolle zum Bearbeiten zu.
   Betrachter
    Mit dieser Rolle weist ein Eigentümer jemand anders die Rolle zum Ansehen zu.
   Redakteur
    Ein Redakteur darf Artikel veröffentlichen sodass sie von allen Benutzern der Website betrachtet werden können.
   Administrator
    Die Rolle Administrator erlaubt alle grundlegenden Änderungen an der Website.
   Site-Administrator
    Die Rolle Site-Administrator hat dieselben Rechte der Rolle Administrator bis auf 

    - die Verwendung des Wartung-Kontrollfeldes
    - den Zugang zum Zope Management Interface (ZMI)
    - das Hinzufügen und Entfernen von Produkten
    - die Änderung des Aussehens
    - die Änderung der Cache-Konfiguration

