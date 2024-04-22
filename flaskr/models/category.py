from flaskr.models.model import Model

class Category(Model):
    def fetch_all(self) -> list:
        return self.db.execute(
            'SELECT * FROM categories'
        ).fetchall()

    def store(self, name: str) -> None:
        self.db.execute(
            'INSERT INTO categories (name) VALUES (?)',
            (name,)
        )
        self.db.commit()
