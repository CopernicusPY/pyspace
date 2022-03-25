import requests
import datetime
import colorama
import numpy, io, cv2
from PIL import Image


class PySpace:
    """
    Class object containing methods that allow easy interaction with NASA API.

    Parameters
    ==========
        api_key: string, default -> DEMO_KEY
        API Key received after registration on https://api.nasa.gov/. If None, a limited-access DEMO_KEY is used.

    Attributes
    ==========
    api_key: string, default -> DEMO_KEY
        API Key received after registration on https://api.nasa.gov/. If None, a limited-access DEMO_KEY is used.
    limit_remaining: integer
        Current available API calls

    Methods
    =======
    picture_of_the_day
        Returns data for the NASA APOD (Astronomy Picture of the Day)
    mars_picture
        Returns a mars picture that matches the given data
    track_iss
        returns a tuple of the iss position
    mars_weather
        Returns a list containing dictionaries with the temperature of each martian day (sol)


    """

    def __init__(self, api_key="DEMO_KEY", weather_api_key=None):
        colorama.init(True)

        self.api_key = api_key
        self.weather_api_key = weather_api_key
        self.limit_remaining = None
        print("""
██████╗░██╗░░░██╗░██████╗██████╗░░█████╗░░█████╗░███████╗
██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝░╚████╔╝░╚█████╗░██████╔╝███████║██║░░╚═╝█████╗░░
██╔═══╝░░░╚██╔╝░░░╚═══██╗██╔═══╝░██╔══██║██║░░██╗██╔══╝░░
██║░░░░░░░░██║░░░██████╔╝██║░░░░░██║░░██║╚█████╔╝███████╗
╚═╝░░░░░░░░╚═╝░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝ 
        """)

    def picture_of_the_day(self, date=None, hd=False, count=None):
        """
        Returns data for the NASA APOD (Astronomy Picture of the Day).
        
        Parameters
        ==========
        date: str, datetime.datetime, default -> ``None``
            Earth date on which a photo was taken. (Must be in ``YYYY-MM-DD`` format)
        hd: bool, default -> False 
            If True returns matching high-definision image of the APOD

        count: integer, default -> None 
            If specified, returns ``count`` random images. (Cant be specified when date != None)
        Raises
        ======
        TypeError
            Raised if the parameter ``hd`` is not boolean. 
        HTTPError
            Raised if response fails. (Status code != 200)
        Returns
        =======
        dict 
            Dictionary object of JSON data returned from API.
        """
        params = {
            "api_key": self.api_key,
            "date": date,
            "hd": hd,
            "count": count
        }
        if hd is not None:
            if not isinstance(hd, bool):
                raise TypeError(
                    colorama.Fore.RED+"[Error] <hd> parameter must be a Boolean (True - False)")
        resp = requests.get(
            "https://api.nasa.gov/planetary/apod", params=params)
        if resp.status_code != 200:
            print(colorama.Fore.RED +
                  f"[Error] Status Code: {resp.status_code} ({resp.reason})\n[ERROR] Response: {resp.text}")
            raise requests.exceptions.HTTPError(resp.reason)
        else:
            self.limit_remaining = resp.headers['X-RateLimit-Remaining']
            print(colorama.Fore.GREEN +
                  f"[INFO] Request completed\n[INFO] Status Code: {resp.status_code}\n[INFO] Response:\n{colorama.Fore.WHITE + resp.text}")
            return resp.json()

    def mars_picture(self, rover: str = "Curiosity", sol=None, earth_date: str = None, camera: str = "all", page=1):
        """
        Returns data for the Mars Picture that matches the given data.

        Parameters
        ==========
        rover: str, default -> ``"Curiosity"``
            Rover name to access the database
        sol: int, default -> None
            The sol (Martian rotation or day) on which the photos were taken
        earth_date: str, default -> None 
            Earth date on which a photo/s was taken
        camera: str, default -> ``"all"``
            Return images that got captured on that specific camera. If not specified images from all cameras are returned.
        page: integer, default -> 1
             How many pages of results to return (25 items per page)

        Raises
        ======
        TypeError
            Raised if both sol and earth_date are specified.
        ValueError
            Raised if rover specified is not one of Curiosity Opportunity Spirit or Perseverance
        HTTPError
            Raised if response fails. (When Status code is not ``200``)

        Returns
        =======
        list 
            List containing dictionaries with the JSON data from the Mars Rover API
        """

        params = {
            "api_key": self.api_key,
            "page": page
        }
        if rover.lower() not in ('curiosity', 'opportunity', 'spirit', 'perseverance'):
            raise ValueError(
                colorama.Fore.RED+"[Error] <rover> must be one of the following: Curiosity, Opportunity, Spirit, Perseverance")
        if earth_date != None and sol != None:
            raise TypeError(
                colorama.Fore.RED+"[Error] Bad combination. Either <earth_date> or <sol> can be specified")
        if camera != "all":
            params['camera'] = camera
        if sol != None:
            params['sol'] = sol
        if earth_date != None:
            if not isinstance(earth_date, (str, datetime.datetime)):
                raise TypeError("[Error] Earth date must be in YYYY-MM-DD format.")
            elif isinstance(earth_date, datetime.datetime):
                earth_date = earth_date.strftime("%Y-%m-%d")
            params['earth_date'] = earth_date

        resp = requests.get(
            f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos", params=params)

        if resp.status_code != 200:
            print(colorama.Fore.RED +
                  f"[Error] Status Code: {resp.status_code} ({resp.reason})\n[ERROR] Response: {resp.text}")
            raise requests.exceptions.HTTPError(resp.reason)
        else:
            self.limit_remaining = resp.headers['X-RateLimit-Remaining']
            print(colorama.Fore.GREEN +
                  f"[INFO] Request completed\n[INFO] Status Code: {resp.status_code}\n[INFO] Response:\n{colorama.Fore.WHITE + resp.text}")
            return resp.json()['photos']

    def track_iss(self, live=False, w=1280, h=720):
        """
        Track the current ISS(International Space Station) and get the names of the Astronauts that are currently on-board

        Parameters
        ==========
        display_on_screen: bool, default -> False
            When True, shows the **live** ISS location on a map picture.

        Raises
        ======
        HTTPError
           Raised if response fails. (Status code != 200)

        Returns
        =======
        dict
            Contains a list with the names of the astronauts  that are currently on board, and a list with tuples of the latitude and the longtitude of the ISS.

        """
        result = {
            "people_on_board": [],
            "live_position": []
        }
        resp = requests.get("http://api.open-notify.org/iss-now.json")
        # Error Handling

        ppl_resp = requests.get("http://api.open-notify.org/astros.json")

        if ppl_resp.status_code != 200:
            print(colorama.Fore.RED +
                  f"[Error] Status Code: {ppl_resp.status_code} ({ppl_resp.reason})\n[ERROR] Response: {ppl_resp.text}")
            raise requests.exceptions.HTTPError(ppl_resp.reason)

        if resp.status_code != 200:
            print(colorama.Fore.RED +
                  f"[Error] Status Code: {resp.status_code} ({resp.reason})\n[ERROR] Response: {resp.text}")
            raise requests.exceptions.HTTPError(resp.reason)

        elif ppl_resp.status_code == 200 and resp.status_code == 200:
            for person in ppl_resp.json()['people']:
                result["people_on_board"].append(person['name'])

            result["longitude"] = float(
                resp.json()["iss_position"]["longitude"])
            result["latitude"] = float(resp.json()["iss_position"]["latitude"])
            print(colorama.Fore.GREEN +
                  f"[INFO] Request completed\n[INFO] Status Code: {resp.status_code}\n[INFO] Response:\n{colorama.Fore.WHITE + str(result)}")

        if live:
            while True:
                # Get live position of ISS
                resp = requests.get("http://api.open-notify.org/iss-now.json")
                lat, lon = float(resp.json()["iss_position"]["latitude"]), float(
                    resp.json()["iss_position"]["longitude"])
                result["live_position"].append((lat, lon))
                print(result['live_position'])

        return result

    def mars_weather(self, version=1.0):
        """
        Returns per Sol data for each of the last seven available Sols.

        Parameters
        ==========

        version: integer, default -> 1.0
            Version of the Insights(Mars Weather Data) API

        Raises
        ======

        HTTPError
            Raised if response fails. (When Status code is not ``200``)
        TypeError
            Raised if ``<version>`` argument is not an integer

        Returns
        =======

        list[dict, ...]
            List object containing dictionaries with data for each sol.(sol, average temp, min temp and max temp) in Celcius.

        """
        params = {
            "api_key": self.api_key,
            "ver": version,
            "feedtype": "json"
        }
        resp = requests.get(
            "https://api.nasa.gov/insight_weather/", params=params)
        if not isinstance(version, (int, float)):
            raise TypeError("API Version must be an integer or a float.")

        if resp.status_code != 200:
            print(colorama.Fore.RED +
                  f"[Error] Status Code: {resp.status_code} ({resp.reason})\n[ERROR] Response: {resp.text}")
            raise requests.exceptions.HTTPError(resp.reason)
        else:
            sols = resp.json()['sol_keys']
            result = []
            for sol in sols:
                sol_info = resp[sol].get('AT')

                result.append({
                    "sol": sol,
                    "average_temperature": float(sol_info['av'] - 32) * (5/9),
                    "minimum_temperature": float(sol_info['mn'] - 32) * (5/9),
                    "maximum_temperature": float(sol_info['mx']-32) * (5/9)
                })

            print(colorama.Fore.GREEN +
                  f"[INFO] Request completed\n[INFO] Response:\n{colorama.Fore.WHITE + str(result)}")
            return result

    def earth_weather(self, location, ugroup="us", start_date='', end_date='', c_type="json"):
        """
        Returns information about the weather of a location in the specified date range, with the specified content type (csv, json etc.).

        Parameters
        ==========
        location: str
        ugroup: str
        start_date: str
        end_date: str
        c_type: str

        Raises
        ======

        HTTPError
            Raised if response fails. (When Status code is not ``200``)
        TypeError
            Raised if ``<location>``, ``<ugroup>``, ``<start_date>``, ``<end_date`` or ``<c_type`` are not ``str``
        TypeError
            Raised if self.weather_api_key is ``None``
        Returns
        =======

        dict
            Dictionary object with JSON data containing information about the weather of the specified location on the specified date range (``start_date`` - ``end_date``)
        """
        if self.weather_api_key is not None:
            for i in [location, ugroup, start_date, end_date, c_type]:
                if not isinstance(i, str):
                    raise TypeError(f"[Error] Expected <class 'str'> got {type(i)}")
                
            params = {
                "key": self.weather_api_key,
                "unitGroup": ugroup,
                "contentType": c_type,
                "include": "days",
            }
            if start_date != '': params["StartDate"] = start_date 
            if end_date != '': params["EndDate"] = end_date

            resp = requests.get(
                f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}', params=params)
            
            if resp.status_code != 200:
                print(colorama.Fore.RED +
              f"[Error] Status Code: {resp.status_code} ({resp.reason})\n[ERROR] Response: {resp.text}")
                raise requests.exceptions.HTTPError(resp.reason)
            else:
                print(colorama.Fore.GREEN +
                  f"[INFO] Request completed\n[INFO] Response:\n{colorama.Fore.WHITE + str(resp.text)}")
                return resp.json()

        else:
            raise TypeError("[Error] <weather_api_key> is missing.")
        #API_KEY = ZDJ7P2WBY2KEZ7A3LHNMDZGLK
    def earth_imagery(self, lat, lon, dim=0.025, date=None,display=True, cloud_score=False, save_as=None):
        """
        Returns numpy array of pixel values for image that matches given data.


        Parameters
        ==========
        lat: float/int, default -> n/a

        lon: float/int, default -> n/a

        dim: float/int, default -> 0.025

        date: string, default -> None
        
        display: boolean, default -> True

        cloud_score: boolean, default -> False

        save_as: string, default -> None

        Raises
        ======
        HTTPError
            Raised if response fails. (Status code != 200)

        TypeError
            Raised if <cloud_score< is not boolean, 
            Raised if <lat> is not an integer or float
            Raised if <lon> >>>     >>>    >>> 
            Raised if <dim> >>>     >>>    >>>
            Raised if <date> is not a string representing a date in YYYY-MM-DD format or a datetime object
        
        ValueError
            Raised if <lat> is out of range (-90 - 90)
            Raise if <lon> is out of range (-180 - 180)

        Returns
        =======
        tuple
            tuple containing a numpy.ndarray with the pixel values of the matching image and the URL for the specified image
        """
        #Argument Error Handling
        if not isinstance(cloud_score, bool):
            raise TypeError('[Error] <cloud_score> must be boolean')
        if not isinstance(lat, (int, float)):
            raise TypeError('[Error] <lat> must be an int or float')
        if not isinstance(lon, (int, (int,float))):
            raise TypeError('[Error] <lon> must be an int or float')
        if not isinstance(dim, (float, int)):
            raise TypeError('[Error] <dim> must be a int or float')

        if not -90 <= lat <= 90:
            raise ValueError('[Error] latitudes range from -90 to 90')
        if not -180 <= lon <= 180:
            raise ValueError('[Error] longitudes range from -180 to 180')
        if date is not None:
            if not isinstance(date, (str, datetime.datetime)):
                raise TypeError('[Error] date must be either a string representing a date in YYYY-MM-DD format or a datetime object')
            if isinstance(date, datetime.datetime):
                date = date.strftime('%Y-%m-%d')

        params = {
            'lon': lon,
            'lat': lat,
            'dim': dim,
            'date': date,
            'cloud_score': cloud_score,
            'api_key': self.api_key
        }

        resp = requests.get("https://api.nasa.gov/planetary/earth/imagery",params=params)

        if resp.status_code != 200:
            print(colorama.Fore.RED + f"[Error] Status Code: {resp.status_code} ({resp.reason})\n[ERROR] Response: {resp.text}")
            raise requests.exceptions.HTTPError(resp.reason)
        else:
            self.limit_remaining = resp.headers['X-RateLimit-Remaining']
            print(colorama.Fore.GREEN +
                f"[INFO] Request completed\n[INFO] Status Code: {resp.status_code}\n[INFO] Response URL: {colorama.Fore.WHITE + str(resp.url)}")
            
            
            img = Image.open(io.BytesIO(resp.content))
            if save_as is not None:
                img.save(str(save_as))
            img, array = numpy.array(img), numpy.array(img)
            if display:
                img = cv2.resize(numpy.uint8(img), (450, 450))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                cv2.imshow("Earth Imagery",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            return array, resp.url
           
    def nasa_library(self, query="moon", nasa_id=None, mode="search"):
        
        if mode in ["search", "asset", "metadata", "captions"]:
            endpoint = mode
        else: 
            raise ValueError(colorama.Fore.RED + f'[Error] <mode> must be one of {colorama.Fore.WHITE + str(["search", "asset", "metadata", "captions"])}')

        resp = requests.get(f"https://images-api.nasa.gov/{endpoint}", params={"q":query} if mode == "search" else nasa_id)
        
        if resp.status_code != 200:
            print(colorama.Fore.RED + f"[Error] Status Code: {resp.status_code} ({resp.reason})\n[ERROR] Response: {resp.text}")
            raise requests.exceptions.HTTPError(resp.reason)
        else:
            print(colorama.Fore.GREEN +
                f"[INFO] Request completed\n[INFO] Status Code: {resp.status_code}\n[INFO] Response: {colorama.Fore.WHITE + str(resp.text)}\n\n[INFO] Response URL: {colorama.Fore.WHITE + resp.url}")
            
            return (resp.json(), resp.url)
