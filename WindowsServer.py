from __future__ import division
import random
import os
import getpass
import time

# Choose 2 proxies for one user (first based on country, then speed)
def choose_proxy(client_info, user_filename, proxy_filename):
	# Initiate user matix from the file
	f = open(user_filename)
	user_line = f.readlines()
	f.close()
	user = [['' for i in range(4)] for j in range(len(user_line))]
	for i in range(0, len(user_line)):
		index = find_index(user_line[i],'+')
		user[i][0] = user_line[i].strip()[:index[0]]
 		user[i][1] = user_line[i].strip()[index[0]+1:index[1]]
		user[i][2] = user_line[i].strip()[index[1]+1:index[2]]
		user[i][3] = user_line[i].strip()[index[2]+1:]

	# Delete the use entry who doesn't want to be other's proxy
	i = 0
	while i < len(user):
		if user[i][2] == '0.0.0.0':
			del user[i]
			i -= 1
		i += 1

	# First match country
	## Group1: '3','4','8'
	## Group2: '5', '2', '16', '1'
	## Group3: others
	if client_info[0] == '3' or client_info[0] == '4' or client_info[0] == '8' or client_info[1] == '3' or client_info[1] == '4' or client_info[1] == '8':
		delete_user_from_country(user, ['3', '4', '8'])
	elif client_info[0] == '1' or client_info[0] == '2' or client_info[0] == '5' or client_info[0] == '16' or client_info[1] == '1' or client_info[1] == '2' or client_info[1] == '5' or client_info[1] == '16':
		delete_user_from_country(user, ['1', '2', '5', '16'])
	else:
		country_list = [''] * 2
		country_list[0] = client_info[0]
		country_list[1] = client_info[1]
		delete_user_from_country(user, country_list)

	# Add Clemson Proxy address to the list
	f = open("our_proxy.txt")
	clemson_proxy_line = f.readlines()
	f.close()
	clemson_proxy = [['' for i in range(4)] for j in range(len(clemson_proxy_line))]
	for i in range(0, len(clemson_proxy_line)):
		index = find_index(clemson_proxy_line[i],'+')
		clemson_proxy[i][0] = clemson_proxy_line[i].strip()[:index[0]]
 		clemson_proxy[i][1] = clemson_proxy_line[i].strip()[index[0]+1:index[1]]
		clemson_proxy[i][2] = clemson_proxy_line[i].strip()[index[1]+1:index[2]]
		clemson_proxy[i][3] = clemson_proxy_line[i].strip()[index[2]+1:]
	user += clemson_proxy

	# Then decide based on connecting speed in a probability way
	## Grab user ip and user speed as input
	user_ip = [''] * len(user)
	user_speed = [0.0] * len(user)
	for i in range(0, len(user)):
		user_ip[i] = user[i][2]
		user_speed[i] = float(user[i][3])
	proxy_addr = choose_two_proxy(client_info[2], user_ip, user_speed)
	return proxy_addr

# Delete users from certain countries
def delete_user_from_country(user, country):
	for j in range(0, len(country)):
		i = 0
		while i < len(user):
			if user[i][0] == country[j] or user[i][1] == country[j]:
				del user[i]
				i -= 1
			i += 1

# Choose 2 proxies from the list
def choose_two_proxy(new_ip, usr_ip,usr_score):
	# if the new user is in the old list, choose proxies from the others	
	g = 0
	for i in range(0,len(usr_ip)):
		if new_ip == usr_ip[i]:
			usr_ip.pop(i)
			usr_score.pop(i)
			g = 1
			break
		else: pass
		if g == 0:
			i = i + 1
		else: pass
	#calculate the summation of usr_score
	sum_usr_score = [0.0] * len(usr_score)
	sum_usr_score[0] = usr_score[0]
	for i in range(1, len(usr_score)):
	       	sum_usr_score[i] = sum_usr_score[i-1] + usr_score[i]
	#calculate borders for choosing proxy
	border = [0] * (len(usr_score)+1)
	#print "Ranges are calculated:"
	for i in range(0,len(usr_score)):
		border[i+1] = sum_usr_score[i]/sum_usr_score[len(usr_score)-1]
	#generate a random number for choosing primary proxy
	random_num1 = random.random()
	#choose primary proxy 
	i = 0
	while i < len(usr_score):
		if random_num1 < border[i+1]: 
			break
       		else: i = i+1
	#choose backup proxy
	k = 1
	while k:
		j = 0
		random_num2 = random.random()
		while j < len(usr_score):
			if random_num2 < border[j+1]: 
				break
    			else: j = j+1
		if j == i: continue
		else: 	
			break
	selected_ip_as_proxy = [0]*2
	selected_ip_as_proxy[0] = usr_ip[i]
	selected_ip_as_proxy[1] = usr_ip[j]
	return selected_ip_as_proxy

# Return all Index of a pattern from a string
def find_index(s, ch):
	return [i for i, ltr in enumerate(s) if ltr == ch]
		
# Retrieve online_clemson_proxy() and do the speed test

# Retrieve online_user_list()

# Change permisson of server folder

# Empty the user data file

# Start main function
if __name__ == '__main__':
	user_filename = "user_list.txt"
	proxy_filename = "our_proxy.txt"
	os.system('mkdir user_data')
	os.system('mkdir proxy_data')
	while True:
		username = getpass.getuser()
		work_dir = os.path.dirname(os.path.realpath(__file__))
		## Check the existence of user file
		flag = 0
		print 'Waiting for the user connection...'
		while flag == 0:
			if os.path.exists(work_dir + '/user_data/client_info.txt'):
				os.system('rm ' + work_dir + '/proxy_data/proxy.txt')
				flag = 1
				print 'One connection!'
			else:
				time.sleep(1)
				#print 'not there'
		#print 'done'
		if flag == 1:
			# Parse user information
			f = open(work_dir + '/user_data/client_info.txt')
			data = f.readlines()[0]
			f.close()
			client_info = data.strip().split('+')
			# Choose proxy for this user
			proxy_addr = choose_proxy(client_info, user_filename, proxy_filename)
			print proxy_addr
			f = open(work_dir + '/proxy_data/proxy.txt','w')
			f.write('https://' + proxy_addr[0] + ':30001/FIP101' + '\n' + 'https://' + proxy_addr[1] + ':30001/FIP101')
			f.close()
			# Write user information to proxy file if he wants to be one proxy
			f = open(user_filename, 'a')
			f.write(data + '\n')
			f.close()
			# Empty the user folder when this user is done
			os.system('rm ' + work_dir + '/user_data/client_info.txt')

			flag = 0



