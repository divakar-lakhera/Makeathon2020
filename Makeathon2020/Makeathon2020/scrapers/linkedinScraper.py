import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver


class linkedinScraper():
    
    def __init__(self):
        self.link=""
        self.browser = webdriver.Chrome()
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
        education = {}

        
        for edu in self.soup.find_all('li',{"class":"pv-profile-section__sortable-item pv-profile-section__section-info-item relative pv-profile-section__sortable-item--v2 pv-profile-section__list-item sortable-item ember-view"}):
            education['school_name'] = edu.find("h3",{"class":"pv-entity__school-name t-16 t-black t-bold"}).get_text().strip()
            
            education['degree_name'] = edu.find("p",{"class":"pv-entity__secondary-title pv-entity_degree-name t-14 t-black t-normal"}
            ).find("span",{"class":"pv-entity__comma-item"}).get_text().strip()

            education['field_of_study'] = edu.find("p",{"class":"pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"}
            ).find("span",{"class":"pv-entity__comma-item"}).get_text().strip()

            educations.append(education)
        
        return educations
    
    def getUserLicenseAndCertifications(self):
        certifications = []
        certification = {}

        certificates = self.soup.find_all("li",{"class":"pv-profile-section__sortable-item pv-certification-entity ember-view"})

        for certificate in certificates:
            certification['course_name'] = certificate.find('h3',{"class":"t-16 t-bold"}).get_text().strip()
            
            certifications.append(certification)
        return certifications
    
    def getUserAccomplishments(self):
        accomplishment = {}

        honors_awards = []
        awards = self.soup.find("div",{"id":"honors-expandable-content"})
        print(awards)
        awards = awards.find_all("li",{"class":"pv-accomplishments-block__summary-list-item"})
        for award in awards:
            honors_awards.append(award.get_text().strip())
        accomplishment['honor_awards'] = honors_awards

        courses = []
        course_list = self.soup.find("div",{"id":"courses-expandable-content",})
        course_list = course_list.find_all("li",{"class":"pv-accomplishments-block__summary-list-item"})
        for course in course_list:
            courses.append(course.get_text().strip())
        accomplishment['courses'] = courses

        languages = []
        language_list = self.soup.find("div",{"id":"languages-expandable-content"})
        language_list = language_list.find_all("li",{"class":"pv-accomplishments-block__summary-list-item"})
        for language in language_list:
            languages.append(language.get_text().strip())
        accomplishment['languages'] = languages

        projects = []
        project_list = self.soup.find("div",{"id":"projects-expandable-content"})
        project_list = project_list.find_all("li",{"class":"pv-accomplishments-block__summary-list-item"})
        for project in projects:
            projects.append(project.get_text().strip())
        accomplishments['projects'] = projects

        test_scores = []
        test_score_list = course_list = self.soup.find("div",{"id":"test-scores-expandable-content"})
        test_score_list = test_score_list.find_all("li",{"class":"pv-accomplishments-block__summary-list-item"})
        for test_score in test_score_list:
            test_scores.append(test_score.get_text().strip())
        accomplishments['test_scores'] = test_scores
        
        return accomplishment
    
    def getUserSkillsEndorsements(self):
        skills = []
        skillsInterests = self.soup.find_all("span",{"class":"pv-skill-category-entity__name-text t-16 t-black t-bold"})

        for skill in skillsInterests:
            skills.append(skill.get_text().strip())
        
        return skills

if __name__ == "__main__":
    profile = linkedinScraper()
    profile.loadProfile("https://www.linkedin.com/in/kanha-khatri-567134171/")

    print(profile.getUserAccomplishments())

