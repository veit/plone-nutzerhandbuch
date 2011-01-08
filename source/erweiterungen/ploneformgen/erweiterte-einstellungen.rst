========================
Erweiterte Einstellungen
========================

Im Reiter *Overrides* des Bearbeitungsformulars für den Formularordner lassen sich Formularaktionen überschreiben:

Eigene Aktion im Erfolgsfall
  Anstatt einer Danke-Seite können Sie auch eine Aktion aufrufen, die nach dem Aktionsadapter aufgerufen wird. Dies kann entweder
für eine eigene ERfolgsvorlage oder ein Skript verwendet werden. Beispiele hierfür sind ``redirect_to`` oder ``traverse_to`` und ein
 TALES-Ausdruck, z.B. ``redirect_to:string:thanks-page``.
Custom Form Action
  Dies überschreibt das Attribut der Formularaktion, wobei eine URL angegeben werden muss, an die das Formular die Inhalte sendet. Dies umgeht die Validierung, die eigene Aktion im Erfolgsfall und die Danke-Seite.
Form Setup Script
  Ein TALES-Ausdruck, der aufgerufen wird wenn das Formular angezeigt wird. Ein typischer Anwendungsfall wäre der Aufruf eines Python-Skripts, das die Standardwerte für die verschiedenen Felder setzt.

  Beachten Sie bitte, dass Fehler in diesem Ausruck einen Fehler bei der Anzeige des Formulars ausgibt.

After Validation Script
  Ein TALES-Ausdruck, der aufgerufen wird nachdem das Formular erfolgreich überprüft wurde und bevor der Aktion-Adapter aufgerufen wird. Ein typischer Anwendungsfall wäre der Aufruf eines Python-Skripts, das die Formularinhalte zurücksetzt.

  Beachten Sie bitte, dass Fehler in diesem Ausruck einen Fehler bei der Anzeige des Formulars ausgibt.

Header Injection
  Dies erlaubt, Inhalte in den XHTML-Header zu schreiben. Ein typischer Anwendungsfall wäre, hier eigene CSS- oder Javascript-Dateien einzufügen. Dabei wird ein TALES-Ausdruck angegeben, der eine Zeichenkette zurückgibt.

  Beachten Sie bitte, dass Fehler in diesem Ausruck einen Fehler bei der Anzeige des Formulars ausgibt.

CSRF Protection
  Ist diese Aktion aktiviert, sollen sog. *Cross-Site Request Forgeries* verhindert werden. Dabei sind nur HTTP-Post-Aktionen zugelassen.

