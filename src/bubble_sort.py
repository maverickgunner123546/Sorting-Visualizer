import pygame
import random
import time
GREEN=(0,255,0)
BLUE=(30,30,230)
RED=(230,30,30)
WHITE=(255,255,255)
BLACK=(0,0,30)
SCREEN_WIDTH=1100
SCREEN_HEIGHT=600
BASE_LINE_Y=500
COUNT_SPACE=8
LINE_WIDTH=6

pygame.init()
display_screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Bubble Sort")
display_screen.fill(BLACK)


def fun_events():
	running=True
	while(running):
		for event in pygame.event.get():
			if(event.type==pygame.QUIT):
				running=False
		pygame.display.flip()
		

def fun_draw_array(arr,j):
	for i in range(len(arr)):
		pygame.draw.line(display_screen,WHITE if i!=j else BLACK,(COUNT_SPACE+COUNT_SPACE*i,BASE_LINE_Y),(COUNT_SPACE+COUNT_SPACE*i,BASE_LINE_Y-arr[i]),LINE_WIDTH)
	pygame.draw.line(display_screen,BLACK,(0,BASE_LINE_Y),(SCREEN_WIDTH,BASE_LINE_Y),3)


def fun_draw_array_final(arr,j):
	for i in range(len(arr)):
		pygame.draw.line(display_screen,WHITE if i>j else GREEN,(COUNT_SPACE+COUNT_SPACE*i,BASE_LINE_Y),(COUNT_SPACE+COUNT_SPACE*i,BASE_LINE_Y-arr[i]),LINE_WIDTH)
	pygame.draw.line(display_screen,BLACK,(0,BASE_LINE_Y),(SCREEN_WIDTH,BASE_LINE_Y),3)
		
		
def fun_bubble_sort():
	arr=[]
	for i in range((int)(SCREEN_WIDTH/COUNT_SPACE)):
		arr.append(random.randint(20,BASE_LINE_Y-100))	
	for i in range(len(arr)-1):
		for j in range(len(arr)-1-i):
			fun_draw_array(arr,j)
			pygame.display.flip()
			pygame.time.delay(3)
			display_screen.fill(BLACK)
			if(arr[j]>arr[j+1]):
				arr[j],arr[j+1]=arr[j+1],arr[j]
	for i in range(len(arr)):
			fun_draw_array_final(arr,i)
			pygame.display.flip()
			pygame.time.delay(10)
			display_screen.fill(BLACK);
	fun_draw_array_final(arr,-1)
		
		
"""pygame.draw.line(display_screen,BLACK,(0,500),(800,500),4)
for i in range():
	pygame.draw.line(display_screen,RED,(0+i*20,500),(0+i*20,500-i*10),15)"""
"""fun_draw()"""
def main():
	fun_bubble_sort()
	fun_events()

main()
