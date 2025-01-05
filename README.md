# TourManager
A tool to organize shows and events. Made for artists, musicians, bookers and event managers.


## Description:

TourManager is a tool to help artists, musicians, bookers and event managers with the organization of shows and events.
TourManager wants to be simple and powerful and it has a lot of tools to help organizing your shows efficiently. 
It has a map to show your venues, a travel costs calculator, notes, statistics, links to locate addresses and get directions, it can generate calender files for you favorite calendar application, export the upcoming shows into html, and many more useful tools. It will definitely reduce the boring tasks, making the booking processes enjoyable, and even bring multi-user cooperation!


![screenshot](https://github.com/sonejostudios/TourManager/blob/main/TourManager.png "TourManager")

![screenshot](https://github.com/sonejostudios/TourManager/blob/main/TourManagerMap.png "TourManagerMap")


## Main Features:

* Manage your shows
* Manage your venues and events
* Map
* Travel costs calculator
* Locate addresses and get directions on OSM or Gmaps (via Web Browser)
* Generate calendar files for calendar applications
* Notes
* Statistics
* Search shows and venues
* Filter shows and venues
* Monitor (according to search and filters)
* Specific show folders
* Tags
* Backup
* Working folder (can be shared with cloud applications)
* and many many more...
  

## Installation (Binaries):


**Linux:**
Grab the [newest release](https://github.com/sonejostudios/TourManager/releases) linux zip file, extract it, cd into folder and run
```
./TourManager
```
**Windows:**
Grab the [newest release](https://github.com/sonejostudios/TourManager/releases) windows file, extract it and start
```
TourManager.exe
```


## Installation (Python Source):

1. Clone the whole TourManager folder on your system
```
git clone https://github.com/sonejostudios/TourManager.git
```

2. Install dependencies:
```
pip install PySide6 pandas folium ics tabulate humanize pyqtdarktheme-fork
```

3. Start TourManager with: 
```
./TourManager.sh
```


## Get Started:

![screenshot](https://github.com/sonejostudios/TourManager/blob/main/TourManagerSections.png "TourManagerSections")

1. First, open `config.ini` and set it up as wanted: 
* Add your homebase city and it's geo-coordinates
* Your default artist name, 
* Default currency
* Distance unit
* Default travel price

2. Start TourManager. You will see a example databases with 3 shows and venues/events. Read the comments to get more information.

3. Create a new venue:
* Click on `Add New` in the venue section on the bottom right (green section)
* Enter the venue's name, city and country. The venue is created
* Fill the venue fields as wanted: add the address, geo-coordinates, website, etc. and hit `Save Venue`
* If you want, press `Locate` to locate the address, `Route` to calculate the directions, `Map` (yellow section) to show the venues on the map

4. Create a new show:
* Select the new venue and press `Add New` in the show section on the bottom left (red section)
* Set a date and press ok. The show is created with the selected venue
* Fill the show fields as wanted: set the booking status, add contacts, create a specific show folder if needed and hit `Save Show`
* To change the venue, just select and new one on the venue list and hit `Save Show`

5. Important:
* After filling the fields (shows and venues), always hit `Save Show` oder `Save Venue`, otherwise your modifications will not be saved.

6. Play around:
* Search the show list and apply booking status filters
* Search the venue list and apply venue filters
* Explore the Monitor (according to searches and filters!): Notes, Paths, Statistics, Lists, Emails and Tags (blue section)
* Explore the Map (according to venue searches and venue filters!): Click on the venue's 'markers to show more information (yellow section)
* Press `Route` to get the distance to your homebase
* Open the `Travel Costs Calculator` and enter that distance to know the travel costs (yellow section)


## Config.ini:



## Working Folder:


## Exports:


## Map:







