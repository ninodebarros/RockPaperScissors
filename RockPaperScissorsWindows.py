# RockPaperScissors for Python 3.4- By Nino DeBarros

import winsound #A Windows exclusive module, creates all the beeps and blonks you want!
import tkinter
from tkinter.constants import * 
import time			 
import math
import random   
import os
import turtle	#The turtle graphics module is excellent to use if you want simple graphics to accompany your program.    
oscore = 0
pscore = 0
tscore = 0      #Set up and activate the scoreboard. 
r = 0
p = 0
s = 0
randomthrow = 0

def introsound():
	winsound.Beep(450,250)
	winsound.Beep(450,250)
	winsound.Beep(450,250)
	winsound.Beep(600,600)	

def winnoise():
	winsound.Beep(450,200)
	winsound.Beep(450,300)
	winsound.Beep(650,350)

def losenoise():
	winsound.Beep(600,200)
	winsound.Beep(450,300)
	winsound.Beep(300,350)

def tienoise():
	winsound.Beep(450,600)
	
def randomnoise():
	winsound.Beep(600,150)
	winsound.Beep(450,150)
	winsound.Beep(350,150)
	winsound.Beep(450,150)
	winsound.Beep(600,150)
	winsound.Beep(450,150)
	winsound.Beep(600,150)
	winsound.Beep(450,400)
def scissors():
	turtle.hideturtle()
	turtle.pensize(10)
	turtle.speed(7)
	turtle.pencolor('orange')
	turtle.fd(180)
	turtle.bk(180)
	turtle.lt(35)
	turtle.fd(180)
	turtle.pencolor('black')
	time.sleep(0.25)

def rock():
	turtle.hideturtle()
	turtle.pensize(1)
	turtle.speed(7)
	turtle.color("black")
	turtle.begin_fill()
	turtle.circle(55)
	turtle.end_fill()
	time.sleep(0.25)
	

def paper():
	turtle.hideturtle()
	turtle.pensize(1)
	turtle.speed(7)
	turtle.color('grey')
	turtle.begin_fill()
	for i in range(4):
		turtle.fd(130); turtle.lt(90)
	turtle.end_fill()
	time.sleep(0.25)
	
def versus():
	turtle.hideturtle()
	turtle.pensize(8)
	turtle.speed(6)
	turtle.pencolor('red')
	turtle.lt(60)
	turtle.fd(150)
	turtle.bk(150)
	turtle.lt(60)
	turtle.fd(150)
	turtle.bk(150)
	turtle.rt(120)
	turtle.pensize(1)
	turtle.penup()
	turtle.fd(20)
	turtle.pendown()
	turtle.color('black')
	turtle.begin_fill()
	turtle.circle(2)
	turtle.end_fill()
	turtle.pencolor('black')
	time.sleep(0.75)

def loss():
	turtle.hideturtle()
	turtle.pensize(10)
	turtle.speed(4)
	turtle.bgcolor('grey')
	time.sleep(0.5)
	turtle.pencolor('red')
	turtle.fd(75)
	turtle.bk(75)
	turtle.lt(90)
	turtle.fd(100)
	turtle.pencolor('black')
	time.sleep(1.75)
	turtle.bgcolor('white')

def win():
	turtle.hideturtle()
	turtle.pensize(10)
	turtle.speed(7)
	turtle.bgcolor('grey')
	time.sleep(0.5)
	turtle.pencolor('green')
	turtle.lt(60)
	turtle.fd(130)
	turtle.bk(130)
	turtle.lt(60)
	turtle.fd(130)
	turtle.lt(120)
	turtle.fd(130)
	turtle.rt(120)
	turtle.fd(130)
	turtle.pencolor('black')
	time.sleep(1.75)
	turtle.bgcolor('white')

def tie():
	turtle.hideturtle()
	turtle.pensize(10)
	turtle.speed(7)
	turtle.bgcolor('grey')
	time.sleep(0.5)
	turtle.pencolor('blue')
	turtle.lt(90)
	turtle.fd(100)
	turtle.rt(90)
	turtle.fd(60)
	turtle.bk(120)
	turtle.pencolor('black')
	time.sleep(1.75)
	turtle.bgcolor('white')	

	#Define all of the graphics, which draws not only every player and opponent choice but a versus symbol and the verdict as well.
	
