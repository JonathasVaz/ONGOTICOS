from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as requisições

# Banco de dados simples em memória (listas)
# Animais
# Banco de dados simples em memória (lista)
animals = [
    {"id": 1, "name": "Lola", "species": "Cobra", "age": 2, "enrollment_duration": 6, "image_url": "http://localhost:5000/images/lola.jpg"},
    {"id": 2, "name": "Bob", "species": "Camaleão", "age": 4, "enrollment_duration": 12, "image_url": "http://localhost:5000/images/bob.jpg"},
    {"id": 3, "name": "Mia", "species": "Iguana", "age": 3, "enrollment_duration": 9, "image_url": "http://localhost:5000/images/mia.jpg"}
]


# Funcionários
employees = [
    {"id": 1, "name": "Carlos", "position": "Veterinário", "experience_years": 5},
    {"id": 2, "name": "Ana", "position": "Tratadora de Animais", "experience_years": 8},
    {"id": 3, "name": "Lucas", "position": "Cuidador", "experience_years": 3}
]

# Histórico dos animais
history = [
    {"animal_id": 1, "history": "Lola foi resgatada de um comércio ilegal de animais de estimação. Ela está no zoológico há 2 anos."},
    {"animal_id": 2, "history": "Bob foi encontrado ferido na natureza e recebeu atendimento médico. Ele está aqui há 4 anos."},
    {"animal_id": 3, "history": "Mia nasceu no zoológico e vive aqui toda a sua vida."}
]


# Rota para obter todos os animais
@app.route('/api/animals', methods=['GET'])
def get_animals():
    return jsonify(animals)

# Rota para adicionar um novo animal
@app.route('/api/animals', methods=['POST'])
def add_animal():
    new_animal = request.get_json()
    new_animal['id'] = len(animals) + 1  # Gerar um id único
    animals.append(new_animal)
    return jsonify(new_animal), 201

# Rota para obter todos os funcionários
@app.route('/api/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# Rota para adicionar um novo funcionário
@app.route('/api/employees', methods=['POST'])
def add_employee():
    new_employee = request.get_json()
    new_employee['id'] = len(employees) + 1  # Gerar um id único
    employees.append(new_employee)
    return jsonify(new_employee), 201

# Rota para obter a história de um animal
@app.route('/api/animal_history/<int:animal_id>', methods=['GET'])
def get_animal_history(animal_id):
    animal_history = next((h for h in history if h['animal_id'] == animal_id), None)
    if animal_history:
        return jsonify(animal_history)
    else:
        return jsonify({"message": "History not found for this animal"}), 404

# Rota para rodar o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)
