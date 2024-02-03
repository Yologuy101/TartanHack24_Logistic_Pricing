from cmu_graphics import *
from PIL import Image
import os, pathlib


class Button:
    def __init__(self, width_scalar, height_scalar, width, height, color, pressed):
        # Scalars to dynamically adjust position based on app dimensions
        self.width_scalar = width_scalar
        self.height_scalar = height_scalar
        self.width = width
        self.height = height
        self.color = color
        self.pressed = pressed
        # Initial position will be set based on app dimensions in update_position
        self.centerX = None
        self.centerY = None

    def update_position(self, app_width, app_height, pressed):
        # Dynamically calculate position based on current app dimensions
        self.centerX = app_width * self.width_scalar
        self.centerY = app_height * self.height_scalar
        self.pressed = pressed

    def draw(self):
        if self.centerX is not None and self.centerY is not None:
            drawRect(self.centerX, self.centerY, self.width, self.height, fill=self.color, align='center')
            drawCircle(self.centerX - self.width/2, self.centerY, self.height/2, fill=self.color)
            drawCircle(self.centerX + self.width/2, self.centerY, self.height/2, fill=self.color)
            drawLabel("Submit", self.centerX, self.centerY, size=16, fill='white', bold=True, font="montserrat")


    def in_button(self, mouseX, mouseY):
        if self.centerX is None or self.centerY is None:
            return False
        mouseX_in_bounds = self.centerX - self.width/2 <= mouseX <= self.centerX + self.width/2
        mouseY_in_bounds = self.centerY - self.height/2 <= mouseY <= self.centerY + self.height/2
        if mouseX_in_bounds and mouseY_in_bounds:
            self.color = 'lightBlue'
        return mouseX_in_bounds and mouseY_in_bounds

class Text_box:
    def __init__(self, width_scalar, height_scalar, width, height, query, response, pressed):
        # Scalars to dynamically adjust position based on app dimensions
        self.width_scalar = width_scalar
        self.height_scalar = height_scalar
        self.width = width
        self.height = height
        self.query = query
        self.response = response
        self.pressed = pressed
        # Initial position will be set based on app dimensions in update_position
        self.centerX = None
        self.centerY = None

    def update_position(self, app_width, app_height, pressed, response):
        # Dynamically calculate position based on current app dimensions
        self.centerX = app_width * self.width_scalar
        self.centerY = app_height * self.height_scalar
        self.pressed = pressed
        self.response = response

    def draw(self):
        if self.centerX is not None and self.centerY is not None:
            #outside
            drawRect(self.centerX, self.centerY, self.width, self.height, fill='gray', align='center')
            drawCircle(self.centerX - self.width/2, self.centerY, self.height/2, fill='gray')
            drawCircle(self.centerX + self.width/2, self.centerY, self.height/2, fill='gray')

            #inside
            inside_scalar = 0.95
            drawRect(self.centerX, self.centerY, self.width * inside_scalar, 
                     self.height * inside_scalar, fill='white', align='center')
            drawCircle(self.centerX - self.width/2, self.centerY, self.height/2 * inside_scalar, fill='white')
            drawCircle(self.centerX + self.width/2, self.centerY, self.height/2 * inside_scalar, fill='white')

            #query label
            centerY_scalar = 1.1
            drawLabel(self.query, self.centerX - self.width/2, self.centerY - self.height * centerY_scalar, 
                      size = 16, bold = True, font = "montserrat", align = 'left-top')
            
            #response label
            drawLabel(self.response, self.centerX - self.width/2, self.centerY - self.height / 5, 
                      size = 20, bold = True, fill = 'gray', font = "montserrat", align = 'left-top')
            
            if self.pressed:
                base_offset = 2  # Adjust this to move the initial cursor position to the right
                char_width = 10.1  # Increase this value to better match the average character width of your font
                cursorX = self.centerX - self.width / 2 + base_offset + len(self.response) * char_width
                drawLine(cursorX, self.centerY - 10, cursorX, self.centerY + 10, fill='black', lineWidth=2)

    def in_box(self, mouseX, mouseY):
        if self.centerX is None or self.centerY is None:
            return False
        mouseX_in_bounds = self.centerX - self.width/2 <= mouseX <= self.centerX + self.width/2
        mouseY_in_bounds = self.centerY - self.height/2 <= mouseY <= self.centerY + self.height/2
        return mouseX_in_bounds and mouseY_in_bounds

