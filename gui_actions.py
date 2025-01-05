from PySide6.QtCore import QDate

import os
import platform
import subprocess





def fill_show_fields(ui, selected_show):
    # get data from show.csv
    ui.field_show_dateedit.setEnabled(True)
    ui.field_show_dateedit.setDate(QDate.fromString(str(selected_show["Date"]), "yyyy-MM-dd"))

    ui.field_show_id.setText(str(int(selected_show["ShowID"])))

    # fill venue id from shows.csv
    ui.field_venue_id.setText(str(int(selected_show["VenueID"])))


    show_status = selected_show["Status"]
    ui.cb_show_status.setCurrentIndex(show_status)
    ui.field_show_artists.setText(str(selected_show["Artists"]))

    ui.field_show_contact.setText(str(selected_show["Contact"]))
    ui.field_show_phone.setText(str(selected_show["Phone"]))
    ui.field_show_email.setText(str(selected_show["Email"]))

    ui.field_show_tech_contact.setText(str(selected_show["TechContact"]))
    ui.field_show_tech_phone.setText(str(selected_show["TechPhone"]))
    ui.field_show_tech_email.setText(str(selected_show["TechEmail"]))

    ui.field_show_info.setPlainText(str(selected_show["Info"]))

    fee = selected_show["Fee"] if selected_show["Fee"] != "" else 0
    travel_fee = selected_show["TravelFee"] if selected_show["TravelFee"] != "" else 0
    ui.field_show_fee.setText(str(fee))
    ui.field_show_travel_fee.setText(str(travel_fee))
    ui.field_show_fee_sum.setText(str(fee + travel_fee))
    ui.field_show_currency.setText(str(selected_show["Currency"]))

    ui.field_show_arrival_time.setText(str(selected_show["ArrivalTime"]))
    ui.field_show_soundcheck_time.setText(str(selected_show["SoundcheckTime"]))
    ui.field_show_opening_time.setText(str(selected_show["OpeningTime"]))
    ui.field_show_show_time.setText(str(selected_show["ShowTime"]))

    ui.field_show_food_drinks.setText(str(selected_show["FoodDrinks"]))
    ui.field_show_accomodation.setText(str(selected_show["Accomodation"]))
    ui.field_show_breakfast.setText(str(selected_show["Breakfast"]))

    ui.field_show_print.setText(str(selected_show["Print"]))
    ui.field_show_print_address.setPlainText(str(selected_show["PrintAddress"]))
    ui.field_show_tags.setText(str(selected_show["Tags"]))
    
    
    
    
def fill_venue_fields(ui, df_venues, venue_id):
    #print(venue_id)
    #print(df_venues.loc[venue_id].to_frame().T)

    # fill venue name and city in show fields - from venues.csv
    venue_name = str(df_venues.loc[venue_id]["VenueName"])
    venue_city = str(df_venues.loc[venue_id]["VenueCity"])
    ui.field_venue_text.setText(venue_city + " - " + venue_name)

    # fill venue id
    ui.field_venue_id.setText(str(int(venue_id)))

    # fill venue fields
    ui.field_venue_name.setText(venue_name)
    ui.field_venue_city.setText(venue_city)
    ui.field_venue_country.setText(str(df_venues.loc[venue_id]["VenueCountry"]))
    ui.field_venue_address.setPlainText(str(df_venues.loc[venue_id]["VenueAddress"]))
    ui.field_venue_geocoordinates.setText(str(df_venues.loc[venue_id]["VenueGeoCoordinates"]))
    ui.field_checkbox_venue_is_event.setChecked(bool(df_venues.loc[venue_id]["VenueIsEvent"]))

    if ui.field_checkbox_venue_is_event.isChecked():
        start_date = str(df_venues.loc[venue_id]["VenueStartDate"])
        ui.field_venue_start_dateedit.setDate(QDate.fromString(start_date, "yyyy-MM-dd"))
        end_date = str(df_venues.loc[venue_id]["VenueEndDate"])
        ui.field_venue_end_dateedit.setDate(QDate.fromString(end_date, "yyyy-MM-dd"))

    ui.field_venue_website.setText(str(df_venues.loc[venue_id]["VenueWebsite"]))
    ui.field_venue_genres.setText(str(df_venues.loc[venue_id]["VenueGenres"]))

    if df_venues.loc[venue_id]["VenueRating"] != "":
        ui.cb_venue_rating.setCurrentIndex(int(df_venues.loc[venue_id]["VenueRating"]))
    else:
        ui.cb_venue_rating.setCurrentIndex(0)

    ui.field_checkbox_venue_is_discontinued.setChecked(bool(df_venues.loc[venue_id]["VenueIsDiscontinued"]))
    ui.field_venue_contact.setText(str(df_venues.loc[venue_id]["VenueContact"]))
    ui.field_venue_phone.setText(str(df_venues.loc[venue_id]["VenuePhone"]))
    ui.field_venue_email.setText(str(df_venues.loc[venue_id]["VenueEmail"]))
    ui.field_venue_info.setPlainText(str(df_venues.loc[venue_id]["VenueInfo"]))
    ui.field_venue_tags.setText(str(df_venues.loc[venue_id]["VenueTags"]))
    


    
