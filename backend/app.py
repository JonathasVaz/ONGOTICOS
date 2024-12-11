import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as requisições


# Função para se conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('database/ongoticos.db')  
    conn.row_factory = sqlite3.Row  # Para retornar os resultados como dicionários
    return conn


# Rota para obter todos os animais
@app.route('/api/animals', methods=['GET'])
def get_animals():
    conn = get_db_connection()
    animals = conn.execute('SELECT * FROM animals').fetchall()  # Consultar todos os animais
    conn.close()
    return jsonify([dict(animal) for animal in animals])  # Retorna os animais como uma lista de dicionários

# Rota para adicionar um novo animal
@app.route('/api/animals', methods=['POST'])
def add_animal():
    new_animal = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO animals (name, species, age, enrollment_duration, image_url) VALUES (?, ?, ?, ?, ?)',
        (new_animal['name'], new_animal['species'], new_animal['age'], new_animal['enrollment_duration'], new_animal['image_url'])
    )
    conn.commit()
    conn.close()
    return jsonify(new_animal), 201

# Rota para obter todos os funcionários
@app.route('/api/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    employees = conn.execute('SELECT * FROM employees').fetchall()  # Consultar todos os funcionários
    conn.close()
    return jsonify([dict(employee) for employee in employees])  # Retorna os funcionários como uma lista de dicionários

# Rota para adicionar um novo funcionário
@app.route('/api/employees', methods=['POST'])
def add_employee():
    new_employee = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO employees (name, position, experience_years) VALUES (?, ?, ?)',
        (new_employee['name'], new_employee['position'], new_employee['experience_years'])
    )
    conn.commit()
    conn.close()
    return jsonify(new_employee), 201

# Rota para obter a história de um animal
@app.route('/api/animal_history/<int:animal_id>', methods=['GET'])
def get_animal_history(animal_id):
    conn = get_db_connection()
    animal_history = conn.execute(
        'SELECT * FROM history WHERE animal_id = ?', (animal_id,)
    ).fetchone()
    conn.close()
    if animal_history:
        return jsonify(dict(animal_history))  # Retorna o histórico do animal
    else:
        return jsonify({"message": "History not found for this animal"}), 404

# Rota para rodar o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)
