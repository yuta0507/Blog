from flaskr.models.model import Model

class Location(Model):
    def fetch_all(self) -> list:
        return self.db.execute(
            'SELECT * FROM locations'
        ).fetchall()

    def fetch_names(self) -> list:
        return self.db.execute(
            'SELECT name FROM categories'
        ).fetchall()

    def store(self, name: str) -> None:
        self.db.execute(
            'INSERT INTO locations (name) VALUES (?)',
            (name,)
        )
        self.db.commit()
