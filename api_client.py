import requests

from config import BASE_URL

def get(endpoint):
	return requests.get(BASE_URL + endpoint)
