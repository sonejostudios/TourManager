# TourManager
A tool to organize shows and events. Made for artists, musicians, bookers and event managers.


__Description:__

BookerDB is a tool to help musicians, artists and bookers with the organization of shows and everything around.
BookerDB is based on a csv database, classified by dates. It is possible to add/delete entries and do a lot more of manipulations.
It has a monitor to show all kind of filters around the database, like coming dates, played dates, statistics, contacts, etc... It can also export database entries into PDF (as info sheet with all important information) to take them as reminder on tour.


![screenshot](https://github.com/sonejostudios/BookerDB/blob/master/BookerDB.png "BookerDB")


__Main Features:__

* Add/Save/Delete Shows
* Monitor Filters COMING, PLAYED, WAITING, CANCELLED, WORK IN PROGRESS, CONTACT ONLY, City, Country, Venue, Artist, Contacts, etc...
* Statistics
* Notes
* Search
* Filter Monitor
* Backup and Restore
* Sync Addresses and Contacts
* Export Show(s) to PDF file(s)
* Export Monitor to text file (i.e for printing)
* Open Monitor with default Text Editor
* View Venue location on OSM or Gmaps (via Web Browser)
* Direct Links to Search engines, Youtube, Facebook, Soundcloud, Mails, etc 
* Send E-Mail to Contact via default Mail Client
* Import/Export database to Working Folder
* Remote Working Folder (in cloud) handling (locked when imported, unlocked when exported)
* Use your own logo
* Open Folders from BookerDB directly (MATE, Cinnemon, GNOME, KDE only)
* Notify actions via OS
* Sync Addresses and Contacts
* and many many more...
  

__Installation:__

1. copy the whole BookerDB folder on your system
```
git clone https://github.com/sonejostudios/BookerDB.git
```

2. from this folder start BookerDB with: 
```
python3 BookerDB.py
```

__Requirements:__

* Python3
* Tkinter
* GNU/Linux (with cp, sed and sort)
* Web Browser (i.e Firefox)
* File Manager (caja, nemo, nautilus, dolphin)
* PDF Reader
