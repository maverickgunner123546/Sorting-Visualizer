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
COUNT_SPACE=6
LINE_WIDTH=4

pygame.init()
display_screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Merge Sort")
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

def pivot(arr,low,high):
	
	delay_time=3
	for i in range(low,high+1):
		fun_draw_array(arr,i)
		pygame.display.flip()
		pygame.time.delay(delay_time)
		display_screen.fill(BLACK)
		
	piv=arr[high]
	iter_1=low-1
	
	for i in range(low,high):
		if(arr[i]<=piv):
			iter_1+=1
			arr[iter_1],arr[i]=arr[i],arr[iter_1]
	iter_1+=1
	arr[iter_1],arr[high]=arr[high],arr[iter_1]
	
	
	for i in range(low,high+1):
		fun_draw_array(arr,i)
		pygame.display.flip()
		pygame.time.delay(delay_time)
		display_screen.fill(BLACK)
			
	return iter_1
	
def quick_sort(arr,low,high):
	if(low>=high):
		return
	piv=pivot(arr,low,high)
	
	quick_sort(arr,low,piv-1)
	quick_sort(arr,piv+1,high)

def main():
	arr=[]
	for i in range((int)(SCREEN_WIDTH/COUNT_SPACE)):
		arr.append(random.randint(20,BASE_LINE_Y))	
		
	quick_sort(arr,0,len(arr)-1)
	for i in range(0,len(arr)):
			fun_draw_array_final(arr,i)
			pygame.display.flip()
			pygame.time.delay(3)
	fun_draw_array(arr,-1)
	fun_events()

main()
