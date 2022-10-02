from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Oferta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # mudar Integer p decimal para representar dinheiro
    valor_km = db.Column(db.Integer)
    valor_carga_descarga = db.Column(db.Integer)
    # temporario! mudar para cod assim que usuarios de fretador/remetente/destinatario forem implementados
    fretadora = db.Column(db.String(100))
    # temporario! mudar para ANTT_piso assim que for implementado com checagem de valores minimos
    categoria_transporte = db.Column(db.String(100))
    tipo_carga = db.Column(db.String(100))
    eixos = db.Column(db.Integer)
    # implementar CNPJ!!!!!
    
db.create_all()

@app.get("/")
def home():
    return render_template("fretadora_ofertas_cadastro.html")

@app.get("/ofertas/busca")
def pesquisar_oferta_view():
    return render_template("ofertas_busca.html")

@app.get("/ofertas/")
def ofertas_view():
    ofertas_lista = db.session.query(Oferta).all()
    return render_template("ofetas.html", ofertas_lista = ofertas_lista)

@app.get("/fretadora/")
def fretadoras_view():
    ofertas_lista = db.session.query(Oferta).all()
    return render_template("fretadora.html", ofertas_lista = ofertas_lista)

@app.get("/ofertas/cadastro")
def ofertas_cadastro_view():
    return render_template("ofertas_cadastro.html")

@app.post("/ofertas/cadastro/criar")
def oferta_post():
    fretadora = request.form.get("fretadora")
    categoria_transporte = request.form.get("categorias")
    tipo_carga = request.form.get("carga")
    eixos = request.form.get("eixos")
    valor_km = request.form.get("valor_km")
    valor_carga_descarga = request.form.get("valor_carga_desgarga")
    
    new_oferta = Oferta(fretadora=fretadora, categoria_transporte=categoria_transporte, tipo_carga = tipo_carga, eixos = eixos, valor_km = valor_km, valor_carga_descarga = valor_carga_descarga)
    db.session.add(new_oferta)
    db.session.commit()
    return redirect(url_for("ofertas_cadastro_view"))



