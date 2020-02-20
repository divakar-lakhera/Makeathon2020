# gitScraper.py
# GitHub Scraping Tool
# Written by: Divakar Lakhera
# Team BabaYaga (NIT Uttarakhand)

from bs4 import BeautifulSoup
import requests
class gitScraper():
    def __init__(self):
        self.name=""
        self.html=""
        self.repos=[]


    def loadProfile(self,link):
        self.name=link
        raw_page=requests.get(link);
        raw_rep=requests.get(link+"?tab=repositories")
        if(raw_page.status_code!=200 or raw_rep.status_code !=200):
            print("GitScraper: Request Failed.. Got "+str(raw_page.status_code))
        else:
            self.html=BeautifulSoup(raw_page.content,'html.parser')
            repStart=BeautifulSoup(raw_rep.content,'html.parser')
            temp=repStart.find("div",attrs={'class':'paginate-container'})
            if temp == None :
                self.repos+=[repStart]
            else:
                print("Fetching Repo Pages..")
                self.repos+=[repStart]
                aa=0
                flag=0
                up=0
                while(1):
                    temp2=temp.find_all("a",attrs={'class':'btn btn-outline BtnGroup-item'})
                    for i in temp2:
                        if(i.get_text()=="Next" and i['href'] != ""):
                            aa=i['href'];
                            flag=1
                            print(aa)
                    if flag==0:
                        break;
                    flag=0
                    raw_rep=requests.get(aa)
                    repStart=BeautifulSoup(raw_rep.content,'html.parser')
                    temp=repStart.find("div",attrs={'class':'paginate-container'})
                    self.repos+=[repStart]
        print("Repo Page Fetch Done..Got "+str(len(self.repos)))
        print("GitScraper: Load Complete..")
    
    def gitFastFetchProfileBySpan(self,tag,prop):
        return self.html.find("span", {tag: prop}).get_text()
        # return self.html.find("span", {"itemprop": "name"}).get_text()
       
    def gitFastFetchRepoBySpan(self,tag,prop):
        return self.repos.find("span", {tag: prop}).get_text()
    
    def gitGetAllLanguages(self):
        listlang=[]
        for i in self.repos:
            raw_list=i.find("div",attrs={'id':'user-repositories-list'})
            for lang in raw_list.find_all('span',attrs={'itemprop':'programmingLanguage'}):
                listlang+=[lang.get_text()]
        return listlang

    def gitGetAllProjects(self):
        listprog=[]
        for i in self.repos:
            raw_list=i.find("div",attrs={'id':'user-repositories-list'})
            for name in raw_list.find_all('a',attrs={'itemprop':'name codeRepository'}):
                listprog.append(name.get_text().split('\n')[1].strip())
        return listprog

    def gitGetUserName(self):
        return self.html.find("span", {"itemprop": "name"}).get_text()