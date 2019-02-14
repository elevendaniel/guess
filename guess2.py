#import random #import是进口，载入 random 是随机的意思 
#是python里面的功能之一；属于standard library里面的功能之一 
#random 是module（模组） 是一个python文档
#package（套件） 打包很多模组 叫做套件
#r = random.randint(1, 100) #randint = random +integer（整数）
#设计一个猜数字的程式
import random
r = random. randint(1, 100)
while True:
	m = input('请猜数字：')
	m = int(m)
	if m == r :
		print('恭喜你猜对了！')
		break
	elif m > r :
		print('你猜的大了')
	elif m < r :
		print('你猜的小了')



	
