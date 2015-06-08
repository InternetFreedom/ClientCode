# This is a updated version of software as a distributed proxy

import urllib, urllib2
import os
import subprocess
from subprocess import Popen, PIPE
from sys import stdout
from cStringIO import StringIO
import sys
import time
import select
import pygeoip
import webbrowser
import pexpect
import findip

# Check proxy option first
def check_proxy(filename):
	f = open(filename)
	proxy_option = f.readlines()[1].strip()
	f.close()
	if proxy_option == '1' or proxy_option == '2':
		proxy_label = proxy_option
	elif proxy_option == '3':
		print '-'*80
		print 'Since you will be provided with a safe proxy from our address pool, we would like to know if you want to be one of our proxies. NOTE that you will be secure to be the proxy, because there will be an additional layer between you and the one who browses through you. We will appreciate a lot for your contribution! :)'
		print '-'*80
		print 'Please choose if you want to be one of the proxies and input 1 or 2:'
		print '1 Yes, for this time'
		print '2 No, for this time'
		proxy_label = raw_input()
	else: 
		proxy_label = '1'
	return proxy_label

# Read the real country
def read_real_country(filename):
	f = open(filename)
	real_country = f.readlines()[0].strip()
	f.close()
	return real_country

# Map IP address with country code
def report_country(my_ip):
	gi = pygeoip.GeoIP(os.path.dirname(os.path.realpath(__file__)) + '/GeoIP.dat')
	geo_code = gi.country_code_by_addr(my_ip)
	return geo_code

# Map country code to numbers
def map_code_to_country(code):
	if code == 'BJ':
		number = '1'
	elif code == 'BF':
		number = '2'
	elif code == 'CM':
		number = '3'
	elif code == 'TD':
		number = '4'
	elif code == 'CI':
		number = '5'
	elif code == 'DJ':
		number = '6'
	elif code == 'FR':
		number = '7'
	elif code == 'GQ':
		number = '8'
	elif code == 'GM':
		number = '9'
	elif code == 'GN':
		number = '10'
	elif code == 'LR':
		number = '11'
	elif code == 'NL':
		number = '12'
	elif code == 'NG':
		number = '13'
	elif code == 'NO':
		number = '14'
	elif code == 'SN':
		number = '15'
	elif code == 'TG':
		number = '16'
	elif code == 'UG':
		number = '17'
	elif code == 'GA':
		number = '18'
	elif code == 'CF':
		number = '19'
	elif code == 'US':
		number = '20'
	else:
		number = '21'
	return number

# Go online to grab client's external IP address
#def report_ip():
#	my_ip = urllib.urlopen('http://curlmyip.com/').read()
#	return my_ip.strip()

# Write user information to a file
def write_client_info(real_country, chosen_country, written_ip, my_speed):
	f = open("client_info.txt","w")
	f.write(real_country + '+' + chosen_country + '+' + written_ip + '+' + my_speed)
	f.close()

# Parse the user speed from file
def find_speed(filename):
	f = open(filename)
	data = f.readlines()
	f.close()
	string_tmp = data[-1].strip()
	index1 = string_tmp.find('M')
	for i in range(index1+6,len(string_tmp)):
		if string_tmp[i] != ' ':
			index2 = i
			break
		else:
			pass
	index3 = string_tmp.find(r'/')
	speed = string_tmp[index2:index3-6].strip()     ##### For real environment use
	return speed

#launch with mozilla
def launch(workingurl):
	if workingurl:
		try:
			browser = webbrowser.get('firefox')
			browser.open(workingurl)
		except Exception as e3:
			print e3

