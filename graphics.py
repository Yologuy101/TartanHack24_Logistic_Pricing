from cmu_graphics import *
from graphics_utils import Button, Text_box, Output_box

def load_graphics():
  #submit button
  ############################################

  app.submitted = False
  submit_button_centerX_scalar = 0.5
  submit_button_centerY_scalar = 0.9
  submit_button_width = app.width * 0.3
  submit_button_height = app.height * 0.1
  app.submit_button = Button(submit_button_centerX_scalar, submit_button_centerY_scalar, 
                              submit_button_width, submit_button_height, 'blue', app.submitted)
  
  
  #text boxes
  #############################################

  #from location text box
  app.from_location_pressed = False
  app.from_location_response = ''
  from_location_text_box_centerX_scalar = 0.15
  from_location_text_box_centerY_scalar = 0.35
  from_location_text_box_width = app.width * 0.5
  from_location_text_box_height = app.height * 0.1
  app.from_location_text_box = Text_box(from_location_text_box_centerX_scalar, from_location_text_box_centerY_scalar,
                                        from_location_text_box_width, from_location_text_box_height, 
                                        "Shipping From (city)", app.from_location_response, app.from_location_pressed)

  #to location text box
  app.to_location_pressed = False
  app.to_location_response = ''
  to_location_text_box_centerX_scalar = 0.4
  to_location_text_box_centerY_scalar = 0.35
  to_location_text_box_width = app.width * 0.5
  to_location_text_box_height = app.height * 0.1
  app.to_location_text_box = Text_box(to_location_text_box_centerX_scalar, to_location_text_box_centerY_scalar,
                                        to_location_text_box_width, to_location_text_box_height, 
                                        "Shipping To (city)", app.to_location_response, app.to_location_pressed)
  
  #cargo weight text box
  app.cargo_weight_pressed = False
  app.cargo_weight_response = ''
  cargo_weight_text_box_centerX_scalar = 0.15
  cargo_weight_text_box_centerY_scalar = 0.55
  cargo_weight_text_box_width = app.width * 0.5
  cargo_weight_text_box_height = app.height * 0.1
  app.cargo_weight_text_box = Text_box(cargo_weight_text_box_centerX_scalar, cargo_weight_text_box_centerY_scalar,
                                        cargo_weight_text_box_width, cargo_weight_text_box_height, 
                                        "Cargo Weight (lbs)", app.cargo_weight_response, app.cargo_weight_pressed)
  
  #cargo volume text box
  app.cargo_volume_pressed = False
  app.cargo_volume_response = ''
  cargo_volume_text_box_centerX_scalar = 0.4
  cargo_volume_text_box_centerY_scalar = 0.55
  cargo_volume_text_box_width = app.width * 0.5
  cargo_volume_text_box_height = app.height * 0.1
  app.cargo_volume_text_box = Text_box(cargo_volume_text_box_centerX_scalar, cargo_volume_text_box_centerY_scalar,
                                        cargo_volume_text_box_width, cargo_volume_text_box_height, 
                                        "Cargo Volume (cubic feet)", app.cargo_volume_response, app.cargo_volume_pressed)

  #cargo value text box
  app.cargo_value_pressed = False
  app.cargo_value_response = ''
  cargo_value_text_box_centerX_scalar = 0.15
  cargo_value_text_box_centerY_scalar = 0.65
  cargo_value_text_box_width = app.width * 0.5
  cargo_value_text_box_height = app.height * 0.1
  app.cargo_value_text_box = Text_box(cargo_value_text_box_centerX_scalar, cargo_value_text_box_centerY_scalar,
                                        cargo_value_text_box_width, cargo_value_text_box_height, 
                                        "Cargo Value (USD)", app.cargo_value_response, app.cargo_value_pressed)
  
  #deliver by date text box
  app.deliver_by_date_pressed = False
  app.deliver_by_date_response = ''
  deliver_by_date_text_box_centerX_scalar = 0.15
  deliver_by_date_text_box_centerY_scalar = 0.8
  deliver_by_date_text_box_width = app.width * 0.5
  deliver_by_date_text_box_height = app.height * 0.1
  app.deliver_by_date_text_box = Text_box(deliver_by_date_text_box_centerX_scalar, deliver_by_date_text_box_centerY_scalar,
                                        deliver_by_date_text_box_width, deliver_by_date_text_box_height, 
                                        "Deliver by date", app.deliver_by_date_response, app.deliver_by_date_pressed)
  
  #deliver by time text box
  app.deliver_by_time_pressed = False
  app.deliver_by_time_response = ''
  deliver_by_time_text_box_centerX_scalar = 0.4
  deliver_by_time_text_box_centerY_scalar = 0.8
  deliver_by_time_text_box_width = app.width * 0.5
  deliver_by_time_text_box_height = app.height * 0.1
  app.deliver_by_time_text_box = Text_box(deliver_by_time_text_box_centerX_scalar, deliver_by_time_text_box_centerY_scalar,
                                        deliver_by_time_text_box_width, deliver_by_time_text_box_height, 
                                        "Deliver by time", app.deliver_by_time_response, app.deliver_by_time_pressed)
  

  #output boxes
  ############################################

  #predicted trip duration
  app.predicted_trip_duration_value = 'test'
  predicted_trip_duration_centerX_scalar = 0.6
  predicted_trip_duration_centerY_scalar = 0.35
  predicted_trip_duration_width = app.width * 0.5
  predicted_trip_duration_height = app.height * 0.1
  app.predicted_trip_duration_output_box = Output_box(predicted_trip_duration_centerX_scalar, predicted_trip_duration_centerY_scalar,
                                                  predicted_trip_duration_width, predicted_trip_duration_height,
                                                  "Predicted Trip Duration (hours)", app.predicted_trip_duration_value)
  
  #length of route
  app.length_of_route_value = 'test'
  length_of_route_centerX_scalar = 0.8
  length_of_route_centerY_scalar = 0.35
  length_of_route_width = app.width * 0.5
  length_of_route_height = app.height * 0.1
  app.length_of_route_output_box = Output_box(length_of_route_centerX_scalar, length_of_route_centerY_scalar,
                                                  length_of_route_width, length_of_route_height,
                                                  "Length of Route (miles)", app.length_of_route_value)
  
  #optimal leave time
  app.optimal_leave_time_value = 'test'
  optimal_leave_time_centerX_scalar = 0.6
  optimal_leave_time_centerY_scalar = 0.45
  optimal_leave_time_width = app.width * 0.5
  optimal_leave_time_height = app.height * 0.1
  app.optimal_leave_time_output_box = Output_box(optimal_leave_time_centerX_scalar, optimal_leave_time_centerY_scalar,
                                                  optimal_leave_time_width, optimal_leave_time_height,
                                                  "Optimal Leave Time", app.optimal_leave_time_value)
  
  #GPS route data
  app.gps_route_data_value = 'test'
  gps_route_data_centerX_scalar = 0.8
  gps_route_data_centerY_scalar = 0.45
  gps_route_data_width = app.width * 0.5
  gps_route_data_height = app.height * 0.1
  app.gps_route_data_output_box = Output_box(gps_route_data_centerX_scalar, gps_route_data_centerY_scalar,
                                                  gps_route_data_width, gps_route_data_height,
                                                  "GPS Route Data (points per mile)", app.gps_route_data_value)
  
  #Predicted weather
  app.predicted_weather_value = 'test'
  predicted_weather_centerX_scalar = 0.6
  predicted_weather_centerY_scalar = 0.55
  predicted_weather_width = app.width * 0.5
  predicted_weather_height = app.height * 0.1
  app.predicted_weather_output_box = Output_box(predicted_weather_centerX_scalar, predicted_weather_centerY_scalar,
                                                  predicted_weather_width, predicted_weather_height,
                                                  "Predicted Weather Conditions", app.predicted_weather_value)
  
  #predicted # of accidents
  app.predicted_accidents_value = 'test'
  predicted_accidents_centerX_scalar = 0.8
  predicted_accidents_centerY_scalar = 0.55
  predicted_accidents_width = app.width * 0.5
  predicted_accidents_height = app.height * 0.1
  app.predicted_accidents_output_box = Output_box(predicted_accidents_centerX_scalar, predicted_accidents_centerY_scalar,
                                                  predicted_accidents_width, predicted_accidents_height,
                                                  "Predicted # of Accidents", app.predicted_accidents_value)

  #risk assessment
  app.risk_assessment_value = 'test'
  risk_assessment_centerX_scalar = 0.6
  risk_assessment_centerY_scalar = 0.8
  risk_assessment_width = app.width * 0.5
  risk_assessment_height = app.height * 0.1
  app.risk_assessment_output_box = Output_box(risk_assessment_centerX_scalar, risk_assessment_centerY_scalar,
                                                  risk_assessment_width, risk_assessment_height,
                                                  "Risk Assessment (-1, 1)", app.risk_assessment_value)
  
  #recommended pricing 
  app.recommended_pricing_value = 'test'
  recommended_pricing_centerX_scalar = 0.8
  recommended_pricing_centerY_scalar = 0.8
  recommended_pricing_width = app.width * 0.5
  recommended_pricing_height = app.height * 0.1
  app.recommended_pricing_output_box = Output_box(recommended_pricing_centerX_scalar, recommended_pricing_centerY_scalar,
                                                  recommended_pricing_width, recommended_pricing_height,
                                                  "Recommended Pricing (USD)", app.recommended_pricing_value)


