from flask import Flask, request, jsonify
from app.controllers.products_service_controller import NumberController


app = Flask(__name__)
number_controller = NumberController()


@app.route('/add_number', methods=['POST'])
def add_number():
    data = request.json
    number = data['number']
    number_controller.add_number(number)
    return jsonify({'message': 'Number added successfully'}), 201


@app.route('/get_number/<int:number>', methods=['GET'])
def get_number(number):
    result = number_controller.get_number(number)
    if result is not None:
        return jsonify({'value': result})
    else:
        return jsonify({'error': 'Number not found'}), 404


@app.route('/get_all_numbers', methods=['GET'])
def get_all_numbers():
    return jsonify({'collection': number_controller.get_all_numbers()})


@app.route('/update_number/<int:number>', methods=['PUT'])
def update_number(number):
    data = request.json
    updated_number = data['number']
    if number_controller.update_number(number, updated_number):
        return jsonify({'message': 'Number updated successfully'}), 200
    else:
        return jsonify({'error': 'Number not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
