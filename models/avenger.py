from models.db import db

class Avenger(db.Model):
    nombre=db.Column(db.String)
    alias=db.Column()
    habilidades=db
    actor=db.Column()