def top_bar_draw():
  #scalar inits
  top_bar_centerX_scalar = 0.5
  top_bar_centerY_scalar = 0.1
  top_bar_width_scalar = 0.9
  top_bar_height_scalar = 0.1

  #vars
  top_bar_centerX = app.width * top_bar_centerX_scalar
  top_bar_centerY = app.height * top_bar_centerY_scalar
  top_bar_width = app.width * top_bar_width_scalar
  top_bar_height = app.height * top_bar_height_scalar

  #drawing 
  drawRect(top_bar_centerX, top_bar_centerY, top_bar_width, top_bar_height, fill = 'gray', align = 'center') 
  drawCircle(top_bar_centerX - top_bar_width/2, top_bar_centerY, top_bar_height/2, fill = 'gray')
  drawCircle(top_bar_centerX + top_bar_width/2, top_bar_centerY, top_bar_height/2, fill = 'gray')

def background_draw():
  #scalar inits
  background_centerX_scalar = 0.5
  background_centerY_scalar = 0.6
  background_width_scalar = 0.9
  background_height_scalar = 0.7
  background_opacity = 25

  #vars
  background_centerX = app.width * background_centerX_scalar
  background_centerY = app.height * background_centerY_scalar
  background_width = app.width * background_width_scalar
  background_height = app.height * background_height_scalar

  #drawing
  drawRect(background_centerX, background_centerY, background_width, background_height, 
           fill = 'gray', align = 'center', opacity = background_opacity)
  
