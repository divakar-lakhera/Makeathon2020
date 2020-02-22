# parserPdf.py
# PDF parse and verification Utility
# Written by: Divakar Lakhera
# BabaYaga (NIT Uttarakhand)

import pdfx
import math
import Makeathon2020.scrapers.gitScraper as gitLab
import Makeathon2020.scrapers.stackScraper as stackLab
import Makeathon2020.scrapers.linkedinScraper as linkLab

class pdfParser():
    def __init__(self,file,uname,gitLink,stackLink,linkedinLink):
       self.pdf = pdfx.PDFx(file)
       # user data from CV and provided
       self.user=uname.lower()
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
       self.linkedEducation=""

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
       if(self.linkedinAccount != None):
           self.linkedin=linkLab.linkedinScraper()
           self.linkedin.loadProfile(self.linkedinAccount)
           self.certi=self.linkedin.getUserLicenseAndCertifications()
           self.linkedEducation=self.linkedin.getUserEducation()
           self.linkedinName=self.linkedin.getUserName().lower()
           self.linkedin.killDriver()
           print(self.certi)
           print(self.linkedEducation)
           

       # End LinkedIn 

    def rawDump(self):
        print(self.rawResume)

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

        print("Done..")



    def getScore(self):
        points=0
        maxpoints=0

        #check name
        fg=0
        nameTok=self.user.split()
        nameTok[0]=nameTok[0].strip()
        nameTok[1]=nameTok[1].strip()
        for i in self.rawResume.split('\n'):
            if nameTok[0] in i.split() and nameTok[1] in i.split():
                fg=1
                points+=1
                maxpoints+=1

        if fg==0:
            print("Name Verification Failed [CV]");
            return "Name Verification Failed [CV]"
               
        if(self.isGit==1 and self.githubName != self.user):
            print("Fatal: Name match error [GitHub]")
            print(self.githubName)
            return "Fatal: Name match error [GitHub]"
        else:
            points+=1
        
        if(self.isStack==1 and self.stackName != self.user):
            print("Fatal: Name match error [StackOverFlow]")
            return "Fatal: Name match error [StackOverFlow]"
        else:
            points+=1

        if(self.isLinked==1 and self.linkedinName != self.user):
            print("Fatal: Name match error [LinkedIn]")
            return "Fatal: Name match error [LinkedIn]"
        else:
            points+=1

        maxpoints+= self.isStack+self.isGit+self.isLinked;

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
        tproj=0
        projz=0
        #generate string pool
        self.generateStringPool(self.proj)
        temp=self.rawResume.split(" ")
        for i in range(len(temp)-1):
            if temp[i].strip().strip('\n') in self.stringPool.keys():
                # print(temp[i])
                if(self.stringPool[temp[i].strip().strip('\n')]==None):
                    tproj+=1
                elif(self.stringPool[temp[i].strip().strip('\n')]==temp[i+1].strip().strip('\n')):
                    tproj+=1
        self.flushStringPool()
        temp=self.rawResume.split('\n')
        for i in range(len(temp)):
            if "projects" in temp[i].split():
                break;
        for j in range(i,len(temp)):
            if ("intrests" in temp[j].split()) or ("achievements" in temp[j].split()):
                break;
        projz=int((j-i+1)/5) #adjustment factor (practical value) 
        print(str(projz)+ " " +str(tproj))
        if(tproj >= projz):
            tproj=projz
        points+=tproj
        maxpoints+=projz
        print(str(points)+" "+str(maxpoints))
        print("ACC: "+str(int((points/maxpoints)*100)))
        return int((points/maxpoints)*100)