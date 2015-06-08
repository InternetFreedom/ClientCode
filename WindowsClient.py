# This is a updated version of software as a distributed proxy

import urllib, urllib2
import os
from os.path import expanduser
import sys
import time
import pygeoip
import webbrowser
import subprocess
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
#        try:
#	    my_ip = urllib.urlopen('http://api.ipify.org/').read()
#        except:
#	    my_ip = urllib.urlopen('http://myexternalip.com/raw').read()
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
	temp = os.environ['TEMP']
	# Find if there is an entry with newtab config
	f = open(temp + "\internetcache\Apps\FirefoxPortable\App\DefaultData\profile\prefs.js")
	line = f.readlines()
	f.close()
	flag = 0
	for i in range(0, len(line)):
		if "browser.newtab.url" in line[i]:
			line[i] = ''
			line[i] = "user_pref(\"browser.newtab.url\", \"" + working_url + "\");" + "\n"
			flag = 1
	if flag == 1:
		f = open(temp + "\internetcache\Apps\FirefoxPortable\App\DefaultData\profile\prefs.js", 'w')
		f.writelines(["%s\n" % item  for item in line])
		f.close()
	else:
		f = open(temp + "\internetcache\Apps\FirefoxPortable\App\DefaultData\profile\prefs.js", 'a')
		f.write("user_pref(\"browser.newtab.url\", \"" + working_url + "\");");
		f.close()

#browser = file path to portable browser or browser executable on file system
def launch(url, browserpath, wait=False):
     if os.path.isfile(browserpath):
         p = subprocess.Popen([browserpath, url])
         if wait:
             p.wait()
     else:
         print 'Invalid browser.'  

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

	# Read domain name
	f = open(real_domain_file)
	real_domain = f.readlines()[0].strip()
	f.close()
	password = real_domain.replace(".", "")

	# Generate client dns2tcp files
	f = open('client.bat','w')
	f.write('start dns2tcpc.exe -z ' + real_domain + ' -r ssh -l 2222 -k ifservermooocom' + '\n' + 'exit');
	f.close()
	f = open('iperf_start.bat','w')
	f.write('start dns2tcpc.exe -z ' + real_domain + ' -r tcp -l 8888 -k ifservermooocom' + '\n' + 'exit');
	f.close()

	# Read client account name
	f = open(ssh_name_filename)
	username = f.readlines()[0].strip()
	f.close()

	# Check the proxy option first
	proxy_label = check_proxy(info_filename)

	# Report the country you are NOT at right now (using negative survey to parse)
	real_country = read_real_country(info_filename)
	my_ip = findip.globalip()  # report_ip()
        my_localip = findip.localip()
	chosen_country = map_code_to_country(report_country(my_ip))

	# Also wirte IP address into the client_info file (yes-real_ip;no-fake_ip)
	if proxy_label == '1':
                if str(my_ip)==str(my_localip):
		        written_ip = my_ip
		        os.system("start cmd /k proxy.bat")
                else:
                        print '-'*80
                        print("Info: It looks like you don't use static IP address. We will not use you as a proxy. Thank you.")
                        print '-'*80
                        written_ip = '0.0.0.0'
	else:
		written_ip = '0.0.0.0'
	# Obtain the home directory
	home_dir = expanduser("~")
	working_dir = os.path.dirname(os.path.realpath(__file__))

	finished = False
	trycount = 5
	while not(finished) and trycount:
                os.system('taskkill /IM dns2tcpc.exe >nul 2>&1')                
                trycount -= 1
		# Start Dsn2tcp client
		print '-' * 80
		print 'Prepare to set up DNS tunnel between client and server!'
		print '-' * 80
		os.system('start cmd /k client.bat')
		time.sleep(2)
		
		# Test connection speed with the server
		os.system('start cmd /k iperf_start.bat')
		time.sleep(2)
		speed_finished = False
		while not speed_finished:
			try:
				os.system("iperf.exe -p 8888 -c 127.0.0.1 -f M > " + speed_filename)
				os.system('exit')
				speed_finished = True
			except:
				time.sleep(1)
				
		# Parse the speed file and write to client_info.txt
		my_speed = find_speed(speed_filename)
		write_client_info(real_country, chosen_country, written_ip, my_speed)
		
		# Try scp with the dns tunnel (copy file from client to server)
		scp_finished = False
		while not scp_finished:
			try:
				os.system("pscp.exe -P 2222 -i id_rsa.ppk client_info.txt " + username + "@127.0.0.1:/home/" + username + "/user_data")
				os.system('exit')
				scp_finished = True
			except:
				time.sleep(1)

		# Copy file back from server to client
		if scp_finished:
			time.sleep(2)
			# Try copy the file
			os.system("pscp.exe -P 2222 -i id_rsa.ppk " + username + "@127.0.0.1:/home/"+ username + "/proxy_data/proxy.txt .")
			#os.system('exit')
			start_time = time.time()
			# Keep copying until the file exists locally
			while not os.path.exists(working_dir + '\proxy.txt'):
				if time.time() - start_time > 2:
					try:
						os.system("pscp.exe -P 2222 -i id_rsa.ppk " + username + "@127.0.0.1:/home/"+ username + "/proxy_data/proxy.txt .")
						#os.system('exit')
						start_time = time.time()
					except:
						print 'not there'
						time.sleep(2)
	
		
		if os.path.exists(working_dir + '/proxy.txt'):
			# Try to open the proxy address
			f = open("proxy.txt","r")
			line = f.readlines()
			f.close()
			url1 = line[0].strip()
			url2 = line[1].strip()
			print 'Proxy address is assigned!'
			#print url1
			#print url2
			#path to portable custom browser
			temp = os.environ['TEMP']
			browserpath = temp + "\internetcache\Apps\FirefoxPortable\FirefoxPortable.exe"
			try:
				file = urllib2.urlopen(url1)
				reset_firefox(url1)
				if(os.path.isfile(browserpath)):
					launch(url1, browserpath) #launch with portable browser
				os.system('cd ' + working_dir)
				os.system('taskkill /IM dns2tcpc.exe >nul 2>&1')
				os.system('taskkill /IM cmd.exe >nul 2>&1')
				finished = True
			except Exception as e:
				print "proxy1 is not available" #For debugging
				try:
					file = urllib2.urlopen(url2)
					reset_firefox(url2)
					if(os.path.isfile(browserpath)):
						launch(url2, browserpath) #launch with portable browser
					os.system('cd ' + working_dir)
					os.system('taskkill /IM dns2tcpc.exe >nul 2>&1')
					os.system('taskkill /IM cmd.exe >nul 2>&1')
					finished = True
				except Exception as e1:
					print "proxy2 is not available" # for debugging
					print "None of the two urls worked! Please wait to try again!"
					print '-' * 80
					finished = False
			# Remove unnecessary files after it is done
			if finished == True:
				os.system("del proxy.txt")
				os.system("del speed.txt")
				os.system("del client_info.txt")
	if not(trycount):
                print "\n"
                print "Sorry! We could not find a proxy for you. Please, try again later."
                os.system('taskkill /IM dns2tcpc.exe >nul 2>&1')
