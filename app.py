from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Configuração do Flask e SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Oferta de frete
class Oferta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    valor_km = db.Column(db.Float)
    valor_carga_descarga = db.Column(db.Float)
    fretadora = db.Column(db.String(100))
    categoria_transporte = db.Column(db.String(100))
    tipo_carga = db.Column(db.String(100))
    eixos = db.Column(db.Integer)
    
# Modelo de Piso como descrito na legislação da ANTT.
class Piso(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    valor_km = db.Column(db.Float)
    valor_carga_descarga = db.Column(db.Float)
    categoria_transporte = db.Column(db.String(100))
    tipo_carga = db.Column(db.String(100))
    eixos = db.Column(db.Integer)


with app.app_context():
    db.create_all()
    db.session.commit()


# Homepage com informações e direcionamentos para outras rotas.
@app.get("/")
def home():
    return render_template("home.html")

# Página com todas as ofertas cadastradas.
@app.get("/ofertas/")
def ofertas_view():
    ofertas_lista = db.session.query(Oferta).order_by(Oferta.fretadora).all()
    return render_template("ofertas.html", ofertas_lista = ofertas_lista)

# Página com form para busca de ofertas
@app.get("/ofertas/busca")
def pesquisar_oferta_view():
    return render_template("ofertas_busca.html")

# Página com resultado de uma busca de ofertas, proveniente de /ofertas/busca.
# Ação do form de /ofertas/busca
@app.post("/ofertas/busca/resultado")
def resultado_pesquisa_oferta_view():
    categoria_transporte = request.form.get("categorias")
    tipo_carga = request.form.get("carga")
    eixos = request.form.get("eixos")
    distancia = request.form.get("distancia")
    # Filtra o banco de dados de Oferta usando as informações do form de busca e ordena pelo valor total
    ofertas_lista = (db.session.query(Oferta)
                        .filter(
                            Oferta.categoria_transporte.like(categoria_transporte),
                            Oferta.tipo_carga.like(tipo_carga),
                            Oferta.eixos.like(eixos)
                        )
                        .order_by((Oferta.valor_km * distancia) + Oferta.valor_carga_descarga)
                        .all()
                    )
    return render_template("ofertas_busca_resultado.html", ofertas_lista = ofertas_lista, distancia = distancia)

# Form de cadastro de ofertas
@app.get("/ofertas/cadastro")
def ofertas_cadastro_view():
    return render_template("ofertas_cadastro.html")

# Ação do form de cadastro de ofertas
# Cadastra a oferta no banco de dados usando os valores do form em /ofertas/cadastro
# Valida Oferta de acordo com Piso de atributos correspondentes
@app.post("/ofertas/cadastro/criar")
def oferta_post():
    fretadora = request.form.get("fretadora")
    categoria_transporte = request.form.get("categorias")
    tipo_carga = request.form.get("carga")
    eixos = request.form.get("eixos")
    valor_km = request.form.get("valor_km")
    valor_carga_descarga = request.form.get("valor_carga_descarga")
    # Valida valores de piso mínimo definidos pela legislação. 
    # Como nem todas validações estão no escopo desse projeto no momento, não impede Ofertas de categorias, tipos e eixos não cadastradas em Piso.
    try:
        piso = getPiso(categoria_transporte=categoria_transporte, tipo_carga=tipo_carga, eixos=eixos)
        if (float(valor_km) < getattr(piso, 'valor_km') or float(valor_carga_descarga) < getattr(piso,'valor_carga_descarga')):
            return render_template("erroANTT.html")
    except:
        print('não foi possível validar a conformidade a legislação desta oferta')
    new_oferta = Oferta(fretadora=fretadora, categoria_transporte=categoria_transporte, tipo_carga = tipo_carga, eixos = eixos, valor_km = valor_km, valor_carga_descarga = valor_carga_descarga)
    db.session.add(new_oferta)
    db.session.commit()
    return redirect(url_for("ofertas_cadastro_view"))

# Página com todas fretadoras cadastradas
@app.get("/fretadoras/")
def fretadoras_view():
    ofertas_lista = db.session.query(Oferta).order_by(Oferta.fretadora).all()
    # .order_by(Oferta.fretadora)
    return render_template("fretadoras.html", ofertas_lista = ofertas_lista)

# As informações de pisos estabelecidas pela ANTT são populadas quando o servidor é ativado. Isso se dá pela natureza efêmera do banco de dados em situações de teste.
# Devido à falta de fatores acessíveis para o cálculo desses valores, eles são inseridos manualmente com a tabela anexa na legislação.
# Como forma de demonstrar a lógica da validação, foram inseridos os pisos para a combinação da primeira categoria de transporte e de carga constantes na legislação.
def getPiso(categoria_transporte, tipo_carga, eixos):
    try:
        piso = (db.session.query(Piso).filter(
                                            Piso.categoria_transporte.like(categoria_transporte),
                                            Piso.tipo_carga.like(tipo_carga),
                                            Piso.eixos.like(eixos)
                                            )
                                        .one()
                )
        return piso
    except:
        print('essa oferta não corresponde a um piso cadastrado')

# Popula os pisos de acordo com a ANTT no banco de dados se ainda não estiverem populados.
def populatePiso():
    with app.app_context():
        if (db.session.query(Piso).first() is not None):
            return
        pisos = {
        Piso(categoria_transporte='Transporte rodoviário de carga lotação', tipo_carga = 'Granel sólido', eixos = 2, valor_km = 3.0908, valor_carga_descarga = 252.70), 
        Piso(categoria_transporte='Transporte rodoviário de carga lotação', tipo_carga = 'Granel sólido', eixos = 3, valor_km = 3.9886, valor_carga_descarga = 300.69),
        Piso(categoria_transporte='Transporte rodoviário de carga lotação', tipo_carga = 'Granel sólido', eixos = 4, valor_km = 4.5346, valor_carga_descarga = 308.26),
        Piso(categoria_transporte='Transporte rodoviário de carga lotação', tipo_carga = 'Granel sólido', eixos = 5, valor_km = 5.2018, valor_carga_descarga = 341.28),
        Piso(categoria_transporte='Transporte rodoviário de carga lotação', tipo_carga = 'Granel sólido', eixos = 6, valor_km = 5.9490, valor_carga_descarga = 381.80),
        Piso(categoria_transporte='Transporte rodoviário de carga lotação', tipo_carga = 'Granel sólido', eixos = 7, valor_km = 6.4105, valor_carga_descarga = 442.25),
        Piso(categoria_transporte='Transporte rodoviário de carga lotação', tipo_carga = 'Granel sólido', eixos = 9, valor_km = 7.3765, valor_carga_descarga = 484.22),
        }
        for piso in pisos:
            db.session.add(piso)
        db.session.commit()

populatePiso()