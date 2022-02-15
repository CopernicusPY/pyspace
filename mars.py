import requests, json, random

class MARS:
    def __init__(self, api_key="DEMO_KEY"):
        self.api_key = api_key
    def latest_mars_picture(self):
        params={
            "api_key":self.api_key
        }
        resp = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos",params=params).json()

        return resp['latest_photos']
    def get_picture(self,rover, sol=0, earth_date=None, camera=None,page=0):
        params ={
            "api_key":self.api_key,
            "sol":sol, 
            "earth_date":earth_date,
            "page":page, 
            "camera":camera
        }
        resp = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/latest_photos",params=params).json()
        return resp
