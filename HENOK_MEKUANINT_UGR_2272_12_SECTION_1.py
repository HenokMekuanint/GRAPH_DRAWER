import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np
import sys
storecommand=[]
storename=[]
def Command1():
    storecommand.append(1)
    storename.append("=> Y= X^3 ")
def Command2():
    storecommand.append(2)
    storename.append("=> Y = SIN( X )")
def Command3():
    storecommand.append(3)
    storename.append("=> Y = X^2")
def Command4():
    storecommand.append(4)
    storename.append("= > Y = tan( X )")
def Command5():
    storecommand.append(5)
    storename.append("=> Y = COS( X )")

def Command6():
    storecommand.append(6)
    storename.append("=> Y= abs ( X ) ")
    
pygame.font.init()
font=pygame.font.Font("freesansbold.ttf",20)
def displaytext1():
    text=font.render("please select two graphs to be plotted by clicking",True,(255,255,255))
    display.blit(text,(50,10))
def displaytext4():
    text=font.render(" the white buttons",True,(255,255,255))
    display.blit(text,(50,30))
def displaytext2():
    text=font.render(storename[0],True,(255,255,255))
    display.blit(text,(200,60))
def displaytext3():
    text=font.render(storename[1],True,(255,255,255))
    display.blit(text,(200,90))
class buttons:
    def __init__(self,width,height,graph,position1,position2,command):
        self.command=command
        self.bg=pygame.Rect(position1,position2,width,height)
        pygame.font.init()
        self.font=pygame.font.SysFont("Algerian",20)
        self.buttontext=self.font.render(graph,True,(0,0,0))
    def new(self,mouseposition):
        if self.bg.collidepoint(mouseposition):
            self.command()

    def generate(self,display):
        pygame.draw.rect(display,(255,255,255),self.bg)
        self.position=self.buttontext.get_rect(center=(self.bg.x+self.bg.width/2,self.bg.y+self.bg.height/2))
        display.blit(self.buttontext,self.position) 

button1=buttons(120,40,"Y= X^3",50 ,150,Command1)
button2=buttons(120,40,"Y= Sin( X )",200 ,150,Command2)
button3=buttons(120,40,"Y=X^2",350 ,150,Command3)
button4=buttons(120,40,"X=Y^2",50 ,250,Command4)
button5=buttons(130,40,"Y=COS( X )",200 ,250,Command5)
button6=buttons(120,40,"Y=abs( X )",350 ,250,Command6)






display=pygame.display.set_mode((600,600))

def init():
    display = pygame.display.set_mode((600,600), DOUBLEBUF|OPENGL)
    gluOrtho2D(-10.0, 10.0,-10.0, 10.0)

    
def draw():
    


    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    x= np.linspace(-10,10,100)
    glColor3f(1,1,1)
    f=np.zeros(x.size)
    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    for a,b in zip(x,f):
        glVertex2f(a,b)

    glEnd()



    glColor3f(1,1,1)
    f=np.zeros(x.size)
    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    for a,b in zip(f,x):
        glVertex2f(a,b)

    glEnd()

    #the other functions goes here
    def func1():
        glColor3f(1.0,0,0)

        y=np.power(x,3) 
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        for a,b in zip(x,y):
            glVertex2f(a,b)

        glEnd()

    def func2():
        glColor3f(0,1.0,0)
        y=np.sin(x) 
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        for a,b in zip(x,y):
            glVertex2f(a,b)

        glEnd()

    def func3():
        glColor3f(0,0,1.0)
        y=np.power(x,2) 
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        for a,b in zip(x,y):
            glVertex2f(a,b)

        glEnd()

    def func4():
        glColor3f(1.0,1.0,0)
        y= np.linspace(-10,10,100)
        x=np.power(y,2) 
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        for a,b in zip(x,y):
            glVertex2f(a,b)

        glEnd()

    def func5():
        glColor3f(1.0,0,1.0)
        y=np.cos(x) 
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        for a,b in zip(x,y):
            glVertex2f(a,b)

        glEnd()

    def func6():
        x= np.linspace(-10,10,100)
        glColor3f(0,1.0,1.0)
        y=np.abs(x) 
        glPointSize(10)
        glBegin(GL_LINE_STRIP)
        for a,b in zip(x,y):
            glVertex2f(a,b)
        glEnd()

    dict={1:func1,2:func2,3:func3,4:func4,5:func5,6:func6}
    dict[storecommand[0]]()
    dict[storecommand[1]]()
    glFlush()   

def main():
    pygame.init()
    running=True
    

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                button1.new(pygame.mouse.get_pos())
                button2.new(pygame.mouse.get_pos())
                button3.new(pygame.mouse.get_pos())
                button4.new(pygame.mouse.get_pos())
                button5.new(pygame.mouse.get_pos())
                button6.new(pygame.mouse.get_pos())





        button1.generate(display)
        button2.generate(display)
        button3.generate(display)
        button4.generate(display)
        button5.generate(display)
        button6.generate(display)
        if len(storename)==0:
            displaytext1()
            displaytext4()
        elif len(storename)==1:
            displaytext2()

        if len(storename)==2:
            storecommand.clear
            break
        pygame.display.flip()
        pygame.time.wait(10)
        
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        draw()
        pygame.display.flip()
        pygame.time.wait(10)
         

main()