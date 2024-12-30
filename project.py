import csv

class Produkt:
    """Repräsentiert ein Produkt im Menü."""

    def __init__(self, name: str, price: float):
        """
        Initialisiert ein Produkt mit einem Namen und einem Preis.

        Args:
            name (str): Der Name des Produkts.
            price (float): Der Preis des Produkts.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """Gibt eine lesbare Darstellung des Produkts zurück."""
        return f"{self.name} - {self.price:.2f} Euro"


class Bestellung:
    """Repräsentiert eine Bestellung, die ein Produkt und Sonderwünsche enthält."""

    def __init__(self, product: Produkt, special_requests=None):
        """
        Initialisiert eine Bestellung mit einem Produkt und optionalen Sonderwünschen.

        Args:
            product (Produkt): Das bestellte Produkt.
            special_requests (list, optional): Eine Liste von Sonderwünschen. Standard ist None.
        """
        if special_requests is None:
            special_requests = []
        self.product = product
        self.special_requests = special_requests
        self.total_price = self.calculate_price()

    def calculate_price(self):
        """
        Berechnet den Gesamtpreis der Bestellung basierend auf dem Produktpreis und den Sonderwünschen.

        Returns:
            float: Der Gesamtpreis der Bestellung.
        """
        extra_count = 0
        for request in self.special_requests:
            if "extra" in request.lower():
                extra_count += 1
        return self.product.price + extra_count

    def __str__(self):
        """Gibt eine lesbare Darstellung der Bestellung zurück."""
        requests = ", ".join(self.special_requests) if self.special_requests else "Keine"
        return f"{self.product.name} ({requests}) - {self.total_price:.2f} Euro"


class Tisch:
    """Repräsentiert einen Tisch im Restaurant."""

    def __init__(self, table_number: int):
        """
        Initialisiert einen Tisch mit einer Tischnummer.

        Args:
            table_number (int): Die Nummer des Tisches.
        """
        self.table_number = table_number
        self.orders = []

    def add_order(self, order: Bestellung):
        """
        Fügt eine Bestellung zum Tisch hinzu.

        Args:
            order (Bestellung): Die hinzuzufügende Bestellung.
        """
        self.orders.append(order)

    def remove_order(self, order_index: int):
        """
        Entfernt eine Bestellung vom Tisch.

        Args:
            order_index (int): Der Index der zu entfernenden Bestellung.
        """
        if 0 <= order_index < len(self.orders):
            self.orders.pop(order_index)
        else:
            print("Ungültige Bestellnummer!")

    def get_total_price(self):
        """
        Berechnet den Gesamtpreis aller Bestellungen am Tisch.

        Returns:
            float: Der Gesamtpreis aller Bestellungen.
        """
        total_price = 0
        for order in self.orders:
            total_price += order.total_price
        return total_price

    def __str__(self):
        """Gibt eine lesbare Darstellung des Tisches und seiner Bestellungen zurück."""
        order_details = "\n".join(f"{i + 1}. {order}" for i, order in enumerate(self.orders))
        return f"Rechnung\nTisch {self.table_number}:\n{order_details}\nGesamt: {self.get_total_price():.2f} €"


class Restaurant:
    """Repräsentiert ein Restaurant mit Tischen und einem Menü."""

    def __init__(self):
        """Initialisiert ein Restaurant mit leeren Tischen und einem leeren Menü."""
        self.tables = {}
        self.menu = []

    def load_menu(self, file_path: str):
        """
        Lädt das Menü aus einer CSV-Datei.

        Args:
            file_path (str): Der Pfad zur CSV-Datei.
        """
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=';')
                next(reader, None)
                for row in reader:
                    if len(row) >= 4:
                        name = row[0].strip()
                        try:
                            price = float(row[3].strip())
                            self.menu.append(Produkt(name, price))
                        except ValueError:
                            print(f"Ungültiger Preis in Zeile: {row}")
                    else:
                        print(f"Ungültige Zeile: {row}")
        except FileNotFoundError:
            print("Menüdaten nicht gefunden!")

    def add_table(self, table_number: int):
        """
        Fügt einen Tisch zum Restaurant hinzu.

        Args:
            table_number (int): Die Nummer des hinzuzufügenden Tisches.
        """
        if table_number not in self.tables:
            self.tables[table_number] = Tisch(table_number)

    def get_table(self, table_number: int):
        """
        Gibt den Tisch mit der angegebenen Nummer zurück.

        Args:
            table_number (int): Die Nummer des Tisches.

        Returns:
            Tisch: Der Tisch mit der angegebenen Nummer oder None, wenn der Tisch nicht existiert.
        """
        return self.tables.get(table_number)

    def generate_bill(self, table_number: int, file_path: str):
        """
        Generiert eine Rechnung für einen Tisch und speichert sie in einer Datei.

        Args:
            table_number (int): Die Nummer des Tisches.
            file_path (str): Der Pfad zur Datei, in der die Rechnung gespeichert werden soll.
        """
        table = self.get_table(table_number)
        if table:
            with open(file_path, mode="w", encoding="utf-8") as file:
                file.write(str(table))
            print(f"Rechnung für Tisch {table_number} gespeichert unter {file_path}")
        else:
            print("Tisch nicht gefunden!")

    def console_ui(self):
        """Startet die Konsolen-Benutzeroberfläche des Restaurant-Verwaltungssystems."""
        print("Willkommen im Restaurant-Verwaltungssystem!")
        print("Geben Sie 'exit' ein, um das Programm zu beenden.\n")

        while True:
            print("\nHauptmenü:")
            print("1. Menü anzeigen")
            print("2. Tisch hinzufügen")
            print("3. Bestellung hinzufügen")
            print("4. Rechnung generieren")
            print("5. Programm beenden")

            choice = input("Wählen Sie eine Option: ").strip()

            if choice == "1":
                print("\nMenü:")
                for produkt in self.menu:
                    print(produkt)

            elif choice == "2":
                try:
                    table_number = int(input("Tischnummer eingeben: "))
                    self.add_table(table_number)
                    print(f"Tisch {table_number} wurde hinzugefügt.")
                except ValueError:
                    print("Ungültige Eingabe! Bitte geben Sie eine gültige Zahl ein.")

            elif choice == "3":
                try:
                    table_number = int(input("Tischnummer eingeben: "))
                    table = self.get_table(table_number)
                    if table:
                        print("\nMenü:")
                        for i, produkt in enumerate(self.menu):
                            print(f"{i + 1}. {produkt}")
                        produktwahl = int(input("Produktnummer wählen: ")) - 1
                        if 0 <= produktwahl < len(self.menu):
                            produkt = self.menu[produktwahl]
                            special_requests = input("Sonderwünsche (mit Komma trennen, falls mehrere): ").split(',')
                            bestellung = Bestellung(produkt, [req.strip() for req in special_requests])
                            table.add_order(bestellung)
                            print(f"{produkt.name} wurde zur Bestellung hinzugefügt.")
                        else:
                            print("Ungültige Produktnummer!")
                    else:
                        print("Tischnummer nicht gefunden!")
                except ValueError:
                    print("Ungültige Eingabe! Bitte versuchen Sie es erneut.")

            elif choice == "4":
                try:
                    table_number = int(input("Tischnummer eingeben: "))
                    file_path = input("Dateipfad für die Rechnung (z. B. 'rechnung.txt'): ").strip()
                    self.generate_bill(table_number, file_path)
                except ValueError:
                    print("Ungültige Eingabe! Bitte versuchen Sie es erneut.")

            elif choice == "5" or choice.lower() == "exit":
                print("Programm wird beendet. Auf Wiedersehen!")
                break

            else:
                print("Ungültige Auswahl! Bitte versuchen Sie es erneut.")


if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.load_menu("/Users/parsaaminian/Desktop/Projekt_mehdi_Parsa/food.csv")
    restaurant.console_ui()

