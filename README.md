# TourManager
A tool to easily organize shows and events. Made for artists, musicians, bookers, and event managers.


## Description:

TourManager is a tool to help artists, musicians, bookers, and event managers with the organization of shows and events.
TourManager wants to be simple and powerful, and it has a lot of tools to help organize your shows efficiently. 
It has a map to show your venues, a travel costs calculator, notes, statistics, links to locate addresses and get directions, it can generate calendar files for your favorite calendar application, export the upcoming shows into html, and many more useful tools. 
It will definitely reduce the boring tasks, making the booking processes enjoyable, and even bring multi-user cooperation!


![screenshot](https://github.com/sonejostudios/TourManager/blob/main/TourManager.png "TourManager")

![screenshot](https://github.com/sonejostudios/TourManager/blob/main/TourManagerMap.png "TourManagerMap")


## Main Features:

* Manage your shows
* Manage your venues and events
* Map (showing locations of venues and events)
* Travel costs calculator
* Locate addresses and get directions on OSM or Gmaps (via Web Browser)
* Generate calendar files for calendar applications, including one-year forecast
* Notes
* Statistics
* Search shows and venues
* Filter shows and venues
* Monitor (according to search and filters)
* Specific show folders for your related documents
* Tags
* Backup
* Dedicated working folder (can be shared with cloud applications)
* Settings
* Custom links (add your links to website and files into the main menu)
* Themes (dark and light)
* and many many more...
  

## Easy Installation (Binaries):

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


1. Start TourManager. You will see a example databases with 3 shows and venues/events. Read the comments to get more information.

2. Create a new venue:
* Click on `Add New` in the venue section on the bottom right (green section)
* Enter the venue's name, city and country. The venue is created
* Fill the venue fields as wanted: add the address, geo-coordinates, website, etc. and hit `Save Venue`
* If you want, press `Locate` to locate the address, `Route` to calculate the directions, `Map` (yellow section) to show the venues on the map

3. Create a new show:
* Select the new venue and press `Add New` in the show section on the bottom left (red section)
* Set a date and press OK. The show is created with the selected venue
* Fill the show fields as wanted: set the booking status, add contacts, create a specific show folder if needed, and hit `Save Show`
* To change the venue, just select a new one in the venue list, press `Assign Venue`(top left) and `Save Show`

4. Important:
* After filling in the fields (shows and venues), always hit `Save Show` or `Save Venue / Event`, otherwise, your modifications will not be saved.

5. Play around:
* Search the show list and apply booking status filters
* Search the venue list and apply venue filters
* Explore the Monitor (according to searches and filters!): Notes, Paths, Statistics, Lists and Emails (blue section)
* Explore the Map (according to venue searches and venue filters!): Click on the venue's 'markers to show more information (yellow section)
* Press `Route` to get the distance to your homebase
* Open the `Travel Costs Calculator` and enter that distance to know the travel costs (yellow section)





## Working Folder vs Application Folder:

### Working Folder:
The following files are stored into the working folder:
* The databases (`shows.csv` and `venues.csv`)
* The show folders (`Shows`)
* The notes (`Notes.txt`)
* The exported files:
	* `FutureShows.html`
	* `TourManagerShows.ics`
	* `TourManagerEvents.ics`
	* `TourManagerEventsForecast.ics`

You can use a shared folder which is synchronized over internet to use TourManager from different computers and users. It works nicely with Dropbox but should also work with others like NextCloud, etc. Using the working folder that way, you can have access to the files from everywhere. So you can have a look at the upcoming shows on your mobile phone and subscribe the calendars with your calendar applications.


### Application Folder:
The following files are stored into the application folder:

* All application files
* The database backups (`Backups` folder)
* `config.ini`

As you can see, the shared files are placed in the working folder and the user's configuration files and backups in the application folder. Using a cloud service, this allows to have different configurations for each client while using the same working folder.




## Exports:

In the menu `Export`, you can export the upcoming shows as .html file or the calendars as .ics files. If set up in the Settings, these files are automatically exported on application closing.

**Future Shows:** 
* `FutureShows.html`: Open this file (e.g. from your mobile phone) to have a quick view of the upcoming (and work in progress) shows. This is really handy when you are on tour without access to TourManager.

**Calendars:** 
Subscribe to these .ics files with your favorite calendar application (only tested with Thunderbird).
* `TourManagerShows.ics`: A calendar with all your shows
* `TourManagerEvents.ics`: A calendar with all events (all venues with start and end dates)
* `TourManagerEventsForecast.ics`: A calendar with all events postponed 1 year ahead. This can be handy to guess when an event could happen, even if you don't have the exact date yet.

**How to subscribe to the calendars with Thunderbird:**
* Select `Paths`in the Monitor (blue section)
* Copy the path of the file you want to subscribe to. E.g.  `file:///path/to/my/workdir/TourManagerShows.ics`
* Open Thunderbird, go to calendar
* On the bottom left, press `New Calendar...`
* Select `On the Network` (yes, even if the file is local)
* Copy the file path to `Location`and check `This location doesn't require credentials`
* Press `Find Calendars`
* If everything works as expected, Thunderbird will find the calendar. Then press `Subscribe`

**How to subscribe to the calendars on Android:**
* You will need an app to import the ICS-files into the android calendars. It works really smoothly with the open source app `ICSx5`, which can be found on [GooglePlay](https://play.google.com/store/apps/details?id=at.bitfire.icsdroid&pcampaignid=web_share) and [F-Droid](https://f-droid.org/packages/at.bitfire.icsdroid/)
* Open `ICSx5` and add a new file subscription, pointing to the ICS-file of your cloud provider (works well with DropBox). 




## More Screenshots:

![screenshot](https://github.com/sonejostudios/TourManager/blob/main/TourManagerThemes.png "TourManagerThemes")


Two themes are available:
1. Fusion (default, following the OS' dark/light theme)
2. PyQtDarkTheme (dark, light, and auto)
---

![screenshot](https://github.com/sonejostudios/TourManager/blob/main/TourManagerCalc.png "TourManagerCal")


Travel Cost Calculator: Handy little tool to calculate travel costs and generate a ready-to-paste calculation text.

---

![screenshot](https://github.com/sonejostudios/TourManager/blob/main/TourManagerSettings.png "TourManagerSettings")


Settings window with Default, View, Paths, Export and Custom Links editor.





