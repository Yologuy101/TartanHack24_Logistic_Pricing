from cmu_graphics import *

from graphics import top_bar_draw, background_draw, load_graphics, text_box_draw, output_draw, title_draw, output_title_draw
from graphics_utils import pressing_events, key_events
from pathrisk import compute_avg_risk_params, PathRisk
import pandas as pd
from query_path_params import query_average
from get_gps_location import RouteInfo

def onAppStart(app):
  load_graphics()

def onAppStep(app):
  dataset = pd.read_csv("US_Accidents_March23.csv")
  filters = ["Severity", "Start_Time", "End_Time", "Distance(mi)", "State", "Start_Lat", "Start_Lng"]
  risk_avgs = compute_avg_risk_params(app.from_location_text_box.response, app.to_location_text_box.response, dataset, filters)
  risk_avgs_us = query_average()
  avg_crash_severity = risk_avgs[0]
  avg_crash_distance = risk_avgs[1]
  avg_num_acc_per_sq_mile = risk_avgs[2]
  avg_crash_duration = risk_avgs[3]
  num_acc_along_trip = PathRisk(dataset, filters, app.from_location_text_box.response, app.to_location_text_box.response).number_of_accidents_total
  num_acc_per_sq_mile_us_avg = risk_avgs_us["average number of accidents per year"]
  relative_acc_freq = (avg_num_acc_per_sq_mile-num_acc_per_sq_mile_us_avg)/num_acc_per_sq_mile_us_avg
  avg_crash_duration_in_hour = avg_crash_duration / 60
  avg_time_waisted_for_this_trip = avg_crash_duration_in_hour * relative_acc_freq * num_acc_along_trip/(365.25*7)
  avg_money_waisted_for_this_trip = avg_time_waisted_for_this_trip * 63.70 #avg operation cost 
  current_route = RouteInfo(app.from_location_text_box.response, app.to_location_text_box.response)
  route_time = current_route.time_traffic
  route_distance = current_route.distance
  #route_weather_condition= current_route.get_city_weather

  app.predicted_trip_duration_value = route_time
  app.length_of_route_value = route_distance
    

def redrawAll(app):
  top_bar_draw()
  background_draw()
  title_draw()
  

  #submit button
  app.submit_button.update_position(app.width, app.height, app.submitted)
  app.submit_button.draw()

  #drawing input text boxes
  text_box_draw()

  if app.submitted:

    output_draw()
    output_title_draw()

    


def onKeyPress(app, key):
  key_events(key)

def onMousePress(app, mouseX, mouseY):
  pressing_events(mouseX, mouseY)

def onMouseRelease(app, mouseX, mouseY):
  if app.submitted and app.submit_button.in_button(mouseX, mouseY):
    app.submit_button.color = 'Blue'


def main():
  runApp()

main()