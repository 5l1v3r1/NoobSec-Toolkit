#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys, traceback
#Title AREA
print"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print"NOOB Security Toolkit 1.9 - BETA"
print"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print"Dev: The_Chosen_One"
print"~~~~~~~~~~~~~~~~~~~"
#End Of Title Area
#Start Of Options 
print "*****************"
print "Toolkit Options:"
print "*****************"
print "----------------"
print "(sqli)SQL Injector"
print "(vulscan) Vulnerability Scanner"
print "(dinfo) Gather Basic Domain Info"
print "(discover) Information Harvester (Kali Linux Only!)"
print "-----------------"
#Extra Options 
print "******************"
print "Security Options:"
print "******************"
print "(macspoof) Spoof Mac Address"
print "(itor) install Tor"
print "(stor) Start Tor"
print "(tors) Check Tor Status"
print "(vpn) Start VPN Launcher"
print "(encdns) Encrypt DNS"
print "(quit) - (home) - (clear)"
print "--------------------------"
def loopfunc():
	#Script Input
	print ""
	choice = raw_input("What do you want to do?:")

	if choice == "macspoof":
                print "Loading Mac Spoof...."
                cmd1 = os.system ("python scripts/macspoof.py")
                
	if choice == "sqli":
		print "Launching SQLI Injector...."
		cmd1 = os.system ("sudo python scripts/sqli.py")
		
	if choice == "vulscan":
		print "Launching NiktoST.pl...."
		cmd1 = os.system ("sudo python scripts/vulscan.py")

	#Start of Misc Options
	if choice == "itor":
		print"Installing Tor...."
		cmd1 = os.system ("sudo apt-get install tor")
		
	if choice == "stor":
		print "Starting Tor...."
		cmd1 = os.system ("sudo service tor start")
		
	if choice == "tors":
                print "----------------"
                print "Tor Status Check"
                print "----------------"
                cmd1 = os.system ("sudo service tor status")
                
	#if choice == "dvpn":
		#print "Downloading VPN Client to /Bitmask-Linux64-latest....." 
		#cmd1 = os.system ("wget 'https://dl.bitmask.net/client/linux/stable/Bitmask-linux64-latest.tar.bz2'")	
		#cmd1 = os.system ("bzip2 -d Bitmask-linux64-latest.tar.bz2 ")
		#cmd1 = os.system ("tar -xvf Bitmask-linux64-latest.tar")
		
		# Start VPN broken
		
	if choice == "vpn":
		print "Starting VPN Launcher for Bitmask...."
		cmd1 = os.system ("sudo python scripts/vpn.py")

	if choice == "discover":
		print "Launching Discover.... By: Lee Baird"
		cmd1 = os.system ("sudo git clone git://github.com/leebaird/discover.git /opt/discover/")
		cmd1 = os.system ("cd /opt/discover/")
		cmd1 = os.system ("/opt/discover/./discover.sh")	
			

	if choice == "dinfo":
		print "Launching NSlookup Script..."
		cmd1 = os.system ("python scripts/dns.py")
		
	if choice == "encdns":
		print "Launching DNS Encryption Install!....."	
		cmd1 = os.system ("sudo git clone git://github.com/simonclausen/dnscrypt-autoinstall.git dloads/")	
		cmd1 = os.system ("cd scripts/")	
		cmd1 = os.system ("./dloads/dnscrypt-autoinstall.sh")

        if choice == "clear":
                cmd1 = os.system ("clear")
                print "--------------"
                print "Fresh Terminal"
                print "--------------"

        if choice == "home":
                cmd1 = os.system ("python NSToolkit.py")
                

	if choice == "exit" or choice == "quit" or choice == "q":
		sys.exit()
	else:
		print "We are done here!"
		
		loopfunc()
loopfunc()


