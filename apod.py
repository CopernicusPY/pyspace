import requests, json, random, datetime, exceptions, colorama
from txt_logo import logos
"""
Error Handling Completed In: picture_by_date
Remaining:
get_picture => Handled Request Error 
"""
class APOD:
    def __init__(self, api_key="DEMO_KEY"):
        colorama.init(True)
        self.api_key = api_key 
        self.today = datetime.datetime.today().strftime('%Y-%m-%d')
        print(logos[0])

    def compare_date(self,date,d_to_compare):
        """
        Compares 2 dates
        """
        date = [int(i) for i in date.split("-")]
        date = datetime.datetime(date[0], date[1], date[2])
        
        date2 = [int(i) for i in d_to_compare.split("-")]
        date2 = datetime.datetime(date2[0], date2[1], date2[2])

        if date < date2: return True
        else: return False

    def picture_of_the_day(self):
        """
        Returns the image of the day
        """
        params={
            "api_key":self.api_key
        }
        try:
            resp = requests.get(f"https://api.nasa.gov/planetary/apod", params=params)
            if resp.status_code != 200:
                raise exceptions.UnsuccessfulRequest
            else:
                tt = json.loads(resp.text)
                tt = colorama.Fore.GREEN + f"[INFO] Request Completed Succesfully\n[-] Status Code:{resp.status_code}" + f"\n[-] Response MSG:" + colorama.Fore.WHITE + f"\n{resp.text}"
                return tt
        except exceptions.UnsuccessfulRequest:
            print(colorama.Fore.RED+f"[ERROR] Request is unsuccesful\n[-] Status Code: {resp.status_code}\n[-] Response MSG: \n{resp.text}")

    def picture_by_date(self, date):
        """
        Returns image that got captured on given date
        """
        params = {
            "api_key":self.api_key,
            "date":date
        }
        print(self.compare_date(date, "2015-02-05"))
            
        try:
            resp = requests.get(f"https://api.nasa.gov/planetary/apod", params=params)
            if resp.status_code != 200:
                raise exceptions.UnsuccessfulRequest
            else:
                tt = json.loads(resp.text)
                tt = colorama.Fore.GREEN + f"[INFO] Request Completed Succesfully\n[-] Status Code:{resp.status_code}" + f"\n[-] Response MSG:" + colorama.Fore.WHITE + f"\n{resp.text}"
                return tt
        except exceptions.ArgOutOfRange:
            print(colorama.Fore.RED+"Date out of range")
        except exceptions.UnsuccessfulRequest:
            print(colorama.Fore.RED+f"[ERROR] Request is unsuccesful\n[-] Status Code: {resp.status_code}\n[-] Response MSG: \n{resp.text}")

  
    def random_picture(self, count=1):
        params = {
            "api_key":self.api_key,
            "count":count
        }
        try:
            resp = requests.get(f"https://api.nasa.gov/planetary/apod", params=params)
            if resp.status_code != 200:
                raise exceptions.UnsuccessfulRequest
            else:
                tt = json.loads(resp.text)
                tt = colorama.Fore.GREEN + f"[INFO] Request Completed Succesfully\n[-] Status Code:{resp.status_code}" + f"\n[-] Response MSG:" + colorama.Fore.WHITE + f"\n{resp.text}"
                return tt
        except exceptions.UnsuccessfulRequest:
            print(colorama.Fore.RED+f"[ERROR] Request is unsuccesful\n[-] Status Code: {resp.status_code}\n[-] Response MSG: \n{resp.text}")

    #APOD General Function

    def get_picture(self, date=None, start_date=None,end_date=None,count=None,vid=False):
        params = {
            "api_key":self.api_key,
            "date":date,
            "start_date":start_date,
            "end_date":end_date,
            "count":count,
            "thumbs":vid
        }
        try:
            resp = requests.get("https://api.nasa.gov/planetary/apod", params=params)
            if resp.status_code != 200:
                raise exceptions.UnsuccessfulRequest
            else:
                tt = json.loads(resp.text)
                tt = colorama.Fore.GREEN + f"[INFO] Request Completed Succesfully\n[-] Status Code:{resp.status_code}" + f"\n[-] Response MSG:" + colorama.Fore.WHITE + f"\n{resp.text}"
                return tt
        except exceptions.UnsuccessfulRequest:
            print(colorama.Fore.RED+f"[ERROR] Request is unsuccesful\n[-] Status Code: {resp.status_code}\n[-] Response MSG: \n{resp.text}")
        except exceptions.ArgOutOfRange:
            print(colorama.Fore.RED+"Date out of range")
