
# Antinatalism Quotes Script

from win10toast import ToastNotifier
import bs4
import time
import random
import pyttsx3
import requests

n = ToastNotifier()

# Antinatalism Quotes url
quotes_url = 'https://bukrate.com/topic/antinatalism-quotes?p='

def say(text):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')[1]
	engine.setProperty('voice', voices.id)
	engine.setProperty('rate', 125)
	engine.say(text)
	engine.runAndWait()

def show_quotes():
	try:
		res = requests.get(quotes_url + str(random.randint(0, 2)))
		html = bs4.BeautifulSoup(res.content, 'html.parser')
		all_quotes = [q.text  for q in html.find_all('a', class_ = 'title')]
		all_author = [a.text  for a in html.find_all('div', class_ = 'author')]

		index = random.randint(0, len(all_quotes))

		author = all_author[index]
		quote = all_quotes[index]

		n.show_toast(
			author,
			quote,
			'imgs/icon.ico',
			duration = 10
		)

		say(author)
		time.sleep(3)
		say(quote)

		time.sleep(100)
		show_quotes()

	except:
		time.sleep(100)
		show_quotes()


time.sleep(2)
show_quotes()