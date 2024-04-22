from flaskr.models.model import Model
from flaskr.utils.card_image import CardImage

class Post(Model):
    PUBLISHED = 1
    ARCHIVED = 0

    def fetch_index(self) -> list:
        return self.db.execute(
            'SELECT posts.id, posts.store_name, posts.title, categories.name as category_name, locations.name as location_name, posts.publish_flag '
            'FROM posts '
            'INNER JOIN categories ON posts.category_id = categories.id '
            'INNER JOIN locations ON posts.location_id = locations.id'
        ).fetchall()

    def store(self, vals: dict) -> None:
        card_image = CardImage

        if 'publish_flag' not in vals:
            vals['publish_flag'] = self.ARCHIVED

        self.db.execute(
            'INSERT INTO posts '
            '(store_name, title, description, body, card_image_path, category_id, location_id, publish_flag) '
            'VALUES(?, ?, ?, ?, ?, ?, ?, ?)',
            (
                vals['store_name'],
                vals['title'],
                vals['description'],
                vals['body'],
                card_image.generate_path(),
                vals['category_id'],
                vals['location_id'],
                vals['publish_flag']
            )
        )
        self.db.commit()


