#!/usr/bin/env python3

"""
    Crypto Studio - Python3 Final Full Stack Artificial Intelligence Project
    Created: Sadip Giri (sadipgiri@bennington.edu)
    Date: 04/01/2018
"""

import web
import crypto_api # another python3 program to access crypto prices
from talk_to_mongodb import add_my_currencies, get_my_currencies # another python3 program to talk to MONGODB
from sentiments import return_sentiments # another program to calculate sentiment of cryptos
import time
#import predictions # for predicting crypto prices using built LSTM deep learning model

# Global Variables to restrict - wrong username or password & to restrict user directly accessing News Feed (that is User Class) without login credentials
username = ""
password = ""

# these are the URL endpoints
urls = (
	'/diet_diary', 'diet_diary',
    '/login', 'login',
	'/my_currencies', 'my_currencies',
	'/currencies_sentiments', 'currencies_sentiments',
	'/predict', 'predict',
    # '/(.*)', 'hello'
)

app = web.application(urls, globals())

# rendering the templates
render_template = web.template.render('templates/')
render_static = web.template.render('static/')

# login system 
class login:
	def POST(self):
		my_input = web.input()
		username = my_input.input_username
		password = my_input.input_password
		if username == "oliver" and password == "oliver":
			currencies = crypto_api.top_crypto_prices() 
			return render_template.user_template(username, currencies)
		else:
			return login.GET(self)	# returning back to user so that no one could directly go to user-template without login.
	# renders the login.html template	
	def GET(self):
		return render_static.login_form()

# returning user's currencies talking to MONGODB database
class my_currencies:
	def POST(self):
		currencies = web.input().currencies	# accessing input from the template
		if currencies:
			add_my_currencies(currencies)	# adding my currencies in MONGODB database
			showing_currencies = crypto_api.top_crypto_prices()	
			return render_template.user_template(username="oliver", crypto_prices=showing_currencies)	# renders the user's template
		else:
			return
	def GET(self):
		currencies = get_my_currencies()
		return render_template.my_currencies_template(currencies)

# returns the sentiments of user choice cryptos
class currencies_sentiments:
	def POST(self):
		# curr_sentiments = []
		# my_currrencies = list(get_my_currencies())
		# print(my_currencies)
		# for i in my_currencies:
		# 	sents = return_sentiments(i)
		# 	curr_sentiments.append(sents)
		sents = return_sentiments('bitcoin')
		# curr_sentiments.append(sents)
		# print(curr_sentiments)
		# print(my_currencies)
		# print(curr_sentiments)
		return render_template.currencies_sentiments('bitcoin', sents)

class predict:
	def GET(self):
		return render_template.predictions()
		
# running the program finally
if __name__ == "__main__":
    app.run()


"""
	References:
		- Bootstrap is used. In addition to that, I have used free bootstrap themes/templates and have given references to them.
"""     



