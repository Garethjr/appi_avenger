from models.db import db

class Avenger(db.Model):
    __tablename__= "avenger"
    id=db.Column(db.Integer(),primary_key=True)
    nombre=db.Column(db.String(100),nullable=True)
    alias=db.Column(db.String(100),unique=True,nullable=True)
    habilidades=db.Column(db.Text(100),nullable=True)
    actor=db.Column(db.String(100),nullable=True)


    def serialize(self):
        return {
            "id":self.id,
            "nombre": self.nombre,
            "alias": self.alias,
            "habilidades": self.habilidades,
            "actor": self.actor,
        }