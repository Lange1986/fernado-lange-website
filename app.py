from flask import Flask, jsonify, render_template

app = Flask(__name__)

CONTACTOS = [

    { 'id': 1, 
     'nome': 'Lange', 
     'celular': '865890288',
     'email': 'lange86@gmail.com',
     'profissão': 'Engenheiro de Software'
    },

    { 'id': 2,
     'nome': 'Pedro',
     'celular': '845890288',
     'email': 'pedro86@gmail.com',
     'profissão': 'Engenheiro Backend'
    },

    { 'id': 3,
     'nome': 'Kendrick',
     'celular': '875890288',
     'email': 'ken86@gmail.com',
     'profissão': 'Engenheiro de Frontend'
     
    }
]


@app.route("/")
def hello():
    return render_template("home.html", contactos=CONTACTOS)


@app.route("/api/contactos")
def lista_contactos():
    return jsonify(CONTACTOS)



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    
  

