=================
Bilder optimieren
=================

Die Bilder sollten optimiert werden um eine möglichst geringe Dateigröße und
damit verringerte Ladezeiten zu erhalten.

Dabei sollten Sie die folgenden Schritte beachten:

#. Beschneiden Sie das Bild sofern möglich
#. Bestimmen Sie die maximal erforderliche Auflösung des Bildes

   Achten Sie darauf, dass Sie bei der Neuberechnung des Bildes
   die richtige Pixelinterpolation wählen.

   *Bikubisch*
     sollte für die meisten Photos die geeignete
     Interpolation sein
   *Pixelwiederholung*
     ist für viele Grafiken geeignet um deren harte
     Kanten erhalten zu können

#. Sofern es sich um ein Farbbild oder eine Farbgrafik handelt,
   überprüfen Sie bitte, ob der Farbmodus *RGB* ist
#. Speichern Sie das Bild in einem geeigneten Format ab,
   z.B. ``.jpg`` für Photos und ``.png`` für Grafiken.

   Achten Sie darauf, dass die Modi *Progressive* bzw. *Interlaced*
   ausgeschaltet sind, da sich durch diese die Gesamtgröße der Bilddatei
   erhöht.

   Bei ``.jpg``-Dateien können Sie meist die Qualität angeben, in der
   das Bild abgespeichert werden soll. Häufig lässt sich mit einer niedrigen
   Qualität die Dateigröße drastisch reduzieren ohne dass das Photo sichtbare
   Einbußen aufweist.

Zum Weiterlesen
===============

- `The Comprehensive Guide to Saving Images for the Web
  <http://sixrevisions.com/web_design/comprehensive-guide-saving-images-for-web/>`_
