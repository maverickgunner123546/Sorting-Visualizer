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
COUNT_SPACE=4
LINE_WIDTH=2

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
	
	
def merge_all(arr,low,high,mid):
	
	delay_time=3
	for i in range(low,high+1):
		fun_draw_array(arr,i)
		pygame.display.flip()
		pygame.time.delay(delay_time)
		display_screen.fill(BLACK)
			
	arr_1=[]
	arr_2=[]
		
	for i in range(low,mid+1):
		arr_1.append(arr[i])
	for i in range(mid+1,high+1):
		arr_2.append(arr[i])
		
	
	iter_1=0
	iter_2=0
	iter_n=low
	while(iter_1<len(arr_1) and iter_2<len(arr_2)):
		if(arr_1[iter_1]<arr_2[iter_2]):
			arr[iter_n]=arr_1[iter_1]
			iter_1+=1
			iter_n+=1
		else:
			arr[iter_n]=arr_2[iter_2]
			iter_n+=1
			iter_2+=1
			
	while(iter_1<len(arr_1)):
		arr[iter_n]=arr_1[iter_1]
		iter_1+=1
		iter_n+=1
	while(iter_2<len(arr_2)):
		arr[iter_n]=arr_2[iter_2]
		iter_2+=1
		iter_n+=1
	
	if(low!=0 and high!=len(arr)-1):
		for i in range(low,high+1):
			fun_draw_array(arr,i)
			pygame.display.flip()
			pygame.time.delay(delay_time)
			display_screen.fill(BLACK)
	
def merge_sort(arr,low,high):
	
	if(low>=high):
		return 
	
	mid=(int)((low+high)/2)
	merge_sort(arr,low,mid)
	merge_sort(arr,mid+1,high)
	merge_all(arr,low,high,mid)

def main():
	
	arr=[]
	for i in range((int)(SCREEN_WIDTH/COUNT_SPACE)):
		arr.append(random.randint(20,BASE_LINE_Y-100))	
		
	merge_sort(arr,0,len(arr)-1);
	for i in range(0,len(arr)):
			fun_draw_array_final(arr,i)
			pygame.display.flip()
			pygame.time.delay(3)
	fun_draw_array(arr,-1)
	fun_events()

main()