def game(): #Start the game!
	
	print('Please make your command prompt/GUI fullscreen and use two monitors for the best experience!')
	introsound()
	time.sleep(0.8)
	
	os.system('cls')
	global oscore
	global pscore #The variables set up outside of the game() function now exist both outside and inside in this dimension. *cue twilight zone theme*
	global tscore
	global r
	global p
	global s
	global randomthrow
	
	opponent = random.choice([1,2,3])
	  #Decide both the opponents move and the players decision.
	player = input('   _______________________________________________________________________ \n'+
				   '    _   __   __       _    _    _   __  _    __   __   __  __   __   _  __\n' +
	               '   |_| |  | |   |/   |_\  /_\  |_\ |__ |_|  |__  |   ||__ |__  |  | |_||__  \n' +
	               '   | \ |__| |__ |\   |   /   \ |   |__ | \   __| |__ | __| __| |__| | \ __| \n' +
	               '   ------------------------------------------------------------------------ \n' +         
				   '   Type 1 to throw rock, 2 for paper, 3 for scissors, and 4 for a random throw!\n' + 
                                         
				   '   Type 5 for game credits!  \n'+
										
    			   '   Type 6 for rules and instructions! \n'+
                                         
				   '   Type here: ' ) 
	
	player = int(player)

	#Countdown!
	count = 3            
	while (count >= 1):
		print (str(count))
		count = count - 1
		time.sleep(0.75)
	print ('Go!')

	time.sleep(1)
	os.system('cls')
	
	
	if player == 4:
		randomnoise()
		randomthrow = randomthrow + 1
		x = random.choice([1,2,3])
		player = x
		
	
	
	
	if player == 6: #It's good to include instructions no matter how simple or common the game is. A Klingon hacking into your computer from space might never have heard of RPS.
		print('Welcome to RockPaperScissors. The game is very simple.')
		time.sleep(2)
		winsound.Beep(450,200)
		print('You have 3 selections, rock, paper, scissors, 1, 2 , and 3 respectively.')
		time.sleep(2)
		winsound.Beep(450,200)
		print('Rock crushes scissors, Scissors snips paper, and Paper covers rock.')
		time.sleep(2)
		winsound.Beep(450,200)
		print('If two throws are the same, it is a tie.')
		time.sleep(1.75)
		winsound.Beep(450,200)
		print('The opponent is built using the random module, so there is an equal chance to win, lose, or tie. \n'+
		  
			                                           'Good luck!')
		time.sleep(2)
		
		
	if player == 5:
		print('_____________________________________________________________\n'+
		      '  |--.RockPaperScissors by Nino DeBarros,copyright 2015.--| \n'+
		      '-------------------------------------------------------------')
		winsound.Beep(450,200)
		time.sleep(2) 
		print('All rights reserved, RockPaperScissors is a product of Nino.py Inc')
		winsound.Beep(450,200)
		time.sleep(2)
		
		      

