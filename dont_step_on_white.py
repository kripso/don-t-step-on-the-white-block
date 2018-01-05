import tkinter,random

class game():
	def __init__(self):

		self.canvasWidth = 500
		self.canvasHeight = 700

		self.canvas = tkinter.Canvas(width = self.canvasWidth, height = self.canvasHeight, bg = 'white')
		self.canvas.pack()

		self.highscore=0
		self.deletableButtons = []
		self.control=0

		self.Start_screen()

		self.canvas.bind_all('<a>',self.movea)
		self.canvas.bind_all('<s>',self.moves)
		self.canvas.bind_all('<d>',self.moved)
		self.canvas.bind_all('<f>',self.movef)

		self.canvas.mainloop()

	def Arcade(self):
		self.canvas.delete('all')

		for button in self.deletableButtons:
			button.destroy()

		self.mode=1

		self.move_blocks = []

		self.number_of_blocks = 1000

		self.n = 0
		self._n = 0
		
		self.time = 0
		self._time = -1

		self.number_of_blocks = 25

		self.grid()
		self.rand_block2()

	def Classic(self):
		self.canvas.delete('all')

		for button in self.deletableButtons:
			button.destroy()

		self.mode=0

		self.move_blocks = []

		self.number_of_blocks = 1000

		self.n = 0
		self._n = 0

		self.actualscore=0

		self.plus_time=25

		self.time=-1
		self._time = -1
		self.grid()
		self.rand_block2()

	def Start_screen(self):

		if self.control == 0:
			self.Start()
		else:
			if self.mode==0:
				self.Start()
				if self.highscore < self.actualscore:
					self.highscore = self.actualscore

				self.canvas.create_text(self.canvasWidth/2, self.canvasHeight/2/2-30, text='High Score: '+str(self.highscore),font= 'Arial 30 bold', fill='black')
				self.canvas.create_text(self.canvasWidth/2, self.canvasHeight/2/2, text='Actual Score: '+str(self.actualscore),font= 'Arial 30 bold', fill='black')
				self.canvas.create_text(self.canvasWidth/2, self.canvasHeight-self.canvasHeight/2/2, text='Game over', font='Arial 40 bold', fill='black')
				self.canvas.update()
			else:
				self.Start()
				self.canvas.create_text(self.canvasWidth/2, self.canvasHeight/2/2, text='time: '+str(self.time),font= 'Arial 30 bold', fill='black')
				if self.win_lose==1:
					self.canvas.create_text(self.canvasWidth / 2, self.canvasHeight - self.canvasHeight / 2 / 2, text='Game over', font='Arial 40 bold', fill='black')
				else:
					self.canvas.create_text(self.canvasWidth / 2, self.canvasHeight - self.canvasHeight / 2 / 2, text='You won', font='Arial 40 bold', fill='black')

		self.canvas.update()

	def Start(self):
		self.canvas.delete('all')
		for button in self.deletableButtons:
			button.destroy()

		button = tkinter.Button (width=15, height=3,  text='Classic mode', font='Arial 15 bold', activeforeground='#1010D2', command=self.Classic)
		button.place (x=self.canvasWidth/2, y=self.canvasHeight/2-35, anchor="c")
		self.deletableButtons.append(button)

		button = tkinter.Button (width=15, height=3,  text='Arcade mode', font='Arial 15 bold', activeforeground='#1010D2', command=self.Arcade)
		button.place (x=self.canvasWidth/2, y=self.canvasHeight/2+35, anchor="c")
		self.deletableButtons.append(button)

	def movea(self,event):
		if self.mode==0:
			self.number = 0
			self.block_move()
		else:
			self.number = 0
			self._block_move()

	def moves(self,event):
		if self.mode==0:
			self.number = 1
			self.block_move()
		else:
			self.number = 1
			self._block_move()

	def moved(self,event):
		if self.mode==0:
			self.number = 2
			self.block_move()
		else:
			self.number = 2
			self._block_move()

	def movef(self,event):
		if self.mode==0:
			self.number = 3
			self.block_move()
		else:
			self.number = 3
			self._block_move()

	def grid(self):
		x = [self.canvasWidth/2, self.canvasWidth/2/2, self.canvasWidth/2/2 + self.canvasWidth/2]
		x1 = [0, self.canvasWidth]
		y = [self.canvasHeight/2, self.canvasHeight/2/2, self.canvasHeight/2/2 + self.canvasHeight/2]
		y1 = [0, self.canvasHeight]

		for i in range(3):
			self.canvas.create_line(x[i], y1[0], x[i], y1[1])
			self.canvas.create_line(x1[0], y[i], x1[1], y[i])

		self.canvas.create_line(0, y1[1], x1[1], y1[1])
		self.canvas.create_line(3, 3, 3, y1[1])
		self.canvas.create_line(3, 3, x1[1], 3)
		self.canvas.create_line(x1[1], 0, x1[1], y1[1])

	def rand_block2(self):
		x1 = [self.canvasWidth/2/2 - 3, self.canvasWidth/2 - 3, self.canvasWidth/2/2 + self.canvasWidth/2 - 3, self.canvasWidth - 3]
		x2 = [6,self.canvasWidth/2/2 + 3, self.canvasWidth/2 + 3, self.canvasWidth/2/2 + self.canvasWidth/2 + 3]
		y1 = [self.canvasHeight - 3]
		y2 = [self.canvasHeight/2/2 + self.canvasHeight/2 + 3]	

		for i in range(self.number_of_blocks):
			i1 = random.randrange(len(x1))	
			self.canvas.create_rectangle(x1[i1], y1[0], x2[i1], y2[0], fill='black', tags=['block' +str(self._n), 'blocks'])
			y1.insert(0, y1[0] - self.canvasHeight/2/2)
			y2.insert(0, y2[0] - self.canvasHeight/2/2)
			self.move_blocks.append(i1)
			self._n += 1

	def block_move(self):
		if self.time>0:
			if self.number == self.move_blocks[self.n] and self.n==self.plus_time:
				self.canvas.delete('block' +str(self.n))
				self.canvas.move('blocks', 0, + self.canvasHeight/2/2)
				self.actualscore+=1	
				self.time+=10
				self.plus_time*=2

			elif self.number == self.move_blocks[self.n]:
				self.canvas.delete('block' +str(self.n))
				self.canvas.move('blocks', 0, + self.canvasHeight/2/2)
				self.actualscore+=1

			else:
				self.control=1
				self.Start_screen()

		elif self._time==-1:
			self.time=10
			self._time = 1
			if self.number == self.move_blocks[self.n]:
				self.canvas.delete('block' +str(self.n))
				self.canvas.move('blocks', 0, + self.canvasHeight/2/2)
				self.actualscore+=1
				self.control=2
				self.timer()
		self.n += 1

	def _block_move(self):
		if self.time>0:
			if self.number == self.move_blocks[self.n] and self.n==self.number_of_blocks-1:
				self.canvas.delete('block' +str(self.n))
				self.canvas.move('blocks', 0, + self.canvasHeight/2/2)
				self.control=1
				self.win_lose=0
				self.Start_screen()

			elif self.number == self.move_blocks[self.n]:
				self.canvas.delete('block' +str(self.n))
				self.canvas.move('blocks', 0, + self.canvasHeight/2/2)

			else:
				self.control=1
				self.win_lose=1
				self.Start_screen()

		elif self._time==-1:
			self.time=10
			self._time = 1
			if self.number == self.move_blocks[self.n]:
				self.canvas.delete('block' +str(self.n))
				self.canvas.move('blocks', 0, + self.canvasHeight/2/2)
				self.control=2
				self._timer()
		self.n += 1

	def _timer(self):
		if self.time<=0:
			self.control=1
			self.win_lose = 1
			self.Start_screen()

		if self.control==2:
			self.canvas.delete('time')
			self.canvas.create_text(self.canvasWidth/2,self.canvasHeight/2/2/2, text='time: ' +str(self.time),font='Arial 30 bold',fill='red',tags='time')
			self.time-=0.5
			self.canvas.after(500,self._timer)

	def timer(self):
		if self.time==-1:
			self.control=1
			self.Start_screen()

		if self.control==2:
			self.canvas.delete('time')
			self.canvas.create_text(self.canvasWidth/2,self.canvasHeight/2/2/2, text='time: ' +str(self.time),font='Arial 30 bold',fill='red',tags='time')
			self.time-=1
			self.canvas.after(1000,self.timer)
game()
