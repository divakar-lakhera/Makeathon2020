import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver


class linkedinScraper():
    
    def __init__(self):
        self.link=""
        self.browser = webdriver.Chrome('Makeathon2020\driver\chromedriver.exe')
        self.browser.get('https://www.linkedin.com/uas/login')

        
        time.sleep(1)

        self.email = 'wajije1434@kamismail.com'
        self.password = 'helloworld123'

        elementID = self.browser.find_element_by_id('username')
        elementID.send_keys(self.email)

        elementID = self.browser.find_element_by_id('password')
        elementID.send_keys(self.password)

        time.sleep(1)

        elementID.submit()

    def killDriver(self):
        self.browser.close();
        
    
    def loadProfile(self, link):
        self.link=link
        self.browser.get(link)

        SCROLL_PAUSE_TIME = 2

        # Get scroll height
        last_height = self.browser.execute_script("return document.body.scrollHeight")

        for i in range(3):
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        src = self.browser.page_source
        
        self.soup = BeautifulSoup(src, 'lxml')
        

        
    
    def getUserName(self):
        name_div = self.soup.find('div', {'class':'flex-1 mr5'})
        name_loc = name_div.find_all('ul')
        name = name_loc[0].find('li').get_text().strip()

        return name
    
    def getUserExperiences(self):
        experiences = []
        experience = {}
        for exp in self.soup.find_all('li',{"class":"pv-entity__position-group-pager pv-profile-section__list-item ember-view"}):
            experience['title'] = exp.find("h3",{"class":"t-16 t-black t-bold"}).get_text().strip()
            
            experience['company'] = exp.find("p", {"class":"pv-entity__secondary-title t-14 t-black t-normal"}).get_text().strip()
                        
            experiences.append(experience)
        return experiences
    

    def getUserEducation(self):
        educations = []
        

        edu_section = self.soup.find('section',{'id':'education-section'}).find('ul').find_all("li")
        for edu in edu_section:
            educations.append(edu.find('div', {"class":"pv-entity__degree-info"}).find('h3').get_text().strip())
        return educations

    def getUserLicenseAndCertifications(self):
        certifications = []
        certification = {}

        certificates = self.soup.find_all("li",{"class":"pv-profile-section__sortable-item pv-certification-entity ember-view"})

        for certificate in certificates:
            certification['course_name'] = certificate.find('h3',{"class":"t-16 t-bold"}).get_text().strip()
            
            certifications.append(certification)
        return certifications
    
    def getUserHonorsAwards(self):
        honors_awards = []
        awards = self.soup.find("div",{"id":"honors-expandable-content"}).find('ul').find_all('li')
        for award in awards:
            honors_awards.append(award.get_text().strip())
        return honors_awards
    
    def getUserCourses(self):
        courses = []
        course_list = self.soup.find("div", {"id":"courses-expandable-content"}).find('ul').find_all('li')
        for course in course_list:
            courses.append(course.get_text().strip())
        return courses
    
    def getUserLanguages(self):
        languages = []
        language_list = self.soup.find('div', {"id":"languages-expandable-content"}).find('ul').find_all('li')
        for language in language_list:
            languages.append(language.get_text().strip())
        return languages

    def getUserProjects(self):
        projects = []
        project_list = self.soup.find('div', {"id":"projects-expandable-content"}).find('ul').find_all('li')
        for project in project_list:
            projects.append(project.get_text().strip())
        return projects
    
    def getUserTestScores(self):
        test_scores = []
        test_score_list = self.soup.find('div', {"id":"test-scores-expandable-content"}).find('ul').find_all('li')
        for test_score in test_score_list:
            test_scores.append(test_score.get_text().strip())
        return test_scores
    
    def getUserSkillsEndorsements(self):
        skills = []
        skillsInterests = self.soup.find_all("span",{"class":"pv-skill-category-entity__name-text t-16 t-black t-bold"})

        for skill in skillsInterests:
            skills.append(skill.get_text().strip())
        
        return skills
