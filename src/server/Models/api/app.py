from flask import Flask, request
from llm.atom_generator import atomGenerator

import json
import sqlite3 as sql

app = Flask(__name__)

def conn(db_path):
    con = sql.connect(db_path)
    return con.cursor()

@app.route('/ATOM', methods=['GET'])
def generateAtom():
    headers = {key: value for key, value in request.headers.items()}

    # atom_description = headers["Atom-Description"]
    atom_description = request.args.get("atom-description")

    llm_response = atomGenerator(atom_description)

    return {
        "Atom": llm_response
    }    

@app.route('/ADD_ATOM', methods=['POST'])
def addUser():
    headers = {key: value for key, value in request.headers.items()}

    #obs: para buscar por ID, usar rowid
    desc = request.args.get("desc")
    img = request.args.get("img")
    code = request.args.get("code")
    pid = request.args.get("pid")

    cur = conn("../../db/atoms.db")
    cur.execute("INSERT INTO atoms VALUES('{desc}, {img}, {code}, {pid}')")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

