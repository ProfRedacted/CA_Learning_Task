import pygame

nonselected_img = pygame.image.load("img/0.png")
selected_img = pygame.image.load("img/1.png")

notselected_width = nonselected_img.get_width()
notselected_height = nonselected_img.get_height()
selected_width = selected_img.get_width()
selected_height = selected_img.get_height()

#button class
class ruleButton():
	def __init__(self, x, y):
		self.image = pygame.transform.scale(nonselected_img, (int(notselected_width * 0.86), int(notselected_height * 0.86)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		self.selected = False


	def toggleOn (self):
		self.image = pygame.transform.scale(selected_img, (int(selected_width * 0.86), int(selected_height * 0.86)))

	def toggleOff (self):
		self.image = pygame.transform.scale(nonselected_img, (int(notselected_width * 0.86), int(notselected_height * 0.86)))


	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))
		

		return action
	

	
