import pygame,time,random



##creating the screen and sizes
X = 400
Y = 400
pygame.init()
display_surface = pygame.display.set_mode((X, Y))

##creating title
pygame.display.set_caption("input abc")


##colors
black=(0,0,0)
red=(220,0,0)
green = (0, 255, 0)
blue=(0,0,180)
white = (255, 255, 255)
yellow=(255,255,0)
font = pygame.font.Font('freesansbold.ttf', 32)


##classes

class timer:
    def __init__(self):
        self.clock_a=0##saves the start time
        self.clock_b=0##saves the current time
    def start_clock(self):
        self.clock_a = time.time()
        self.clock_b = time.time()
    def update_clock(self):
        self.clock_b=time.time()
    def reset_clock(self):
        self.clock_a = 0
        self.clock_b = 0
    def backward_clock(self):
        format_float = "{:.2f}".format(15-(self.clock_b - self.clock_a))
        return format_float
    def show_clock(self):
        format_float = "{:.2f}".format(self.clock_b-self.clock_a)
        return (format_float)


class array(timer):
   pass
   def __init__(self):
       super().__init__()
       self.pos=0
       self.arr=[]
       self.first_time=True
       self.count_letters=0


   def init_array(self):##create abc array
       ch = 'a'
       self.pos = ord(ch)
       while ch != 'z':
           self.arr.append(ch)
           self.pos += 1
           ch = chr(self.pos)
       self.arr.append(ch)

   def reset_game(self):
       self.pos=0
       self.count_letters = 0
       self.reset_clock()
       self.start_clock()


   def Create_Text(self, num):
       if num == 1:
           ##creating text on screen
           text_abc = font.render(self.arr[self.pos], True, red, black)
           textRect = text_abc.get_rect()
           textRect.center = (X // 2, Y // 2)
           display_surface.fill(black)
           display_surface.blit(text_abc, textRect)

           ##creating timer on screen
           obj.update_clock()
           text_timer = font.render(str(self.show_clock()), True, green, black)
           textRect = text_timer.get_rect()
           textRect.center = (50, 50)
           display_surface.blit(text_timer, textRect)

       elif num == 2:
           ##creating text on screen
           text_abc = font.render(self.arr[self.pos], True, red, black)
           textRect = text_abc.get_rect()
           textRect.center = (X // 2, Y // 2)
           display_surface.fill(black)
           display_surface.blit(text_abc, textRect)

           ##creating timer on screen
           self.update_clock()
           text_timer = font.render(str(self.backward_clock()), True, green, black)
           textRect = text_timer.get_rect()
           textRect.center = (50, 50)
           display_surface.blit(text_timer, textRect)

           ##creating counter on screen
           text_counter = font.render(str(self.count_letters), True, green, black)
           textRect = text_counter.get_rect()
           textRect.center = (300, 50)
           display_surface.blit(text_counter, textRect)

   def event_handler(self, num):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           ##key pressing
           if event.type == pygame.KEYDOWN:
               if num == 1:
                   if pygame.key.name(event.key) == self.arr[self.pos]:

                       self.pos += 1

                   elif pygame.key.name(event.key) == '0':
                       self.reset_game()
               if num == 2:
                   if pygame.key.name(event.key) == self.arr[self.pos]:

                       self.count_letters += 1
                       self.pos = random.randint(0, len(self.arr) - 1)

                   elif pygame.key.name(event.key) == '0':
                       self.reset_game()

   def game(self, num):

       if num == 1:
           self.start_clock()
           self.pos = 0
           while self.pos < 26:
               self.Create_Text(num)

               self.event_handler(num)

               pygame.display.update()
           self.first_time = False
       elif num == 2:
           self.pos = random.randint(0, len(self.arr) - 1)
           self.start_clock()
           while float(self.backward_clock()) > 0:
               self.Create_Text(num)

               self.event_handler(num)

               pygame.display.update()
           self.first_time = False

   def load(self, num):
       ##creating text on screen
       loop = True
       while loop:
           text_abc = font.render("start new game? Y\\N", True, white, black)
           textRect = text_abc.get_rect()
           textRect.center = (X // 2, Y // 2)
           display_surface.fill(black)
           display_surface.blit(text_abc, textRect)
           if obj.first_time == False:

               if num == 1:
                   ##creating timer on screen
                   text_timer = font.render(str(self.show_clock()), True, green, black)
                   textRect = text_timer.get_rect()
                   textRect.center = (50, 50)
                   display_surface.blit(text_timer, textRect)

               if num == 2:
                   ##creating timer and counter on screen
                   text_timer = font.render(str(self.backward_clock()), True, green, black)
                   textRect = text_timer.get_rect()
                   textRect.center = (50, 50)
                   display_surface.blit(text_timer, textRect)

                   text_timer = font.render(str(self.count_letters), True, green, black)
                   textRect = text_timer.get_rect()
                   textRect.center = (300, 50)
                   display_surface.blit(text_timer, textRect)

           pygame.display.update()
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()
               ##key pressing
               if event.type == pygame.KEYDOWN:
                   if pygame.key.name(event.key) == 'y':
                       self.game(num)
                   elif pygame.key.name(event.key) == 'n':
                       obj.reset_clock()
                       obj.first_time = True
                       loop = False

   def main_menu(self):

       while True:
           display_surface.fill(black)
           text_1 = font.render("Choose game:", True, white, black)
           textRect1 = text_1.get_rect()
           textRect1.center = (X // 2, Y // 2 - 75)
           display_surface.blit(text_1, textRect1)

           text_2 = font.render("ABC Speed Run: 1", True, white, black)
           textRect2 = text_2.get_rect()
           textRect2.center = (X // 2, Y // 2 - 25)
           display_surface.blit(text_2, textRect2)

           text_3 = font.render("Random Attack: 2", True, white, black)
           textRect3 = text_3.get_rect()
           textRect3.center = (X // 2, Y // 2 + 25)
           display_surface.blit(text_3, textRect3)

           pygame.display.update()
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()
               ##key pressing
               if event.type == pygame.KEYDOWN:
                   if pygame.key.name(event.key) == '1':
                       self.load(1)
                   elif pygame.key.name(event.key) == '2':
                       self.load(2)


##constant variables:
obj=array()
obj.init_array()
obj.pos=0


obj.main_menu()

