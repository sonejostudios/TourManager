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
* Map
* Travel costs calculator
* Locate addresses and get directions on OSM or Gmaps (via Web Browser)
* Generate calendar files for calendar applications
* Notes
* Statistics
* Search shows and venues
* Filter shows and venues
* Monitor (according to search and filters)
* Specific show folders for your related documents
* Tags
* Backup
* Dedicated working folder (can be shared with cloud applications)
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

1. First, open `config.ini` and set it up as wanted: 
* Add your homebase city and its geo-coordinates
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
* Fill the show fields as wanted: set the booking status, add contacts, create a specific show folder if needed, and hit `Save Show`
* To change the venue, just select a new one on the venue list and hit `Save Show`

5. Important:
* After filling in the fields (shows and venues), always hit `Save Show` or `Save Venue`, otherwise, your modifications will not be saved.
* If you want to change the venue for one show, choose a new venue and press `Assign Venue` in the show fields. Then, of course, `Save Show` to save everything in the selected show.

6. Play around:
* Search the show list and apply booking status filters
* Search the venue list and apply venue filters
* Explore the Monitor (according to searches and filters!): Notes, Paths, Statistics, Lists, Emails and Tags (blue section)
* Explore the Map (according to venue searches and venue filters!): Click on the venue's 'markers to show more information (yellow section)
* Press `Route` to get the distance to your homebase
* Open the `Travel Costs Calculator` and enter that distance to know the travel costs (yellow section)


## Config.ini:
```
[defaults]
homebase_city = Homebase City (please setup config.ini)
homebase_geocoordinates = 0.0, 0.0
artists = My Artist
currency = EUR
distance_unit = km
travel_unit_price = 0.30

[paths]
working_directory = 

[settings]
auto_export_shows = 0
auto_export_calendars = 0
map_provider = osm #gmaps
calc_text_decimal_separator = ,
custom_links = [("TourManager Web", "https://github.com/sonejostudios/TourManager"), ("|",""), ("App Notes", r"Notes.txt"), ("App Folder", r".")]

[gui]
theme = none #auto #dark #light
font_size = #10
field_area_width = #430
save_window_size = 0
window_width = 1700
window_height = 1000
start_maximized = 0
```
* defaults:
	* homebase_city = Enter your city or where you want to start your trip.
	* homebase_geocoordinates = It's geo-coordinates (in decimal form, e.g. 47.994853, 7.843950).
	* artists = Your default artist's name.
	* currency = The default currency code you want to use (e.g. EUR or USD).
	* distance_unit = the default distance unit (e.g. km).
	* travel_unit_price = The default price per unit (e.g. 0.30€/km).

* paths:
	* working_directory = Enter the path of your working folder. If empty, the application's folder is used. See chapter "Working Folder".

* settings:
	* auto_export_shows = If 1, the upcoming shows will be exported as .html on application closing.
	* auto_export_calendars = If 1, the calendars will be exported as .ics on application closing.
	* map_provider =  Enter `gmaps` if you want to use google maps instead of open street map.
    * calc_text_decimal_separator = Set the decimal separator of the Travel Costs Calculator's text.
    * custom_links = Here you can add your own links to the menu. It can be web links, files and folders. Use the python's list syntax with tuples containing the title and the url/path, like this: `[("title", "url"), ("title", r"path")]`. Use `("|", "")` to add a separator. If you are using windows, don't forget to mark file and folder paths as raw strings (`r"my\path"`), otherwise backslashes will be misinterpreted as escape sign. If empty, the Custom Links menu will be hidden.

* gui:
    * theme = Enter `dark`, `light` or `auto` (follows OS color theme) to use pyqtdarktheme.
    * font_size = Set the font size. If empty, the default is 10.
    * field_area_width = Set the with of the field areas (left for the shows, right for the venues). Increase it while increasing font size to match the lool'n'feel. If empty, the default is 430.
    * save_window_size = If 1, the window size is saved and restored.
    * window_width = The width of the window (will be overwritten is save_window_size = 1).
    * window_height = The height of the window (will be overwritten is save_window_size = 1).
    * start_maximized = Maximize the window on start.



## Working Folder vs Application Folder:

### Working Folder:
The following files are stored into the working folder:
* The databases (`shows.csv` and `venues.csv`)
* The show folders (`Shows`)
* The notes (`Notes.txt`)
* The exported files:
	* `UpcomingShows.html`
	* `TourManagerShows.ics`
	* `TourManagerEvents.ics`
	* `TourManagerEventsForecast.ics`

You can use a shared folder that is synchronized over internet to use TourManager from different computers and users. It works nicely with DropBox but should also work with others like NextCloud, etc. Using the working folder that way, you can have access to the files from everywhere. So you can have a look at the upcoming show on your mobile phone and subscribe the calendars with your calendar application.


### Working Folder:
The following files are stored into the application folder:

* All application files
* The database backups (`Backups` folder)
* `config.ini`

As you can see, the shared files are placed in the working folder and the user's configuration files and backups in the application folder.




## Exports:

In the menu `Export`, you can export the upcoming shows as .html file or the calendars as .ics files. If set up in `config.ini`, these files are automatically exported on application closing.

**Upcoming Shows:** 
* `UpcomingShows.html`: Open this file (e.g. from your mobile phone) to have a quick view of the upcoming shows. This is really handy when you are on tour without a computer with TourManager

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
* Open `ICSx5` and add a new file subscription, pointing to the ICS-file of your cloup provider (works well with DropBox). 