def check_venue_is_event(ui): # enable/disable event date fields
    if ui.field_checkbox_venue_is_event.isChecked():
        ui.field_venue_start_dateedit.setEnabled(True)
        ui.field_venue_end_dateedit.setEnabled(True)
        if ui.field_venue_start_dateedit.specialValueText() == " ":
            ui.field_venue_start_dateedit.setDate(QDate.currentDate())
        if ui.field_venue_end_dateedit.specialValueText() == " ":
            ui.field_venue_end_dateedit.setDate(QDate.currentDate())

    else:
        ui.field_venue_start_dateedit.setEnabled(False)
        ui.field_venue_end_dateedit.setEnabled(False)
        ui.field_venue_start_dateedit.setDate(QDate.fromString("0001-01-01", "yyyy-MM-dd"))
        ui.field_venue_end_dateedit.setDate(QDate.fromString("0001-01-01", "yyyy-MM-dd"))




def start_date_changed(ui):
    if ui.field_venue_start_dateedit.date() > ui.field_venue_end_dateedit.date():
        ui.field_venue_end_dateedit.setDate(ui.field_venue_start_dateedit.date())

def end_date_changed(ui):
    if ui.field_venue_start_dateedit.date() > ui.field_venue_end_dateedit.date():
        ui.field_venue_start_dateedit.setDate(ui.field_venue_end_dateedit.date())
        
    
    

def clear_show_fields(ui):
    # show
    ui.field_show_dateedit.setEnabled(False)
    ui.field_show_dateedit.setDate(QDate.fromString("0001-01-01", "yyyy-MM-dd"))

    ui.field_show_id.clear()
    #ui.field_venue_id.clear() # do not clear venue id because it is needed for saving
    ui.field_show_artists.clear()

    ui.field_show_contact.clear()
    ui.field_show_phone.clear()
    ui.field_show_email.clear()

    ui.field_show_tech_contact.clear()
    ui.field_show_tech_phone.clear()
    ui.field_show_tech_email.clear()

    ui.field_show_info.clear()

    ui.field_show_fee.clear()
    ui.field_show_travel_fee.clear()
    ui.field_show_fee_sum.clear()
    ui.field_show_currency.clear()

    ui.field_show_arrival_time.clear()
    ui.field_show_soundcheck_time.clear()
    ui.field_show_opening_time.clear()
    ui.field_show_show_time.clear()

    ui.field_show_food_drinks.clear()
    ui.field_show_accomodation.clear()
    ui.field_show_breakfast.clear()

    ui.field_show_print.clear()
    ui.field_show_print_address.clear()
    ui.field_show_tags.clear()

    # disable folder button
    ui.bt_show_folder.setEnabled(False)

    # disable save, delete and duplicate buttons
    ui.bt_save_show.setEnabled(False)
    ui.bt_delete_show.setEnabled(False)
    ui.bt_duplicate_show.setEnabled(False)
    
    


