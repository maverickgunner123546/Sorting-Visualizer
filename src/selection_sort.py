import pygame
import random

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
SCREEN_WIDTH=1100
SCREEN_HEIGHT=600
LINE_SPACE=8
LINE_WIDTH=6
BASE_LINE=500

pygame.init()
display_screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Selection Sort")
display_screen.fill(WHITE)


def fun_events():
	running=True
	while(running):
		for event in pygame.event.get():
			if(event.type==pygame.QUIT):
				running=False
		pygame.display.flip()
		

def fun_draw_array_1(arr,j):
	for i in range(len(arr)):
		pygame.draw.line(display_screen,WHITE if i!=j else BLACK,(LINE_SPACE+LINE_SPACE*i,BASE_LINE),(LINE_SPACE+LINE_SPACE*i,BASE_LINE-arr[i]),LINE_WIDTH)
	pygame.draw.line(display_screen,BLACK,(0,BASE_LINE),(SCREEN_WIDTH,BASE_LINE),5)


def fun_draw_array_2(arr,j):
	for i in range(len(arr)):
		pygame.draw.line(display_screen,WHITE if i>j else GREEN,(LINE_SPACE+i*LINE_SPACE,BASE_LINE),(LINE_SPACE+i*LINE_SPACE,BASE_LINE-arr[i]),LINE_WIDTH)
	pygame.draw.line(display_screen,BLACK,(0,BASE_LINE),(SCREEN_WIDTH,BASE_LINE),5)


def fun_insertion_sort():
	arr=[]
	for i in range((int)(SCREEN_WIDTH/LINE_SPACE)):
		arr.append(random.randint(20,BASE_LINE-100))	
	for i in range(len(arr)):
		min_ind=i
		min_ele=arr[i]
		for j in range(i,len(arr)):
			if(min_ele>arr[j]):
				min_ind=j
				min_ele=arr[j]
			fun_draw_array_1(arr,j)
			pygame.display.flip()
			pygame.time.delay(3)
			display_screen.fill(BLACK)
		arr[i],arr[min_ind]=arr[min_ind],arr[i]
	for i in range(len(arr)):
		fun_draw_array_2(arr,i)
		pygame.display.flip()
		pygame.time.delay(10)
		display_screen.fill(BLACK)
	fun_draw_array_1(arr,-1)


def main():
	fun_insertion_sort()
	fun_events()
	
main()
