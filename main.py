from cmu_graphics import *

from graphics import top_bar_draw, background_draw, load_graphics, text_box_draw, output_draw, title_draw, output_title_draw
from graphics_utils import pressing_events, key_events

def onAppStart(app):
  load_graphics()

def onAppStep(app):
  pass
    

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