# app/services/product_service.py
import requests
from app.repositories.product_repository import ProductRepository

class ProductService:
        # Implementa la lógica para obtener todos los productos
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def get_all_products(self):
        try:
            # Realiza una solicitud GET a la API externa para obtener productos
            response = requests.get(f"{self.api_base_url}/products")
            
            if response.status_code == 200:
                # La solicitud fue exitosa, devuelve los datos en formato JSON
                return response.json()
            else:
                # Maneja errores de la API externa
                response_data = response.json() if response.headers.get('content-type') == 'application/json' else response.text
                raise Exception(f"Error en la API externa: {response.status_code}, {response_data}")
        except Exception as e:
            # Maneja errores de red u otros errores
            raise Exception(f"Error al obtener productos de la API externa: {str(e)}")


    # Define otros métodos de servicio para productos
