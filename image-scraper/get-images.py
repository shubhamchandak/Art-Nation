#image scrapping for twitter image bot

import requests
from bs4 import BeautifulSoup as bs
import os

#create directory for images
if not os.path.exists('pictures'):
	os.makedirs('pictures')

#move to new directory
os.chdir('pictures')

#image file name variable
x = 0

def extractImages(pageNumber):

	global x

	#website for images
	url = 'https://www.canva.com/photos/arts/?page=' + str(pageNumber)

	#download page for parsing
	page = requests.get(url)
	soup = bs(page.text, 'html.parser')
	#print(soup)
	#locate all elements with img tag
	img_tags = soup.findAll('img')


	#writing images
	for image in img_tags:
		try:
			img_url = image['src']
			#print('url' + str(x) + ': ' + img_url)
			source = requests.get(img_url)
			if source.status_code == 200:
				with open('img-' + str(x) + '.jpg', 'wb') as f:
					f.write(source.content)
					f.close()
					x = x + 1
		except:
			pass

#website page number
page = 1
for i in range(2):
	url = 'https://www.canva.com/photos/arts/?page=' + str(i)
	if(requests.get(url).status_code == 200):
		print(str(i) + 'xxxxxxxxxxxxxxxxx')
		extractImages(i)

print(x)