class Output_box:
    def __init__(self, width_scalar, height_scalar, width, height, title, value):
        # Scalars to dynamically adjust position based on app dimensions
        self.width_scalar = width_scalar
        self.height_scalar = height_scalar
        self.width = width
        self.height = height
        self.title = title
        self.value = value
        # Initial position will be set based on app dimensions in update_position
        self.centerX = None
        self.centerY = None

    def update_position(self, app_width, app_height, value):
        # Dynamically calculate position based on current app dimensions
        self.centerX = app_width * self.width_scalar
        self.centerY = app_height * self.height_scalar
        self.value = value

    def draw(self):
        if self.centerX is not None and self.centerY is not None:

            output_box_left_circle_centerX = self.centerX - self.width/2
            output_box_left_circle_radius = self.height/2

            output_box_right_circle_centerX = self.centerX + self.width/2
            output_box_right_circle_radius = self.height/2

            drawRect(self.centerX, self.centerY, self.width, self.height, fill='gray', align='center')
            drawCircle(output_box_left_circle_centerX, self.centerY, output_box_left_circle_radius, fill='gray')
            drawCircle(output_box_right_circle_centerX, self.centerY, output_box_right_circle_radius, fill='gray')

            #title label
            centerY_scalar = 1.1
            output_titles_centerX = self.centerX - self.width/2
            output_titles_centerY = self.centerY - self.height * centerY_scalar
            drawLabel(self.title, output_titles_centerX, output_titles_centerY, 
                      size = 16, bold = True, font = "montserrat", align = 'left-top')
            
            #value label
            output_values_centerX = self.centerX - self.width/2
            output_values_centerY = self.centerY - self.height / 5
            drawLabel(self.value, output_values_centerX, output_values_centerY, 
                      size = 20, bold = True, fill = 'white', font = "montserrat", align = 'left-top')
            

  