def ask_home_country():
	a = 0
	while (a == 0):
		a = 1
		print "Please enter the number of your home country:"
		print u"S'il vous pla\u00eet entrer le num\u00e9ro de votre pays d'origine:\n"

		print u"\t1  - BENIN                     | B\u00c9NIN"
		print "\t2  - BURKINA FASO              | BURKINA FASO"
		print "\t3  - CAMEROON                  | CAMEROUN"
		print "\t4  - CHAD                      | TCHAD"
		print "\t5  - IVORY COAST               | COTE D'IVOIRE"
		print "\t6  - DJIBOUTI                  | DJIBOUTI"
		print "\t7  - FRANCE                    | FRANCE"
		print u"\t8  - EQUATORIAL GUINEA         | GUIN\u00c9E \u00c9QUATORIALE"
		print "\t9  - GAMBIA                    | GAMBIE"
		print u"\t10 - GUINEA CONAKRY            | GUIN\u00c9E CONAKRY"
		print "\t11 - LIBERIA                   | LIBERIA"
		print "\t12 - NETHERLANDS               | PAYS-BAS"
		print "\t13 - NIGERIA                   | NIGERIA"
		print u"\t14 - NORWAY                    | NORV\u00c9GE"
		print u"\t15 - SENEGAL                   | S\u00c9N\u00c9GAL"
		print "\t16 - TOGO                      | TOGO"
		print "\t17 - UGANDA                    | OUGANDA"
		print "\t18 - GABON                     | GABON"
		print u"\t19 - CENTRAL AFRICAN REPUBLIC  | R\u00c9PUBLIQUE CENTRAFRICAINE"
		print "\t20 - US                        | US"

		value = input("number|nombre:")
		if (value == 1):
			print u"BENIN | B\u00c9NIN"
			sts = "BENIN"
		elif (value == 2):
			print "BURKINA FASO | BURKINA FASO"
			sts = "BURKINA FASO"
		elif (value == 3):
			print "CAMEROON | CAMEROUN"
			sts = "CAMEROON"
		elif (value == 4):
			print "CHAD | TCHAD"
			sts = "CAMEROON"
		elif (value == 5):
			print "IVORY COAST | COTE D'IVOIRE"
			sts = "IVORY COAST"
		elif (value == 6):
			print "DJIBOUTI | DJIBOUTI"
			sts = "DJIBOUTI"
		elif (value == 7):
			print "FRANCE | FRANCE"
			sts = "FRANCE"
		elif (value == 8):
			print u"EQUATORIAL GUINEA | GUIN\u00c9E \u00c9QUATORIALE"
			sts = "EQUATORIAL GUINEA"
		elif (value == 9):
			print "GAMBIA | GAMBIE"
			sts = "GAMBIA"
		elif (value == 10):
			print u"GUINEA CONAKRY | GUIN\u00c9E CONAKRY"
			sts = "GUINEA CONAKRY"
		elif (value == 11):
			print "LIBERIA | LIBERIA"
			sts = "LIBERIA"
		elif (value == 12):
			print "NETHERLANDS | PAYS-BAS"
			sts = "NETHERLANDS"
		elif (value == 13):
			print "NIGERIA | NIGERIA"
			sts = "NIGERIA"
		elif (value == 14):
			print u"NORWAY | NORV\u00c9GE"
			sts = "NORWAY"
		elif (value == 15):
			print u"SENEGAL | S\u00c9N\u00c9GAL"
			sts = "SENEGAL"
		elif (value == 16):
			print "TOGO | TOGO"
			sts = "TOGO"
		elif (value == 17):
			print "UGANDA | OUGANDA"
			sts = "UGANDA"
		elif (value == 18):
			print "GABON | GABON"
			sts = "GABON"
		elif (value == 19):
			print u"CENTRAL AFRICAN REPUBLIC | R\u00c9PUBLIQUE CENTRAFRICAINE"
			sts = "CENTRAL AFRICAN REPUBLIC"
		elif (value == 20):
			print "US | US"
			sts = "US"
		else:
			print "\n\nSorry, that was not recognized. Please try again."
			print u"D\u00e9sol\u00e9, ce n'\u00e9tait pas reconnu. S'il vous pla\u00eet essayez de nouveau.\n"
			a = 0
	return value


def volunteer_proxy():
	print '-'*80
	print 'Since you will be provided with a safe proxy from our address pool, we would like to know if you want to be one of our proxies. NOTE that you will be secure to be the proxy, because there will be an additional layer between you and the one who browses through you. We will appreciate a lot for your contribution! :)'
	print '-'*80
	print 'Please choose if you want to be one of the proxies and input 1 2 or 3:'
	print '1 Yes always'
	print '2 No always'
	print '3 Let me decide at each session'
	usr_input = raw_input()
	return usr_input

def reset_firefox(working_url):
	# Locate the filename of firefox
	home_dir = os.getenv("HOME")
	f = open(home_dir+'/.mozilla/firefox/profiles.ini')
	data = f.readlines()
	f.close()
	for i in range(0, len(data)):
		if data[i].startswith("Path="):
			filename = data[i][5:].strip()
	# Find if there is an entry with newtab config
	f = open(home_dir+'/.mozilla/firefox/' + filename + '/prefs.js')
	line = f.readlines()
	f.close()
	flag = 0
	for i in range(0, len(line)):
		if "browser.newtab.url" in line[i]:
			line[i] = ''
			line[i] = "user_pref(\"browser.newtab.url\", \"" + working_url + "\");" + "\n"
			flag = 1
	if flag == 1:
		f = open(home_dir+'/.mozilla/firefox/' + filename + '/prefs.js', 'w')
		f.writelines(["%s\n" % item  for item in line])
		f.close()
	else:
		f = open(home_dir+'/.mozilla/firefox/' + filename + '/prefs.js', 'a')
		f.write("user_pref(\"browser.newtab.url\", \"" + working_url + "\");");
		f.close()

