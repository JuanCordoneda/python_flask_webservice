import unittest
import json
from app import app
from app.controllers.number_controller import NumberController

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.number_controller = NumberController()

    def test_add_number(self):
        # Prueba agregar un número a la colección
        response = self.app.post('/add_number', data=json.dumps({'number': 15}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.number_controller.get_number(15), 'Type 3')

    def test_get_number(self):
        # Agrega un número a la colección antes de la prueba
        self.number_controller.add_number(10)

        # Prueba obtener un número específico
        response = self.app.get('/get_number/10')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['value'], 'Type 2')

    def test_get_number_not_found(self):
        # Prueba obtener un número que no está en la colección
        response = self.app.get('/get_number/999')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['error'], 'Number not found')

    def test_get_all_numbers(self):
        # Agrega varios números a la colección antes de la prueba
        self.number_controller.add_number(6)
        self.number_controller.add_number(9)
        self.number_controller.add_number(25)

        # Prueba obtener todos los números de la colección
        response = self.app.get('/get_all_numbers')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(data['collection']), 3)

    def test_update_number(self):
        # Agrega un número a la colección antes de la prueba
        self.number_controller.add_number(7)

        # Prueba actualizar un número existente
        response = self.app.put('/update_number/7', data=json.dumps({'number': 12}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.number_controller.get_number(7), 'Type 1')

    def test_update_number_not_found(self):
        # Prueba actualizar un número que no está en la colección
        response = self.app.put('/update_number/999', data=json.dumps({'number': 20}), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['error'], 'Number not found')


if __name__ == '__main__':
    unittest.main()