import requests, json , datetime
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError

class EARTH:
    def __init__(self, api_key="DEMO_KEY") -> None:
        self.api_key = api_key
    today = str(datetime.datetime.today().strftime('%Y-%m-%d'))
    
    def get_image(self,
        lat: float, lon: float, date: str = None, 
        dim: float = 0.15, info: bool = False) -> Image.Image:

        if not date:
            date = datetime.datetime.today().strftime(r'%Y-%m-%d')
        if lat < -90 or lat > 90:
            raise Exception("Latitudes range from 0 to 90",)
        if lon < -180 or lon > 180:
            raise Exception("Longtitudes range from -180 - 180")
        params = {
            "api_key":self.api_key,
            "lat":lat,
            "lon":lon,
            "date":date,
            "dim":dim 
        }
        resp = requests.get("https://api.nasa.gov/planetary/earth/assets", params=params)
        print(json.loads(resp.text))
