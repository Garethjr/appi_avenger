from models.db import db
from models.avenger import Avenger
from flask import render_template,redirect,Blueprint,flash,request,url_for

avenger_bp=Blueprint("avnger_bp",__name__)
@avenger_bp.route("/", methods=["GET"])
def get_avenger():
    avenger = Avenger.query.all()
    return render_template("avenger/avenger.html",avengers=avenger)

@avenger_bp.route("/avenger", methods=["POST"])

def add_avenger():
    nombre = request.form["nombre"]
    alias = request.form["alias"]
    habilidades = request.form.get("habilidades","")
    actor = request.form["actor"]
    try:
        nuevo_avenger= Avenger(
            nombre = nombre,
            alias=alias ,
            habilidades=habilidades ,
            actor=actor,
        )
        db.session.add(nuevo_avenger)
        db.session.commit()
        flash("Agente subido con exito","success")
        return redirect(url_for("avenger_bp.get_avenger"))
    except Exception as e:
        db.session.rollback()
        flash(f"error inesperado: {e}","danger")
        return redirect(url_for("avenger_bp.get_avneger"))

@avenger_bp.route("/avenger/edit/<int:id>",methods = ["GET","POST"])

def edit_avenger(id):
    avenger = Avenger.query.get_or_404(id)

    if request.method == "POST":
        nombre = request.form.get("nombre")
        alias= request.form.get("alias")
        habilidades = request.form.get("habilidades","")
        actor= request.form.get("actor")
        try:
            avenger.nombre = nombre
            avenger.alias = alias
            avenger.habilidades=habilidades
            avenger.actor = actor
            flash("avenger actualizado","success")
            db.session.commit()
            return redirect(url_for("avenger_bp.get_avenger"))
        
        except Exception as e:
            db.session.rollback()
            flash(f"error inesperado: {e}","danger")
            return redirect(url_for("avenger_bp.edit_avenger",id=id))
        
    return render_template("agente/edit_avenger.html",avenger=avenger)

@avenger_bp.route("/avenger/delete/<int:id>" ,methods =["POST"])
def delete_avenger(id):
    avenger = Avenger.query.get_or_404(id)
    try:
        db.session.delete(avenger)
        db.session.commit()
        flash("agente eliminado","success")
        return redirect(url_for("avenger_bp.get_avenger"))
    except Exception as e:
        db.session.rollback()
        flash(f"error inesperado {e}","danger")
        return redirect(url_for("avenger_bp.get_avenger"))

