from flask import Flask, redirect, render_template, request, url_for
import sqlite3 as sq

app = Flask(__name__)

# ==== CONNESSIONE DATABASE ====
def get_db():
    conn = sq.connect('preventivi.sqlite3')
    conn.row_factory = sq.Row
    return conn


# ==== HOME: MOSTRA TUTTI I PREVENTIVI ====
@app.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    conn.close()
    return render_template('index.html')


# ==== AGGIUNGI NUOVO PREVENTIVO ====
@app.route('/add', methods=['POST'])
def add_preventivo():
    nomeCliente = request.form.get('nomeCliente')
    cognomeCliente = request.form.get('cognomeCliente')
    nascitaCliente = request.form.get('nascitaCliente')
    codiceFiscale = request.form.get('codiceFiscale')
    tipo = request.form.get('tipo')
    codice = request.form.get('codice')
    descrizione = request.form.get('descrizione')
    unitaMisura = request.form.get('unitaMisura')
    quantita = request.form.get('quantita')
    prezzoUnitario = request.form.get('prezzoUnitario')
    prezzoTotale = request.form.get('prezzoTotale')
    MRprezzoUnitario = request.form.get('MRprezzoUnitario')
    MRprezzoTotale = request.form.get('MRprezzoTotale')
    MRricarico = request.form.get('MRricarico')
    manoRprezzoUnitario = request.form.get('manoRprezzoUnitario')
    manoRprezzoTotale = request.form.get('manoRprezzoTotale')
    manoRricarico = request.form.get('manoRricarico')
    PMprezzoUnitario = request.form.get('PMprezzoUnitario')
    PMprezzoTotale = request.form.get('PMprezzoTotale')
    CMprezzoUnitario = request.form.get('CMprezzoUnitario')
    CMprezzoTotale = request.form.get('CMprezzoTotale')

    conn = get_db()
    cur = conn.cursor()

    cur.execute('''
        INSERT INTO preventivi(
            nomeCliente, cognomeCliente, nascitaCliente, codiceFiscale,
            tipo, codice, descrizione, unitaMisura, quantita, prezzoUnitario, prezzoTotale,
            MRprezzoUnitario, MRprezzoTotale, MRricarico,
            manoRprezzoUnitario, manoRprezzoTotale, manoRricarico,
            PMprezzoUnitario, PMprezzoTotale,
            CMprezzoUnitario, CMprezzoTotale
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        nomeCliente, cognomeCliente, nascitaCliente, codiceFiscale,
        tipo, codice, descrizione, unitaMisura, quantita, prezzoUnitario, prezzoTotale,
        MRprezzoUnitario, MRprezzoTotale, MRricarico,
        manoRprezzoUnitario, manoRprezzoTotale, manoRricarico,
        PMprezzoUnitario, PMprezzoTotale,
        CMprezzoUnitario, CMprezzoTotale
    ))

    conn.commit()
    conn.close()

    return redirect(url_for('index'))


# ==== RICERCA CLIENTE PER NOME E COGNOME ====
@app.route('/search', methods=['GET'])
def search_cliente():
    nome = request.args.get('nomeCliente', '').strip()
    cognome = request.args.get('cognomeCliente', '').strip()

    query = "SELECT * FROM preventivi WHERE 1=1"
    params = []

    if nome:
        query += " AND nomeCliente LIKE ?"
        params.append(f"%{nome}%")

    if cognome:
        query += " AND cognomeCliente LIKE ?"
        params.append(f"%{cognome}%")

    conn = get_db()
    cur = conn.cursor()
    cur.execute(query, params)
    preventivi = cur.fetchall()
    conn.close()

    return render_template('index.html', preventivi=preventivi)


# ==== AVVIO APP ====
if __name__ == '__main__':
    app.run(debug=True)
