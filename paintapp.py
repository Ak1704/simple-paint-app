from tkinter import *

from tkinter.constants import *

from tkinter.ttk import *

from tkinter.colorchooser import askcolor

from PIL import Image, ImageGrab 

class paintapp(object):
	"""docstring for paintapp"""
	def __init__(self, arg):
		
		super(paintapp, self).__init__()
		self.arg = arg
		
		self.root = Tk()
		self.root.geometry("+100+0")
		self.f = Frame(self.root)


		self.leftf = Frame(self.root)
		
		self.canvas_width = 800
		
		self.canvas_height = 500

		self.ask = None

		self.w = Canvas(self.root, 
		           width=self.canvas_width,
		           height=self.canvas_height)
		
		self.w.pack()
		
		self.v1 = IntVar()

		self.s1 = Scale( self.root, variable = self.v1,  
           from_ = 1, to = 20,  
           orient = HORIZONTAL)  
		self.s1.pack(side=TOP)
		self.color = Button(
			self.f,
			text="color",
			command = self.colors
			)
		
		self.squareb = Button(
			self.f,
			text="square point",
			command = self.square
			)
		self.oval = Button(
			self.f,
			text="oval point",
			command = self.oval
			)
		self.withoutlineb = Button(
			self.f,
			text="With outline",
			command = self.withoutline
			)

		self.saveb = Button(
			self.leftf,
			text="save",
			command = self.save
			)
		self.saveentry = Entry(self.leftf,width = 30) 

		self.saveentry.pack(side=LEFT)
		
		self.saveb.pack()

		self.withoutlineb.pack(side=LEFT)

		self.withline = False

		self.color.pack(side = RIGHT)
		
		self.squareb.pack(side=LEFT)

		self.oval.pack(side=LEFT)
		
		self.shape = "oval"
		
		self.w.bind( "<B1-Motion>", self.paint )
		
		self.python_green = "#476042"

		self.leftf.pack(side=TOP, anchor='w' )

		self.f.pack()
		mainloop()

	def save(self):
		fname = self.saveentry.get()
		box = (self.w.winfo_rootx()+30,self.w.winfo_rooty()-5,self.w.winfo_rootx()+self.canvas_width+100,self.w.winfo_rooty() + self.canvas_height)
		grab = ImageGrab.grab(bbox = box)
		grab.save(fname+".PNG")



	def withoutline(self):

		if self.withline:
			self.withoutlineb.config(text="Without outline")
			self.withline = False

		else:

			self.withline = True

	def colors(self):
		self.ask = askcolor()
	
	def square(self):
		self.shape = "square"
	
	def oval(self):
		self.shape = "oval"
	
	def drawsquare(self):
		try:
			if self.withline:
				self.w.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = self.ask[1])
			else:
				self.w.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = self.ask[1], outline="")
		except:
			if self.withline:
				self.w.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill =self.python_green )
			else:
				self.w.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill = self.python_green, outline="")

	def drawoval(self):
		try:
			if self.withline:
				self.w.create_oval(self.x1, self.y1, self.x2, self.y2, fill = self.ask[1]  )
			else:
				self.w.create_oval(self.x1, self.y1, self.x2, self.y2, fill = self.ask[1] , outline="" )
		except:
			if self.withline:
				self.w.create_oval(self.x1, self.y1, self.x2, self.y2, fill = self.python_green )
			else:
				self.w.create_oval(self.x1, self.y1, self.x2, self.y2, fill = self.python_green , outline="" )


	def paint( self,event ):
		
		self.x1, self.y1 = ( event.x - self.v1.get() ), ( event.y - self.v1.get() )
		self.x2, self.y2 = ( event.x + self.v1.get() ), ( event.y + self.v1.get() )
		
		if self.shape=="oval":
			self.drawoval()

		elif self.shape=="square":
			self.drawsquare()

arg = 0

p = paintapp(arg)

