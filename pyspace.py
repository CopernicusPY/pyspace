import requests, datetime, colorama

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
    
    """
    def __init__(self, api_key="DEMO_KEY"):
        colorama.init(True)

        self.api_key = api_key 
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
        date: string, datetime object, default -> None
        hd: bool, default -> False 
            If True returns matching high-definision image of the APOD
        count: integer, default -> None 
            If specified, returns <count> random images. (Cant be specified when date != None)
        Raises
        ======
        TypeError
            Raised if the parameter <hd> is not boolean. 
        HTTPError
            Raised if response fails. (Status code != 200)

        Returns
        =======
        dict 
            Dictionary object of JSON data returned from API.
        
        Usage Examples
        ==============

        #Initialize PySpace Class with a DEMO_KEY
        >>> apod = PySpace() 
        # Returns the APOD of given date (2022-01-01) with the hd URL.
        >>> apod.picture_of_the_day('2022-01-01', hd=True) 
        """
        params = {
            "api_key":self.api_key,
            "date":date,
            "hd":hd,
            "count":count
        }
        if hd is not None:
            if not isinstance(hd, bool):
                raise TypeError(colorama.Fore.RED+"<hd> parameter must be a Boolean (True - False)")
        resp = requests.get("https://api.nasa.gov/planetary/apod", params=params)
        if resp.status_code != 200:
            print(colorama.Fore.RED+f"[Error] Status Code: {resp.status_code} ({resp.reason})\n[ERROR] Response: {resp.text}")
            raise requests.exceptions.HTTPError(resp.reason)
        else:
            self.limit_remaining = resp.headers['X-RateLimit-Remaining']
            print(colorama.Fore.GREEN + f"[INFO] Request completed\n[INFO] Status Code: {resp.status_code}\n[INFO] Response:\n{colorama.Fore.WHITE + resp.text}")
            return resp.json()
    
    def mars_picture(self,rover:str="Curiosity", sol=None,earth_date:str=None, camera:str="all", page=1):
        """
        Returns data for the Mars Picture that matches the given data.

        Parameters
        ==========
        rover: string, default -> "Curiosity"
            Rover name to access the database
        sol: integer, default -> None
            Martian date that corresponds to when the image got captured. 
        earth_date: string, default -> None 
            Earth date that corresponds to when the image got captured
        camera: string, default -> "all"
            Return results from specific camera on passed Rover
        page: integer, default -> 1
            How many pages of results to return. (25 items per page)

        Raises
        ======
        TypeError
            Raised if both sol and earth_date are specified.
        ValueError
            Raised if rover specified is not one of Curiosity Opportunity Spirit or Perseverance
        HTTPError
            Raised if response fails. (Status code != 200)

        Returns
        =======
        list 
            List containing dictionaries with the JSON data from the Mars Rover API
        """
        
        params =  {
            "api_key":self.api_key,
            "page":page
        }
        if rover.lower() not in ('curiosity', 'opportunity', 'spirit', 'perseverance'):
            raise ValueError(colorama.Fore.RED+"<rover> must be one of the following: Curiosity, Opportunity, Spirit, Perseverance")
        if earth_date != None and sol != None:
            raise TypeError(colorama.Fore.RED+"Bad combination. Either <earth_date> or <sol> can be specified")
        if camera != "all":
            params['camera'] = camera
        if sol != None:
            params['sol'] = sol
        if earth_date != None:
            if not isinstance(earth_date, (str, datetime.datetime)):
                raise TypeError("Earth date must be in YYYY-MM-DD format.")
            elif isinstance(earth_date, datetime.datetime):
                earth_date = earth_date.strftime("%Y-%m-%d")
            params['earth_date'] = earth_date

        resp = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos", params=params)

        if resp.status_code != 200:
            print(colorama.Fore.RED+f"[Error] Status Code: {resp.status_code} ({resp.reason})\n[ERROR] Response: {resp.text}")
            raise requests.exceptions.HTTPError(resp.reason)
        else:
            self.limit_remaining = resp.headers['X-RateLimit-Remaining']
            print(colorama.Fore.GREEN + f"[INFO] Request completed\n[INFO] Status Code: {resp.status_code}\n[INFO] Response:\n{colorama.Fore.WHITE + resp.text}")
            return resp.json()['photos']
#Tests 

my_apod = PySpace() #Initialize with DEMO_KEY
my_apod.mars_picture(rover="spirit",sol=1000)
# my_apod.picture_of_the_day(date="2022-02-05")
print(my_apod.limit_remaining)
