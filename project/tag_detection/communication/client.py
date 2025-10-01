import requests
import json

class JavaAPIClient:
    def __init__(self, base_url, yard_id):
        self.base_url = base_url
        self.yard_id = yard_id

    def send_detections(self, detections):
        """
        Responsável por enviar as tags detectadas para a API de Java

        Retorna a resposta da API
        """
        url = f"{self.base_url}/yards/{self.yard_id}/tags"
        response = requests.post(url, json=detections)
        return response.json() if response.ok else {"error": response.text}