def text_box_draw():
  #text input boxes
  #########################
  
  #from location
  app.from_location_text_box.update_position(app.width, app.height, app.from_location_pressed, app.from_location_response)
  app.from_location_text_box.draw()

  #to location
  app.to_location_text_box.update_position(app.width, app.height, app.to_location_pressed, app.to_location_response)
  app.to_location_text_box.draw()

  #cargo weight
  app.cargo_weight_text_box.update_position(app.width, app.height, app.cargo_weight_pressed, app.cargo_weight_response)
  app.cargo_weight_text_box.draw()

  #cargo volume
  app.cargo_volume_text_box.update_position(app.width, app.height, app.cargo_volume_pressed, app.cargo_volume_response)
  app.cargo_volume_text_box.draw()

  #cargo value
  app.cargo_value_text_box.update_position(app.width, app.height, app.cargo_value_pressed, app.cargo_value_response)
  app.cargo_value_text_box.draw()

  #Deliver by (date)
  app.deliver_by_date_text_box.update_position(app.width, app.height, app.deliver_by_date_pressed, app.deliver_by_date_response)
  app.deliver_by_date_text_box.draw()

  #Deliver by (time)
  app.deliver_by_time_text_box.update_position(app.width, app.height, app.deliver_by_time_pressed, app.deliver_by_time_response)
  app.deliver_by_time_text_box.draw()

def output_draw():
  #center line draw
  center_line_x1 = app.width / 2
  center_line_y1 = app.height * .3
  center_line_x2 = app.width /2 
  center_line_y2 = app.height * .85
  drawLine(center_line_x1, center_line_y1, center_line_x2, center_line_y2, fill='gray', lineWidth=4)

  #Predicted trip duration
  app.predicted_trip_duration_output_box.update_position(app.width, app.height, app.predicted_trip_duration_value)
  app.predicted_trip_duration_output_box.draw()

  #length of route
  app.length_of_route_output_box.update_position(app.width, app.height, app.length_of_route_value)
  app.length_of_route_output_box.draw()

  #optimal leave time
  app.optimal_leave_time_output_box.update_position(app.width, app.height, app.optimal_leave_time_value)
  app.optimal_leave_time_output_box.draw()

  #GPS route data
  app.gps_route_data_output_box.update_position(app.width, app.height, app.gps_route_data_value)
  app.gps_route_data_output_box.draw()

  #predicted weather
  app.predicted_weather_output_box.update_position(app.width, app.height, app.predicted_weather_value)
  app.predicted_weather_output_box.draw()

  #predicted # of accidents
  app.predicted_accidents_output_box.update_position(app.width, app.height, app.predicted_accidents_value)
  app.predicted_accidents_output_box.draw()

  #risk assessment
  app.risk_assessment_output_box.update_position(app.width, app.height, app.risk_assessment_value)
  app.risk_assessment_output_box.draw()

  #recommended pricing
  app.recommended_pricing_output_box.update_position(app.width, app.height, app.recommended_pricing_value)
  app.recommended_pricing_output_box.draw()


