import tkinter,random

class game():
	def __init__(self):

		self.canvasWidth = 500
		self.canvasHeight = 700

		self.canvas = tkinter.Canvas(width = self.canvasWidth, height = self.canvasHeight, bg = 'white')
		self.canvas.pack()

		self.n = 0
		self._n = 0
		self.number_of_blocks = 100
		self.blocks = []
		self.move_blocks = []

		self.grid()
		self.rand_block2()

		self.canvas.bind_all('<a>',self.movea)
		self.canvas.bind_all('<s>',self.moves)
		self.canvas.bind_all('<d>',self.moved)
		self.canvas.bind_all('<f>',self.movef)

		self.canvas.mainloop()

	def movea(self,event):
		self.number = 0
		self.block_move()

	def moves(self,event):
		self.number = 1
		self.block_move()

	def moved(self,event):
		self.number = 2
		self.block_move()

	def movef(self,event):
		self.number = 3
		self.block_move()

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
		self.x1 = [self.canvasWidth/2/2 - 3, self.canvasWidth/2 - 3, self.canvasWidth/2/2 + self.canvasWidth/2 - 3, self.canvasWidth - 3]
		self.x2 = [6,self.canvasWidth/2/2 + 3, self.canvasWidth/2 + 3, self.canvasWidth/2/2 + self.canvasWidth/2 + 3]
		self.y1 = [self.canvasHeight - 3]
		self.y2 = [self.canvasHeight/2/2 + self.canvasHeight/2 + 3]	

		for i in range(self.number_of_blocks):
			self.i1 = random.randrange(len(self.x1))	
			self.canvas.create_rectangle(self.x1[self.i1], self.y1[0], self.x2[self.i1], self.y2[0], fill='black', tags=['block' +str(self._n), 'blocks'])
			self.y1.insert(0, self.y1[0] - self.canvasHeight/2/2)
			self.y2.insert(0, self.y2[0] - self.canvasHeight/2/2)
			self.move_blocks.append(self.i1)
			self._n += 1

	def block_move(self):
		if self.number == self.move_blocks[self.n]:
			self.canvas.delete('block' +str(self.n))
			self.canvas.move('blocks', 0, + self.canvasHeight/2/2)

		else:
			self.canvas.delete('all')

		self.n += 1
game()