#Depending on your choice, the program can run up to 9 possible outcomes.	
	if player == 1 and opponent == 1:
		rock()
		print('You threw rock and the opponent threw...')
		time.sleep(2.5)
		turtle.reset()
		versus()
		time.sleep(1)
		tscore = tscore + 1
		turtle.reset()
		rock()
		time.sleep(1)
		turtle.reset()
		tie()
		turtle.reset()
		r = r + 1
		tienoise()
		print('                                        rock! It is a tie!')
		print('Current score: You: ' + str(pscore) + ' Opponent: ' + str(oscore) + ' Ties: ' + str(tscore))
	
	
	if player == 3 and opponent == 1:
		scissors()	
		print('You threw scissors and the opponent threw... ')
		time.sleep(2.5)
		turtle.reset()
		versus()
		time.sleep(1)
		oscore = oscore + 1
		turtle.reset()
		rock()
		time.sleep(1)
		turtle.reset()
		loss()
		turtle.reset()
		s = s + 1
		losenoise()
		print('                                             rock! You lose.')
		print('Current score: You: ' + str(pscore) + ' Opponent: ' + str(oscore) + ' Ties: ' + str(tscore))
		
	
	if player == 2 and opponent == 1:
		paper()
		print('You threw paper and the opponent threw...')
		time.sleep(2.5)
		turtle.reset()
		versus()
		time.sleep(1)
		pscore = pscore + 1
		turtle.reset()
		rock()
		time.sleep(1)
		turtle.reset()
		win()
		turtle.reset()
		p = p + 1
		winnoise()
		print('                                         rock! You win!')
		print('Current score: You: ' + str(pscore) + ' Opponent: ' + str(oscore) + ' Ties: ' + str(tscore))
		
	if player == 1 and opponent == 3:
		rock()
		print('You threw rock and the opponent threw...')
		time.sleep(2.5)
		turtle.reset()
		versus()
		time.sleep(1)
		pscore = pscore + 1
		turtle.reset()
		scissors()
		time.sleep(1)
		turtle.reset()
		win()
		turtle.reset()
		r = r + 1
		winnoise()
		print('                                        scissors! You win!')
		print('Current score: You: ' + str(pscore) + ' Opponent: ' + str(oscore) + ' Ties: ' + str(tscore))
		
	if player == 3 and opponent == 3:
		scissors()	
		print('You threw scissors and the opponent threw...')
		time.sleep(2.5)
		turtle.reset()
		versus()
		time.sleep(1)
		tscore = tscore + 1
		turtle.reset()
		scissors()
		time.sleep(1)
		turtle.reset()
		tie()
		turtle.reset()
		s = s + 1
		tienoise()
		print('                                            scissors! It is a tie!')
		print('Current score: You: ' + str(pscore) + ' Opponent: ' + str(oscore) + ' Ties: ' + str(tscore))

	if player == 2 and opponent == 3:
		paper()
		print('You threw paper and the opponent threw...')
		time.sleep(2.5)
		turtle.reset()
		versus()
		time.sleep(1)
		oscore = oscore + 1
		turtle.reset()
		scissors()
		time.sleep(1)
		turtle.reset()
		loss()
		turtle.reset()
		p = p + 1
		losenoise()
		print('                                         scissors! You lose.')
		print('Current score: You: ' + str(pscore) + ' Opponent: ' + str(oscore) + ' Ties: ' + str(tscore))

	if player == 1 and opponent == 2:
		rock()
		print('You threw rock and the opponent threw...')
		time.sleep(2.5)
		turtle.reset()
		versus()
		time.sleep(1)
		oscore = oscore + 1
		turtle.reset()
		paper()
		time.sleep(1)
		turtle.reset()
		loss()
		turtle.reset()
		r = r + 1
		losenoise()
		print('                                        paper! You lose.')
		print('Current score: You: ' + str(pscore) + ' Opponent: ' + str(oscore) + ' Ties: ' + str(tscore))

	if player == 3 and opponent == 2:
		scissors()	
		print('You threw scissors and the opponent threw...')
		time.sleep(2.5)
		turtle.reset()
		versus()
		time.sleep(1)
		pscore = pscore + 1
		turtle.reset()
		paper()
		time.sleep(1)
		turtle.reset()
		win()
		turtle.reset()
		s = s + 1
		winnoise()
		print('                                            paper! You win!')
		print('Current score: You: ' + str(pscore) + ' Opponent: ' + str(oscore) + ' Ties: ' + str(tscore))
		 
	if player == 2 and opponent == 2:
		paper()
		print('You threw paper and the opponent threw...')
		time.sleep(2.5)
		turtle.reset()
		versus()
		time.sleep(1)
		tscore = tscore + 1
		turtle.reset()
		paper()
		time.sleep(1)
		turtle.reset()
		tie()
		turtle.reset()
		p = p + 1
		tienoise()
		print('                                         paper! It is a tie!')
		print('Current score: You: ' + str(pscore) + ' Opponent: ' + str(oscore) + ' Ties: ' + str(tscore))
		
	turtle.hideturtle() #This terrapin hides often! I hear he's a bit shy... 
	
	time.sleep(2.15) # The time.sleep function is very good for timed aesthetics. Text that appears all at once is very BASIC. (Pun intended) 
	winsound.Beep(450,200)
	tryagain = input('\n'+
					'Do you want to play again? Press 1 for yes, type 2 to exit: ')	
	
	tryagain = int(tryagain)
	
	if tryagain == 1:
		os.system('cls')
		game()

	if tryagain == 2:
		exit = input('Are you sure you want to exit? Type 1 to play again, type 2 to exit: ')
		exit = int(exit)
	
		if exit == 2:
			time.sleep(1.75)
			turtle.bye() #See ya!
			
		
		if exit == 1:
			time.sleep(1.75)
			os.system('cls')
			game()
			

start = time.time()			
game()
end = time.time() #See how many seconds of your life you have devoted to watching pixels rearrange themselves on a screen! 
elapsed = end - start

if elapsed > 3600:
	print('You played for more than an hour! Wow!')
elif elapsed > 7200:
	print('Maybe it\'s time to take a break...')

print('Results: You threw rock ' + str(r) + ' time(s),')
time.sleep(0.35)
print('				  paper ' + str(p) + ' time(s),') 
time.sleep(0.35)
print('					  scissors ' + str(s) + ' time(s),') 
time.sleep(0.35)
print('						  and made ' + str(randomthrow) + ' random throw(s)!')
time.sleep(0.75) 
rounds = r + p + s                                                                                                                          
print('You played ' + str(rounds) + ' round(s) for ' + str(round(elapsed,1)) + ' seconds, \n'
	'	or more specifically ' + str(elapsed) + ' seconds!')
time.sleep(1.25)
	
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=20)
frame.pack(fill=BOTH,expand=20)
label = tkinter.Label(frame, text="Thanks for playing!")
label.pack(fill=X, expand=20)
button = tkinter.Button(frame,text="Exit", fg = "red",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()

os.system('cls')