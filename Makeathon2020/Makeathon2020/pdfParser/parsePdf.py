# parserPdf.py
# PDF parse and verification Utility
# Written by: Divakar Lakhera
# BabaYaga (NIT Uttarakhand)

import pdfx
import Makeathon2020.scrapers.gitScraper as gitLab
import Makeathon2020.scrapers.stackScraper as stackLab


class pdfParser():
    def __init__(self,file,uname,gitLink,stackLink,linkedinLink):
       self.pdf = pdfx.PDFx(file)
       self.user=uname
       self.github=""
       self.githubName=""
       self.linkedin=""
       self.githubLocation=""
       self.stack=""
       self.stackName=""
       self.stackLang=""
       self.lang=[]
       self.proj=[]
       self.certi=[]
       self.gitAccount=gitLink
       self.stackAccount=stackLink
       self.linkedinAccount=linkedinLink
       self.isGit=0
       self.isStack=0
       self.isLinked=0
       self.linkedinName=""
       self.rawResume=""
       self.resumeLang=[]
       self.dummyLang=['python',"python3",'html','css','html5',"html 5",'css3',"css 3",'js','javascript','php','ajax','kotlin',"c++","c","java","swift","golang","c#","scala","kotlin","ruby","assembly"]
       if gitLink != None:
           self.isGit=1
       else:
           print("Warning GitHub Account Not Added...may drastically affect output..");
       if stackLink != None:
           self.isStack=1
       else:
           print("Warning StackOverFlow Account Not Added...may drastically affect output..")
       if linkedinLink != None:
           self.isLinked=1
       else:
           print("Warning LinkedIn Account Not Added...may drastically affect output..")


    def loadLinks(self):
       # Start GitHub Scrap
       if(self.gitAccount != None):
           self.github=gitLab.gitScraper()
           self.github.loadProfile(str(self.gitAccount))
           self.lang=self.github.gitGetAllLanguages()
           self.proj=self.github.gitGetAllProjects()
           self.githubName=self.github.gitGetUserName()
           self.githubLocation=self.github.gitGetLocation()
       # End GitHub Scrap

       # Start StackOverflow Scrap
       if(self.stackAccount != None):
           self.stack=stackLab.stackScraper()
           self.stackName=self.stack.find_name(self.stackAccount)
           self.stackLang=self.stack.find_tags(self.stackAccount)

       # End

       # Start LinkedIn Scrap

       # TODO

       # End LinkedIn 

    def dumpContent(self):
        print("Dumping Content..")
        print(self.githubName)


    def processCV(self):
        print("Pre-Processing CV..")
        self.rawResume=self.pdf.get_text().lower()
        print("Searching for Languages.(slow search).")

        for i in self.rawResume.split(" "):
            if i in self.dummyLang:
                print(i)
                self.resumeLang+=[i]
            elif i[0:len(i)-1] in self.dummyLang:
                print(i[0:len(i)-1])
                self.resumeLang+=[i[0:len(i)-1]]


        print("Done..")



    def getScore(self):
        points=0
        maxpoints=0

        #check name
        if(self.isGit==1 and self.githubName != self.user):
            print("Fatal: Name match error [GitHub]")
            return 0
        else:
            points+=1
        
        if(self.isStack==1 and self.stackName != self.user):
            print("Fatal: Name match error [StackOverFlow]")
            return 0
        else:
            points+=1

        if(self.isLinked==1 and self.linkedinName != self.user):
            print("Fatal: Name match error [LinkedIn]")
            return 0
        else:
            points+=1
            
        maxpoints+=3

        #Check Languages

        
        

