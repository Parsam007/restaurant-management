# Restaurant Management System

Dieses Python-Projekt ist ein einfaches Restaurant-Verwaltungssystem, das es ermöglicht, Tische zu verwalten, Bestellungen aufzunehmen und Rechnungen zu generieren. Das System verwendet eine Konsolen-Benutzeroberfläche.

## Features

- **Menüverwaltung:** Laden eines Menüs aus einer CSV-Datei.
- **Tischverwaltung:** Hinzufügen und Verwalten von Tischen.
- **Bestellungen:** Hinzufügen von Bestellungen mit Sonderwünschen.
- **Rechnungen:** Generieren und Speichern von Rechnungen als Textdatei.
- **Konsolen-UI:** Interaktive Benutzeroberfläche für die Bedienung.

## Anforderungen

- Python 3.8 oder höher
- Eine CSV-Datei mit Menüinformationen im folgenden Format:
  ```
  Produktname;Kategorie;Beschreibung;Preis
  Pizza Margherita;Pizza;Klassische Pizza;8.50
  Spaghetti Carbonara;Pasta;Pasta mit Sahnesauce;10.00
  ```

## Installation

1. Klone das Repository:

   ```bash
   git clone https://github.com/username/repo.git
   cd repo
   ```

2. Stelle sicher, dass du Python installiert hast:

   ```bash
   python --version
   ```

3. Lege eine CSV-Datei mit den Menüinformationen an und passe den Pfad in der `load_menu`-Methode an.

## Verwendung

1. Starte das Programm:

   ```bash
   python restaurant.py
   ```

2. Wähle eine Option aus dem Hauptmenü:

   - Menü anzeigen
   - Tisch hinzufügen
   - Bestellung hinzufügen
   - Rechnung generieren
   - Programm beenden

3. Folge den Anweisungen in der Konsole, um Bestellungen zu verwalten und Rechnungen zu erstellen.

## Struktur

- **`Produkt`**: Repräsentiert ein Menüprodukt.
- **`Bestellung`**: Speichert Informationen über eine Bestellung.
- **`Tisch`**: Verwalten von Bestellungen an einem bestimmten Tisch.
- **`Restaurant`**: Zentrale Verwaltung des Systems.

## Beispiel

### Menü laden:

```
Menü:
1. Pizza Margherita - 8.50 Euro
2. Spaghetti Carbonara - 10.00 Euro
```

### Bestellung hinzufügen:

```
Tischnummer eingeben: 1
Menü:
1. Pizza Margherita - 8.50 Euro
2. Spaghetti Carbonara - 10.00 Euro
Produktnummer wählen: 1
Sonderwünsche (mit Komma trennen, falls mehrere): Extra Käse
Pizza Margherita wurde zur Bestellung hinzugefügt.
```

### Rechnung generieren:

```
Rechnung für Tisch 1:
1. Pizza Margherita (Extra Käse) - 9.50 €
Gesamt: 9.50 €
```


## Autor

Erstellt von **Parsa Aminian**.

