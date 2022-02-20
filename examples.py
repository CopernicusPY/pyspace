from pyspace import PySpace
import random

#Initialize PySpace Module with a demo api key.
pyspace = PySpace()

#============================================
#       Astronomy Picture Of The Day        #
#============================================

#Get the picture of the day
pyspace.picture_of_the_day()
#Get picture by date
pyspace.picture_of_the_day(date="2022-01-01")
#Get n random pictures
n = 5 
pyspace.picture_of_the_day(count=n)

#============================================
#              Mars Rover Picture           #
#============================================

#Get the picture of the day by a random Rover
rovers = ["Curiosity", "Spirit", "Opportunity", "Perseverance"]
pyspace.mars_picture(rover=random.choice(rovers))

#Get picture from mars that got captured on a sol(Martian Date) / Earth Date
pyspace.mars_picture(sol=1000)
pyspace.mars_picture(earth_date="2022-01-01")

#Get picture from mars from a specified camera

pyspace.mars_picture(sol=1000,camera="FHAZ")

#============================================
#              ISS Track                    #
# > ISS Track method is currently on beta,  #
# so please keep in mind that there will be #
# bugs                                      #
#============================================

#Get the astronauts that are currently on-board on ISS
people_on_board = pyspace.track_iss()['people_on_board']
print(people_on_board)

#Get a live display of the ISS
pyspace.track_iss(live=True)

#Get all the ISS positions by following a timeline
moment1 = pyspace.track_iss["live_position"][0]
moment2 = pyspace.track_iss["live_position"][1]
moment3 = pyspace.track_iss["live_position"][2]