def pressing_events(mouseX, mouseY):
    if app.submit_button.in_button(mouseX, mouseY): 
        app.submitted = True
        app.from_location_pressed = False
        app.to_location_pressed = False
        app.cargo_weight_pressed = False
        app.cargo_volume_pressed = False
        app.cargo_value_pressed = False
        app.deliver_by_date_pressed = False
        app.deliver_by_time_pressed = False
    elif app.from_location_text_box.in_box(mouseX, mouseY):
        app.from_location_pressed = True
        app.to_location_pressed = False
        app.cargo_weight_pressed = False
        app.cargo_volume_pressed = False
        app.cargo_value_pressed = False
        app.deliver_by_date_pressed = False
        app.deliver_by_time_pressed = False
    elif app.to_location_text_box.in_box(mouseX, mouseY):
        app.to_location_pressed = True
        app.from_location_pressed = False
        app.cargo_weight_pressed = False
        app.cargo_volume_pressed = False
        app.cargo_value_pressed = False
        app.deliver_by_date_pressed = False
        app.deliver_by_time_pressed = False
    elif app.cargo_weight_text_box.in_box(mouseX, mouseY):
        app.cargo_weight_pressed = True
        app.from_location_pressed = False
        app.to_location_pressed = False
        app.cargo_volume_pressed = False
        app.cargo_value_pressed = False
        app.deliver_by_date_pressed = False
        app.deliver_by_time_pressed = False
    elif app.cargo_volume_text_box.in_box(mouseX, mouseY):
        app.cargo_volume_pressed = True
        app.from_location_pressed = False
        app.to_location_pressed = False
        app.cargo_weight_pressed = False
        app.cargo_value_pressed = False
        app.deliver_by_date_pressed = False
        app.deliver_by_time_pressed = False
    elif app.cargo_value_text_box.in_box(mouseX, mouseY):
        app.cargo_value_pressed = True
        app.from_location_pressed = False
        app.to_location_pressed = False
        app.cargo_weight_pressed = False
        app.cargo_volume_pressed = False
        app.deliver_by_date_pressed = False
        app.deliver_by_time_pressed = False
    elif app.deliver_by_date_text_box.in_box(mouseX, mouseY):
        app.deliver_by_date_pressed = True
        app.from_location_pressed = False
        app.to_location_pressed = False
        app.cargo_weight_pressed = False
        app.cargo_volume_pressed = False
        app.cargo_value_pressed = False
        app.deliver_by_time_pressed = False
    elif app.deliver_by_time_text_box.in_box(mouseX, mouseY):
        app.deliver_by_time_pressed = True
        app.from_location_pressed = False
        app.to_location_pressed = False
        app.cargo_weight_pressed = False
        app.cargo_volume_pressed = False
        app.cargo_value_pressed = False
        app.deliver_by_date_pressed = False
    else:
        app.from_location_pressed = False
        app.to_location_pressed = False
        app.cargo_weight_pressed = False
        app.cargo_volume_pressed = False
        app.cargo_value_pressed = False
        app.deliver_by_date_pressed = False
        app.deliver_by_time_pressed = False

def key_events(key):
    if app.from_location_pressed:
        if key == 'space':
            app.from_location_response += ' '
        elif key == "backspace":
            app.from_location_response = app.from_location_response[:-1]
        elif key == 'enter':
            app.from_location_pressed = False
        else:
            app.from_location_response += key
    if app.to_location_pressed:
        if key == 'space':
            app.to_location_response += ' '
        elif key == "backspace":
            app.to_location_response = app.to_location_response[:-1]
        elif key == 'enter':
            app.to_location_pressed = False
        else:
            app.to_location_response += key
    if app.cargo_weight_pressed:
        if key == 'space':
            app.cargo_weight_response += ' '
        elif key == "backspace":
            app.cargo_weight_response = app.cargo_weight_response[:-1]
        elif key == 'enter':
            app.cargo_weight_pressed = False
        else:
            app.cargo_weight_response += key
    if app.cargo_volume_pressed:
        if key == 'space':
            app.cargo_volume_response += ' '
        elif key == "backspace":
            app.cargo_volume_response = app.cargo_volume_response[:-1]
        elif key == 'enter':
            app.cargo_volume_pressed = False
        else:
            app.cargo_volume_response += key
    if app.cargo_value_pressed:
        if key == 'space':
            app.cargo_value_response += ' '
        elif key == "backspace":
            app.cargo_value_response = app.cargo_value_response[:-1]
        elif key == 'enter':
            app.cargo_value_pressed = False
        else:
            app.cargo_value_response += key
    if app.deliver_by_date_pressed:
        if key == 'space':
            app.deliver_by_date_response += ' '
        elif key == 'backspace':
            app.deliver_by_date_response = app.deliver_by_date_response[:-1]
        elif key == 'enter':
            app.deliver_by_date_pressed = False
        else:
            app.deliver_by_date_response += key
    if app.deliver_by_time_pressed:
        if key == 'space':
            app.deliver_by_time_response += ' '
        elif key == 'backspace':
            app.deliver_by_time_response = app.deliver_by_time_response[:-1]
        elif key == 'enter':
            app.deliver_by_time_pressed = False
        else:
            app.deliver_by_time_response += key

def openImage(fileName):
    return Image.open(os.path.join(pathlib.Path(__file__).parent, fileName))