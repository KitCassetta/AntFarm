from kivy.app import App # for the main app
from kivy.uix.floatlayout import FloatLayout #the UI layout
from kivy.uix.label import label # a label to show information
from plyer import accelerometer # object to read the accelerometer
from kivy.clock import Clock #clock to schedule method

class UI(FloatLayout): #the app ui
    def __init__(self, **kwargs):
    	super(UI, self).__init__(**kwargs)
    	self.lblAcce = Label(text="Accelerometer: ") # create a label at the center
    	self.add_widget(self.lblAcce) # add the label at the screen
    	try:
    		accelerometer.enable()
    		Clock.schedule_interval(self.update, 1.0/24) # 24 calls per-second
    	except:
    		self.lblAcce.text = "Failed to start accelerometer" #error message


	def update(self, dt):
		txt = ""
		try:
			txt = "Accelerometer:\nX = %.2f\nY = %.2f\nZ = %2.f" %(
					accelerometer.acceleration[0], #read the X value
					accelerometer.acceleration[1], # Y
					accelerometer.acceleration[2]) # Z
		except:
			txt = "Cannot read accelerometer" # error message
		self.lblAcce.text = txt # add the correct text