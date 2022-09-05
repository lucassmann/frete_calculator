from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Oferta(db.Model):
    # mudar pra Integer e auto increment quando souber como faz
    id = db.Column(db.String(100), primary_key = True)
    # mudar Integer p decimal para representar dinheiro
    valor_km = db.Column(db.Integer)
    valor_carga_descarga = db.Column(db.Integer)
    # temporario! mudar para cod assim que usuarios de fretador/remetente/destinatario forem implementados
    fretador = db.Column(db.String(100))
    # temporario! mudar para ANTT_piso assim que for implementado com checagem de valores minimos
    categoria_transporte = db.Column(db.String(100))
    tipo_carga = db.Column(db.String(100))
    eixos = db.Column(db.Integer)
    
db.create_all()

@app.get("/")
def home():
    return render_template("fretadora_ofertas_cadastro.html")

@app.get("/cliente/ofertas/pesquisa")
def pesquisar_oferta():
    return render_template("cliente_ofertas_pesquisa.html")

@app.get("/fretadora/ofertas")
def fretadora_ofertas_view():
    return render_template("fretadora_ofertas.html")

@app.get("/fretadora/ofertas/cadastro")
def fretadora_oferta_cadastro_view():
    return render_template("fretadora_ofertas_cadastro.html")

@app.post("/fretadora/ofertas/cadastro/criar")
def oferta_post():
    empresa = request.form.get("empresa")
    categoria_transporte = request.form.get("categorias")
    tipo_carga = request.form.get("carga")
    eixos = request.form.get("eixos")
    valor_km = request.form.get("valor_km")
    valor_carga_descarga = request.form.get("valor_carga_desgarga")
    
    new_oferta = Oferta(id=empresa, categoria_transporte=categoria_transporte, tipo_carga = tipo_carga, eixos = eixos, valor_km = valor_km, valor_carga_descarga = valor_carga_descarga)
    db.session.add(new_oferta)
    db.session.commit()
    return redirect(url_for("home"))




