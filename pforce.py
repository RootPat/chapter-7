import urllib.request
import threading 
from multiprocessing import Queue
import urllib.error

threads = 5
target_url = "http://testphp.vulnweb.com"
wordlist_file = "/Users/patrickharris/Desktop/linkedin_passwords.txt" 
resume = None 
user_agent = "Mozilla/5.0 (x11; Linux x86_64;rv:19.0) Gecko/20100101 Firefox/19.0"

def build_wordlist (wordlist_file):

	#read in the word list 
	fd = open(wordlist_file, "rb")
	raw_words = fd.readlines()
	fd.close()

	found_resume = False 
	words = Queue.Queue()

	for word in raw_words:

		word = word.rstrip() 

		if resume is not None:

			if found_resume:
				words.put(word)
			else:
				if word == resume:
					found_resume = True 
					print("Resuming wordlist from: %s" % resume)
		else:
			words.put(word)
	return words

	def dir_bruter(word_queue, extensions=none):

		while not word_queue.empty():
			attempt = word_queue.get()

			attempt_list = []

			#check to see if there is a file extension; if not, 
			# it's a directory path to brute force

			if  "." not in attempt:
				attempt_list.append("/%s%s" % attempt)
			else:
				attempt_list.append("/%s" % attempt)

			#if we want brute force extensions
			if extensions:
				for extension in extensions:
					attempt_list.append("/%s%s" % (attempt,extension))

			#iterate over our list of attempts 
			for brute in attempt_list:

				url = "%s%s" % (target_url, urllib.quote(brute))

				try:
					headers = {}
					headers["User-Agent"] = user_agent
					r = urllib.request.urlopen(url,headers=headers)

					response = urllib.request.urlopen(r)

					if len(response.read()):
						print("[%d] = > %s" % (response.code,url))

				except urllib.request.URLError:

					if hasattr(e, 'code') and e.code !=404:
						print("!!! %d +> %s" % (e.code,url))

					pass


