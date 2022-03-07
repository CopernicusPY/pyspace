.. PySpace documentation master file, created by
   sphinx-quickstart on Fri Mar  4 20:06:12 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PySpace
===================================
PySpace is an easy, simple but powerful library for NASA APIs.

.. important::
   The purpose of this library is to make the exploration of our universe fun and most importantly, easy!


We offer:
***********
- **Full coverage on the supported APIs**: Currently we do not support all the `NASA.gov <https://api.nasa.gov/>`_ APIs. Although on the ones we support, we provide **full** coverage.

.. list-table:: List of supported APIs
   :header-rows: 1

   * - Nasa APIs
     - External APIs 
    
   * - APOD 
     - Visual Crossing Weather API
    

   * - Mars Rover Pictures  
     -

   * - Image and Video Library
     -
   * - Insights 
     -
   * - Earth Imagery
     -

.. note::
   Keep in mind that this list will change overtime.
   - If you have any suggestions on what API we should add/remove please feel free to contact us

- **Extra-capable methods for result storing and visualization**: We provide methods that allow external result manipulation. (For example, our earth_imagery() method lets you save the image into a directory of your desire and even returns a NumPy Array of the pixel values that opens the way for advanced image annotation using third-party libraries such as OpenCV). As we are mentioning below this helps users create awesome projects.(**Visualization methods** are comming soon in ``v.2.0.0 BETA``)

- **Tons of possible usages of our library**: The variety of methods we offer opens the way for users to combine our library and their imagination to create awesome projects!

- **Easy to read error handling**: afraid of facing errors? Not any-more! We took care of this by transforming the tracebacks and providing you straight to the point-answers!

- **Easy to read outputs**: data returned from each request are really easy to read!

- **API-strict naming**: we follow strictly the naming style of each endpoint from the official `NASA.gov <https://api.nasa.gov/>`_ documentation. Therefore, no more confusion for our users on what method to use.

Downsides?
***************
- As we mentioned above, we have lots to offer. Although since this project is still in BETA we do not provide full-coverage on the `NASA.gov <https://api.nasa.gov/>`_ APIs.

Where do I start?
*********************
Please take a look at our pages

.. toctree::
   :maxdepth: 2
   :caption: Pages:

   quickstart.rst
   api.rst


Advanced Search
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

