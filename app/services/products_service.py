# app/services/products_service.py
import requests

class ProductsService:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def get_all_products(self):
        try:
            response = requests.get(f"{self.api_base_url}/posts")  # products == posts (json fake de pruebas)
            
            if response.status_code == 200:
                return response.json()
            else:
                response_data = response.json() if response.headers.get('content-type') == 'application/json' else response.text
                raise Exception(f"Error in the external API: {response.status_code}, {response_data}")
        except Exception as e:
            raise Exception(f"Error fetching products from the external API: {str(e)}")

    def get_product_by_id(self, product_id):
        try:
            response = requests.get(f"{self.api_base_url}/posts/{product_id}")
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return None  # Product not found
            else:
                response_data = response.json() if response.headers.get('content-type') == 'application/json' else response.text
                raise Exception(f"Error in the external API: {response.status_code}, {response_data}")
        except Exception as e:
            raise Exception(f"Error fetching product from the external API: {str(e)}")

    def create_product(self, data):
        try:
            response = requests.post(f"{self.api_base_url}/posts", json=data)
            
            if response.status_code == 201:
                return response.json()
            else:
                response_data = response.json() if response.headers.get('content-type') == 'application/json' else response.text
                raise Exception(f"Error in the external API: {response.status_code}, {response_data}")
        except Exception as e:
            raise Exception(f"Error creating a product in the external API: {str(e)}")

    def update_product(self, product_id, data):
        try:
            response = requests.put(f"{self.api_base_url}/posts/{product_id}", json=data)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return None  # Product not found
            else:
                response_data = response.json() if response.headers.get('content-type') == 'application/json' else response.text
                raise Exception(f"Error in the external API: {response.status_code}, {response_data}")
        except Exception as e:
            raise Exception(f"Error updating the product in the external API: {str(e)}")

    def delete_product(self, product_id):
        try:
            response = requests.delete(f"{self.api_base_url}/posts/{product_id}")
            
            if response.status_code == 200:
                return True  # Product deleted successfully
            elif response.status_code == 404:
                return False  # Product not found
            else:
                response_data = response.json() if response.headers.get('content-type') == 'application/json' else response.text
                raise Exception(f"Error in the external API: {response.status_code}, {response_data}")
        except Exception as e:
            raise Exception(f"Error deleting the product in the external API: {str(e)}")
