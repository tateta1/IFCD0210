from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventario (
        producto TEXT,
        cantidad INTEGER
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()

    if request.method == "POST":
        producto = request.form["producto"]
        cantidad = request.form["cantidad"]
        cursor.execute("INSERT INTO inventario VALUES (?, ?)", (producto, cantidad))
        conn.commit()

    cursor.execute("SELECT * FROM inventario")
    datos = cursor.fetchall()
    conn.close()

    return render_template("index.html", datos=datos)

if __name__ == "__main__":
    app.run(debug=True)