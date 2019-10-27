#The_Dark_Web_Links_Project
import time
banner ="""
		====================================================
		==[+]Hello And Wellcome to #the_dark_web_links_prj
		==[*]Telegram:DID_Family 
		==[*]Instagram:sweet.dre3m
		====================================================
		[+]Select What Do You Want :
		[1]Shops
		[2]Mail
		[3]Search_Engine
		[4]Upload
		[5]Chatrooms
		[6]Dir(Directory)
		[7]Forum
		[8]Hosting
		[99]Exit
	"""
while True:
	print(banner)
	Shops_l = open("shop.txt","r")
	Mail_l = open("mail.txt","r")
	Search_Engine_l = open("search.txt","r")
	Upload_l = open("upload.txt","r")
	Chatrooms_l = open("chat.txt","r")
	Dir_l = open("dir.txt",'r')
	Forum_l = open("forum.txt","r")
	Host_l = open("host.txt","r") 
	q = 99
	try :
		t_l = int(input('~> '))
		print("[*]Wait...")
		time.sleep(2)
		if t_l == 1 :
			print(Shops_l.read())
		elif t_l == 2 :
			print(Mail_l.read())
		elif t_l == 3 :
			print(Search_Engine_l.read())
		elif t_l == 4 :
			print(Upload_l.read())
		elif t_l == 5 :
			print(Chatrooms_l.read())
		elif t_l == 6 :
			print(Dir_l.read())
		elif t_l == 7 :
			print(Forum_l.read())
		elif t_l == 8 :
			print(Host_l.read())
		elif t_l == (q) :
			break
		else :
			print("Wrong Number!")
	except ValueError:
		print("0ops ! That was no valid number.Try again...")
	print("[$]GoodLuck")
