Picture Of the day 
==================

.. py:function:: picture_of_the_day(self, date=None, hd=False, count=None)

    Returns data for the NASA APOD (Astronomy Picture of the Day).

    :param date: If specified data for the APOD corresponding to that date will be returned. If ``None`` todays APOD will be returned.
    :param hd: If ``True`` the High Definition Image URL is returned.
    :param count: If specified ``<count>`` random images will be returned. (Cant be used with date.)


    :type date: str, datetime.datetime or None
    :type hd: bool
    :type count: int or None

    :raise TypeError: Raised if the parameter ``<hd>`` is not boolean. 
    :raise HTTPError: Raised if response fails. (When Status code is not ``200``)

    :return: Dictionary object containing JSON data returned from the API.
    :rtype: dict


Mars Picture 
============
.. py:function:: mars_picture(self, rover:str = "Curiosity", sol=None, earth_date = None, camera="all", page=1)
    
    Collect image data gathered by NASA's Curiosity, Opportunity, and Spirit rovers on Mars

    :param rover: 
    :param sol: The sol (Martian rotation or day) on which the photos were taken
    :param earth_date: Earth date on which a photo/s was taken
    :param camera: Return images that got captured on that specific camera. If not specified images from all cameras are returned.
    :param page: How many pages of results to return (25 items per page)

    :type rover: str
    :type sol: int or None
    :type earth_date: str or None
    :type camera: str
    :type page: int

    :raise TypeError: Raised if both ``<sol>`` and ``<earth_date>`` are specified.
    :raise ValueError: Raised if the rover specified is not one of Curiosity Opportunity or Spirit.
    :raise HTTPError: Raised if response fails. (When Status code is not ``200``)

    :return: Dictionary object containing JSON data returned from the API.
    :rtype: dict
