from flaskr.models.model import Model
from flaskr.utils.card_image import CardImage

class Post(Model):
    def store(self, vals: dict) -> None:
        card_image = CardImage

        self.db.execute(
            'INSERT INTO posts'
            '(store_name, title, description, body, card_image_path, category_id, location_id, publish_flag)'
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


