Weather
=======
- PySpace provides 2 methods that help you access data about Earth and Martian weather.

Earth Weather
*************
.. warning::
    To use this method, you need to specify the `Weather API <https://www.visualcrossing.com/weather-api>`_

    .. code-block:: python
        :linenos:
        :emphasize-lines: 3

        import pyspace 

        nasa = pyspace.PySpace(weather_api_key="API_KEY")

.. py:function:: earth_weather(self, location, ugroup="us", start_date='', end_date='', c_type="json"):

    Returns data for the NASA APOD (Astronomy Picture of the Day).

    :param location:
    :param ugroup: The Unit Group
    :param start_date, end_date: Range of the weather data 
    :param c_type:  The content type in which data is returned. 

    :type location: str (Name of country, city etc.)
    :type ugroup: str
    :type start_date: str
    :type end_date: str
    :type c_type: str

    :raise TypeError: Raised if location, ugroup, start_date, end_date or c_type are not ``str``
    :raise HTTPError: Raised if response fails. (When Status code is not ``200``)
    :return: Dictionary object with JSON data containing information about the weather of specified location, date range.
    :rtype: dict

Martian Weather
***************
.. attention::
    You do not need an API_KEY to retrieve data from the Insights (Mars Weather Data) API. Although it is highly recommended. 
    Please read more information about NASA's :ref:`Rate Limits <rate_limits>`

.. py:function:: mars_weather(self, version=1.0):

    Returns per Sol weather data for each of the last seven available Sols.

    :param version: Version of the Insights (Mars Weather Data) API           
    :type version: int or float

    :raise TypeError: Raised if location, ugroup, start_date, end_date or c_type are not ``str``
    :raise HTTPError: Raised if response fails. (When Status code is not ``200``)

    :return: list object containing dictionaries for each Sol followed by the average, min, and max temperature of that martian day (Sol) in Celcius

    :rtype: list[dict, ...]

.. note::
    
    We will soon add a unit parameter so that the user can choose the unit in which the temperatures are. (Fahrenheit or Celcius)
    
