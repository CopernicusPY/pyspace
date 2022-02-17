import requests, datetime, colorama
from txt_logo import logos

class PySpace:
    def __init__(self, api_key="DEMO_KEY"):
        colorama.init(True)

        self.api_key = api_key 
        print(logos[0])

    def picture_of_the_day(self, date=datetime.datetime.today().strftime('%Y-%m-%d'), hd=False):
        """
        Returns data for the NASA APOD (Astronomy Picture of the Day).

        Parameters
        ==========
        date: string, datetime object, default -> datetime.datetime.today()
        hd: bool, default -> False 
            If True returns matching high-definision image of the APOD

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
            "hd":hd
        }
        if hd is not None:
            if not isinstance(hd, bool):
                raise TypeError(colorama.Fore.RED+"<hd> parameter must be a Boolean (True - False)")
        resp = requests.get("https://api.nasa.gov/planetary/apod", params=params)
        if resp.status_code != 200:
            raise requests.exceptions.HTTPError(resp.reason)
        else:
            print(colorama.Fore.GREEN + f"[INFO] Request completed\n[INFO] Status Code: {resp.status_code}\n[INFO] Response:\n{colorama.Fore.WHITE + resp.text}")
            return resp.json()
    
                
