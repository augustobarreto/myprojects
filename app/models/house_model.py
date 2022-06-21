from extensions import db
from .immobile_model import Immobile


class House(Immobile):
    __tablename__ = "houses"

    id = db.Column(db.String, db.ForeignKey("immobiles.id"), primary_key=True)

    backyard = db.Column(db.Boolean, default=True)
    pool = db.Column(db.Boolean, default=False)


    __mapper_args__ = {"polymorphic_identity": "houses"}

    def __init__(self, description, value, area, is_available, backyard, pool):
        super().__init__(description, value, area, is_available)
        self.backyard = backyard
        self.pool = pool
        