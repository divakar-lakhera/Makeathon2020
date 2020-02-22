from bs4 import BeautifulSoup
import requests

class stackScraper():
	def __init__(self):
		self.link=""
		# list will contain name of person
		self.name=[]
		# list will hold all tag of that person
		self.tags=[]

	def find_tags(self,link):
		try:
			self.link=link+"?tab=tags"
			page_url=requests.get(link)
			if(page_url.status_code!=200):
				print(f"Stackoverflow Request Failed... :{page_url.status_code}")

			else:
				soup=BeautifulSoup(page_url.content,"html.parser")
				raw_tag=soup.find_all("a",class_="post-tag")
				for i in raw_tag:
					self.tags.append(i.get_text())

				self.tags=list(set(self.tags))
				return self.tags

		except:
			return ("Invalid Url")

	def find_name(self,link):
		try:
			page_url=requests.get(self.link)
			if(page_url.status_code!=200):
				print("Stackoverflow: Request Failed... Got"+str(page_url.status_code))

			else:
				soup=BeautifulSoup(page_url,"html.parser")
				names=soup.find_all("div",class_="name")
				for i in names:
					i=(i.get_text()).split('\n')[1].strip()
					self.name.append(i)
				return name

		except:
			return ("Invalid Url")
