# Pyspace
PySpace is an easy-to-use open-source NASA API Wrapper. Nasa developed a few apis to help the developers explore our world and even better, the space! \
This wrapper currently supports Earth API, APOD(Astronomical Pictures of the Day) API, and also Mars Rover Photos API.

> For more information about each API please visit https://api.nasa.gov/
> To generate an API Key visit https://api.nasa.gov/. (It is not required but recommended. By default we use the "DEMO_KEY")

# Installation

>:warning: This wrapper is not a package as of now. So please store this repository to your projects directory\

**Firstly git clone the repository** 
>:warning: Remember to use cd to change your directory to a dir you prefer before git cloning.

`git clone https://github.com/CapernicusPY/pyspace/`
# Usage
Firstly, import the module. (Keep in mind the setup of this repo is not that good (will be changed soon) so you install all the different modules for all the different apis. 
```py
#Import APOD Module Example
from pyspace import PySpace
```
After that, initialize the module while specifying the API_KEY(Can be None since default is "DEMO_KEY")
```py
apod = PySpace("API_KEY") # Initialize module using api key from https://api.nasa.gov/
apod = PySpace() # Initialize module using demo key
```
For usage examples check out the [examples file](examples.py)

# PySpace ISS Tracking
