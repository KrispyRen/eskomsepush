import requests
import logging
from decouple import config
import json



class EskomSePush:

    def __init__(self, area_id : str = None):
        self.api_key = config('API_KEY')
        self.area_id = area_id
        self.headers = {"token" : self.api_key}
        self.base_url = config('BASE_URL')

    #used to make the request
    def make_request(self, endpoint: str,  payload : dict = None ) -> None:
        query_url = self.base_url + endpoint
        try:
            response = requests.get(url=query_url, headers=self.headers, params=payload)
            if response.status_code == 200:
                print('successful')
                return response.json()
            if response.status_code == 400:
                print('Bad Request')
            if response.status_code == 403:
                print('Not Authenticated - Token invalid or disabled')
            if response.status_code == 404:
                print('Not Found')
            if response.status_code == 429:
                print('Too many requests - Slow down, this is Africa')
            if response.status_code == 500:
                print('Server side error')
            else:
                print(f'eish, response status code is {response.status_code}')
        except requests.RequestException as e:
            # Exception occurred while making the request
            print(f'Request failed: {e}')

    #search areas - input is str
    def search_areas(self, area_search : str) -> dict:
        payload = {"text": area_search}
        return self.make_request("/areas_search", payload=payload)
    
    #get the area information based on the area_id retrieved from search_areas()
    def get_area_information(self) -> dict:
        payload = {"id": self.area_id, "test" : "current"}
        return self.make_request("/area", payload=payload)

    #check how many credits you have and limit
    def get_allowance(self) -> dict:
        return self.make_request("/api_allowance")

    #get the national schedule
    def get_status(self) -> dict:
        return self.make_request("/status")
    
    #get areas nearby based on latitude and longitude
    def get_areas_nearby(self, lat, lon) -> dict:
        payload = {"lat": lat, "lon": lon}
        return self.make_request("/areas_nearby", payload=payload)

    #get topics nearby created by users
    def get_topics_nearby(self, lat, lon) -> dict:
        payload = {"lat": lat, "lon": lon}
        return self.make_request("/topics_nearby", payload=payload)


