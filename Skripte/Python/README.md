# Info
Die Skripte in diesem Ordner sind nicht dafür gedacht einzeln ausgeführt zu werden. Es handelt sich bei diesem Ordner eher um ein ganzes Python Modul. Es setzt voraus, dass folgende Python Module vorinstalliert sind:
* `scipy`
* `numpy`
* `matplotlib`

Außerdem müssen die Ordner `Data`, `PGFplots` und `PNGplots` existieren um Daten abrufen und speichern zu können. Der `Data` Ordner muss hierbei einfach mit den CSV-Dateien aus `Messdaten` gefüllt werden.

Ausgeführt werden die Programme folgendermaßen:
```python name_des_skripts.py [png/pgf]```
`PNG` und `PGF` sind hierbei optional um das Diagramm in das gewünschte Format zu exportieren.

Die fertigen Diagramme können auch direkt unter `Bilder\Plots\PNG` abgerufen werden.