def clear_venue_fields(ui):
    #venue
    ui.field_venue_name.clear()
    ui.field_venue_city.clear()
    ui.field_venue_country.clear()
    ui.field_venue_address.clear()
    ui.field_venue_geocoordinates.clear()
    ui.field_checkbox_venue_is_event.setChecked(False)

    ui.field_venue_start_dateedit.setDate(QDate.fromString("0001-01-01", "yyyy-MM-dd"))
    ui.field_venue_end_dateedit.setDate(QDate.fromString("0001-01-01", "yyyy-MM-dd"))

    ui.field_venue_website.clear()
    ui.field_venue_genres.clear()
    ui.cb_venue_rating.setCurrentIndex(0)
    ui.field_checkbox_venue_is_discontinued.setChecked(False)
    ui.field_venue_contact.clear()
    ui.field_venue_phone.clear()
    ui.field_venue_email.clear()
    ui.field_venue_info.clear()
    ui.field_venue_tags.clear()

    # disable save and delete buttons
    ui.bt_save_venue.setEnabled(False)
    ui.bt_delete_venue.setEnabled(False)



# copy fields to df_shows
def update_df_shows(ui, df_shows, show_id, copy_venue_info):

    # Save (copy) Venue, City and Country into df_shows (for reference and also NEEDED for the show SEARCH function!) - but only if venue exists
    if copy_venue_info == True:
        df_shows.loc[show_id, "Venue"] = ui.field_venue_name.text()
        df_shows.loc[show_id, "City"] = ui.field_venue_city.text()
        df_shows.loc[show_id, "Country"] = ui.field_venue_country.text()


    # Save all show fields (except ShowID because it is new generated on each loading)
    df_shows.loc[show_id, "Date"] = ui.field_show_dateedit.date().toString("yyyy-MM-dd")

    df_shows.loc[show_id, "VenueID"] = int(ui.field_venue_id.text())
    df_shows.loc[show_id, "Status"] = int(ui.cb_show_status.currentIndex()) # status index
    df_shows.loc[show_id, "StatusText"] = ui.cb_show_status.currentText() # save status text for csv readability - not used in app
    df_shows.loc[show_id, "Artists"] = ui.field_show_artists.text()

    df_shows.loc[show_id, "Contact"] = ui.field_show_contact.text()
    df_shows.loc[show_id, "Phone"] = ui.field_show_phone.text()
    df_shows.loc[show_id, "Email"] = ui.field_show_email.text()

    df_shows.loc[show_id, "TechContact"] = ui.field_show_tech_contact.text()
    df_shows.loc[show_id, "TechPhone"] = ui.field_show_tech_phone.text()
    df_shows.loc[show_id, "TechEmail"] = ui.field_show_tech_email.text()

    df_shows.loc[show_id, "Info"] = ui.field_show_info.toPlainText()

    df_shows.loc[show_id, "Fee"] = float(ui.field_show_fee.text()) if ui.field_show_fee.text() != "" else 0
    df_shows.loc[show_id, "TravelFee"] = float(ui.field_show_travel_fee.text()) if ui.field_show_travel_fee.text() != "" else 0
    df_shows.loc[show_id, "Currency"] = ui.field_show_currency.text()

    df_shows.loc[show_id, "ArrivalTime"] = ui.field_show_arrival_time.text()
    df_shows.loc[show_id, "SoundcheckTime"] = ui.field_show_soundcheck_time.text()
    df_shows.loc[show_id, "OpeningTime"] = ui.field_show_opening_time.text()
    df_shows.loc[show_id, "ShowTime"] = ui.field_show_show_time.text()

    df_shows.loc[show_id, "FoodDrinks"] = ui.field_show_food_drinks.text()
    df_shows.loc[show_id, "Accomodation"] = ui.field_show_accomodation.text()
    df_shows.loc[show_id, "Breakfast"] = ui.field_show_breakfast.text()

    df_shows.loc[show_id, "Print"] = ui.field_show_print.text()
    df_shows.loc[show_id, "PrintAddress"] = ui.field_show_print_address.toPlainText()
    df_shows.loc[show_id, "Tags"] = ui.field_show_tags.text()
    



