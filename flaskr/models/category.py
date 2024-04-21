from flaskr.db import get_db

class Category(object):
    def __init__(self) -> None:
        self.db = get_db()

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
