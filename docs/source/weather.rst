.. currentmodule:: pyspace.py

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

.. note:: 
    As of now this method is still in BETA. Therefore, there is no ``Error Handling`` as of now.
    Keep in mind that there is not any additional handling for the date range (``start_date`` - ``end_date``)

.. automethod:: pyspace.PySpace.earth_weather


Martian Weather
***************
.. attention::
    You do not need an API_KEY to retrieve data from the Insights (Mars Weather Data) API. Although it is highly recommended. 
    Please read more information about NASA's :ref:`Rate Limits <rate_limits>`

.. automethod:: pyspace.PySpace.mars_weather

.. note::
    
    We will soon add a unit parameter so that the user can choose the unit in which the temperatures are. (Fahrenheit or Celcius)
    
