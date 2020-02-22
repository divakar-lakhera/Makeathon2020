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
       # user data from CV and provided
       self.user=uname
       self.rawResume=""
       self.resumeLang=[]
       # - 
       # GitHub
       self.github=""
       self.githubName=""
       self.githubLocation=""
       self.isGit=0
       self.gitAccount=gitLink
       self.lang=[]
       self.proj=[]
       # -
       # StackOverFlow
       self.stack=""
       self.stackName=""
       self.stackLang=""
       self.stackAccount=stackLink
       self.isStack=0
       # -
       # LinkedIn 
       self.linkedin=""
       self.certi=[]
       self.linkedinAccount=linkedinLink
       self.isLinked=0
       self.linkedinName=""
       # -
       self.stringPool={}
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
        print(self.lang)
        print(self.proj)
        print("done..")
        
    def generateStringPool(self,strings):
        print("Generating Pool")
        for i in strings:
            t=i.split(" ")
            if(len(t)>=2):
                self.stringPool[t[0]]=t[1]
            else:
                self.stringPool[t[0]]=None
        print("Done")

    def dumpStringPool(self):
        print(self.stringPool)

    def flushStringPool(self):
        self.stringPool={}

    def checkPool(self):
        temp=self.rawResume.split(" ")
        for i in range(len(temp)-1):
            if temp[i].strip().strip('\n') in self.stringPool.keys():
                print(temp[i])
                if(self.stringPool[temp[i].strip().strip('\n')]==None):
                    print("Got")
                elif(self.stringPool[temp[i].strip().strip('\n')]==temp[i+1].strip().strip('\n')):
                    print("Got 2")

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
        self.generateStringPool(self.proj)

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
        langpts=0
        maxlang=len(self.resumeLang)

        for i in self.resumeLang:
            if i in self.lang:
                langpts+=1

        if(langpts > maxlang):
            #error due to uncertainity
            langpts=maxlang
        points+=langpts
        maxpoints+=maxlang

        #Check Projects

        #generate string pool
        self.generateStringPool(self.proj)
