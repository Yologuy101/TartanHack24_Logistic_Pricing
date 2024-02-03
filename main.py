from cmu_graphics import *
from cmu_graphics import CMUImage
from graphics import top_bar_draw, background_draw, load_graphics, text_box_draw, output_draw
from graphics_utils import pressing_events, key_events, openImage

def onAppStart(app):
  load_graphics()

def onAppStep(app):
  pass

def redrawAll(app):
  top_bar_draw()
  background_draw()

  #title
  drawLabel('PLS Logistics Services Contract Risk Assessment & Pricing Model', app.width*0.5, app.height*0.1, 
            fill = 'white', bold = True, font = 'montserrat', size = 30)
  title_image = CMUImage(openImage("pls_logo.png"))
  image_x_reduction_scalar = .08
  image_y_reduction_scalar = .08
  drawImage(title_image,app.width * 0.1, app.height*0.1, width = app.width * image_x_reduction_scalar,
            height = app.height * image_y_reduction_scalar,align="center")

  #submit button
  app.submit_button.update_position(app.width, app.height, app.submitted)
  app.submit_button.draw()

  text_box_draw()

  if app.submitted:
    output_draw()


def onKeyPress(app, key):
  key_events(key)

def onMousePress(app, mouseX, mouseY):
  pressing_events(mouseX, mouseY)



def main():
  runApp()

main()