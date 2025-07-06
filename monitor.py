import os
import sys
import datetime
import humanize

CB_MONITOR_ITEMS = ["Notes",                                             # 0
                    "Statistics (Shows)",                                # 1
                    "Date - City - Venue (Shows)",                       # 2
                    "Artists: Date - City - Venue (Shows)",              # 3
                    "Artists & Shows (Shows)",                           # 4
                    "Fee, Travel Costs, SUM, Date, Venue, Currency (Shows)",   # 5
                    "Contact Emails (Shows)",                            # 6
                    "Contact Emails (Venues)",                           # 7
                    "Tags (Shows)",                                      # 8
                    "Tags (Venues)"]                                     # 9



NOTES_FILE = "Notes.txt"



def fill_monitor(parent):
    monitor_cb_index = parent.ui.cb_monitor.currentIndex()
    notes_path = os.path.join(parent.config_workdir, NOTES_FILE)

    # create note file if it doesn't exist
    if not os.path.isfile(notes_path):
        with open(notes_path, "w", encoding='utf-8') as file:
            file.write("Welcome to TourManager!")


    # open notes
    if monitor_cb_index == 0:
        with open(notes_path, "r+", encoding='utf-8') as file:
            parent.ui.txt_monitor.setPlainText(file.read())
        parent.notes_opened = True


    # paths
    # elif monitor_cb_index == 1:
    #     save_notes(parent, notes_path)
    #     set_paths_text(parent)


    # statistics
    elif monitor_cb_index == 1:
        save_notes(parent, notes_path)
        set_stats_text(parent)


    # all iterations (monitor_cb_index == 2, 3, 4, 5, 6, 7, 8, 9)
    else:
        save_notes(parent, notes_path)
        # get text and insert into widget
        monitor_text = get_monitor_iterated_text(monitor_cb_index, parent.df_shows_in_list, parent.df_venues_in_list)
        parent.ui.txt_monitor.setPlainText(monitor_text)




def save_notes(parent, notes_path):
    # save notes only if opened before
    if parent.notes_opened == True:
        with open(notes_path, "w", encoding='utf-8') as file:
            file.write(parent.ui.txt_monitor.toPlainText())
        parent.notes_opened = False



def set_paths_text(parent):
    workdir = os.path.abspath(parent.config_workdir)
    calendar_shows = os.path.abspath(os.path.join(parent.config_workdir, "TourManagerShows.ics"))
    calendar_events = os.path.abspath(os.path.join(parent.config_workdir, "TourManagerEvents.ics"))
    calendar_events_forecast = os.path.abspath(os.path.join(parent.config_workdir, "TourManagerEventsForecast.ics"))

    monitor_text = ("Working Directory:\n" + workdir + 
                    "\n\nShow Calendar:\nfile://" + calendar_shows +
                    "\n\nEvent Calendar:\nfile://" + calendar_events +
                    "\n\nEvent Forecast Calendar:\nfile://" + calendar_events_forecast)
    parent.ui.txt_monitor.setPlainText(monitor_text)




def set_stats_text(parent):
    shows_amount = len(parent.df_shows_in_list)
    if shows_amount == 0:
        monitor_text = "No statistics (show list is empty)"
    else:
        date = parent.df_shows_in_list["Date"]
        first_date = datetime.datetime.fromisoformat(date.iloc[0]).date()
        latest_date = datetime.datetime.fromisoformat(date.iloc[-1]).date()
        timedelta = (latest_date - first_date)#.days

        currency = parent.config_currency
        fee = parent.df_shows_in_list["Fee"]
        travel_costs = parent.df_shows_in_list["TravelCosts"]

        monitor_text = ("SHOWS: " + str(shows_amount) +
                        "\n\nTIME RANGE: " + humanize.precisedelta(timedelta) +
                        # "\nIn years:\t" + str(round(timedelta / 365, 2)) +
                        # "\nIn days:\t" + str(timedelta) +
                        "\n\nSUM (" + currency + "):"
                        "\nFees:\t" + str(fee.sum()) +
                        "\nTravel Costs:\t" + str(travel_costs.sum()) +
                        "\nSum:\t" + str(fee.sum() + travel_costs.sum()) +
                        "\n\nAVERAGE (" + currency + "):"
                        "\nFees:\t" + str(round(fee.mean(), 2)) +
                        "\nTravel Costs:\t" + str(round(travel_costs.mean(), 2)) +
                        "\nSum:\t" + str(round(fee.mean() + travel_costs.mean(), 2))
                        )

    # set monitor text
    parent.ui.txt_monitor.setPlainText(monitor_text)





