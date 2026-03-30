from flask import Flask, jsonfy
import mysql.connector
import config

app = Flask(__name__)

usuarios = {
    1: {"nombre":"Paco","edad":44},
    2: {"nombre":"Ana","edad":22}
}

@app.route('/usuarios/<int_id_usuarios>')