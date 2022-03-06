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