# Start main function
if __name__ == '__main__':

	print '-'*80
	print 'Welcome to our distributed proxy system!'
	print '-'*80
	if not os.path.exists('option.txt'):
		# Write the home country to the first line in file 'option.txt'
		home_country = ask_home_country()
		# Write the proxy option to the second line in file 'option.txt'
		usr_input = volunteer_proxy()
	
		f = open('option.txt', "w")
		f.write(str(home_country) + '\n' + usr_input)
		f.close()

	# Some parameters
	info_filename = 'option.txt'
	real_domain_file = 'domain.txt'
	speed_filename = 'speed.txt'
	ssh_name_filename = 'username.txt'

	f = open(real_domain_file)
	real_domain = f.readlines()[0].strip()
	f.close()

	f = open(ssh_name_filename)
	username = f.readlines()[0].strip()
	f.close()

	# Check the proxy option first
	proxy_label = check_proxy(info_filename)

	# Report the country you are NOT at right now (using negative survey to parse)
	real_country = read_real_country(info_filename)
	my_ip = findip.globalip()  # get global Ip
        my_localip = findip.localip() # get local IP
	chosen_country = map_code_to_country(report_country(my_ip))

	# Also wirte IP address into the client_info file (yes-real_ip;no-fake_ip)
	if proxy_label == '1':
				if str(my_ip)==str(my_localip):
					written_ip = my_ip
					subprocess.call(['./proxy.sh'])
				else:
					print '-'*80
					print("Info: It looks like you don't use static IP address. We will not use you as a proxy. Thank you.")
					written_ip = '0.0.0.0'
	else:
		written_ip = '0.0.0.0'

	# Copy the ssh keys to the home directory
	home_dir = os.getenv("HOME")
	working_dir = os.path.dirname(os.path.realpath(__file__))
	os.system('tar -xzf ssh.tar.gz')
	os.system('cp -r ' + working_dir+ '/.ssh ' + home_dir)

	
	finished = False
	trycount = 5
	while not(finished) and trycount:
		trycount -= 1
		# Start Iodine client
		print '-' * 80
		print 'Prepare to set up DNS tunnel between client and server!'
		print '-' * 80
		password = real_domain.replace(".", "")
		iodine_cmd = ["sudo", "iodine", "-P", password, "-r", real_domain]
		p = Popen(iodine_cmd,stdout=PIPE, stderr=PIPE)

		while True:
			read = p.stderr.readline()
			sys.stderr.write(read)
			if read == 'Connection setup complete, transmitting data.'+'\n':
				print '-' * 80
				print 'DNS tunnel is set up between client and server!'
				print 'Please wait! The server will assign proxies to you soon!'
				print '-' * 80
				os.system('iperf -c 192.168.99.1 -f M > ' + speed_filename)
				my_speed = find_speed(speed_filename)
				write_client_info(real_country, chosen_country, written_ip, my_speed)
				finished = False
				while not finished:
					os.system("scp client_info.txt " + username + "@192.168.99.1:/home/" + username + "/user_data")
					# Wait until server puts the file in the destination folder
					flag = 0
					while flag == 0:
						try:
							command = pexpect.spawn('scp ' + username + '@192.168.99.1:/home/' + username+ '/proxy_data/proxy.txt .')
					 		if not command.expect("proxy.txt                                     100%"):
								flag = 1
								print 'Proxy address is assigned!'
						except:
							time.sleep(1)

					#os.system("scp " + username + "@192.168.99.1:/home/" + username + "/proxy_data/proxy.txt .")
					f = open("proxy.txt","r")
					line = f.readlines()
					url1 = line[0].strip()
					url2 = line[1].strip()
					f.close()
					try:
						file = urllib2.urlopen(url1)
						reset_firefox(url1)
						launch(url1)# launch with mozilla or default system browser
						os.system('pkill terminal')
						finished = True
					except Exception as e:
						print "proxy1 is not available" #For debugging
						try:
							file = urllib2.urlopen(url2)
							reset_firefox(url2)
							launch(url2)# launch with mozilla or default system browser
							os.system('pkill terminal')
							finished = True
						except Exception as e1:
							print "proxy2 is not available" # for debugging
							print "None of the two urls worked! Please wait to try again!"
							print '-' * 80
							finished = False
					if finished == True:
						os.system("rm proxy.txt")
						os.system("rm speed.txt")
						os.system("rm client_info.txt")
	if not(trycount):
		print "\n"
		print "Sorry! We could not find a proxy for you. Please, try again later."
		os.system('pkill terminal')



