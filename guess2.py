#import random #import是进口，载入 random 是随机的意思 
#是python里面的功能之一；属于standard library里面的功能之一 
#random 是module（模组） 是一个python文档
#package（套件） 打包很多模组 叫做套件
#r = random.randint(1, 100) #randint = random +integer（整数）
#设计一个猜数字的程式
import random
start = input('请决定随机数字范围开始值：')
end = input('请决定随机数字范围结束值：')
start = int (start)
end = int (end)
r = random. randint(start, end)
count = 0 
while True:
	count += 1 # count = count +1 是一样的意思 简写的方式
	m = input('请猜数字：')
	m = int(m)
	if m == r :
		print('恭喜你猜对了！')
		print('这是你猜的第', count ,'次')
		break
	elif m > r :
		print('你猜的大了')
	elif m < r :
		print('你猜的小了')
	print('这是你猜的第', count ,'次')



	
