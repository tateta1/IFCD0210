from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulación de Base de Datos (en memoria)

tasks = [
    {"id": 1, "titulo": "Aprender Flask", "completada": False},
    {"id": 2, "titulo": "Diseñar una API", "completada": True}
]

# 1. Obtener tareas (GET)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tareas": tasks}), 200

# 2. Crear tarea (POST)

@app.route('/tasks', methods=['POST'])
def create_task():
    nueva_tarea = {
        "id": len(tasks) + 1,
        "titulo": request.json.get('titulo'),
        "completada": False
    }
    tasks.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

# 3. Actualizar tarea (PUT)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tarea = next((t for t in tasks if t['id'] == task_id), None)
    if tarea:
        tarea['titulo'] = request.json.get('titulo', tarea['titulo'])
        tarea['completada'] = request.json.get('completada', tarea['completada'])
        return jsonify(tarea)
    return jsonify({"error": "Tarea no encontrada"}), 404

# 4. Eliminar tarea (DELETE)
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({"mensaje": "Tarea eliminada"}), 200

if __name__ == '__main__':
    app.run(debug=True)