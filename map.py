import folium
import folium.plugins as plugins


def generate_map_with_venues(df_venues_in_list, homebase_city, homebase_geocoordinates):
    geopos_split = homebase_geocoordinates.split(",")

    # create map with homebase as center point
    m = folium.Map(location=(float(geopos_split[0]), float(geopos_split[1])), zoom_start=6, control_scale=True)

    # add plugins
    folium.plugins.Geocoder().add_to(m)
    #folium.ClickForMarker("${lat}, ${lng}").add_to(self.m)
    #folium.plugins.MousePosition().add_to(self.m)
    #self.m.add_child(folium.plugins.MeasureControl())
    #self.m.add_child(folium.ClickForLatLng(format_str='lat + "," + lng', alert=True)) # use this with webbrowser


    # add homebase marker
    folium.Marker(location=(float(geopos_split[0]), float(geopos_split[1])), icon=folium.Icon(icon="home", color="red"), tooltip=homebase_city + " (Homebase)",
                  popup=folium.Popup("Homebase:<br>" + homebase_city + "<br><br>" + homebase_geocoordinates, max_width=200)).add_to(m)


    # fill all venues markers with coodinates and texts
    for i, row in df_venues_in_list.iterrows():
        geo_coords = row["VenueGeoCoordinates"]
        if geo_coords != "":
            geo_coords_split = geo_coords.split(",")

            popup_text = row["VenueName"]

            if row["VenueIsDiscontinued"] == 1:
                popup_text += " (DISCONTINUED)"

            if row["VenueAddress"] != "":
                popup_text += "<br><br>" + row["VenueAddress"]

            if row["VenueIsEvent"] == 1:
                popup_text += "<br><br>Event: " + row["VenueStartDate"] + " &#8594; " + row["VenueEndDate"]

            if row["VenueGenres"] != "":
                popup_text += "<br><br>Genres: " + row["VenueGenres"]


            folium.Marker(location=(float(geo_coords_split[0]), float(geo_coords_split[1])), tooltip=row["VenueCity"] + " - " + row["VenueName"], popup=folium.Popup(popup_text, max_width=200)).add_to(m)


    # save
    m.save("map.html")
