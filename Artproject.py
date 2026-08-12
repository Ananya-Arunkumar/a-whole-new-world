from tkinter import *  
from random import *

screen = Canvas( Tk(), width=800, height=600, background="white" )

screen.pack()
spacing = 50

#TYPING SHORTCUTS!
oval = screen.create_oval
rect = screen.create_rectangle
line = screen.create_line
poly = screen.create_polygon
text = screen.create_text
arc = screen.create_arc

#SKY
w = 0
h = 30
skyOptions = ["#070B34", "#080a38", "#090c3d", "#0a0e41", "#0b1045",
                "#0d1249", "#0e144d", "#101651", "#121855", "#141a59",
                "#161c5d", "#181e61", "#1a2065", "#1c2269", "#1e246d",
                "#2b2f77", "#3b377d", "#4a3f83", "#594789", "#694f8f",
                "#785795", "#855988"]
for sky in range (1,22):
    skyColour = (skyOptions[sky%22]) 
    screen.create_rectangle (0,w,800,h, fill = skyColour, outline = skyColour)
    w += 30
    h += 30

#STARS
for i in range(250):
    x=randint(0,800)
    y=randint(0,600)
    size=randint(1,2)
    oval(x,y,x+size,y+size,fill="#F8F4EC",outline="#F8F4EC")

#BIG DIPPER
oval(350,153,356,159,fill="#F8F4EC",outline="white",width=1)
oval(360,190,366,196,fill="#F8F4EC",outline="white",width=1)
oval(410,190,416,196,fill="#F8F4EC",outline="white",width=1)
oval(420,153,426,159,fill="#F8F4EC",outline="white",width=1)
oval(330,135,336,141,fill="#F8F4EC",outline="white",width=1)
oval(294,130,300,136,fill="#F8F4EC",outline="white",width=1)
oval(274,130,280,136,fill="#F8F4EC",outline="white",width=1)

#LITTLE DIPPER
oval(350,105,356,111,fill="#F8F4EC",outline="white",width=1)
oval(355,70,361,76,fill="#F8F4EC",outline="white",width=1)
oval(405,85,411,91,fill="#F8F4EC",outline="white",width=1)
oval(399,115,405,121,fill="#F8F4EC",outline="white",width=1)
oval(440,75,446,81,fill="#F8F4EC",outline="white",width=1)
oval(480,75,486,81,fill="#F8F4EC",outline="white",width=1)
oval(500,75,506,81,fill="#F8F4EC",outline="white",width=1)

#MOON
x=randint(50,750)
y=randint(0,150)
oval(x,y,x+135,y+115,fill="#1a1d3a",outline="#1a1d3a", width=1)
oval(x+5,y+5,x+130,y+110,fill="#2b305a",outline="#2b305a", width=1)
oval(x+10,y+10,x+125,y+105,fill="#3d4a80",outline="#3d4a80", width=1)
oval(x+15,y+15,x+120,y+100,fill="#5c7cb5",outline="#5c7cb5", width=1)
oval(x+20,y+20,x+115,y+95,fill="#dce6f2",outline="#dce6f2", width=1)

#FLYING CARPET - OUTSIDE
x=randint(0,750)
y=randint(100,300)

poly(x,y,
        x+80,y-30,
        x+125,y-5,
        x+160,y+5,
        x+220,y+35,
        x+220,y+95,
        x+190,y+75,
        x,y,fill="#4E0E62",outline="#D0AC29",width=2)

#FLYING CARPET - INSIDE
poly(x+20,y,#corner1
        x+80,y-20,#Corner2
        x+125,y+5,
        x+160,y+15,
        x+210,y+40,#Corner3
        x+210,y+80,#Corner4
        x+190,y+65,
        x+20,y,fill="#2D3081",outline="#D0AC29", width=2)
#CARPET DETAILS
arc(x+5,y-5,x+45,y+5,start=-50,extent=90,fill="#D0AC29",outline="#D0AC29")
arc(x+65,y-25,x+95,y-12,start=-145,extent=100,fill="#D0AC29",outline="#D0AC29")
arc(x+195,y+35,x+225,y+45,start=120,extent=150,fill="#D0AC29",outline="#D0AC29")
arc(x+190,y+70,x+220,y+85,start=58,extent=45,fill="#D0AC29",outline="#D0AC29")
line(x+50,y-10,x+210,y+60,fill="#544E91")
poly(x,y,
        x-15,y+10,
        x,y+15,
        x,y,fill="#D0AC29")
poly(x+220,y+95,
        x+235,y+105,
        x+220,y+110,
        x+220,y+95,fill="#D0AC29")

#ROUND CITY OF BAGHDAD
rect(550,450,750,600,fill="#FFFDD0",outline="#FFFDD0",width=1)
rect(545,445,755,450,fill="#FFFDD0",outline="sienna",width=1)
arc(550,375,750,510,start=0,extent=180,fill="#3EB489",outline="#389c7a",width=3)
poly(600,700,
        600,540,
        615,525,
        625,525,
        640,540,
        650,500,
        660,540,
        675,525,
        685,525,
        700,540,
        700,700,fill="sienna",smooth=True)
poly(555,455,
        600,455,
        555,495,
        555,455,fill="#A08B75")
poly(700,455,
        745,455,
        745,498,
        700,455,fill="#A08B75")
rect(560,510,580,600,fill="#A08B75",outline="#A08B75",width=1)
rect(720,510,740,600,fill="#A08B75",outline="#A08B75",width=1)
rect(480,400,515,600,fill="#FFFDD0",outline="black",width=1)
oval(472,350,522,400,fill="#3EB489",outline="#3EB489",width=1)
rect(780,400,815,600,fill="#FFFDD0",outline="black",width=1)
oval(772,350,822,400,fill="#3EB489",outline="#3EB489",width=1)

#ZEUS' TEMPLE
x=255
y=450
gap=52

for n in range(5):
    rect(x,y,x+25,y+200,fill="#E5DCE0",outline="#BAAC8E",width=1)
    x=x+gap
rect(255,580,500,600, fill="#E5DCE0", outline="#E5DCE0", width=1)
rect(250,420,500,450, fill="#E5DCE0", outline="black", width=1)
poly(255,420,
        375,395,
        495,420,fill="#E5DCE0",outline="black",width=1)
x=255
y=450
gap=30
for i in range(5):
    for i in range(5):
        line(x,y,x,y+125,fill="black",width=1)
        x+=5
    x+=gap
    gap-=1
line(250,580,500,580,fill="black")
line(250,450,500,450,fill="black")

#PYRAMIDS OF GIZA
poly(0,600,   
        0,450,
        60,375,
        100,430,
        125,600,fill="#EA914B", outline="#d68845", width=5)
poly(0,600,
        150,350,
        275,600,fill="#EA914B", outline="#d68845", width=5)

x1=20
y1=425
x2=185
y2=425
for n in range(11):
    line(x1,y1,x2,y2,fill="#d68845",width=2)
    y=y+gap
    x1-=20
    x2+=10
    y1+=20
    y2+=20
x1=20
y1=425
for n in range(9):
    line(x1,y1,x1,y1+175,fill="#d68845",width=1)
    x1=x1+20
line(200,450,200,600,fill="#d68845",width=1)
line(225,500,225,600,fill="#d68845",width=1)

#PROGRAMMER TEXT
text(400,275, text="A Whole New World",font="Times 32", fill="white")
text(140,575,text="Made by: Ananya Arunkumar",font="Times 9",fill="white")

mainloop()