# copy fields to df_venues
def update_df_venues(ui, df_venues, venue_id):
    df_venues.loc[venue_id, "VenueName"] = ui.field_venue_name.text()
    df_venues.loc[venue_id, "VenueCity"] = ui.field_venue_city.text()
    df_venues.loc[venue_id, "VenueCountry"] = ui.field_venue_country.text()
    df_venues.loc[venue_id, "VenueAddress"] = ui.field_venue_address.toPlainText()
    df_venues.loc[venue_id, "VenueGeoCoordinates"] = ui.field_venue_geocoordinates.text()
    df_venues.loc[venue_id, "VenueIsEvent"] = int(ui.field_checkbox_venue_is_event.isChecked())

    if ui.field_checkbox_venue_is_event.isChecked():
        df_venues.loc[venue_id, "VenueStartDate"] = ui.field_venue_start_dateedit.date().toString("yyyy-MM-dd")
        df_venues.loc[venue_id, "VenueEndDate"] = ui.field_venue_end_dateedit.date().toString("yyyy-MM-dd")
    else:
        df_venues.loc[venue_id, "VenueStartDate"] = ""
        df_venues.loc[venue_id, "VenueEndDate"] = ""


    df_venues.loc[venue_id, "VenueWebsite"] = ui.field_venue_website.text()
    df_venues.loc[venue_id, "VenueGenres"] = ui.field_venue_genres.text()

    df_venues.loc[venue_id, "VenueRating"] = str(ui.cb_venue_rating.currentIndex()) if ui.cb_venue_rating.currentIndex() != 0 else ""

    df_venues.loc[venue_id, "VenueIsDiscontinued"] = int(ui.field_checkbox_venue_is_discontinued.isChecked())
    df_venues.loc[venue_id, "VenueContact"] = ui.field_venue_contact.text()
    df_venues.loc[venue_id, "VenuePhone"] = ui.field_venue_phone.text()
    df_venues.loc[venue_id, "VenueEmail"] = ui.field_venue_email.text()
    df_venues.loc[venue_id, "VenueInfo"] = ui.field_venue_info.toPlainText()
    df_venues.loc[venue_id, "VenueTags"] = ui.field_venue_tags.text()

    df_venues.loc[venue_id, "VenueID"] = venue_id




def get_show_folder_path(selected_show, df_venues, workdir):
    date = selected_show["Date"]
    venue_id = selected_show["VenueID"]

    if venue_id in df_venues["VenueID"]:
        city = df_venues.loc[venue_id]["VenueCity"]
        venue = df_venues.loc[venue_id]["VenueName"]
    else:
        city = selected_show["City"]
        venue = selected_show["Venue"]

    show_folder_path = os.path.join(workdir, "Shows/")
    show_folder = show_folder_path + date + " " + city + " " + venue
    return show_folder



def check_show_folder_exists(ui, selected_show, df_venues, workdir):
    show_folder = get_show_folder_path(selected_show, df_venues, workdir)
    if os.path.isdir(show_folder):
        ui.bt_show_folder.setText("Open Folder")
    else:
        ui.bt_show_folder.setText("Create Folder")


def open_or_create_show_folder(ui, selected_show, df_venues, workdir):
    show_folder = get_show_folder_path(selected_show, df_venues, workdir)
    os.makedirs(show_folder, exist_ok=True)
    open_file_or_folder(show_folder)
    check_show_folder_exists(ui, selected_show, df_venues, workdir)




def open_file_or_folder(path): # cross-platform file and folder opener
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


