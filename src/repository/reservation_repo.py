# src/repository/reservation_repo.py

class ReservationRepository:
    def __init__(self, filepath="reservations.txt"):
        self.filepath = filepath

    def load(self):
        try:
            items = []
            with open(self.filepath, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(";")
                    if len(parts) != 3:
                        continue
                    items.append((parts[0], parts[1], parts[2]))
            return items
        except FileNotFoundError:
            return []

    def save(self, reservations):
        with open(self.filepath, "w", encoding="utf-8") as f:
            for u, b, d in reservations:
                f.write(f"{u};{b};{d}\n")
