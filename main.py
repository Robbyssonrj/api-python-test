from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de tarefas inicial
tasks = []

# Rota para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Rota para adicionar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.json.get('task')
    if new_task:
        tasks.append(new_task)
        return jsonify({'message': 'Tarefa adicionada com sucesso!'})
    else:
        return jsonify({'error': 'Falta o campo "task" no corpo da solicitação'}), 400

if __name__ == '__main__':
    app.run(debug=True)