def get_monitor_iterated_text(monitor_cb_index, df_shows_in_list, df_venues_in_list):
    monitor_text = ""
    show_str = ""
    venue_str = ""
    fee_list = []

    # iterate SHOWS (df_shows_in_list)
    if monitor_cb_index in [2,3,4,5,6,8]:
        for index, row in df_shows_in_list.iterrows():
            if monitor_cb_index == 2:
                show_str = str(row["Date"]) + " - " + str(row["City"]) + " - " + str(row["Venue"])
            elif monitor_cb_index == 3:
                show_str = str(row["Artist"]) + ":\t" + str(row["Date"]) + " - " + str(row["City"]) + " - " + str(row["Venue"])
            elif monitor_cb_index == 4:
                show_str = str(row["Artist"])
            elif monitor_cb_index == 5:
                fee_list_item = [float(row["Fee"]), float(row["TravelCosts"]), row["Date"], row["Venue"], row["Currency"]]
                fee_list.append(fee_list_item)
            elif monitor_cb_index == 6: # show emails
                if bool(row["EmailHide"]) == False:
                    show_str = str(row["Email"])
            elif monitor_cb_index == 8: # show tags
                show_str = str(row["Tags"])

            # append to text
            monitor_text += show_str + "\n"



    # iterate VENUES (df_venues_in_list)
    if monitor_cb_index in [7,9]:
        for index, row in df_venues_in_list.iterrows():
            if monitor_cb_index == 7: # venue emails
                if bool(row["VenueEmailHide"]) == False:
                    venue_str = str(row["VenueEmail"])
            elif monitor_cb_index == 9: # venue tags
                venue_str = str(row["VenueTags"])

            # append to text
            monitor_text += venue_str + "\n"





    # POST-PROCESSING (if needed)
    if monitor_cb_index == 4:  # artists and sum of shows
        artists_list = sorted(set(monitor_text.splitlines()), key=str.lower)
        monitor_text = ""
        for i in artists_list:
            shows = sum(df_shows_in_list['Artist'] == i)
            monitor_text += i + "\t" + str(shows) + "\n"


    if monitor_cb_index == 5:  # fees and travel costs -> sorted descending
        monitor_text = ""
        fee_list = sorted(fee_list, reverse=True)
        for i in fee_list:
            monitor_text += str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[0] + i[1]) + "\t" + str(i[2]) + "\t" + str(i[3]) + " (" + str(i[4]) + ")" + "\n"


    if monitor_cb_index in [6, 7]:  # emails only (shows and venues): remove blank lines, duplicates and entries without "@"
        email_list = sorted(set(monitor_text.splitlines()), key=str.lower)
        monitor_text = ""
        for i in email_list:
            if "@" in i:
                monitor_text += i + "\n"


    if monitor_cb_index in [8, 9]: # tags (shows and venues)
        tag_list = set(monitor_text.splitlines())
        final_tag_list = []
        for i in tag_list:
            sublist = i.split()
            for j in sublist:
                final_tag_list.append(j.replace(",", "").strip())
        final_tag_list = sorted(set(final_tag_list), key=str.casefold)
        monitor_text = ""
        for i in final_tag_list:
            monitor_text += i + "\n"




    return monitor_text